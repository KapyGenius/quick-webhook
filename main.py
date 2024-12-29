import os
from fastapi import FastAPI, Request
from dotenv import load_dotenv
import requests

# Load environment variables from a .env file
load_dotenv()

app = FastAPI()

# Get the Formspark ID from the environment variable
FORMSPARK_ID = os.getenv("FORMSPARK_ID")
FORMSPARK_URL = f"https://submit-form.com/{FORMSPARK_ID}"


@app.post("/webhook")
async def webhook(request: Request):
    """
    Receive POST requests and forward the data to Formspark.
    """
    try:

        print("Request Header : ", request.headers)        
        content_type = request.headers.get("Content-Type", "")

        if "application/json" in content_type:
            # Parse JSON payload
            payload = await request.json()

        elif "application/x-www-form-urlencoded" in content_type:
            # Parse form data payload
            form_data = await request.form()
            payload = dict(form_data)  # Convert to a dictionary

        else:
            return {"error": "Unsupported Content-Type"}
        
        print("Recieved Payload : \n", payload)

        # Forward the data to Formspark
        response = requests.post(FORMSPARK_URL, json=payload)

        print("Response : ", response.status_code)

        # Return the status from Formspark
        return {"formspark_status": response.status_code}
    except Exception as e:
        return {"error": str(e)}