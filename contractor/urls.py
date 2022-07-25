
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ContractorHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("privacy/", views.privacy, name="PrivacyView"),
    path("checkout/", views.checkout, name="Checkout"),
]

