import wave
import requests
import time
import os
from playsound import playsound
import base64
from aip import AipSpeech
from pronounce import pronounce
import os
from pyaudio import PyAudio, paInt16
import webbrowser
from play_music import music


base_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
APIKey = "0EtY9qLKdEt3GSiTLfGO6GPO"
SecretKey = "lsGdj5Htynk9ma14Z1D0CIOllEY2jcxX"
APP_ID = "24282208"


def create_Mp3(content):

    client = AipSpeech(APP_ID, APIKey, SecretKey)            # 获取一个在线请求的client
    result = client.synthesis(content, 'zh', 1, {'spd':6,'vol': 5})  # 设置并获取返回语音的二进制文件流
    print(result)

    if not isinstance(result, dict):                           # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        with open('audio.mp3', 'wb') as f:
            f.write(result)



if __name__ == '__main__':
    create_Mp3('主任')
    pronounce()

    create_Mp3('你好')
    pronounce()
