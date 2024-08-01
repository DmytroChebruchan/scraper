from constants import sources
from request_info import RequestInfoWorkUa


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
    print(url_generated)
