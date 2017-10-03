from django.contrib import admin
from .models import Category, Product


# ACTIONS
def export_as_json(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type="application/json")
    response['Content-Disposition'] = 'attachment; filename={}.json'.format(opts.verbose_name)
    serializers.serialize("json", queryset, stream=response)
    return response
export_as_json.short_description = 'Export to JSON'

# Register your models here.
class ShopApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'updated', 'created']
    list_editable = ['name']
    list_filter = ['name', 'updated', 'created']
    prepopulated_fields = {'slug': ('name',)}
    actions = [export_as_json]
    
admin.site.register(ShopApplication, ShopApplicationAdmin)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    actions = [export_as_json]
    
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    actions = [export_as_json]
    
admin.site.register(Product, ProductAdmin)
