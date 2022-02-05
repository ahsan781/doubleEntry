from django.contrib import admin
from mainapp.models import *
# Register your models here.
admin.site.register(categoryTypes),
admin.site.register(VendorsType),
admin.site.register(category),
admin.site.register(Vendors),
admin.site.register(Bills),
admin.site.register(Bill_Item),
admin.site.register(Invoiceable_item),
admin.site.register(customer),
admin.site.register(invoices),
admin.site.register(invoice_items)
admin.site.register(Adjustmenttypes),
admin.site.register(Bank),
admin.site.register(bankaccounttypes),
admin.site.register(Bankaccount),
admin.site.register(Adjustment),
admin.site.register(invoice_item),
admin.site.register(Adjustment_item),
admin.site.register(category_group_type),
admin.site.register(category_group),
admin.site.register(check)
admin.site.register(checkcategories),
admin.site.register(card),
admin.site.register(payment),
admin.site.register(invoice_payment),
admin.site.register(Report),
admin.site.register(Table_id),
admin.site.register(Accountant_frims),
admin.site.register(accountant)
admin.site.register(check_type),
admin.site.register(invoice_type),
admin.site.register(client_type),
admin.site.register(clients),
admin.site.register(table_ID_client),
admin.site.register(trial_Balance_item)