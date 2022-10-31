import requests
import random

ACTIVITY_IDS = range(1, 11)


def get_activity_by_id(activity_id):
    response = requests.get(f"http://127.0.0.1:8002/activity/{activity_id}")
    activity = response.json()
    return activity


# def get_activity_by_name(activity_name):
#     response = requests.get(f"http://127.0.0.1:8002/activity/{activity_name}")
#     activity = response.json()
#     return activity


def get_random_activity_list():
    random_activity_ids = random.sample(ACTIVITY_IDS, 1)
    random_activity = [get_activity_by_id(activity_id) for activity_id in random_activity_ids]
    return random_activity
