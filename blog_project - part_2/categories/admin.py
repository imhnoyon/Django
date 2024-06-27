from django.contrib import admin
from . import models
# Register your models here.

# admin.site.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('Category_name',)}
    list_display=['Category_name','slug']

admin.site.register(models.Category,CategoryAdmin)