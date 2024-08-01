class RequestInfo:
    resource: str
    years_of_experience_min: int
    years_of_experience_max: int
    skills: list
    keywords: list
    salary_range: dict
    locations: list
    url: str = ""

    def __init__(self):
        self.resource = ""
        self.years_of_experience_min = 0
        self.years_of_experience_max = 0
        self.skills = []
        self.keywords = []
        self.salary_range = {"from": 0, "to": 1}
        self.locations = []

    def url_generator(self):
        if self.url != "":
            return self.url

        url = self.resource
        url += "/?keywords="
        self.url = url
        return url
