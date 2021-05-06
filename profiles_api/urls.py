from django.urls import path, include

from profiles_api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('hello_viewset', views.HelloViewSet, base_name='hello_viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))

]
