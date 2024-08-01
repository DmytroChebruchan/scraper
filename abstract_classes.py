from abc import ABC


class RequestInfoBase(ABC):
    resource: str
    position: str
    experience: list
    salary_range: dict
    location: str
    url: str = ""

    def url_generator(self):
        raise NotImplementedError
