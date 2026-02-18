# Задания 1.1 - 1.5
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

import models  # Задание 1.4-1.5

app = FastAPI()


# Задание 1.1
@app.get("/task_1_1", tags=["Task_1_1"])
async def task_1_1():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}


# Задание 1.2
@app.get("/task_1_2", tags=["Task_1_2"], response_class=FileResponse)
async def task_1_2():
    return FileResponse("index.html")


# Задание 1.3
@app.post("/task_1_3/calclulate", tags=["Task_1_3"])
async def task_1_3(num1: int, num2: int):
    return num1 + num2


# Задание 1.4
@app.get("/task_1_4/user", tags=["Task_1_4"], response_model=models.User)
async def task_1_4():
    user = models.User(name="Max Gvriti", id=1)
    return user


# Задание 1.5
@app.post("/task_1_5/user", tags=["Task_1_5"])
async def task_1_5(user: models.User_task_1_5):
    data = user.model_dump()
    data["is_adult"] = user.age >= 18
    return data


# Задание 2.1
messages_list = []


@app.post("/task_2_1/feedback", tags=["Task_2_1"])
async def task_2_1(feedback: models.Feedback):
    messages_list.append(feedback.model_dump())

    return {
        "detail": f"Feedback received. Thank you, {feedback.name}!"
    }


# Задание 2.2
feedbacks_list = []

@app.post("/task_2_2/feedback", tags=["Task_2_2"])
async def task_2_2(feedback: models.Feedback):
    messages_list.append(feedback.model_dump())
    return {
        "message": "Спасибо, {name}! Ваш отзыв сохранён."
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
