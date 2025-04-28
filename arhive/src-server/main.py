from fastapi import FastAPI

from api import api_router

app = FastAPI(title="Управление домашним бюджетом")
app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8010)
