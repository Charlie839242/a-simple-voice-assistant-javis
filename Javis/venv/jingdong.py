start_url="https://music.taihe.com/"

import requests
response=requests.get(url=start_url)
# print(response)
if response.status_code==200:
    # print(response.text)
    html=response.text
    with open("music.html","a+",encoding='utf-8') as file:
        file.write(html)
