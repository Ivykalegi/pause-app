import requests

from config import PIXELA_USERNAME, PIXELA_TOKEN


def create_graph(user_id):
    """
    creates new pixelation graph definition for users

    *(API used: Pixela)*

    :param user_id: the id of the user to create graph
    :type user_id: int
    """
    requests.post(f'https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs', headers={
        'X-USER-TOKEN': PIXELA_TOKEN,
    }, json={
        'id': f'p{user_id}',
        'name': 'Total Study Time',
        'unit': 'minutes',
        'type': 'int',
        'color': 'ichou',
    })


def get_graph(user_id):
    """
    gets pixelation graph definition for users
    tries to get the graph with the user_id , excepts RequestException and returns 'no graph to show'

    *(API used: Pixela)*

    :param user_id: the id of the user to get graph
    :type user_id: int
    """
    try:
        response = requests.get(f'https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/p{user_id}', headers={
            'X-USER-TOKEN': PIXELA_TOKEN,
        }, params={
            'appearance': 'dark',
            'mode': 'short',
        })
        response.raise_for_status()
        return response.text.split('\n', 3)[-1]
    except requests.exceptions.RequestException:
        return "No graph to show"


def add_session_to_graph(user_id, session_date, session_duration):
    """
    adds pixelation graph definition for longer/continued session
    tries until status code is not 503, then adds new session to the existing session

    *(API used: Pixela)*

    :param user_id: the id of the user to get graph
    :type user_id: int
    :param session_date: the date of the user began/continued the study session
    :type session_date: datetime
    :param session_duration: the time in minutes the study session lasted/continued
    :type session_duration: int
    """
    try:
        while True:
            response = requests.get(
                f'https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/p{user_id}/{session_date.strftime("%Y%m%d")}',
                headers={
                    'X-USER-TOKEN': PIXELA_TOKEN,
                })
            if response.status_code != 503:
                response.raise_for_status()
                break
    except requests.exceptions.RequestException:
        while True:
            response = requests.post(f'https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/p{user_id}', headers={
                'X-USER-TOKEN': PIXELA_TOKEN,
            }, json={
                'date': session_date.strftime("%Y%m%d"),
                'quantity': str(session_duration),
            })
            if response.status_code != 503:
                break
    else:
        existing_data = response.json()
        existing_quantity = int(existing_data.get('quantity'))
        while True:
            response = requests.put(
                f'https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/p{user_id}/{session_date.strftime("%Y%m%d")}',
                headers={
                    'X-USER-TOKEN': PIXELA_TOKEN,
                }, json={
                    'quantity': str(existing_quantity + session_duration),
                })
            if response.status_code != 503:
                break
