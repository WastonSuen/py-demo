# coding=utf-8
"""
@version: 2017/12/15 015
@author: Suen
@contact: sunzh95@hotmail.com
@file: download_by_subject
@time: 9:50
@note:  ??
"""
#

import codecs
import os
import re
import time
import requests
from lxml import html as htmltool
from crawler.download_video import batch_download

main_site = 'main_site_without_slash%s'
passed_courses = ['']  # won't download these couses inthis list
need_courses = ['', ]


def lesson_video_page(lessons, dir_name):
    video_urls = []
    catalog_path = os.path.join(dir_name, 'catalog.txt')
    already_download_urls = []
    if os.path.exists(catalog_path.encode('gbk')):
        with codecs.open(catalog_path.encode('gbk'), 'r', 'utf_8_sig') as f:
            for line in f.readlines():
                res = re.search(r'\t(?P<lesson_url>.+)$', line)
                if res:
                    already_download_urls.append(res.groupdict().get('lesson_url'))

    with codecs.open(catalog_path.encode('gbk'), 'ab+', 'utf_8_sig') as f:
        for url, title in lessons:
            html = requests.get(main_site % url).content
            res = re.search(r'\$lessonUrl(\s?)=(\s?)\"(\s?)(?P<video>(.+))(\s?)\"', html, re.MULTILINE)
            if res:
                video = res.groupdict().get('video')
                if video not in already_download_urls:
                    f.write('{}\t{}\n'.format(title, video))
                    print('获取{}下载链接成功: {}'.format(title, video))
                    video_urls.append(video)
                else:
                    print('{} 视频已下载: {}'.format(title, video))
            else:
                print('获取{}下载链接失败: {}'.format(title, url))
    return video_urls


def course_main_page(course):
    lesson_site = main_site % course
    html = requests.get(lesson_site).content
    doc = htmltool.fromstring(html)
    lessons_url = doc.xpath('//ul[@class="lesson-lists"]/li/a/@href')
    lessons_title = [span.text for i, span in
                     enumerate(doc.xpath('//ul[@class="lesson-lists"]/li/a/span'))
                     if i % 2 == 0]
    lessons_info = zip(lessons_url, lessons_title)
    return lessons_info


def subject_main_page(subject):
    subject_site = main_site % '/course/%s/' % subject
    html = requests.get(subject_site).content
    doc = htmltool.fromstring(html)
    cources_title = doc.xpath('//dl[@class="course-stage-dl"]/dt[@style="font-size: 26px;"]')[0].text
    cources_des = doc.xpath('//dl[@class="course-stage-dl"]/dd')[0].text
    print(cources_title, '\n', cources_des)
    sections = doc.xpath('//div[@class="container"]/div[@class="course-stage zy_tab2 zy_tabBB"]//section[1]')[0]

    courses_info = zip(sections.xpath('//div[@class="artc-bt"]//a/@href'),
                       sections.xpath('//div[@class="artc-bt"]//a/@title'))
    return courses_info


def download_by_subject(subject):
    cources = subject_main_page(subject)
    if not os.path.exists(os.path.abspath(subject)):
        os.mkdir(os.path.abspath(subject))
    for i, (cource, title) in enumerate(cources, 1):
        if title in passed_courses:
            continue
        if title not in need_courses:
            continue
        print(title)
        title = re.sub(r'[:：\.]', '_', title)  # batch replace
        dir_name = '{}_{}'.format(i, title)
        path = os.path.abspath(os.path.join(subject, dir_name))  # chinese directory
        if not os.path.exists(path.encode('gbk')):
            os.mkdir(path.encode('gbk'))
        lessons = course_main_page(cource)
        video_urls = lesson_video_page(lessons, path)
        batch_download(video_urls, path)
        time.sleep(30)
    print('all finished')


if __name__ == '__main__':
    download_by_subject('python')
