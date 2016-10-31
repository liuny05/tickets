# -*- coding:utf-8 -*-
import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971'
# 添加verify=False参数不验证证书
response = requests.get(url, verify=False)
# \|代表转义的|而不是或，而findall以list的形式返回匹配到的所有结果，因此匹配的结果是如“北京北|VAP”的tuple
# 但因为用()加了分组，因此将“北京北|VAP”拆分成了“北京北”和“VAP”，并以tuple的形式返回
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
pprint(dict(stations), indent=4)