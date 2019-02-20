from django.contrib import admin

# Register your models here.
from .models import ExpnsCatg, AccountBook

class AccountBookAdmin(admin.ModelAdmin):
    list_display=('sls_dt','expns_catg_nm','prc_amt','memo')

admin.site.register(ExpnsCatg)
admin.site.register(AccountBook,AccountBookAdmin)
