#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from bs4 import BeautifulSoup
import requests
import re


class Courses:
    """
    分析,并且储存课程的类,传入的数据为课程的li标签
    """
    def __init__(self, course):
        # 找到课程名字,并且存储为self.courses_name属性
        self.courses_name = course.find('a', class_='item-tt-link').get('title')
        # 找到课程图片的链接url,并且存储为self.courses_url属性
        self.courses_url = 'https:' + course.find('a', class_='item-img-link').get('href')
        # 找到课程报名人数,并且存储为self.courses_students属性
        self.courses_students = int(course.find('span', class_='line-cell item-user').text.split('人')[0].strip())
        # 找到课程价格,并且存储为self.courses_price属性
        self.courses_price = course.find('span', class_=re.compile("^line-cell item-price.*")).text

    def __repr__(self):
        # 格式化类的打印输出字符串
        return "课程名: {} \n 课程URL: {} \n 课程报名人数: {} \n 课程价格: {} \n".format(self.courses_name,
                                                                                      self.courses_url,
                                                                                      self.courses_students,
                                                                                      self.courses_price)


def getpage(direction, id):
    client = requests.session()
    url = "https://ke.qq.com/course/list/" + direction + "?page=" + str(id)
    qqketang_page = client.get(url)

    # lxml HTML 解析器
    qqketang_page_soup = BeautifulSoup(qqketang_page.text, 'lxml')
    # 找到每一个课程'li'标签,直接放入page_courses_list列表
    course_card_items = qqketang_page_soup.find('ul', class_="course-card-list").find_all('li', class_='course-card-item')
    page_courses_list = []
    for course in course_card_items:
        page_courses_list.append(Courses(course))

    return page_courses_list


if __name__ == "__main__":
    print(getpage("python", 1))
