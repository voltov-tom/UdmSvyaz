from django.contrib import admin

from .models import Elevators


class FindAddress(admin.ModelAdmin):
    search_fields = ['address']
    ordering = ['address']


admin.site.register(Elevators, FindAddress)
