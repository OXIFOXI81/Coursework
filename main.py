import requests
import json
import pprint

# #  Задание 1
# names_of_characters = [{"name": "Hulk","intell":"0"},
#                        {"name": "Captain America","intell":"0"},
#                        {"name": "Thanos","intell":"0"}]
# url="https://akabab.github.io/superhero-api/api/all.json"
# response = requests.get(url)
# # print(response.text)
# #pprint.pprint(response.json())
# djson=response.json()
# for i,halk in enumerate(names_of_characters):
#     for  every in djson:
#         if  every['name']==halk['name']:
#             print(every['name'])
#             halk['intell']=every['powerstats']['intelligence']
# print(names_of_characters)
# max_intell=0
# for index , person in enumerate(names_of_characters):
#     if person['intell']> max_intell :
#         max_intell=person['intell']
#         max_name=person['name']
# print(max_name)
#
# Задание 2
# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#
#     def upload(self, file_path: str,photo: str):
#         """Метод загружает файлы по списку file_list на яндекс диск"""
#         url='https://cloud-api.yandex.net:443/v1/disk'
#         str= photo + '.jpg'
#         params = {
#             "path": "Homework/" +str
#         }
#         headers = {
#             "Authorization": self.token
#         }
#         response = requests.get(url, headers=headers)
#         if 200 <= response.status_code < 300:
#             print(response.status_code)
#             pprint.pprint(response.json())
#
#         rr = requests.get(url + r"/resources/upload", headers=headers, params=params)
#         print(rr.json())
#         href_for_load = rr.json()["href"]
#         print(href_for_load)
#
#         with open(path_to_file +'\\'+str, 'rb') as file:
#             response2 = requests.put(href_for_load, files={"file": file})
#
#
# if __name__ == '__main__':
#     # Получить путь к загружаемому файлу и токен от пользователя
#     photo_list=['P1080058','P1080404','P1080422','Fox']
#     path_to_file =r'C:\Users\skobeleva.o\Documents\My\Foto'
#     token = 'OAuth '
#     uploader = YaUploader(token)
#     for photo in enumerate(photo_list):
#       result = uploader.upload(path_to_file,photo[1])



import requests
import os
import datetime


# class VK:
#
#    def __init__(self, access_token, user_id, version='5.131'):
#        self.token = access_token
#        self.id = user_id
#        self.version = version
#        self.params = {'access_token': self.token, 'v': self.version}
#
#    def users_info(self):
#        url = 'https://api.vk.com/method/users.get'
#        params = {'user_ids': self.id}
#        response = requests.get(url, params={**self.params, **params})
#        return response.json()
#
#
# access_token = 'vk1.a.B4hhJCbVmnyVeEpLU2KEH-WsJoKiTUxn38CVZjgb48hrFH3Y2x7SfWZHSm52BFtgQydo9HVkuchnsi40VM1-_M_yo9XLyCKrh-qEmtTwCXpARbDFOD8bMIMWbugpko7I3S2YxSfy0_2-DQBRAVGbp2jOme1GSoeBAKnVr51X8Ia4ipdHsE74cBBt6CHd9KXPnZY8bMQuhIM4CEKrZyf-JA'
# user_id = '327085850'
# vk = VK(access_token, user_id)
# print(vk.users_info())

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
            # pprint.pprint(res.json())
            return res.json()

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str,photo: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url='https://cloud-api.yandex.net:443/v1/disk'
        str= photo + '.jpg'
        params = {
            "path": "FROM_VK/" +str
        }
        headers = {
            "Authorization": self.token
        }
        response = requests.get(url, headers=headers)
        if 200 <= response.status_code < 300:
            print(response.status_code)
            pprint.pprint(response.json())

        rr = requests.get(url + r"/resources/upload", headers=headers, params=params)
        # print(rr.json())
        href_for_load = rr.json()["href"]
        # print(href_for_load)

        with open(file_path +'\\'+str, 'rb') as file:
            response2 = requests.put(href_for_load, files={"file": file})


if __name__ == '__main__':
 token_vk='vk1.a.wCEnyJqJPI9cDosgNokllsOE-QOIGT1fi7Au02vh6ifmRC21dy6Go9B6U0hLBq28YyFQDKib1zYKVqviirL5gpg7rSaPZXj1QcKb-f5UcIBAlQJsH3ZVjQFWzf9W4X3I9MN4VmqomBKJLbYpbJx6x35yBnveqFrFPY_d3k4RqXYJ2SL2GpvpjKjz05AvDmvMTeV_IWvyJJws9U0nxA-GNg'
 user_vk ='327085850'
# VK
 vk = VK(token_vk)
 dataFromVK =vk.get_picture(user_vk)
# YADisk
 token_ya = 'OAuth y0_AgAAAABQN9UWAADLWwAAAADlD6RxrDk4OWICSe2aIW4AZC2JQkCkHFE'
 uploader = YaUploader(token_ya)

# Создаём папку на компьютере для скачивания фотографий
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
 # pprint.pprint(pict_json)

 # Скачиваем фотографии c VK  и записываем на ЯД
 #    with open('Pictures_from_vk/%s' % f'{pict_name}.jpg', 'wb') as file:
 #                     img = requests.get(url)
 #                     file.write(img.content)
 #                     uploader.upload('Pictures_from_vk', pict_name)
     with open("log_file.txt",'a', encoding='utf-8') as log:
                     log.write(f'считана и записана фотография - {pict_name}.jpg \n')
 with open("pictures.json", "w") as file:
                json.dump(pict_json, file, indent=4)
 with open("log_file.txt", 'a', encoding='utf-8') as log:
                log.write(f'Фотографии записаны на ЯндексДиск в папку : https://disk.yandex.ru/client/disk/FROM_VK \n')








