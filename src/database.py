import motor.motor_asyncio

MONGO_DETAILS = 'mongodb://localhost:27017'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.MongoDB_FastAPI

student_collection = database.get_collection("students")


def student_helper(student) -> dict:
    return {
        "student_id": str(student["_id"]),
        "first_name": student["first_name"],
        "last_name": student["last_name"],
        "email": student["email"],
        "age": student["age"],
        "course_of_study": student["course_of_study"],
        "begin_study_year": student["begin_study_year"]
    }
