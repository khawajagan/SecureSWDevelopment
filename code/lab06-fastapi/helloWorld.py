from fastapi import FastAPI
# For Info : faisal.rwp@gmail.com
# For Video : YouTube.com/khawajagan
# For Blog : khawajagan.com

app = FastAPI()

@app.get("/hi")
def greet():
    return "Hello? World?"

@app.get("/hi/{who}")
def greet(who):
    return f"Hello? {who}?"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("helloWorld:app", reload=True)
