from fastapi import FastAPI
from pydantic import BaseModel      # it checks whether data has the correct type and structure


app = FastAPI()     # create an object

students = {        # create a temp database
    1: {
        "id": 1,
        "name": "Emad",
        "email": "emad@kntu.ac.ir",
        "level": "Undergraduate"
    },
    2: {
        "id": 2,
        "name": "Nima",
        "email": "nima@kntu.ac.ir",
        "level": "Graduate"
    }
}


class Student(BaseModel):           # Request model for creating/replacing a student
    name: str
    email: str
    level: str


class StudentUpdate(BaseModel):     # Request model for partially updating a student
    name: str | None = None
    email: str | None = None
    level: str | None = None


@app.get("/students")               # Create an endpoint using FastAPI Decorator
def get_students():                 # When send a GET request to /students, execute this function
    return students


@app.get("/students/{student_id}")  # Get a specific student
def get_student(student_id: int):
    return students[student_id]


@app.post("/students")              
def create_student(student: Student):

    new_id = max(students.keys()) + 1

    new_student = {
        "id": new_id,
        "name": student.name,
        "email": student.email,
        "level": student.level
    }

    students[new_id] = new_student

    return new_student


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    updated_student = {
        "id": student_id,
        "name": student.name,
        "email": student.email,
        "level": student.level
    }

    students[student_id] = updated_student

    return updated_student


@app.patch("/students/{student_id}")
def patch_student(student_id: int, student: StudentUpdate):
    
    existing_student = students[student_id]

    if student.name is not None:
        existing_student["name"] = student.name

    if student.email is not None:
        existing_student["email"] = student.email

    if student.level is not None:
        existing_student["level"] = student.level

    return existing_student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    deleted_student = students.pop(student_id)

    return deleted_student
