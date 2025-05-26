# 🎨 Docker ML API Hub – Image Colorizer

This project demonstrates how to run the [IBM MAX Image Colorizer](https://developer.ibm.com/exchanges/models/all/max-image-colorizer/) using Docker and access it through a simple REST API. The model colorizes grayscale images into vivid colorizations using deep learning.

---

## 📦 Features

- 🧠 Uses a pre-trained deep learning model from IBM's Model Asset eXchange (MAX)
- 🚀 Runs entirely in Docker with zero setup
- 🌐 RESTful API interface
- 🐍 Python script to send image and save the result

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/keerthanshetty6/docker-ml-api-hub.git
cd docker-ml-api-hub
```
### 2. Run the Docker container
```bash
docker run -it -p 5000:5000 quay.io/codait/max-image-colorizer
```

Once running, the model API will be available at:
http://localhost:5000/model/predict

## 🧪 Inference: Python Example
Use the provided image_coloriser.py script to send an image and save the colorized output.

## ✔️ Requirements
Python 3.x

requests library (install via pip install requests)

## 📝 License
This project is released under the MIT License.
The MAX image colorizer model is provided under the Apache 2.0 License by IBM.

## 🙌 Acknowledgments
IBM Developer – Model Asset eXchange

codait/max-image-colorizer
