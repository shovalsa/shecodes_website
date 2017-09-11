"""sc_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from scsite.views import index, members, members_index, tracks, branches, faq, team, contact, partners, \
    next_generation, about, jobs, signup, newsletter, newsletter_index
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.conf.urls.i18n import i18n_patterns
# from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

js_info_dict = {
    'packages': ('scsite',)
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="home"),
    url(r'^members/(?P<id>[^/]+)/$', members),
    url(r'^members/$', members_index, name="members"),
    url(r'^tracks/$', tracks, name="tracks"),
    url(r'^career-center/$', jobs, name="jobs"),
    url(r'^branches/$', branches, name="branches"),
    url(r'^next-generation/$', next_generation),
    url(r'^faq/$', faq),
    url(r'^team/$', team),
    url(r'^newsletter/(?P<id>[^/]+)/$', newsletter),
    url(r'^newsletter/$', newsletter_index, name='newsletter'),
    url(r'^about/$', about),
    url(r'^contact/$', contact),
    url(r'^partners/$', partners),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^$', TemplateView.as_view(template_name='static_pages/index.html'), #this is for defining 'home' in settings.py
        name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^he/', include('django.conf.urls.i18n')), # this enables the set language redirect view
    # url(r'^jsi8n/$', 'django.views.i18n.javascript_catalog', js_info_dict),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # this is unsafe in production. Replace!

"""The following adds /en/ or /he/ to the URL. However, for the moment it causes a bug that
when /en/ is added to the url, the switch to hebrew doesn't work.
 """
# urlpatterns += i18n_patterns(
#     url(r'^$', index, name="home"),
#     url(r'^members/(?P<id>[^/]+)/$', members),
#     url(r'^members/$', members_index, name="members"),
#     url(r'^tracks/$', tracks, name="tracks"),
#     url(r'^career-center/$', jobs, name="jobs"),
#     url(r'^branches/$', branches, name="branches"),
#     url(r'^next-generation/$', next_generation),
#     url(r'^faq/$', faq),
#     url(r'^team/$', team),
#     url(r'^about/$', about),
#     url(r'^contact/$', contact),
#     url(r'^partners/$', partners),
#     url(r'^login/$', auth_views.login, name='login'),
#     url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
#     url(r'^$', TemplateView.as_view(template_name='static_pages/index.html'), #this is for defining 'home' in settings.py
#         name='home'),
#     url(r'^signup/$', signup, name='signup'),
#     )

urlpatterns += staticfiles_urlpatterns()