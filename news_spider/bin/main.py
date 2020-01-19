# -*- coding: utf-8 -*-
# Time: 2019/04/01 01:18
# Author: caiongbo
# File: main.py
# 功能：
'''
以中国新闻网社会新闻板块为抓取对象
http://www.chinanews.com/society.shtml
当前抓取了3月份所有数据新闻数据，后期进行数据分析
可以在news_spider.py中设置任意的时间段
'''

from multiprocessing import Pool
from news_spider import news, get_res, get_all_links, item_info, url_lists

def all_links():
    '''
    先从网页爬取所有的链接数据存入数据库，
    然后从数据库里读取所有的链接
    :return: 以所有链接的列表形式
    '''
    get_all_links()
    allLinks = []
    for data in url_lists.find():
        allLinks.append(data['links'])
    return  allLinks

if __name__ == '__main__':
    pool = Pool()  # 创建多线程池
    pool.map(get_res, all_links())
