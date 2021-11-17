import requests
import csv

url = "https://careers.tencent.com/tencentcareer/api/post/Query"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
}

params = {'area': ' cn',
          'attrId': ' ',
          'bgIds': ' ',
          'categoryId': ' ',
          'cityId': ' ',
          'countryId': ' ',
          'keyword': ' ',
          'language': ' zh-cn',
          'pageIndex': ' 1',
          'pageSize': ' 10',
          'parentCategoryId': ' ',
          'productId': ' ',
          'timestamp': ' 1602211262824'}


def parse_json(url, params={}):
    """解析url，得到字典"""
    response = requests.get(url=url, headers=headers, params=params)
    return response.json()


def get_position(data):
    """获取职位数据"""
    item = {
        "postion_name":"",#职位名称
        #"postion_department":"",#职位部门
        "postion_location":"",#职位所在地
        "postion_country":"",#职位所在国家
        "postion_category":"",#职位类别
        "postion_url":"",#职位url
    }
    data_list = data["Data"]["Posts"]
    for data in data_list:
        item["postion_name"] = data["RecruitPostName"]
        item["postion_location"] = data["LocationName"]
        item["postion_country"] = data["CountryName"]
        item["postion_category"] = data["CategoryName"]
        item["postion_url"] = data["PostURL"]

        save(item)

def save(item):
    """将数据保存到csv中"""
    with open("./腾讯招聘.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(item.values())


def start():
    for i in range(1,618):
        params["pageIndex"] = i
        data = parse_json(url,params)
        get_position(data)

if __name__ == '__main__':
    with open("./腾讯招聘.csv", "a", encoding="utf-8") as file:
       writer = csv.writer(file)
       writer.writerow(["职位名称", "职位所在地","职位所在国家","职位类别","职位url"])
    start()
