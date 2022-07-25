
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="labourHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("login/", views.login, name="Login"),
    path("search/", views.search, name="Search"),
    path("privacy/", views.privacy, name="PrivacyView"),
    path("jobs/", views.jobs, name="Jobs"),
    path("services/", views.services, name="services"),
]

