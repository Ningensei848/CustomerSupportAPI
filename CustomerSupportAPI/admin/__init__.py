from django.contrib import admin

from CustomerSupportAPI.models.calling import CallingModel
from CustomerSupportAPI.admin.calling import CallingAdmin

from CustomerSupportAPI.models.matter import MatterModel

admin.site.register(CallingModel, CallingAdmin)
admin.site.register(MatterModel)
