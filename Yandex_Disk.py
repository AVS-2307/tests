import requests
import json

with open('token.txt', 'r') as file_object:
    token = file_object.read().strip()


class YandexDisk:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _create_directory(self):
        directory_name = input('Введите имя папки для создания: ')
        headers = self.get_headers()
        params = {'path': directory_name}
        dir_query = 'https://cloud-api.yandex.net/v1/disk/resources/'
        requests.put(dir_query, headers=headers, params=params)
        return directory_name


if __name__ == '__main__':
    YandexDisk = YandexDisk(token)
    YandexDisk._create_directory()
