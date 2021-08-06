import requests

# 发送请求api，得到天气信息，发送的参数包含城市和聚合数据请求的key.
def getWeather_infor(city):

    url = "http://apis.juhe.cn/simpleWeather/query"            # 请求的地址头部
    params = {                                                 # 地址参数
        "city": city,
        "key": "3fc906e9272620531cd3651136fa9258"
    }
    resp = requests.get(url, params=params).json()       # 发出请求,使用json()，返回了字典类型数据
    return resp


# 筛选信息，选取需要的内容，并处理
def select_info(resp):
    if resp["result"]:  # 请求成功
        realtime_Weather = resp["result"]["realtime"]           # 当前温度
        day_Weather = resp["result"]["future"][0]               # 当天天气
        temp = day_Weather["temperature"].split("/")            # 分割最低温度和最高温度
        speak_content = f'当前温度是{realtime_Weather["temperature"]}℃,相对湿度{realtime_Weather["humidity"]}%' \
                        f',天气：{realtime_Weather["info"]},{realtime_Weather["direct"]},' \
                        f'强度：{realtime_Weather["power"]}。\n' \
                        f'温度范围：{temp[0]}--{temp[1]},天气变化：{day_Weather["weather"]}'
    else:
        speak_content = resp["reason"]
    return speak_content


if __name__ == '__main__':
    city = input("\n请输入城市(输入exit可退出):")
    resp=getWeather_infor(city)
    print(resp)
    resp=select_info(resp)
    print(resp)