"""linky URL Configuration

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
from django.contrib.auth.decorators import login_required as auth
from django.contrib import admin
from linkey.views import LinkListView
from django.contrib.auth.views import login, logout_then_login
from linkey.views import UserProfileDetailView, UserProfileEditView, LinkCreateView, LinkDetailView, LinkUpdateView, LinkDeleteView, VoteFormView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LinkListView.as_view(), name='home'),
    url(r'^login/$', login, {"template_name" : 'login.html'}, name='login'),
    url(r'^logout/$',logout_then_login, name='logout'),
    url(r'^accounts/', include("registration.backends.simple.urls")),
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name="profile" ),
    url(r'edit_profile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),
    url(r'^link/create/$', auth(LinkCreateView.as_view()), name='link_create'),
    url(r'^link/(?P<pk>\d+)/$', LinkDetailView.as_view(), name='link_detail'),
    url(r'^link/update/(?P<pk>\d+)/$', auth(LinkUpdateView.as_view()), name='link_update'),
    url(r'^link/delete/(?P<pk>\d+)/$', auth(LinkDeleteView.as_view()), name='link_delete'),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^vote/$', auth(VoteFormView.as_view()), name="vote"),
]
