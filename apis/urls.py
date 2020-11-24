from django.urls import path
from .views import ListTravelBlog, DetailTravelBlog,ListTravelPlace,DetailTravelPlace,ListFood,DetailFood,ListDrama,DetailDrama,ListAbout,DetailAbout

urlpatterns = [
    path('', ListTravelBlog.as_view()),
    path('<int:pk>/', DetailTravelBlog.as_view()),
    path('place/', ListTravelPlace.as_view()),
    path('place_detail/<int:pk>/', DetailTravelPlace.as_view()),
    path('food/', ListFood.as_view()),
    path('food_detail/<int:pk>/', DetailFood.as_view()),
    path('drama/', ListDrama.as_view()),
    path('drama_detail/<int:pk>/', DetailDrama.as_view()),
    path('about/', ListAbout.as_view()),
    path('about_detail/<int:pk>/', DetailAbout.as_view()),
]