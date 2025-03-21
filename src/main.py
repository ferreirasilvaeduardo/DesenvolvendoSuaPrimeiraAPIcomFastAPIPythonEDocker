from fastapi import FastAPI

from src.config import settings


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title=settings.PROJECT_NAME,
            root_path=settings.ROOT_PATH
        )


def create_app():
    app = App()
    # app.include_router(controllers_api_router)
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
