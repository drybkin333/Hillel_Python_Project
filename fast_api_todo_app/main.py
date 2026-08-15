from fastapi import FastAPI, Request
from routes.tasks import router as todos_router
from routes.users import router as users_router
import time
from database import Base, engine

app = FastAPI()

@app.middleware("http")
async def middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    response_time = time.time() - start_time

    print(request.method, request.url, response_time)

    response.headers['X-Process-Time'] = str(round(response_time,4))

    return response

app.include_router(todos_router)
app.include_router(users_router)

Base.metadata.create_all(engine)