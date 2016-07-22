from django.conf.urls import url
from django.contrib import admin
from main import views
from main.views import requires_login
urlpatterns = [
    url(r'^$', views.home),    
    url(r'^accounts/login/$',  'django.contrib.auth.views.login', {
        'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {
        'next_page': '/'}),
    url(r'^search/$', views.search),
    url(r'^contact/$', views.contact),
    #(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', views.month_archive),
    url(r'^calendar/(?P<user>\w+)$', requires_login(views.user_day_view)),
    url(r'^calendar/(?P<month>\w{3})/(?P<day>\d\d)/$', views.day_view),        
]
#url('^', include('django.contrib.auth.urls')), 
#This will include the following URL patterns:
# ^login/$ [ ']
# ^logout/$ [name='logout']
# ^password_change/$ [name='password_change']
# ^password_change/done/$ [name='password_change_done']
# ^password_reset/$ [name='password_reset']
# ^password_reset/done/$ [name='password_reset_done']
# ^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
# ^reset/done/$ [name='password_reset_complete']