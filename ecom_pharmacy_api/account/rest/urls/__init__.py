from django.urls import path, include

urlpatterns = [
    path("", include("account.rest.urls.account"))
]

# from .account import urlpatterns as account_urls
# urlpatterns = account_urls