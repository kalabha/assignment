from django.contrib import admin

from .models import *

class CityInline(admin.TabularInline):
    model = City
    extra = 1
class StateInline(admin.TabularInline):
    model = State
    extra = 1
    inlines = [CityInline]

class CountryAdmin(admin.ModelAdmin):
    inlines = [StateInline]


class StateAdmin(admin.ModelAdmin):
    inlines = [CityInline]
    exclude = ('name', 'country')
    list_display = ('name', 'country',)


admin.site.register(Country, CountryAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(Coordinate)

