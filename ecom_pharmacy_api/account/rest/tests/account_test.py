# from rest_framework.test import APITestCase
# from rest_framework import status
# from account.models import Organization, PersonOrganization

# class OrganizationTestCase(APITestCase):
#     def test_create_organization(self):
#         data = {'shop_name': 'Test Shop', 'address': '123 Test Street', 'phone_number': '1234567890'}
#         response = self.client.post('/api/v1/account/organizations/', data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

# class PersonOrganizationTestCase(APITestCase):
#     def test_create_person_organization(self):
#         # Assuming relevant test setup with user and organization
#         data = {'user': 1, 'shop': 1, 'role': 'owner'}
#         response = self.client.post('/api/v1/account/person-organizations/', data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# python manage.py test account.rest.tests
