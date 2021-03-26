from django.contrib import admin
from .models import Pic
# Register your models here.
@admin.register(Pic)
class ImageAdmin(admin.ModelAdmin):
 list_display = ['id', 'image', 'date','description']