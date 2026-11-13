from django.urls import path
from api import views
urlpatterns = [
    path("add_employee/",views.EmployeeCrudOperation.as_view(),name = "add_employee")
]