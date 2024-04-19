from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from students.schemas import *
from students.CRUD_operations import *

students_router = APIRouter(prefix="/students", tags=["students"])


@students_router.get("/", response_description="Students retrieved")
async def list_students():
    students = await retrieve_students()
    if students:
        return response_model(students, "Students data retrieved successfully")
    return response_model(students, "Empty list returned")


@students_router.get("/{student_id}", response_description="Student retrieved")
async def get_student(student_id):
    student = await retrieve_student(student_id)
    if student:
        return response_model(student, "Student data retrieved successfully")
    return error_response_model("An error occurred.", 404, "Student doesn't exist.")


@students_router.post("/", response_description="Student data added into the database")
async def create_student(student_data: StudentSchema):
    student = jsonable_encoder(student_data)
    new_student = await add_student(student)
    return response_model(new_student, "Student created successful")


@students_router.post("/{student_id}")
async def update_student_data(student_id, student_data: UpdateStudentSchema):
    student_data = {k: v for k, v in student_data.dict().items() if v is not None}
    updated_student = await update_student(student_id, student_data)
    if updated_student:
        return response_model(
            "Student with id: {} was successful updated".format(student_id),
            "Student update successful"
        )
    return error_response_model(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@students_router.delete("/{student_id}")
async def delete_student_data(student_id):
    deleted_student = await delete_student(student_id)
    if deleted_student:
        return response_model(
            "Student with id: {} was successful deleted".format(student_id),
            "Student delete successful"
        )
    return error_response_model(
        "An error occurred",
        404,
        "Student with id: {} doesn't exists".format(student_id),
    )

