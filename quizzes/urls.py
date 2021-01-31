from django.urls import path
from django.conf.urls import url
from . import views
from django.urls import include
from rest_framework import routers


#
# router = routers.DefaultRouter()
# router.register(r'book', PytaniaViewSet)

urlpatterns = [
    path('', views.home, name="home"),
    path('start_test', views.start_test, name="test_arkusz"),
    # url(r'^', include(router.urls)),
    # url(r'^pytanie/', include('rest_framework.urls', namespace='rest_framework'))
]