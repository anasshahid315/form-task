
from django.contrib import admin
from django.urls import path
from mainApp import views
# from mainApp.views import homePage, get_states, get_cities



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path("delete/<int:num>/", views.deletePage),
    path("update/<int:num>/", views.updatePage),
    path("data/", views.dataPage)
]
