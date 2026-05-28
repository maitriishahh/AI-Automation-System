async def append_to_google_sheet(payload: dict):

    """
    Mock Google Sheets integration.
    """

    print("\n===== GOOGLE SHEETS SERVICE =====")
    print("Appending row:", payload)

    return {
        "status": "success",
        "service": "google_sheets",
        "data": payload
    }