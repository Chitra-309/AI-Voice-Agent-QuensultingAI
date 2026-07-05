import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES,
)

client = gspread.authorize(creds)

SPREADSHEET_ID = "1ryA3Ue0iLnI4VENEeUBBz6trluRvfAKy5CjOVhwbKbE"

sheet = client.open_by_key(SPREADSHEET_ID).sheet1


def save_appointment(data):
    sheet.append_row([
        data["name"],
        data["phone"],
        data["email"],
        data["service"],
        data["date"],
        data["time"],
        data["timestamp"]
    ])