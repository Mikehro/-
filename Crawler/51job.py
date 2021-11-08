import requests
import re
import json
import csv
import pymysql
f = open('前程无忧网招聘数据.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '职位',
    '公司名字',
    '城市',
    '薪资',
    '招聘信息',
    '公司属性',
    '公司规模',
    '企业性质',
    '招聘发布日期',
    '公司详情页',
    '招聘详情页',
])
csv_writer.writeheader()

conn = pymysql.Connect(host = 'rm-bp1y78ry9s88298yfzo.mysql.rds.aliyuncs.com',
                       port = 3306,
                       user = 'huangdong0122',
                       passwd = 'Huangdong521',
                       db = '爬虫数据库',
                       charset='utf8')
cur = conn.cursor()

for page in range(1, 11):
    url = f'https://search.51job.com/list/000000,000000,0000,01%252c37%252c38,9,99,+,2,{page}.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    html_data = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text, re.S)[0]
    json_data = json.loads(html_data)
    for index in json_data['engine_jds']:
        # pprint.pprint(index)
        index['attribute_text']='|'.join(index['attribute_text'])
        into = "INSERT INTO 51job(job_name,company_name,workarea_text,providesalary_text,attribute_text,companyind_text,companysize_text,companytype_text,issuedate,company_href,job_href) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (index['job_name'],index['company_name'],index['workarea_text'],index['providesalary_text'],index['attribute_text'],index['companyind_text'],index['companysize_text'],index['companytype_text'],index['issuedate'],index['company_href'],index['job_href'])
        cur.execute(into, values)
        conn.commit()
        dit = {
            '职位': index['job_name'],
            '公司名字': index['company_name'],
            '城市': index['workarea_text'],
            '薪资': index['providesalary_text'],
            '招聘信息': index['attribute_text'],
            '公司属性': index['companyind_text'],
            '公司规模': index['companysize_text'],
            '企业性质': index['companytype_text'],
            '招聘发布日期': index['issuedate'],
            '公司详情页': index['company_href'],
            '招聘详情页': index['job_href'],
        }
        csv_writer.writerow(dit)
        print(dit)
conn.close()

