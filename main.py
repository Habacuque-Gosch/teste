from fastapi import FastAPI
import uvicorn
import modules
import modules
import modules.routers.route1_router




app = FastAPI()

@app.get("/")
def hello_word() -> str:
    return "Hello Word"

app.include_router(modules.routers.route1_router.router)

if __name__ == "__main__":
    uvicorn.run(app)


