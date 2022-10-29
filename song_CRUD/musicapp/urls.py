from django.urls import path

from.views import index

urlpatterns = [
    path("", index, name="index")
    #Note: we can add home here:path("home/", index, name="index")
]