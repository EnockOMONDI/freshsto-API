from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from . import views

app_name = 'shop'


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^welcome/', views.welcome, name='welcome'),
    url(r'^vendorrequest/', views.vendorrequest, name='vendorrequest'),
    url(r'^Vendorfaqs/', views.Vendorfaqs, name='Vendorfaqs'),
    url(r'^log/', views.log, name='log'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^mens/', views.mens, name='mens'),
    url(r'^womens/', views.womens, name='womens'),
    url(r'^decorbeauty/', views.decorbeauty, name='decorbeauty'),
    url(r'^homeaccesories/', views.homeaccesories, name='homeaccesories'),
    url(r'^negotiate/price/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.client_price, name='client_price'),
    url(r'^shop/', views.product_list, name='product_list'),
    url(r'^negotiate/(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.negotiate, name='negotiate'),

   
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail, name='product_detail'),

    url(r'^(?P<subcategory_slug>[-\w]+)/$',
        views.subcategory_list, name='product_list_by_subcategory'),
    url(r'^(?P<minicategory_slug>[-\w]+)/$',
        views.minicategory_list, name='product_list_by_minicategory')




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
