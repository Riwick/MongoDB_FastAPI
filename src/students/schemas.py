from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    age: int = Field(gt=0)
    course_of_study: str
    study_year: int = Field(gt=0, lt=9)

    class Config:
        schema_extra= {
            "example": {
                "first_name": "string",
                "last_name": "string",
                "email": "example@example.com",
                "age": 1,
                "course_of_study": "Computer modeling",
                "study_year": 1,
            }
        }


class UpdateStudentSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "first_name": "string1",
                "last_name": "string1",
                "email": "example1@example.com",
                "age": 2,
                "course_of_study": "Computer modeling and programming",
                "study_year": 2,
            }
        }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }


def error_response_model(error, code, message):
    return {
        "error": error,
        "code": code,
        "messsage": message
    }