from django.urls import path
from ayat import views
urlpatterns = [
    path("home",views.Home.as_view(),name="home")
]