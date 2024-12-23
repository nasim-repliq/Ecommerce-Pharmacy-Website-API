from django.urls import path, include

urlpatterns = [
    path("", include('inventory.rest.urls.inventory'))
]

