from django.contrib import admin

# Register your models here.
from product.models import Category, Cars, Images

class CarImageInline(admin.TabularInline):
    model =  Images
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ["status","parent"]
    readonly_fields = ('image_tag',)

class CarsAdmin(admin.ModelAdmin):
    list_display = ['title',"category","price","amount",'status']
    readonly_fields = ('image_tag',)
    list_filter = ["status","category"]
    inlines = [CarImageInline]

class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title',"car","image_tag"]
    readonly_fields = ('image_tag',)

admin.site.register(Category,CategoryAdmin)
admin.site.register(Cars,CarsAdmin)
admin.site.register(Images,ImagesAdmin)