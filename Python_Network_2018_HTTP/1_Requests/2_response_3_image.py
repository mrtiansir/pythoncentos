#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
import requests
from PIL import Image  # pip install Pillow
from io import BytesIO

r = requests.get('http://www.qytpython.com/qyt_logo.jpg')

imgContent = r.content

# 在PyCharm中展示图片
i = Image.open(BytesIO(r.content))
i.show()

# 下载并保存图片
imageFile = open('2_response_3_image.jpg', 'wb')
imageFile.write(imgContent)
imageFile.close()

