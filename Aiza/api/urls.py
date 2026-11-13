from django.urls import path
from api import views
urlpatterns = [
    path("add_emp/",views.EmployeeView.as_view(),name="add_emp")
]