from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.EmpListAPIView.as_view()),
    path('create/', views.EmpCreteAPIView.as_view()),
    path('retrive/<int:id>/', views.EmpRetriveAPIView.as_view()),
    path('update/<int:id>/', views.EmpUpdateAPIView.as_view()),
    path('destroy/<int:id>/', views.EmpDestroyAPIView.as_view()),
    path('lc/', views.EmployeeListCreateAPIView.as_view()),
    path('ru/<int:id>/', views.EmployeeRetrieveUpdateAPIView.as_view()),
    path('rd/<int:id>/', views.EmployeeRetrieveDestroyAPIView.as_view()),
    path('rud/<int:id>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
]