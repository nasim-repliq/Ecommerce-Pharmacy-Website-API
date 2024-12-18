from django.urls import path
from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('people/', PersonListCreateView.as_view(), name='person-list-create'),
    path('people/<int:pk>/', PersonDetailView.as_view(), name='person-detail'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('organizations/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),

]
