from abstract_classes import RequestInfoBase


class RequestInfoInit(RequestInfoBase):

    def __init__(
        self,
        resource: str,
        position: str,
        experience: list,
        min_salary: int,
        max_salary: int,
        location: str,
    ):
        self.resource = resource
        self.experience = experience
        self.salary_range = {"from": min_salary,
                             "to": max_salary}
        self.location = location
        self.position = position


class RequestInfoWorkUa(RequestInfoInit):

    def url_generator(self):
        if self.url != "":
            return self.url

        url = self.resource

        if self.location:
            url += self.location + "-"

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


class RequestInfoRabotaUa(RequestInfoInit):

    def url_generator(self):
        pass
