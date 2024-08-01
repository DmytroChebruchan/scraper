import unittest
from request_info import RequestInfoWorkUa


class TestRequestInfoWorkUa(unittest.TestCase):

    def setUp(self):
        self.request_info = RequestInfoWorkUa(
            resource="https://www.work.ua/jobs-",
            position="Python Developer",
            experience=["0"],
            min_salary=1000,
            max_salary=3000,
            location="kyiv"
        )

    def test_url_generator(self):
        expected_url = (
            "https://www.work.ua/jobs-"
            "kyiv-"
            "Python+Developer/?"
            "salaryfrom=1000&salaryto=3000"
            "experience=0"
        )
        self.assertEqual(self.request_info.url_generator(), expected_url)

    def test_url_generator_no_location(self):
        self.request_info.location = ""
        expected_url = (
            "https://www.work.ua/jobs-"
            "Python+Developer/?"
            "salaryfrom=1000&salaryto=3000"
            "experience=0"
        )
        self.assertEqual(self.request_info.url_generator(), expected_url)

    def test_url_generator_no_salary(self):
        self.request_info.salary_range = None
        expected_url = (
            "https://www.work.ua/jobs-"
            "kyiv-"
            "Python+Developer/?"
            "experience=0"
        )
        self.assertEqual(expected_url, self.request_info.url_generator())

    def test_url_generator_no_experience(self):
        self.request_info.experience = []
        expected_url = (
            "https://www.work.ua/jobs-"
            "kyiv-"
            "Python+Developer/?"
            "salaryfrom=1000&salaryto=3000"
        )
        self.assertEqual(self.request_info.url_generator(), expected_url)

    def test_url_generator_with_existing_url(self):
        self.request_info.url = "https://existing.url"
        self.assertEqual(self.request_info.url_generator(), "https://existing.url")


if __name__ == "__main__":
    unittest.main()
