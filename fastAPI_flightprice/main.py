from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from model_flight_price import get_price
import re

app = FastAPI()

# 1. Shows the "Box" (HTML Form)
@app.get("/", response_class=HTMLResponse)
def get_flight():
    return """
    <form action="/check" method="post">
        <input type="text" name="flight_num" placeholder="Enter Flight Number">
        <button type="submit">Submit</button>
    </form>
    """

# 2. Handles the Input
@app.post("/check")
def flight_num_val(flight_num: str = Form(...)):
    # I fixed the regex syntax from your original code (d -> \d)
    if re.match(r"^[A-Za-z]\d{3}$", flight_num):
        return get_price(flight_num)
    else:
        return "Please input in right format"