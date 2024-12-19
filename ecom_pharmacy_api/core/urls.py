from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

    path('users', PersonListCreateView.as_view(), name='person-list-create'),
    path('users/<int:pk>', PersonDetailView.as_view(), name='person-detail'),
    path('auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

]


    # #-------------Organizations 
    # path('organizations/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    # path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization-detail'),
    
    # #-------------PersonOrganizations
    # path('person-organizations/', PersonOrganizationListCreateView.as_view(), name='person-organization-list-create'),
    # path('person-organizations/<int:pk>/', PersonOrganizationDetailView.as_view(), name='person-organization-detail'),
