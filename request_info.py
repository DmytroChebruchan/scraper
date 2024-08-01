class RequestInfo:
    resource: str
    position: str
    experience: list
    salary_range: dict
    locations: list
    url: str = ""

    def __init__(
        self,
        resource: str,
        position: str,
        experience: list,
        min_salary: int,
        max_salary: int,
        locations: list,
    ):
        self.resource = resource
        self.experience = experience
        self.salary_range = {"from": min_salary, "to": max_salary}
        self.locations = locations
        self.position = position

    def url_generator(self):
        if self.url != "":
            return self.url

        url = self.resource + "/resumes-"

        if self.locations:
            url += "locations=" + "+".join(self.locations)

        if self.position:
            split_position_name = self.position.split(" ")
            url += "+".join(split_position_name) + "/?"

        if self.salary_range:
            url += (
                "salaryfrom="
                + str(self.salary_range["from"])
                + "&salaryto="
                + str(self.salary_range["to"])
            )
        if self.experience:
            url += "experience=" + "+".join(*self.experience)

        self.url = url
        return url
