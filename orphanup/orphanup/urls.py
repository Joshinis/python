"""orphanup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from showhope import views
from django.contrib.auth.views import LoginView,LogoutView


#-------------FOR ADMIN RELATED URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),

#-------------------------admin-------------------------------#
    path('admins/', views.admin_signup_view,name='admins'),
    path('dashindex/', views.dashpage, name='dashindex'),
    path('childrens/',views.admin_childrens_view,name='childrens'),
    path('pagein/',views.admin_income_view,name='pagein'),
    path('view_children/',views.admin_view_childrens_view,name='view_children'),
    path('addOrphan/',views.admin_add_orphans_view,name="addOrphan"),
    path('seniors/',views.admin_seniors_view,name='seniors'),
    path('view_seniors/',views.admin_view_seniors_view,name='view_seniors'),
    path('addOldage/', views.admin_add_oldage_view,name="addOldage"),
    path('expenditure/',views.admin_expenditures_view,name='expenditure'),
    path('view_expences/',views.admin_view_expence_view,name='view_expences'),
    path('exp/',views.admin_add_Expence_view,name="exp"),
    path('asset/',views.admin_asset_view,name='asset'),
    path('view_assets/',views.admin_view_asset_view,name='view_assets'),
    path('assets/',views.admin_add_Assets_view,name="assets"),

    path('admin-approve-payment', views.admin_approve_Payment_view,name='admin-approve-payment'),
    path('approve-payment/<int:pk>', views.approve_Payment_view,name='approve-payment'),
    path('reject-payment/<int:pk>', views.reject_Payment_view,name='reject-payment'),



    path('view_donors/',views.view_donors,name='view-donor'),

#---------------------end------------------------------------#
#------------------------------------------------------------#
#------------------------------------------------------------#
#-----------------------------------------------------------------------#
    path('afterlog', views.afterlog_view,name='afterlog'),
    path('logout', LogoutView.as_view(template_name='site/index.html')),


    
    
    path('adminlogin', LoginView.as_view(template_name='site/adminLogin.html')),
    
    path('donorlogin', LoginView.as_view(template_name='site/login.html')),

#------------------------------------------------------------------------#
]
#----------------------------Donor---------------------------#
urlpatterns +=[ 
    path('registration', views.donors_signup_view,name='registration'),
    path('contact/', views.contact_view,  name="contact"),
    path('aboutus/', views.about_view, name='aboutus'),
    path('ddash', views.donor_dash_view, name='ddash'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('adoption/', views.donor_adoption_view,name="adoption"),
    path('donation/', views.donor_donation_view,name="donation"),
     path('payment', views.client_Payment_view,name='payment'),
     path('vpayment', views.client_view_Payment_view,name='vpayment'),
    
    path('client-book-page', views.client_BookPage_view,name='client-book-page'),

#----------------------------end-----------------------------#



]
