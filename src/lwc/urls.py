from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^admin', include(admin.site.urls)), 						# Admin page
    url(r'^$', 'joins.views.home', name='home'), 
    url(r'^importdata$', 'joins.views.importdata', name='home'),
    url(r'^gettickdata$', 'joins.views.getTickData', name='home'),
    url(r'^pychart/(?P<ref_id>.*)$', 'joins.views.pychart', name='share'),
    url(r'^pychart', 'joins.views.pycharthome', name='share'),						# Home Page
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),	# Share page


    #url(r'^home2/$', 'joins.views.home2', name='home2'),
    #url(r'^home2/$', 'lwc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


)
