from django.contrib import admin
from django.urls import path
from private import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greetings/',views.greetings,name='greetings'),
    path('greetings1/',views.greetings1,name='greetings1'),
    path('greetings2/',views.greetings2,name='greetings2'),
    path('greetings3/',views.greetings3,name='greetings3'),



]