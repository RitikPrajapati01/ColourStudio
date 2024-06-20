from django.contrib import admin
from .models import ImageData

# Register your models here.
@admin.register(ImageData)
class ModelAdmin(admin.ModelAdmin):
    list_display =('image',)