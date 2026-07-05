# AI Receptionist Voice Agent – QuensultingAI Internship Assignment

## Overview

This project is an AI Receptionist Voice Agent built for QuensultingAI Dental Clinic using RetellAI Conversational Flow and FastAPI.

## Features

- AI-powered appointment booking
- FAQ handling
- Emergency call handling
- Human receptionist transfer
- Google Sheets integration
- Confirmation webhook ready

## Tech Stack

- RetellAI Conversational Flow
- Python
- FastAPI
- Google Sheets API
- gspread

## Conversation Flow

Incoming Call
↓
Greeting
↓
Intent Detection
├── Appointment Booking
├── FAQs
├── Emergency
└── Human Receptionist

## API

POST /book-appointment

Stores appointment details in Google Sheets.

## Future Improvements

- Email confirmation
- Calendar integration
- SMS reminders
- Live webhook deployment