from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}
        ),
        url(r'^static/(?P<path>.*)$',
            'django.views.static.serve',
                {'document_root': settings.STATIC_ROOT}
        ),

    )
