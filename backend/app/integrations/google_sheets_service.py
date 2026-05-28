import gspread

from oauth2client.service_account import (
    ServiceAccountCredentials
)

from app.core.config import settings


scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]


credentials = (
    ServiceAccountCredentials
    .from_json_keyfile_name(
        settings.GOOGLE_CREDENTIALS_FILE,
        scope
    )
)


client = gspread.authorize(
    credentials
)


async def append_to_google_sheet(payload: dict):

    """
    Append workflow data into Google Sheets.
    """

    try:
        rows = payload.get("rows", [])
        sheet = client.open(
            settings.GOOGLE_SHEET_NAME
        ).sheet1

        sheet.append_row(rows)

        print("\n===== GOOGLE SHEETS SERVICE =====")
        print("Row appended successfully")

        return {
            "status": "success",
            "service": "google_sheets",
            "message": "Row added"
        }

    except Exception as e:

        print("\n===== GOOGLE SHEETS ERROR =====")
        print(str(e))

        raise Exception(
            f"Google Sheets Failed: {str(e)}"
        )