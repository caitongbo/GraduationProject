import requests
from bs4 import BeautifulSoup
import re
import json
import jieba
#获取html页面信息
def getKeywordResult(keyword, pagenum):
    url = 'http://www.baidu.com/s?wd=' + keyword + '&pn=' + pagenum + '0'
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""
#解析并抽取数据
def parserLinks(html):
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for div in soup.find_all('div', {'data-tools':re.compile('title')}):
        data = div.attrs['data-tools']
        d = json.loads(data)
        links.append(d['title'])
        words_all.append(d['title'])
    return links, words_all
#词频统计
def words_ratio(words_all):
    words = []
    for i in words_all:
        tmp = jieba.lcut(i)
        for tmp_word in tmp:
            words.append(tmp_word)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(30):
        word, count = items[i]
        print("{0:<10}{1:>5} 占比：{2}".format(word, count, int(count)/len(words)))
def main():
    key = input("请输入关键字：")
    pagenum = input("请输入页数：")
    for k in range(0, int(pagenum)):
        html = getKeywordResult(key, str(k))#输入搜索关键词和页数
        ls, words_all = parserLinks(html)
        count = k + 1
        for i in ls:
            print("[{:^3}]{}".format(count, i))
        ls = []
    words_ratio(words_all)
if __name__ == '__main__':
    words_all = []
    main()
