# crud.py
from bson.objectid import ObjectId
from fastapi import HTTPException
from .database import user_collection, user_helper

# crud.py
from server.database import user_collection

async def add_user(user_data):
    new_user = await user_collection.insert_one(user_data)
    created_user_id = new_user.inserted_id
    created_user = await user_collection.find_one({"_id": created_user_id})
    return created_user

async def do_count():
    n_total = await user_collection.count_documents({})
    # print(f"{n_total} documents in collection")
    return n_total

    # n_gt_1000 = await user_collection.count_documents({"i": {"$gt": 1000}})
    # print(f"{n_gt_1000} documents where i > 1000")
async def update_user_by_id(user_id: str, new_data: dict):
    # Convert the user_id string to ObjectId
    user_obj_id = ObjectId(user_id)
    
    # Update the user document by ID
    result = await user_collection.update_one(
        {"_id": user_obj_id},
        {"$set": new_data}
    )

    if result.modified_count == 1:
        return {"message": "User updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")

async def retrieve_user(email: str) -> dict:
    user = await user_collection.find_one({"email": email})
    if user:
        return user
    return None


def verify_password(plain_password, hashed_password):
    # Code to compare plain_password with hashed_password and return True/False
    return plain_password == hashed_password


async def find_user_by_id(user_id: str):
    # type(user_id)
    # Convert the user_id string to ObjectId
    user_obj_id = ObjectId(user_id)
    # user_collection = db["user"]  # Assuming "user" is the collection name
    # Find the user document by ID
    user = await user_collection.find_one({"_id": user_obj_id})
 
    # return {"message": "User updated successfully"}
    return user