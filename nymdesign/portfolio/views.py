from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from nymdesign.utils.helper_vars import PAGE_CACHE_TIME
from django.views.decorators.cache import cache_page
from nymdesign.portfolio.models import *

@cache_page(PAGE_CACHE_TIME)
def view_homepage(request):
    """
    View home page
    """

    # retrieve homepage images
    homepage_imgs = HomePageImage.objects.all().order_by('?')[:6]

    lu = { 'homepage_imgs' : homepage_imgs
        , 'is_homepage' : True
        , 'media_types' : MediaType.objects.all().order_by('sort_order')
    }

    return render(request,
                  'portfolio/homepage.html',
                  lu)

@cache_page(PAGE_CACHE_TIME)
def view_media_category(request, media_type_slug):
    """
    View a category page for a media type
    """

    # retrieve media type
    try:
        selected_media_type = MediaType.objects.get(slug=media_type_slug)
    except:
        return HttpResponse('MediaType not found')

    # retrieve projects in same category
    category_projects = Project.objects.filter(media_type=selected_media_type, visible=True,  is_showcase_item=True)

    # retrieve category images
    category_imgs = CategoryPageImage.objects.filter(project__media_type__id=selected_media_type.id, project__is_showcase_item=True, visible=True).order_by('?')[:12]
    #from django.db import connection
    #print connection.queries

    #print category_imgs

    lu = { 'category_projects' :category_projects
        , 'category_imgs' : category_imgs
        , 'selected_media_type' : selected_media_type
        , 'media_types' : MediaType.objects.all().order_by('sort_order')

    }
    return render(request,
                  'portfolio/view_category.html',
                  lu)


@cache_page(PAGE_CACHE_TIME)
def view_single_project(request, portfolio_slug, image_number=1):
    """
    View a single project including it's images and other projects in that category
    """
    image_number = int(image_number)

    # retrieve the project
    try:
        project = Project.objects.get(slug=portfolio_slug,
                                      visible=True)
    except:
        return HttpResponse('project not found: %s' % portfolio_slug)

    # retrieve the images
    project_images = project.get_image_list()

    # set the selected image
    selected_image = None
    image_count = project_images.count()
    if project_images.count() > 0:
        if image_number > 0 and  project_images.count() >= image_number:
            selected_image = project_images[(image_number-1)]

    # retrieve projects in same category
    category_projects = Project.objects.filter(media_type=project.media_type, visible=True, is_showcase_item=True)


    lu = { 'p' : project
        , 'image_count' : image_count
        , 'image_number' : image_number
        , 'selected_image' : selected_image
        , 'project_images' : project_images
        , 'category_projects' :category_projects
        , 'selected_media_type' :  project.media_type
        , 'media_types' : MediaType.objects.all().order_by('sort_order')

    }
    return render(request,
                  'portfolio/view_single_project.html',
                  lu)
