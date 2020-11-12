import urllib.request as request
from io import BytesIO

request.urlretrieve("http://cxsq-test.oss-cn-shanghai.aliyuncs.com/merchant/af47a966bd754b18b05b502cc8cdb03e",
                    'E:/wwwww/1.png')

request.urlretrieve(
    'http://cxsq-test.oss-cn-shanghai.aliyuncs.com/merchant/af47a966bd754b18b05b502cc8cdb03e?x-oss-process=image/resize,h_200,w_450/quality,Q_60',
    'E:/wwwww/2.png')
