import requests

# Мне пришлось прогнать файл app.py через Gemini и с нею его подробно разобрать, чтобы понять что, вообще, там внутри происходит.
# Сложно.

url = 'http://127.0.0.1:8080'
test_image = 'example.jpg'
image_path = test_image

print()
print("- POST, GET, DELETE -")
print()

with open(image_path, 'rb') as f:
    files = {'image': (test_image, f, 'image/jpeg')}
    response = requests.post(f"{url}/upload", files=files)  # нагуглила, что с бинарниками надо вот так использовать именно files=files

print(f" Request POST: {response.status_code}. Expected status is: 201")

uploaded_url = response.json().get('image_url')
print(uploaded_url)
print("-" * 80)
print()

print("- [GET] Get image url -")
headers = {'Content-Type': 'text'}  # я хочу получить джейсон с урлом, поэтому беру text
get_url = f"{url}/image/{test_image}"
get_response = requests.get(get_url, headers=headers)

print(f" GET status: {get_response.status_code}. Expected status is: 200.")

url_on_server = get_response.json().get('image_url')
print(f" File url: {url_on_server}")
print("-" * 80)
print()

print("- [DELETE] Deleting of file -")
deleted_url = f"{url}/delete/{test_image}"
delete_response = requests.delete(deleted_url)

print(f"DELETE status: {delete_response.status_code}. Expected status is: 200.")
print("-" * 80)
print()
