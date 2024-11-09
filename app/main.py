from fastapi import FastAPI


app = FastAPI()

@app.get("/users")
def get_users():
    return {"users": ["burak", "ahmet", "selim", "osman"]}

@app.get("/")
def root():
    return {"message": "verison 0.0.1!!!"}