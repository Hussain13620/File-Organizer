from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize the app
app = FastAPI()

# 2. Define exactly what data you expect using Pydantic
# This acts as a strict bouncer. If the frontend sends the wrong data, 
# FastAPI automatically rejects it with a helpful error.
class LoginData(BaseModel):
    username: str
    password: str

# 3. A basic GET route (Notice it's @app.get, not @app.route)
@app.get("/")
def test_server():
    # Just return a normal Python dictionary. FastAPI automatically turns it into JSON!
    return {"status": "success", "message": "The OS File Organizer API is alive!"}

# 4. A basic POST route (Receiving data from the frontend)
@app.post("/api/login")
def login(data: LoginData):
    # You access the data using dot notation (data.username), NOT dictionary notation.
    print(f"User {data.username} is trying to log in.")
    
    # We will hook this up to your database later
    return {"status": "success", "user_provided": data.username}