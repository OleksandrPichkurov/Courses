from django.test import TestCase

import datetime

from .models import Course

# Create your tests here.


class AliasModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        start_date = datetime.datetime(2021, 5, 17)
        end_date = datetime.datetime(2021, 6, 17)
        start_date_java = datetime.datetime(2021, 7, 17)
        end_date_java = datetime.datetime(2021, 8, 17)

        cls.course = Course.objects.create(
            name="Python basic",
            start_date=start_date,
            end_date=end_date,
            number_of_lectures=22,
        )
        cls.course = Course.objects.create(
            name="Java basic",
            start_date=start_date_java,
            end_date=end_date_java,
            number_of_lectures=40,
        )

    def test_get_courses_list(self):
        response = self.client.get("/api/courses/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), [{"name": "Python basic"}, {"name": "Java basic"}]
        )

    def test_get_detail_of_course(self):
        response = self.client.get("/api/courses/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "name": "Python basic",
                "start_date": "2021-05-17",
                "end_date": "2021-06-17",
                "number_of_lectures": 22,
            },
        )

    def test_post_course(self):
        response = self.client.post(
            "/api/courses/",
            {
                "name": "Golang",
                "start_date": "2021-07-17",
                "end_date": "2021-08-17",
                "number_of_lectures": 50,
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            {
                "name": "Golang",
                "start_date": "2021-07-17",
                "end_date": "2021-08-17",
                "number_of_lectures": 50,
            },
        )

    def test_put_course(self):
        response = self.client.put(
            "/api/courses/1/",
            {
                "name": "Python basic!!!",
                "start_date": "2021-05-17",
                "end_date": "2021-06-17",
                "number_of_lectures": 22,
            },
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get("/api/courses/1/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "name": "Python basic!!!",
                "start_date": "2021-05-17",
                "end_date": "2021-06-17",
                "number_of_lectures": 22,
            },
        )

    def test_delete_courses(self):
        response = self.client.delete("/api/courses/2/")
        self.assertEqual(response.status_code, 204)
        response = self.client.get("/api/courses/2/")
        self.assertEqual(response.status_code, 404)

    def test_search_courses(self):
        response = self.client.get("/api/courses/?search=java")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"name": "Java basic"}])

    def test_filtering_by_date_courses_for_one_match(self):
        response = self.client.get(
            "/api/courses/?start_date=2021-07-01&end_date=2021-08-30"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [{"name": "Java basic"}])

    def test_filtering_by_date_courses_for_more_match(self):
        response = self.client.get(
            "/api/courses/?start_date=2021-04-01&end_date=2021-08-30"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(), [{"name": "Python basic"}, {"name": "Java basic"}]
        )
