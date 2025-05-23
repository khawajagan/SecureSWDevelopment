import uuid

import cv2
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image

import config
import inference
# For Info : faisal.rwp@gmail.com
# For Video : YouTube.com/khawajagan
# For Blog : khawajagan.com
# For Github : github.com/khawajagan

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome from the MyPicStyler API"}



@app.post("/{style}")
def get_image(style: str, file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    model = config.STYLES[style]
    output, resized = inference.inference(model, image)
    name = f"/storage/{str(uuid.uuid4())}.jpg"
    cv2.imwrite(name, output)
    return {"name": name}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)