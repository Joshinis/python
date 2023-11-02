from django.contrib import admin
from .models import Orphans,Oldage,Expence,Assets,Payment,Donor,Admin1,Adoption,Donation,Contact, Payment

# Register your models here.
admin.site.register(Orphans)
admin.site.register(Oldage)
admin.site.register(Contact)
admin.site.register(Expence)
admin.site.register(Assets)
admin.site.register(Adoption)
admin.site.register(Donation)
admin.site.register(Payment)
class DonorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Donor, DonorAdmin)

class Admin1Admin(admin.ModelAdmin):
    pass
admin.site.register(Admin1,Admin1Admin)

