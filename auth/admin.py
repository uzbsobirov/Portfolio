from django.contrib import admin
from .models import Register

uneditable_fields = ('id')

@admin.register(Register)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'status',
        'description',
        'product_id',
        'category'
    )
    fields = [field.name for field in Register._meta.fields if field.name not in uneditable_fields]