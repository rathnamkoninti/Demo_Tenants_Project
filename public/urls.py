from django.contrib import admin
from django.urls import path
from public import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',views.greet,name='greet'),



]