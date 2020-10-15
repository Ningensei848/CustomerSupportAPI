from django.contrib import admin


class CallingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'affiliation')
