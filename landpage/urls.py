from django.urls import include
from django.urls import path, re_path
from . import views
# from django.contrib.sitemaps.views import sitemap
# from .sitemaps import StaticViewSitemap   

# sitemaps = {
#     'static': StaticViewSitemap,
# }
app_name = 'landpape'
urlpatterns = [

     #homepages 
     #nologing in required
    re_path(r'^$',views.main_page, name='main_page'),
    re_path(r'^land_page$', views.land_page, name='land_page'),
    re_path(r'^welcome/$', views.welcome, name='welcome'),
    re_path(r'^aboutus$', views.about_us, name='about_us'),
    re_path(r'^aboutus2$', views.about_us2, name='about_us2'),
    re_path(r'^whyfood4less$', views.whyfood4less, name='whyfood4less'),
    re_path(r'^news$', views.news, name='news'),
    re_path(r'^how_it_works$', views.how_it_works, name='how_it_works'),
    re_path(r'^faqs$', views.faqs, name='faqs'),
    re_path(r'^pricingtable$', views.pricingtable, name='pricingtable'),
    re_path(r'^contactus$', views.contact_us, name='contact_us'), 
  

    
    # re_path(r'^edit/', views.edit, name='edit'),
                  
#     # Off-Convas Stuff
#     re_path(r'^terms$', terms.terms_page, name='terms'),
#     re_path(r'^privacy', privacy.privacy_page, name='privacy'),
#     re_path(r'^forgot_password$', forgot_password.forgot_password_page, name='forgot_password'),
#     re_path(r'^reset_password$', forgot_password.reset_password, name='reset_password'),
                       
#     # Sitemap
#     re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
#     re_path(r'^captcha/', include('captcha.urls')),
]