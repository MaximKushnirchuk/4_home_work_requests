'''Задача №2
У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон. Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс.Диск с таким же именем.
Все ответы приходят в формате json;
Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".
HOST: https://cloud-api.yandex.net:443
Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!'''
import json
import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str) :
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for one_file in file_path :
            name_file = one_file.split('\\')[-1]
            url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
            params = {'path' : name_file}
            headesr = {'Authorization' : self.token}
            response = requests.get(url, params=params, headers=headesr)
            print(response.status_code)
            if 200 <= response.status_code < 300 :
                url_for_load = response.json().get('href')
                with open(one_file, 'r') as file :
                    response_2 = requests.put(url_for_load, files={'file' : file})
                    print(response_2.status_code, 'Файл загружен!!!!!')
            else : print('Something went wrong')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 
    token = 
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

'''Я в переменную path_to_file подставлял вот такой список моих файлов :'''
# path_to_file = [r'C:\Users\ch\Desktop\home_work\4_home_work_requests\numbers.txt', r'C:\Users\ch\Desktop\home_work\4_home_work_requests\range3.txt', r'C:\Users\ch\Desktop\home_work\4_home_work_requests\text.txt']