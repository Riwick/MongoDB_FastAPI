from bson import ObjectId

from database import student_collection, student_helper


async def retrieve_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students


async def add_student(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


async def retrieve_student(student_id: str) -> dict:
    student = await student_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        return student_helper(student)


async def update_student(student_id: str, student_data: dict):
    if len(student_id) < 1:
        return False
    student = await student_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        updated_student = await student_collection.update_one(
            {"_id": ObjectId(student_id)}, {"$set": student_data}
        )
        if updated_student:
            return True
        return False
    return False


async def delete_student(student_id: str):
    student = await student_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        await student_collection.delete_one({"_id": ObjectId(student_id)})
        return True
    return False
