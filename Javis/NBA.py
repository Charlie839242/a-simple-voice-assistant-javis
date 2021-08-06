import requests

# 发送请求api，得到天气信息，发送的参数包含城市和聚合数据请求的key.
def getNBA_infor():

    url = "http://apis.juhe.cn/fapig/nba/query"            # 请求的地址头部
    params = {                                                 # 地址参数
        "key": "3dbe962ae3d49f6773fa6e5167e4be73"
    }
    resp = requests.get(url, params=params).json()       # 发出请求,使用json()，返回了字典类型数据
    return resp

def select_info2(team,resp):
    matches = resp["result"]["matchs"][2]["list"][0]
    if (team in matches["team1"])or(team in matches["team2"]):
        speak_content = f'今天是{matches["team1"]}对抗{matches["team2"]},比分为{matches["team1_score"]}比{matches["team2_score"]}'
    else:
        speak_content = "今天没有该队的比赛"
    return speak_content

