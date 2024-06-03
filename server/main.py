from fastapi import Body, FastAPI, HTTPException,Form
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from server.crud import add_user, retrieve_user
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from server.crud import verify_password
from server.crud import update_user_in_db
from server.crud  import do_count
from server.database import user_helper  # Make sure to import user_helper
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
   allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST","PUT"],  # Only allow POST requests
    allow_headers=["*"],  # Allow all headers
)

class User(BaseModel):
    username: str
    email: str
    password: str

# @app.post("/signup")
# async def signup(user: User):
#     # Your signup logic here
#     return {"message": "Signup successful"}


@app.post("/signup")
async def signup(user: User):
    # Check if the email is already registered
    existing_user = await retrieve_user(email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create a new user
    new_user_data = user.dict()
    created_user = await add_user(new_user_data)

    # Format the response
    response_user = user_helper(created_user)
    return response_user




from server.models import User



@app.post("/login")
async def login(user: User):
    # Retrieve the user by email

    # print(user)


    user_data = await retrieve_user(email=user.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the password
    if not verify_password(user_data['password'], user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    # Log in successful
    return {"message": "Login successful"}


@app.put("/update-user")
async def update_user(user: User):
    # Validate and process updated_data (assuming it's a dictionary)
    # Update user data in MongoDB based on updated_data
    updated_user = await update_user_in_db(user)  # Replace with your DB update logic

    if updated_user:
        return updated_user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/count-documents")
async def count_documents():
    try:
        # Call the async function to get the count
        counts = await do_count()
        return JSONResponse(content=counts)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)





# @app.put("/user/{user_id}")
# async def update_user(user_id: str, new_data: dict):
#     # Call the async function to update the user by ID
#     response = await update_user_by_id(user_id, new_data)
#     return response

# @app.post("/login")
# async def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     # Retrieve the user by email
#     user = await retrieve_user(email=form_data.username)
#     if not user:
#         raise HTTPException(status_code=400, detail="Invalid credentials")

#     # Verify the password
#     if not verify_password(form_data.password, user['password']):
#         raise HTTPException(status_code=400, detail="Invalid credentials")

# @app.post("/signup")
# async def signup(user: User):
#     # Check if the email is already registered
#     existing_user = await retrieve_user(email=user.email)
#     if existing_user:
#         raise HTTPException(status_code=400, detail="Email already registered")

#     # Create a new user
#     new_user_data = user.dict()
#     created_user = await add_user(new_user_data)

#     # Format the response
#     response_user = user_helper(created_user)

    # return response_user
# @app.get("/user/{user_id}")
# async def get_user_by_id(user_id:str):
#     # Call the async function to find the user by ID
#     user = await find_user_by_id(user_id)
    
#     # Check if user is found
#     if user:
#        print(user)
#     else:
#         raise HTTPException(status_code=404, detail="User not found")

