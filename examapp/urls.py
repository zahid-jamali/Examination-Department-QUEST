from django.contrib import admin
from django.urls import path, include
from examapp  import views
urlpatterns = [
	path('', views.index, name='home'),
    path('circular', views.circular_func, name="circular"),
	path('gallery', views.gallery, name='gallery'),
    path('faculty', views.facultyfunc, name='faculty'),
    path('contactus', views.contactus, name='contactus'),
    path("facultyinfo", views.facultyinfo, name='facultyinto'),
    path("registeration", views.registeration, name="registeration"),
    path("download", views.download, name='download'),
    path("faq", views.faqfunc, name="faqfunc"),
    path("examination", views.examinationfunc, name='examination')
]
