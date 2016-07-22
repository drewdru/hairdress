from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
# from django.contrib.sitemaps.views import sitemap
# from textRPG import sitemaps
from main import views

urlpatterns = [
    # url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    #     name='django.contrib.sitemaps.views.sitemap'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^lang/$', views.lang),
]
urlpatterns += i18n_patterns(
    # url(r'^', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
)
