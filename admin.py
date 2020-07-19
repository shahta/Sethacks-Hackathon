from django.contrib import admin
from . models import SDG


class SDGAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'id')


admin.site.register(SDG, SDGAdmin)
