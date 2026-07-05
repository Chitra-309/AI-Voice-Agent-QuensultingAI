from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from datetime import datetime
from sheets import save_appointment

app = FastAPI(title="QuensultingAI Dental Clinic API")


class Appointment(BaseModel):
    name: str
    phone: str
    email: EmailStr
    service: str
    date: str
    time: str


@app.get("/")
def home():
    return {
        "message": "Welcome to QuensultingAI Dental Clinic API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/book-appointment")
def book_appointment(appointment: Appointment):

    data = appointment.model_dump()

    data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_appointment(data)

    return {
        "success": True,
        "message": "Appointment booked successfully!",
        "appointment": data
    }