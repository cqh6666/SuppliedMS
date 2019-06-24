"""SuppliedMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
import xadmin

from users.views import IndexView,LoginView,RegisterView,CommentView,AddCommentView,tableView,LogoutView,UserShow,UserModify,UserAuthShow,GrantUserAuth
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^search/$',IndexView.as_view(),name="search"),
    url(r'^login/', LoginView.as_view(),name="login"),
    url(r'^register/', RegisterView.as_view(),name="register"),
    url(r'^logout/', LogoutView.as_view(),name="logout"),
    url(r'^UserShow/', UserShow.as_view(),name="UserShow"),
    url(r'^UserModify',UserModify.as_view(),name="UserModify"),
    url(r'^Comment/',CommentView.as_view(),name="Comment"),
    url(r'^addComment',AddCommentView.as_view(),name="addComment"),
    url(r'^table/',tableView.as_view(),name="table"),

    url(r'^user_auth',UserAuthShow.as_view(),name="user_auth"),
    url(r'^grant_user_auth',GrantUserAuth.as_view(),name="grant_user_auth"),

    url(r'^supplied/', include('supplied.urls',namespace="supplied")),

]

