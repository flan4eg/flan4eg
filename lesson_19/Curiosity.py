import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

downloaded_photos = 2

print()
print("- Get data and see what in the json file -")
print()

response = requests.get(url, params=params)
response.raise_for_status()
data = response.json()
print(data)
print("-" * 80)

photo_links = []
for photo in data['photos']:
    photo_links.append(photo['img_src'])  # в json файле видно, что все изображения имеют ключ img_src

    if len(photo_links) >= downloaded_photos:  # я не совсем поняла из задания надо ли скачать только 2 фото, на всякий случай скачиваю 2
        break

print("- Downloading photos -")
print()

for index, link in enumerate(photo_links):
    file_name = f"mars_photo{index + 1}.jpg"

    img_response = requests.get(link)

    with open(file_name, 'wb') as f:
        f.write(img_response.content)

    print(f"File {file_name} is saved")

# я хотела сделать вывод результата в print более читаемым, но мне сайт стал выдавать Error 429 - превысила лимит обращений :(