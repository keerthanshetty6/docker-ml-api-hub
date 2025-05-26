import requests

image_path = 'images.jpeg'
url = 'http://localhost:5000/model/predict'

with open(image_path, 'rb') as img:
    files = {'image': img}
    response = requests.post(url, files=files)

if response.status_code == 200:
    with open('colorized_output.jpg', 'wb') as f:
        f.write(response.content)
    print("✔️ Colorized image saved as 'colorized_output.jpg'")
else:
    print("❌ Failed:", response.status_code, response.text)
