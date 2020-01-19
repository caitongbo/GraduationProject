# -*- coding:utf-8 -*- 
import pyecharts
from pyecharts import Bar
from pyecharts import online
# online()
import json
import codecs

path = '03_result.json'
with open(path, 'r', encoding='utf-8') as f:
    temp = json.load(f)
    list = []
    list = temp
temp = []
for i in list:
    temp.append(i)

print(len(temp))
for i in temp:
    try:
        i['nums'] = float(i['nums'])
    except:
        print('error')

dic_n_new = {} #新词
dic_nr = {} # 人名
dic_ns = {} # 地名
dic_nt = {} # 机构团体名
dic_nz = {} # 其它专名
dic_wh = {}

res_n_new = [] #新词
res_nr = [] # 人名
res_ns = [] # 地名
res_nt = [] # 机构团体名
res_nz = [] # 其它专名
res_wh = {}
for i in temp:
    try:
        if i['cates'] == 'n_new': 
            if i['words'] in dic_n_new:
                dic_n_new[i['words']] = dic_n_new[i['words']] + i['nums']
            else:
                dic_n_new[i['words']] = i['nums']
        if i['cates'] == 'nr':
            if i['words'] in dic_nr:
                dic_nr[i['words']] = dic_nr[i['words']] + i['nums']
            else:
                dic_nr[i['words']] = i['nums']
        if i['cates'] == 'ns':
            if i['words'] in dic_ns:
                dic_ns[i['words']] = dic_ns[i['words']] + i['nums']
            else:
                dic_ns[i['words']] = i['nums']
        if i['cates'] == 'nt':
            if i['words'] in dic_nt:
                dic_nt[i['words']] = dic_nt[i['words']] + i['nums']
            else:
                dic_nt[i['words']] = i['nums']
        if i['cates'] == 'nz':
            if i['words'] in dic_nz:
                dic_nz[i['words']] = dic_nz[i['words']] + i['nums']
            else:
                dic_nz[i['words']] = i['nums']
        if i['cates'] == 'nz':
            if i['words'] in dic_wh:
                dic_wh[i['words']] = dic_wh[i['words']] + i['nums']
            else:
                dic_wh[i['words']] = i['nums']       
    except:
        #print("eroor")
        pass

#处理各个词性的数据，最后逆序排列
def deal(res, dic):
    res.clear()
    c = {}
    for key in dic:
        c['words'] = key
        c['nums'] = dic[key]
        res.append(c)
        c = {}
    res.sort(key = lambda x:x['nums'])
    res.reverse() 

# 输出list数据
def output(res, num = 200):
    for i in res[:num]:
        print(i)


deal(res_n_new, dic_n_new) #进行数据储存
output(res_n_new, 30) #数据输出
attr_n_new = []
value_n_new = []
for n_new in res_n_new[4:30]:
    attr_n_new.append(n_new['words'])
    value_n_new.append(n_new['nums'])
bar = Bar("2019年03月份名词记", "2019年03月份出现频率最高的名词")
bar.add("主视图", attr_n_new, value_n_new, xaxis_interval=0, xaxis_rotate=30, yaxis_rotate=30)
bar.render("2019年03月份出现频率最高的名词.html")



from pyecharts import WordCloud

deal(res_nr, dic_nr)
output(res_nr)

attr_nr = []
value_nr = []
for nr in res_nr:
    attr_nr.append(nr['words'])
    value_nr.append(nr['nums'])

wordcloud = WordCloud("2019年03月份人名记", "2019年03月出现频率最高的人名",width=900, height=620, title_pos="center")
wordcloud.add("人名", attr_nr[:40], value_nr[:40], word_size_range=[20, 120], shape='tree')
wordcloud.render("2019年03月出现频率最高的人名.html")
# wordcloud



from pyecharts import Map
deal(res_ns, dic_ns)
output(res_ns)
attr_ns = []
value_ns = []
for ns in res_ns:
    attr_ns.append(ns['words'])
    value_ns.append(ns['nums'])
map = Map("2019年03月份各省市新闻出现频率", width=800, height=600)
try:
    map.add("", attr_ns, value_ns, maptype='china', is_visualmap=True, visual_text_color='#000', is_label_show=True)
except Exception as e:
            pass
map.render("2019年03月份各省市新闻出现频率.html")
# map

from pyecharts import Geo
deal(res_ns, dic_ns)
# output(res_ns)
data = []
data.clear()
for ns in res_ns:
    tupl = (ns["words"], ns["nums"])
    data.append(tupl)
   
geo = Geo("2019年03月份全国城市出现频率", "data from chinanews", title_color="#fff", title_pos="center",
width=800, height=600, background_color='#434a59')
attr, value = geo.cast(data)

geo.add("", attr, value, visual_range=[0, 300], visual_text_color="#fff",symbol_size=15, is_visualmap=True)
geo.render("2019年03月份全国城市出现频率.html")
# geo

from pyecharts import Pie
deal(res_nt, dic_nt)
output(res_nt)
attr_nt = []
value_nt = []
for nt in res_nt:
    attr_nt.append(nt['words'])
    value_nt.append(nt['nums'])
pie = Pie("2019年03月份出现的高频机构", title_pos='right')
pie.add("", attr_nt[2:15], value_nt[2:15], radius=[40, 75], label_text_color=None, is_label_show=True,
        legend_orient='vertical', legend_pos='left')
pie.render("2019年03月份出现的高频机构.html")
# pie







