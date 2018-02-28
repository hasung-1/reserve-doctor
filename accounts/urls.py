from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from .views import SignUpView

urlpatterns=[
    url(r'^login/$',auth_views.login,name='login',kwargs={
        'template_name':'accounts/login_form.html',
    }),
    url(r'^logout/$', auth_views.logout, name='logout',kwargs={
        'next_page':'/'
    }),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^signup/$',SignUpView.as_view(),name='signup'),
]