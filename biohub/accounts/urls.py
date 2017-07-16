from rest_framework.routers import DefaultRouter

from biohub.core.routes import register_api, url

from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

register_api(r'^', [
    url(r'^users/register/$', views.register, name='register'),
    url(r'^users/login/$', views.login, name='login'),
    url(r'^users/logout/$', views.logout, name='logout'),
] + router.urls, 'accounts')