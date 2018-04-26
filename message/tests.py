from django.test import TestCase
from django.test import Client
# Create your tests here.

client = Client()
response = client.get('/')
print(response.status_code)
print '123'

