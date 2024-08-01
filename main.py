from request_info import RequestInfo


def main():
    request_info_dict = {
        "resource": "work.ua",
        "position": "Python developer",
        "experience": [],
        "min_salary": 1,
        "max_salary": 2,
        "locations": [],
        # "locations": ["Odessa", "Lviv"],
    }
    request_info = RequestInfo(**request_info_dict)
    url_generated = request_info.url_generator()
    print(url_generated)

    # request = requests.get(url=request_info.url_generator())


if __name__ == "__main__":
    main()
