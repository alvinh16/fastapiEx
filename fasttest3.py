from fastapi import Fastapi 

app = Fastapi()

@app.get("/")
def read_root():
     return {"Hello World."}
