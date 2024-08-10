from constants import sources
from request_info import RequestInfoWorkUa
import requests


def fetch_cvs():
    resource = sources["work.ua"]

    request_info_dict = {
        "resource": resource,
        "position": "Python developer",
        "experience": [],
        "min_salary": 1,
        "max_salary": 2,
        "location": "remote",
        # "locations": ["Odessa", "Lviv"],
    }
    request_info = RequestInfoWorkUa(**request_info_dict)
    url_generated = request_info.url_generator()
    print(f'address is {url_generated}')
    request = requests.get(url=url_generated)
    print(f"status code is {request.status_code}")
    return request.status_code
