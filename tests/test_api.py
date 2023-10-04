from unittest import TestCase
from parameterized import parameterized

from main import token_ya,url_ya,YaUploader,namedir

FIXTURES = [(namedir, token_ya,url_ya,YaUploader)]


class TestFunction(TestCase):
    @parameterized.expand(FIXTURES)
    def test_dir_exist(self, namedir, token_ya, url_ya,YaUploader):
            self.maxDiff = None
            uploader = YaUploader(token_ya)
            result = uploader.exists_dir(namedir, url_ya)
            self.assertEqual(result.status_code, 200,'Папка существует')



