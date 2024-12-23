# from django.urls import path
# from account.rest.views.account import OrganizationViewSet, PersonOrganizationViewSet

# urlpatterns = [
#     path('organizations/', OrganizationViewSet.as_view(), name='organization-list'),
#     path('organizations/<uuid:pk>/', OrganizationViewSet.as_view(), name='organization-detail'),
#     path('person-organizations/', PersonOrganizationViewSet.as_view(), name='person-organization-list'),
#     path('person-organizations/<uuid:pk>/', PersonOrganizationViewSet.as_view(), name='person-organization-detail'),
# ]


from django.urls import path
from account.rest.views.account import *


urlpatterns = [

    #-------------Organizations 
    path('organizations', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('organizations/<uuid:pk>', OrganizationDetailView.as_view(), name='organization-detail'),
    
    #-------------PersonOrganizations
    path('person-organizations', PersonOrganizationListCreateView.as_view(), name='person-organization-list-create'),
    path('person-organizations/<uuid:pk>', PersonOrganizationDetailView.as_view(), name='person-organization-detail'),

]

