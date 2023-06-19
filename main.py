import json
import requests
import os
import datetime
import pprint

class VK:

        def __init__(self, access_token, version='5.131'):

           self.token = access_token
           self.version = version
           self.params = {'access_token': self.token, 'v': self.version}
           self.token = access_token

        def get_picture(self, user_vk,offset=0, count=50):

            url = 'https://api.vk.com/method/photos.get'
            params = {'owner_id': user_vk,
                      'album_id': 'profile',
                      'access_token': self.token,
                      'extended': 1,
                      'v': '5.131'
                      }
            res = requests.get(url=url, params=params)
            return res.json()

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str,photo: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url='https://cloud-api.yandex.net:443/v1/disk'
        str= photo + '.jpg'
        params = {
            "path": "FROM_VK/"+str
        }
        headers = {
            "Authorization": self.token
        }
        response = requests.get(url, headers=headers)
        if 200 <= response.status_code < 300:
            print(response.status_code)

        rr = requests.get(url + r"/resources/upload", headers=headers, params=params)

        href_for_load = rr.json()["href"]


        with open(file_path +'\\'+str, 'rb') as file:
            response2 = requests.put(href_for_load, files={"file": file})


if __name__ == '__main__':
 token_vk='vk1.a...'
 user_vk ='327085850'
# VK
 vk = VK(token_vk)
 dataFromVK =vk.get_picture(user_vk)
# YADisk
 token_ya = 'OAuth ...'
 uploader = YaUploader(token_ya)

# # Создаём папку на компьютере для скачивания фотографий
 if not os.path.exists('Pictures_from_vk'):
       os.mkdir('Pictures_from_vk')
 url_pict=[]
 with open("log_file.txt",'w', encoding='utf-8') as log:
    log.write('Начинаем считывание информации с VK \n')

 for pict in dataFromVK['response']['items']:
    for pict_size in pict['sizes']:
      if pict_size['type']=='z':
           url_pict.append({
             'url': pict_size['url'],
             'likes': pict['likes']['count'],
             'date': pict['date']
           })

# Cортируем и отбираем 5 фото
#  pprint.pprint(url_pict)
 al=[]
 for ob in url_pict:
    al.append(str(ob["likes"]) + "|" + datetime.datetime.fromtimestamp(ob["date"]).strftime(
        "%Y-%m-%d_%H-%M-%S") + "|" + ob["url"])
 al.sort(reverse=True)
 like_pred=''
 pict_json = []
 for i in range(0,5):
     like,dated,url=al[i].split('|')
    # print(f'like={like},{dated},{url}')
     if like==like_pred or like=='0':
        pict_name=like+'_'+dated
     else:
        pict_name=like
     pict_json.append({
         'file_name': pict_name+'.jpeg',
         'size': 'z',
         'likes': like
      })
     like_pred=like


 # Скачиваем фотографии c VK  и записываем на ЯД
     with open('Pictures_from_vk/%s' % f'{pict_name}.jpg', 'wb') as file:
                     img = requests.get(url)
                     file.write(img.content)
                     uploader.upload('Pictures_from_vk', pict_name)
     with open("log_file.txt",'a', encoding='utf-8') as log:
                     log.write(f'считана и записана фотография - {pict_name}.jpg \n')
 with open("pictures.json", "w") as file:
                json.dump(pict_json, file, indent=4)
 with open("log_file.txt", 'a', encoding='utf-8') as log:
                log.write(f'Фотографии записаны на ЯндексДиск в папку : https://disk.yandex.ru/client/disk/FROM_VK \n')








