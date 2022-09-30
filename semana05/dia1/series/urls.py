from django.urls import include,path
from rest_framework import routers
from . import views


router=routers.DefaultRouter()
router.register(r'seriesapi',views.SerieViewSet)


urlpatterns=[
    path('', include(router.urls))
]