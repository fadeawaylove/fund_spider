import requests


class BaTuPian(object):
    pid = 14821
    key = "e47fa8fb9e8a1054375f58a9a77630a5"
    url_a = "http://web.8tupian.com/api/a.php"
    url_b = "http://web.8tupian.com/api/b.php"
    url_c = "http://web.8tupian.com/api/c.php"

    @classmethod
    def _set_params(cls, act, **kwargs):
        params = {"key": cls.key, "pid": cls.pid, "act": act}
        if kwargs:
            params.update(kwargs)
        return params

    @classmethod
    def get_merchants_info(cls):
        params = cls._set_params("query")
        resp = requests.get(cls.url_a, params=params)
        return resp.json()

    @classmethod
    def get_pic_info(cls, pic_url):
        params = cls._set_params(act="pic", picurl=pic_url)
        resp = requests.get(cls.url_a, params=params)
        return resp.json()

    @classmethod
    def get_pics_info(cls):
        params = cls._set_params(act="pictures")
        return requests.get(cls.url_a, params=params).json()

    @classmethod
    def delete_pic(cls, pic_url):
        params = cls._set_params(act="del", picurl=pic_url)
        return requests.get(cls.url_a, params=params).json()

    @classmethod
    def upload_pic_mode1(cls, pic, price):
        params = cls._set_params(act="up1", pic=pic, price=price)
        return requests.get(cls.url_b, params=params)

    @classmethod
    def upload_pic_mode2(cls, pic, pic2, price):
        params = cls._set_params(act="up2", pic=pic, pic2=pic2, price=price)
        return requests.get(cls.url_b, params=params).json()

    @classmethod
    def upload_pic_mode3(cls, pic, texturl, price):
        params = cls._set_params(act="up3", pic=pic, texturl=texturl, price=price)
        return requests.get(cls.url_b, params=params).json()


if __name__ == '__main__':
    baTupian = BaTuPian()
    # print(baTupian.get_pic_info('http://dt4.8tupian.com/14821a5b1.pg3'))
    print(baTupian.delete_pic('http://dt4.8tupian.com/14821a5b1.pg3'))
    # print(baTupian.get_pics_info())
