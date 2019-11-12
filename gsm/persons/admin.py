from django.contrib import admin

from gsm.persons.models import Person, Address, Client, Employee, Customer, Invoice, Item


class AdressInline(admin.TabularInline):
     model = Address
     extra = 1


class PersonModelAdmin(admin.ModelAdmin):
    pass
    inlines = [AdressInline]
    list_display = ('pk','name', 'birthday', 'observation', 'purchase_limit')


admin.site.register(Person, PersonModelAdmin)


class ClientModelAdmin(admin.ModelAdmin):
    pass
    inlines = [AdressInline]
    list_display = ('pk', 'name', 'birthday', 'observation', 'purchase_limit', 'compra_sempre')


admin.site.register(Client, ClientModelAdmin)


class EmployeeModelAdmin(admin.ModelAdmin):
    pass
    inlines = [AdressInline]
    list_display = ('name', 'birthday', 'observation', 'purchase_limit', 'ctps', 'salary')


admin.site.register(Employee, EmployeeModelAdmin)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


class ItensInline(admin.TabularInline):
    model = Item
    extra = 1


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    inlines = [ItensInline]
