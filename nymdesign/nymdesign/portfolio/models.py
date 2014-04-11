from django.db import models
import os
from django.template.defaultfilters import slugify 
from django.core.urlresolvers import reverse
from nymdesign import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    sort_order = models.IntegerField(default=1)
    
    class Meta:
        ordering = ('name', )
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

class MediaType(models.Model):
    name = models.CharField(max_length=200)
    sort_order = models.IntegerField(default=1)
    
    band_color = models.CharField(max_length=10, help_text='hex color such as "#006699"')
    project_bg_color = models.CharField('project title background color', max_length=10, help_text='hex color such as "#006699"')
    logo_name = models.CharField(max_length=255, help_text='logo file name (not the path) e.g. "logo_web.gif"')
    slug = models.SlugField(max_length=200, blank=True)
    description = models.TextField(blank=True, help_text='optional')
    
    
    def logo_preview(self):
        return '<img src="%s/imgs/logo/%s" width="40" />' % (settings.STATIC_URL, self.logo_name)
    logo_preview.short_description = 'Thumbnail'
    logo_preview.allow_tags = True
        
    def save(self):
        self.slug = slugify(self.name)
        super(MediaType, self).save()
    
    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category)

    website = models.URLField(blank=True)

    def get_projects(self):
        return Project.objects.filter(visible=True, client=self)

    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ('name', )


class ProjectTag(models.Model):
    name = models.CharField(max_length=200, unique=True)


    class Meta:
        ordering = ('name', )

    def __unicode__(self):
        return self.name

    
class Project(models.Model):  
    name = models.CharField(max_length=200)
    visible = models.BooleanField(default=False)
    is_showcase_item = models.BooleanField(default=True)

    project_url = models.URLField(blank=True)

    slug = models.SlugField(help_text='auto-filled on save', blank=True)
    client = models.ForeignKey(Client, null=True, blank=True)
    media_type = models.ForeignKey(MediaType)

    date_text = models.CharField(blank=True, max_length=200)
    date = models.DateTimeField('date published')

    description = models.TextField(blank=True)
      
    add_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    related_projects = models.ManyToManyField('self', null=True, blank=True)
    
    tags = models.ManyToManyField(ProjectTag, null=True, blank=True)
    
    def image_count(self):
        return ProjectImage.objects.filter(project=self).count()
    
    def get_absolute_url(self):
        return reverse('view_single_project', kwargs={ 'portfolio_slug': self.slug} )

    
    def get_absolute_url_for_admin(self):
        return '<a href="%s">view</a>' % self.get_absolute_url()
    get_absolute_url_for_admin.short_description = 'preview'
    get_absolute_url_for_admin.allow_tags = True
    
    def get_image_list(self):
        return ProjectImage.objects.filter(project=self)

    def save(self):
        self.slug = slugify(self.name)
        super(Project, self).save()
        
    def __unicode__(self):
        #if self.description:
        #    return '%s - %s' % (self.name, self.description)
        return self.name
        
    class Meta:
        ordering = ('name', )

def get_project_hm_strip_path(instance, filename):
    return os.path.join('imgs','hm_strip', instance.project.media_type.name, filename)

def get_project_cat_strip_path(instance, filename):
    return os.path.join('imgs','cat_strip', instance.project.media_type.name, filename)

class HomePageImage(models.Model):
    project =  models.ForeignKey(Project)
    name =  models.CharField(max_length=200, blank=True)
    img = models.ImageField(upload_to=get_project_hm_strip_path)
    visible= models.BooleanField(default=True)

    class Meta:
        ordering = ['project',  'name']

    def get_img_view(self):
        return '<a href="%s"><img src="%s" height="75" alt="%s" /></a>' % (self.img.url, self.img.url, self.img.url)
    get_img_view.short_description = 'preview'
    get_img_view.allow_tags = True

    def __unicode__(self):
        if self.name:
            return self.name
        return  '%s - %s' % (self.project, self.img)

class CategoryPageImage(models.Model):
    project =  models.ForeignKey(Project)
    name =  models.CharField(max_length=200, blank=True)
    img = models.ImageField(upload_to=get_project_cat_strip_path)
    visible= models.BooleanField(default=True)

    class Meta:
        ordering = ['project',  'name']

    def get_img_view(self):
        return '<a href="%s"><img src="%s" height="75" alt="%s" /></a>' % (self.img.url, self.img.url, self.img.url)
    get_img_view.short_description = 'preview'
    get_img_view.allow_tags = True

    def __unicode__(self):
        if self.name:
            return self.name
        return  '%s - %s' % (self.project, self.img)

def get_project_image_regular_path(instance, filename):
    return os.path.join('project_regular', instance.project.media_type.name, filename)

MAX_THUMB_WIDTH = 50                
class ProjectImage(models.Model):
    project =  models.ForeignKey(Project)
    label =  models.CharField(max_length=200, blank=True)
    regular = models.ImageField(max_length=255, upload_to=get_project_image_regular_path, width_field='iwidth', height_field='iheight')
    iwidth = models.IntegerField(default=-1, help_text='auto-filled on save')
    iheight = models.IntegerField(default=-1, help_text='auto-filled on save')
    sort_order = models.IntegerField(default=1)

    class Meta:
        ordering = ['project', 'sort_order', 'label']

    def save(self):
        #self.slug = slugify(self.name)
        super(ProjectImage, self).save()

    
    def get_thumbnail_view(self):
        return '<a href="%s"><img src="%s" width="75" alt="%s" /></a>' % (self.regular.url, self.regular.url, self.regular.url)
    get_thumbnail_view.short_description = 'preview'
    get_thumbnail_view.allow_tags = True


    def __unicode__(self):
        return '%s - %s' % (self.project, self.regular)
        if self.label is None:
            return '%s - %s' % (self.project, self.regular)
        return self.label        
        
'''
# open each image and save it's size
from PIL import Image
import os
from portfolio.models import *
from settings import MEDIA_ROOT
for p in ProjectImage.objects.all():
    if not os.path.isfile(p.regular.path):
        p.delete()
        
        print 'file not found: ', p.id, p.regular.path
    else:    
        im = Image.open(p.regular.path)
        w, h = im.size
        print w,h
        p.iwidth=w
        p.iheight=h
        #p.save()

'''        
        