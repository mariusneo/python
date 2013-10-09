from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import books.views
import contact.views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'booksite.views.home', name='home'),
    # url(r'^booksite/', include('booksite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^latest/$', books.views.latest_books),
    url(r'^hello/$', books.views.hello),
    url(r'^now/$', books.views.current_date),
    url(r'^$', books.views.hello),
    url(r'time/plus/(\d{1,2})/$', books.views.hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search-form/$', books.views.search_form),
    url(r'^search/$', books.views.search),
    url(r'^contact-form/$', contact.views.contact_form),
    url(r'^contact/$', contact.views.contact),

)
