import json
import unittest
import requests


class StudentsTestCase(unittest.TestCase):
    base_url = "http://127.0.0.1:10000/api/v1/students/"

    last_student_id = requests.get(url=base_url).json().get("data")[0][0].get("student_id")

    def test_get_students(self):
        response = requests.get(url=self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "data": [
                [
                    {
                        "student_id": str(self.last_student_id),
                        "first_name": "string",
                        "last_name": "string",
                        "email": "user@example.com",
                        "age": 1,
                        "course_of_study": "string",
                        "study_year": 1
                    }
                ]
            ],
            "code": 200,
            "message": "Students data retrieved successfully"
        })

    def test_get_student_by_id(self):
        response = requests.get(url=self.base_url + str(self.last_student_id))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "data": [
                {
                    "student_id": str(self.last_student_id),
                    "first_name": "string",
                    "last_name": "string",
                    "email": "user@example.com",
                    "age": 1,
                    "course_of_study": "string",
                    "study_year": 1
                }
            ],
            "code": 200,
            "message": "Student data retrieved successfully"
        })

    def test_create_student(self):
        response = requests.post(url=self.base_url, data=json.dumps({
            "first_name": "string",
            "last_name": "string",
            "email": "user@example.com",
            "age": 1,
            "course_of_study": "string",
            "study_year": 1
        }))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "data": [
                {
                    "student_id": response.json().get("data")[0].get("student_id"),
                    "first_name": "string",
                    "last_name": "string",
                    "email": "user@example.com",
                    "age": 1,
                    "course_of_study": "string",
                    "study_year": 1
                }
            ],
            "code": 200,
            "message": "Student created successful"
        })

    def test_update_student(self):
        last_student_id_after_create = requests.get(url=self.base_url).json().get("data")[-1][-1].get("student_id")
        response = requests.put(url=self.base_url + str(last_student_id_after_create), data=json.dumps({
            "first_name": "string",
            "last_name": "string",
            "email": "user@example.com",
            "course_of_study": "string"
        }))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "data": [
                "Student with id: {} was successful updated".format(str(last_student_id_after_create))
            ],
            "code": 200,
            "message": "Student update successful"
        })

    def test_delete_student(self):
        last_student_id_after_create = requests.get(url=self.base_url).json().get("data")[-1][-1].get("student_id")
        response = requests.delete(url=self.base_url + str(last_student_id_after_create))
        self.assertEqual(response.status_code, 200)
