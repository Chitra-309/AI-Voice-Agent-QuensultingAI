# 🦷 AI Receptionist Voice Agent – QuensultingAI Internship Assignment

## Overview

This project is an AI-powered Dental Receptionist Voice Agent built using **RetellAI Conversational Flow** and **FastAPI**.

The agent can:

- 📅 Book dental appointments
- ❓ Answer clinic FAQs
- 🚨 Handle emergency calls
- 👩‍💼 Transfer callers to a human receptionist
- 📊 Store appointment details in Google Sheets

---

## Tech Stack

- RetellAI (Conversational Flow)
- Python 3.14
- FastAPI
- Google Sheets API
- gspread
- Git

---

## Features

### Appointment Booking

Collects:

- Patient Name
- Phone Number
- Email Address
- Dental Service
- Preferred Date
- Preferred Time

---

### FAQ Handling

Answers questions about:

- Clinic Timings
- Consultation Fee
- Walk-ins
- Payment Methods
- Services
- Clinic Location

---

### Emergency Handling

Identifies urgent dental cases and directs callers appropriately.

---

### Human Escalation

Transfers callers to a receptionist when requested.

---

## Backend Architecture

```
Caller
      │
      ▼
RetellAI Conversation Flow
      │
      ▼
FastAPI Backend
      │
      ▼
Google Sheets
```

---

## API Endpoint

POST `/book-appointment`

Stores appointment information in Google Sheets.

---

## Project Structure

```
AI-Voice-Agent-QuensultingAI/
│
├── app.py
├── sheets.py
├── requirements.txt
├── README.md
├── RetellAI_Dental_Receptionist.json
└── .gitignore
```

---

## Future Improvements

- Confirmation Email
- Calendar Integration
- SMS Notifications
- Live Webhook Deployment
- Appointment Rescheduling