import requests

from config import PIXELA_USERNAME, PIXELA_TOKEN


requests.post('https://pixe.la/v1/users', json={
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
})
