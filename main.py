from request_info import RequestInfo
import requests


def main():
    request_info = RequestInfo()
    url_generated = request_info.url_generator()
    # request = requests.get(url=request_info.url_generator())
    print(url_generated)


if __name__ == "__main__":
    main()
