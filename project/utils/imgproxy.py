"""
imgproxy
获取图片处理管道地址

imgproxy_url = imgproxy.get_img_url(img_path=obj.save_name, options=ImgProxyOptions.COVER_IMG)
"""

import hmac
import enum
import base64
import hashlib

from django.conf import settings


class ImgProxyOptions(enum.Enum):
    COVER_IMG = '/rs:fit:150:150/q:60'
    SHARE_COVER_IMG = '/rs:fit:200:200'
    SHARE_SCREENSHOT = '/rs:fit:600:250/q:60'

class ImgProxy:
    def __init__(self, key, salt):
        self._key = bytes.fromhex(key)
        self._salt = bytes.fromhex(salt)

    def _get_signature(self, path):
        path = path.encode()
        digest = hmac.new(self._key, msg=self._salt + path, digestmod=hashlib.sha256).digest()
        signature = base64.urlsafe_b64encode(digest).rstrip(b"=")
        url = b'%s%s' % (signature, path)
        return url.decode()

    def get_img_url(self, img_path, options: ImgProxyOptions = ImgProxyOptions.COVER_IMG):
        source_url = f'{settings.PROJ_IMG_BASE_URL}{img_path}'
        base64_path = base64.b64encode(source_url.encode('utf-8')).decode('utf-8')
        url_path = self._get_signature(path=f'{options.value}/{base64_path}')
        return f'{settings.PROJ_IMAGE_BASE_URL}{url_path}'


imgproxy = ImgProxy(
    key=settings.IMGPROXY_KEY,
    salt=settings.IMGPROXY_SALT
)

if __name__ == '__main__':
    data = imgproxy.get_img_url('099c988eeb0c4c66851e4bdffa53d370.jpg', options=ImgProxyOptions.COVER_IMG)
    print(data)

