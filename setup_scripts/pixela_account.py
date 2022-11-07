import requests

from config import PIXELA_USERNAME, PIXELA_TOKEN

"""
creates a new user account on Pixela API

*(request body)*

:param token: [required] Used to authenticate as a user to be created. It is hashed and saved
:type token: str
:param username: [required] User name for account
:type username: str
:param agreeTermsOfService: [required] Specify 'yes' or 'no' to whether you agree to the terms of service
:type agreeTermsOfService: str
:param notMinor: [required] Specify 'yes' or 'no' as to whether you are not a minor or if you are and you have parental consent
:type notMinor: str
:param thanksCode: [optional] set thanks-code
:type thanksCode: str
"""
requests.post('https://pixe.la/v1/users', json={
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
})
