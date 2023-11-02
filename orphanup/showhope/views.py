from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.views.generic import ListView, DetailView, TemplateView
#from .models import Profile
#from .forms import EditForm
from django.conf import settings

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlog')
    return render(request,'site/index.html')



def admin_signup_view(request):
    userForm=forms.AdminSigupForm()
    AdminForm=forms.AdminForm()
    mydict={'userForm':userForm,'AdminForm':AdminForm}
    if request.method=='POST':
        userForm=forms.AdminSigupForm(request.POST)
        AdminForm=forms.AdminForm(request.POST,request.FILES)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            Admin1=AdminForm.save(commit=False)
            Admin1.user=user
            Admin1=Admin1.save()
            
            
            my_Admin1_group = Group.objects.get_or_create(name='ADMIN')
            my_Admin1_group[0].user_set.add(user)
        return HttpResponseRedirect('adminlogin')
    return render(request,'site/admin_signup.html',context=mydict)


def donors_signup_view(request):
    userForm=forms.DonorUserForm()
    form2=forms.ExtraForm()
    mydict={'userForm':userForm,'form2':form2}
    if request.method=='POST':
        userForm=forms.DonorUserForm(request.POST)
        form2=forms.ExtraForm(request.POST,request.FILES)
        if userForm.is_valid() and form2.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            Donor=form2.save(commit=False)
            Donor.user=user
            Donor=Donor.save()
            my_Donor_group=Group.objects.get_or_create(name='DONOR')
            my_Donor_group[0].user_set.add(user)
        return HttpResponseRedirect('donorlogin')
    return render(request,'site/donorsignup.html',context=mydict)


#------------payment-------





#--------------------------------


#-----------for checking user is client or admin
def is_Admin1(user):
    return user.groups.filter(name='ADMIN').exists()
def is_Donor(user):
    return user.groups.filter(name='DONOR').exists()

#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN, OR CLIENT
def afterlog_view(request):
    if is_Admin1(request.user):
        accountapproval=models.Admin1.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect(reverse('dashindex'))
        else:
            return render(request,'site/admin_wait_for_approval.html')
    elif is_Donor(request.user):
        accountapproval=models.Donor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect(reverse('ddash'))
        else:
            return render(request,'site/donor_wait_for_approval.html')

@login_required(login_url='donorlogin')
@user_passes_test(is_Donor)
def donor_dash_view(request):
    return render(request,'site/main.html')




#----------------Admin Views---------------------#

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def dashpage(request):
    childcount=models.Orphans.objects.all().count()
    seniorcount=models.Oldage.objects.all().count()

    donorcount=models.Donor.objects.all().filter(status=True).count()
    pendingdonorcount=models.Donor.objects.all().filter(status=False).count()

    mydict={
        'childcount':childcount,
        'seniorcount':seniorcount,
        'donorcount':donorcount,
        'pendingdonorcount':pendingdonorcount,
    }

    return render(request, 'site/dash_index.html', context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def view_donors(request):
    records=models.Donor.objects.all().filter(Status=True)
    return render(request,"site/view_donors.html",{'records':records})


@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_approve_donor_view(request):
    records=models.Donor.objects.all().filter(Status=False)
    return render(request, 'site/admin_approve_donor.html',{'records':records})

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def approve_Payment_view(request,pk):
    Payment=models.Payment.objects.get(id=pk)
    Payment.status=True
    Payment.save()
    return redirect(reverse('admin-approve-payment'))

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def reject_Payment_view(request,pk):
    Payment=models.Payment.objects.get(id=pk)
    Payment.delete()
    return redirect('admin-approve-payment')

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_approve_Payment_view(request):
    #those whose approval are needed
    Payment=models.Payment.objects.all().filter(status=False)
    return render(request,'site/admin_approve_payment.html',{'Payment':Payment})


@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def approve_donor_view(requset,pk):
    record=models.Donor.objects.get(id=pk)
    record.Status=True
    record.save()
    return redirect(reverse('admin-approve-donor'))



@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def reject_donor_view(request,pk):
    record=models.Donor.objects.get(id=pk)
    user=models.User.Objects.get(id=Donor.user_id)
    user.delete()
    record.delete()
    return redirect('approvedonor')

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_childrens_view(request):
    return render(request,'site/childrens.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_income_view(request):
    return render(request,'site/pagein.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_view_childrens_view(request):
    records=models.Orphans.objects.all().filter(status=True)
    return render(request,'site/view_children.html',{'records':records})

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_add_orphans_view(request):
    # userForm=forms.AddorphanUserForm()
    orphanForm=forms.AddorphanForm()
    mydict={'orphanForm':orphanForm}
    if request.method=='POST':
        # userForm=forms.AddorphanUserForm(request.POST)
        orphanForm=forms.AddorphanForm(request.POST, request.FILES)
        if orphanForm.is_valid():
    

            orphan=orphanForm.save(commit=False)
        
            orphan.status=True
            orphan.save()

            my_orphan_group = Group.objects.get_or_create(name='Orphan')
           
        return redirect('view_children')
    return render(request,'site/add_orphan.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_seniors_view(request):
    return render(request,'site/seniors.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_view_seniors_view(request):
    records=models.Oldage.objects.all()
    return render(request,'site/view_seniors.html',{'records':records})

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_add_oldage_view(request):
    # userForm=forms.AddorphanUserForm()
    oldageForm=forms.AddoldageForm()
    mydict={'oldageForm':oldageForm}
    if request.method=='POST':
        # userForm=forms.AddorphanUserForm(request.POST)
        oldageForm=forms.AddoldageForm(request.POST, request.FILES)
        if oldageForm.is_valid():
    

            oldage=oldageForm.save(commit=False)
            
            oldage.status=True
            oldage.save()

            my_oldage_group = Group.objects.get_or_create(name='Oldage')
            
        return redirect('view_seniors')
    return render(request,'site/addOldage.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_expenditures_view(request):
    return render(request,'site/expenditure.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_view_expence_view(request):
    records=models.Expence.objects.all()
    return render(request,'site/view_expences.html',{'records':records})

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_add_Expence_view(request):
    # userForm=forms.AddorphanUserForm()
    expenceForm=forms.AddexpenceForm()
    mydict={'expenceForm':expenceForm}
    if request.method=='POST':
        # userForm=forms.AddorphanUserForm(request.POST)
        expenceForm=forms.AddexpenceForm(request.POST, request.FILES)
        if expenceForm.is_valid():
    

            expence=expenceForm.save(commit=False)
            
            expence.status=True
            expence.save()

            my_expence_group = Group.objects.get_or_create(name='Expence')
            

        return redirect('expenditure')
    return render(request,'site/exp.html',context=mydict)


@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def client_view_Payment_view(request):
    
    records=models.Payment.objects.all().filter(status=True)
    return render(request,'site/view_payment.html',{'records':records})



@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_asset_view(request):
    return render(request,'site/dash_assets.html')

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_view_asset_view(request):
    records=models.Assets.objects.all()
    return render(request,'site/view_assets.html',{'records':records})

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def admin_add_Assets_view(request):
    # userForm=forms.AddorphanUserForm()
    assetsForm=forms.AddassetsForm()
    mydict={'assetsForm':assetsForm}
    if request.method=='POST':
        # userForm=forms.AddorphanUserForm(request.POST)
        assetsForm=forms.AddassetsForm(request.POST, request.FILES)
        if assetsForm.is_valid():
    

            assets=assetsForm.save(commit=False)
            
            assets.status=True
            assets.save()

            my_assets_group = Group.objects.get_or_create(name='Assets')
            
        return redirect('view_assets')
    return render(request,'site/assets.html',context=mydict)

@login_required(login_url='adminlogin')
@user_passes_test(is_Admin1)
def client_BookPage_view(request):
   
    return render(request,'site/client_Book_page.html')


#---------------donor views------------------#
@login_required(login_url='donorlogin')
@user_passes_test(is_Donor)
def about_view(request):
    return render(request,'site/about_us.html')


@login_required(login_url='donorlogin')
@user_passes_test(is_Donor)
def gallery_view(request):
    return render(request,'site/gallery.html')


@login_required(login_url='donorlogin')
@user_passes_test(is_Donor)
def contact_view(request):
    return render(request,'site/contact.html')


@login_required(login_url='donorlogin')
@user_passes_test(is_Donor)
def donor_adoption_view(request):
    # userForm=forms.AddorphanUserForm()
    adoptionForm=forms.AddadoptionForm()
    mydict={'adoptionForm':adoptionForm}
    if request.method=='POST':
        # userForm=forms.AddorphanUserForm(request.POST)
        adoptionForm=forms.AddadoptionForm(request.POST, request.FILES)
        if adoptionForm.is_valid():
    
            Orphans=models.Orphans.objects.get(user_id=request.POST.get('OrphanId'))
            adoption=adoptionForm.save(commit=False)
         
            adoption.status=True
            adoption.save()

            my_adoption_group = Group.objects.get_or_create(name='Adoption')
           

        return redirect('ddash')
    return render(request,'site/adoption.html',context=mydict)


@login_required(login_url='donorlogin')
@user_passes_test(is_Donor)
def contact_view(request):
    # userForm=forms.AddorphanUserForm()
    contactForm=forms.ContactForm()
    mydict={'contactForm':contactForm}
    if request.method=='POST':
        # userForm=forms.AddorphanUserForm(request.POST)
        contactForm=forms.ContactForm(request.POST, request.FILES)
        if contactForm.is_valid():
    

            contact=contactForm.save(commit=False)
           
            contact.status=True
            contact.save()

            my_contact_group = Group.objects.get_or_create(name='contact')
            

        return redirect('ddash')
    return render(request,'site/contact.html',context=mydict)



@login_required(login_url='donorlogin')
@user_passes_test(is_Donor)
def donor_donation_view(request):
    # userForm=forms.AddorphanUserForm()
    donationForm=forms.AdddonationForm()
    mydict={'donationForm':donationForm}
    if request.method=='POST':
        # userForm=forms.AddorphanUserForm(request.POST)
        donationForm=forms.AdddonationForm(request.POST, request.FILES)
        if donationForm.is_valid():
    

            donation=donationForm.save(commit=False)
          
            donation.status=True
            donation.save()

            my_donation_group = Group.objects.get_or_create(name='Donation')
            

        return redirect('ddash')
    return render(request,'site/donation.html',context=mydict)

def client_Payment_view(request):
    PaymentForm=forms.ClientPaymentForm()

 
    mydict={'PaymentForm':PaymentForm}
    if request.method=='POST':
        PaymentForm=forms.ClientPaymentForm(request.POST)
        if PaymentForm.is_valid():
            
            amount=request.POST.get('amount')

        
            
            

            


            Payment=PaymentForm.save(commit=False)
            
            Payment.donorName=request.user.first_name
            Payment.status=False
            Payment.save()
        return redirect('ddash')
    return render(request,'site/payment.html',context=mydict)






#------------------end-------------------------------------------------#
