from django.contrib import admin
from .models import Service, Testimonial, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "available", "created", "updated"]
    list_filter = ["available", "created", "updated"]
    prepopulated_fields = {"slug": ("title",)}

# Register your models here.
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(Product, ProductAdmin)