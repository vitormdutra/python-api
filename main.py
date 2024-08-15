from fastapi import FastAPI
import uvicorn

static_string = "Initial Text"
app = FastAPI()


@app.get("/get-message")
def hello(name: str):
    return {'Message': "Congrats " + name + '! This is your first API!'}


@app.post("/add")
async def add_text(text: str):
    global static_string
    static_string += text
    return {"Message": "Text added", "current_string": static_string}


@app.put("/change")
async def change_text(new_text: str):
    global static_string
    static_string = new_text
    return {"Message": "Text changed", "current_string": static_string}


@app.delete("/delete")
async def delete_text():
    global static_string
    static_string = ""
    return {"Message": "Text deleted"}

@app.get("/get-all")
async def all_text():
    global static_string
    return static_string


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
