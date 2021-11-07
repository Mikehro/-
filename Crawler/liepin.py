import requests
import re
import json
import csv
f = open('招聘数据1.csv', mode='a', encoding='utf-8', newline='')
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
        dit = {
            '职位': index['job_name'],
            '公司名字': index['company_name'],
            '城市': index['workarea_text'],
            '薪资': index['providesalary_text'],
            '招聘信息': '|'.join(index['attribute_text']),
            '公司属性': index['companyind_text'],
            '公司规模': index['companysize_text'],
            '企业性质': index['companytype_text'],
            '招聘发布日期': index['issuedate'],
            '公司详情页': index['company_href'],
            '招聘详情页': index['job_href'],
        }
        csv_writer.writerow(dit)
        print(dit)
