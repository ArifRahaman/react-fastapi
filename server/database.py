# database.py
import motor.motor_asyncio

MONGO_DETAILS = "mongodb+srv://arifrahaman2606:NTambC6dzWTscSn1@mernstack.emb8nvx.mongodb.net/PDFPYTHON"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.user_database
user_collection = database.get_collection("users")

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "password": user["password"],
    }

# async def do_count():
#     n = await client.get_collection.count_documents({})
#     print("%s documents in collection" % n)
#     n = await client.get_collection.count_documents({"i": {"$gt": 1000}})
#     print("%s documents where i > 1000" % n)


