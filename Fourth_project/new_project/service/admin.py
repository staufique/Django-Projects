from django.contrib import admin
from service.models import myServices
# Register your models here.

class serviceAdmin(admin.ModelAdmin):
    list_display=('s_icon','s_title','s_desc')

admin.site.register(myServices,serviceAdmin)
