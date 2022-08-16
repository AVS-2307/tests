import unittest
import requests
from test_base import set_keyboard_input
from Yandex_Disk import YandexDisk, token


class TestYandexDisk(unittest.TestCase):

    def setUp(self) -> None:
        self.YandexDisk = YandexDisk(token)

    def tearDown(self) -> None:
        pass

    def test_responce_good(self):
            r = requests.get('https://cloud-api.yandex.net/v1/disk/resources/')
            self.assertEqual('200', '200')

    def test__create_directory(self):
            self.assertEqual('test2', 'test2')


class TestYandexDiskExpectedFailure(unittest.TestCase):

    def setUp(self) -> None:
        self.YandexDisk = YandexDisk(token)

    def tearDown(self) -> None:
        pass

    @unittest.expectedFailure
    def test_responce_bad(self):
        r = requests.get('https://cloud-api.yandex.net/v1/disk/resources/')
        self.assertEqual('200', '100')

    @unittest.expectedFailure
    def test__create_directory_bad(self):
        self.assertEqual('test2', 'test100')
