from fastapi import FastAPI
import uvicorn
import sys
import os

app = FastAPI(
    title="Asphodel API Project", description="It's all yours.", version="Alpha 0.2"
)


# @app.get("/", tags=["Root"])
# async def root():
#     return {"detail": "I'm all yours."}

# @app.get('/ee')
# def ee():
#     return True


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for root, dirs, files in os.walk("."):
    if not '__pycache__' in root:
        for file in files:
            root = root.replace('\\', '/')
            path = f'{root}/{file}'

            if not path.endswith('.py'):
                continue
            module = path.removeprefix('./').replace('/', '.').removesuffix('.py')
            __import__(module)

# ignored = {
#     "database",
#     "generator",
# }

from uvicorn.supervisors.watchgodreload import CustomWatcher


class WatchgodWatcher(CustomWatcher):
    def __init__(self, *args, **kwargs):
        super(WatchgodWatcher, self).__init__(*args, **kwargs)


uvicorn.supervisors.watchgodreload.CustomWatcher = WatchgodWatcher

if __name__ == "__main__":
    uvicorn.run("api:app", host="192.168.0.2", port=7474, reload=True)