from django.contrib import admin
from nymdesign.portfolio.models import *


class CategoryAdmin(admin.ModelAdmin):
    save_on_top = True
    fields = ('name', 'sort_order',)
    
admin.site.register(Category, CategoryAdmin)

class MediaTypeAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'slug', 'logo_name','logo_preview', 'sort_order', 'description',)
admin.site.register(MediaType, MediaTypeAdmin)

class ClientAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'description','category', 'website',)
    list_filter = ('category',)
    
admin.site.register(Client, ClientAdmin)

class ProjectTagAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name',)
    
admin.site.register(ProjectTag, ProjectTagAdmin)

class HomePageImageInline(admin.TabularInline):
    model = HomePageImage
    fields = ('project', 'name','img', 'visible',)
    max_num=1

class CategoryPageImageInline(admin.TabularInline):
    model = CategoryPageImage
    fields = ('project', 'name','img', 'visible',)
    max_num=1

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    fields = ('project', 'label','regular', )
    
class ProjectAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name', 'get_absolute_url_for_admin','image_count', 'date', 'client','media_type', 'visible', 'update_date',)
    search_fields = ('name',)
    list_filter = ('visible','is_showcase_item', 'client', 'media_type', 'tags', )
    inlines = (ProjectImageInline, CategoryPageImageInline, HomePageImageInline, )
    filter_vertical = ('related_projects', 'tags',)
admin.site.register(Project, ProjectAdmin)

class ProjectImageAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('project', 'get_thumbnail_view', 'label','regular', 'iwidth', 'iheight')
    list_filter = ('project',)
admin.site.register(ProjectImage, ProjectImageAdmin)

class HomePageImageAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('project', 'name', 'img','get_img_view', 'visible', )
    list_filter = ('visible', 'project',)
admin.site.register(HomePageImage, HomePageImageAdmin)

class CategoryPageImageAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('project', 'name', 'img','get_img_view', 'visible', )
    list_filter = ('visible','project',)
admin.site.register(CategoryPageImage, CategoryPageImageAdmin)