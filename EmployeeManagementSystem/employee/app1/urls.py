

from django.urls import path

from .views import EmployeeList, EmployeeDetailView

urlpatterns = [
    path('Employee/',EmployeeList.as_view(),name='employee'),
    path("detail/<int:pk>",EmployeeDetailView.as_view(),name='detail')

]
