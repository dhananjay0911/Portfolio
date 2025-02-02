from django.urls import path
from .import views
urlpatterns=[
    path("",views.home,name="home"),
    path("about/", views.about,name="about"),
    path("projects/",views.projects,name="projects"),
    path("experience/",views.experience,name="experience"),
    path("Certificate/",views.Certificate,name="Certificate"),
    path("Contact/",views.Contact,name="Contact"),
    path("Resume",views.Resume,name="Resume"),
] 