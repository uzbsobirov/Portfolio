from django.contrib import admin
from .models import RegisterModel

uneditable_fields = ('id')

@admin.register(RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'status',
        'description',
        'product_id',
        'category'
    )
    fields = [field.name for field in RegisterModel._meta.fields if field.name not in uneditable_fields]