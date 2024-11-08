from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "verison 0.0.1!!!"}