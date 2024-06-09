from django.contrib import admin
from .models import Myfile
# Register your models here.
@admin.register(Myfile)
class FileAdmin(admin,ModelAdmin):
    list_display=['id','file']