from django.contrib import admin
from .models import Product, Invoice #Book, Author, BookAdmin#, Publisher, WrittenBy


class ProductTabular(admin.TabularInline):
    model = Invoice.product.through

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [ProductTabular]
    exclude = ('product', )

    class Meta:
        model = Invoice


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Product)

#admin.site.register(Book)
#admin.site.register(BookAdmin)
#admin.site.register(Author)
#admin.site.register(Publisher)
#admin.site.register(WrittenBy)
