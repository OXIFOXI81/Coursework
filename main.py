import requests
import json
import pprint

#  Задание 1
names_of_characters = [{"name": "Hulk","intell":"0"},
                       {"name": "Captain America","intell":"0"},
                       {"name": "Thanos","intell":"0"}]
url="https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)
# print(response.text)
#pprint.pprint(response.json())
djson=response.json()
for i,halk in enumerate(names_of_characters):
    for  every in djson:
        if  every['name']==halk['name']:
            print(every['name'])
            halk['intell']=every['powerstats']['intelligence']
print(names_of_characters)
max_intell=0
for index , person in enumerate(names_of_characters):
    if person['intell']> max_intell :
        max_intell=person['intell']
        max_name=person['name']
print(max_name)

Задание 2
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str,photo: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url='https://cloud-api.yandex.net:443/v1/disk'
        str= photo + '.jpg'
        params = {
            "path": "Homework/" +str
        }
        headers = {
            "Authorization": self.token
        }
        response = requests.get(url, headers=headers)
        if 200 <= response.status_code < 300:
            print(response.status_code)
            pprint.pprint(response.json())

        rr = requests.get(url + r"/resources/upload", headers=headers, params=params)
        print(rr.json())
        href_for_load = rr.json()["href"]
        print(href_for_load)

        with open(path_to_file +'\\'+str, 'rb') as file:
            response2 = requests.put(href_for_load, files={"file": file})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    photo_list=['P1080058','P1080404','P1080422','Fox']
    path_to_file =r'C:\Users\skobeleva.o\Documents\My\Foto'
    token = 'OAuth y0_AgAAAABQN9UWAADLWwAAAADlD6RxrDk4OWICSe2aIW4AZC2JQkCkHFE'
    uploader = YaUploader(token)
    for photo in enumerate(photo_list):
      result = uploader.upload(path_to_file,photo[1])








