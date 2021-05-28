from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('dashboard/<str:user>/', views.dashboard , name = "dashboard"),
    path('signup/', views.signup, name = "signup"),
    path('newlead/<str:user>', views.newlead, name = "newlead"),
    path('profile/<str:user>/', views.profile, name = "profile"),
    path('assigned/<str:user>/', views.assigned, name = "assigned"),
    path('submitted/<str:user>/', views.submitted, name = "submitted"),
    path('update/<str:user>/<str:status>/<str:id>/<str:origin>/', views.update, name = "update"),
    path('export/<str:user>/', views.export, name = "export"),
]