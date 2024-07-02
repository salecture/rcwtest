from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Allow all origins, you can specify allowed origins if needed
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Name(BaseModel):
    first_name: str
    last_name: str

@app.post("/welcome")
async def welcome(name: Name):
    return {"message": f"Welcome Mr/Ms {name.last_name}, {name.first_name}!"}

if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8001)
    uvicorn.run(app, host="0.0.0.0", port=8000)
