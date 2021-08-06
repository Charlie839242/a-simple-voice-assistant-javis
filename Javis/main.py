#贾维斯可识别的口令有三条：
# 1：贾维斯+城市+天气  例如 贾维斯成都天气
# 2：贾维斯今天NBA+XXX球队+怎么样   例如  贾维斯今天NBA湖人队怎么样
# 3：贾维斯播放+歌名   例如  贾维斯播放稻香
import wave
import requests
import time
import os
from playsound import playsound
import base64
from aip import AipSpeech
from pyaudio import PyAudio, paInt16
import webbrowser
from play_music import music
from WeatherBroadcast import getWeather_infor,select_info
from pronounce import pronounce
from NBA import getNBA_infor,select_info2



framerate = 16000  # 采样率
num_samples = 2000  # 采样点
channels = 1  # 声道
sampwidth = 2  # 采样宽度2bytes
FILEPATH = 'speech.wav'

base_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
APIKey = "0EtY9qLKdEt3GSiTLfGO6GPO"
SecretKey = "lsGdj5Htynk9ma14Z1D0CIOllEY2jcxX"
APP_ID = "24282208"

HOST = base_url % (APIKey, SecretKey)


def getToken(host):
    res = requests.post(host)
    return res.json()['access_token']


def save_wave_file(filepath, data):
    wf = wave.open(filepath, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b''.join(data))
    wf.close()


def my_record():
    pa = PyAudio()
    stream = pa.open(format=paInt16, channels=channels,
                     rate=framerate, input=True, frames_per_buffer=num_samples)
    my_buf = []
    # count = 0
    t = time.time()
    print('正在录音...')

    while time.time() < t + 10:  # 秒
        string_audio_data = stream.read(num_samples)
        my_buf.append(string_audio_data)
    print('录音结束.')
    save_wave_file(FILEPATH, my_buf)
    stream.close()


def get_audio(file):
    with open(file, 'rb') as f:
        data = f.read()
    return data


def speech2text(speech_data, token, dev_pid=1537):
    FORMAT = 'wav'
    RATE = '16000'
    CHANNEL = 1
    CUID = '*****'
    SPEECH = base64.b64encode(speech_data).decode('utf-8')

    data = {
        'format': FORMAT,
        'rate': RATE,
        'channel': CHANNEL,
        'cuid': CUID,
        'len': len(speech_data),
        'speech': SPEECH,
        'token': token,
        'dev_pid': dev_pid
    }
    url = 'https://vop.baidu.com/server_api'
    headers = {'Content-Type': 'application/json'}
    # r=requests.post(url,data=json.dumps(data),headers=headers)
    print('正在识别...')
    r = requests.post(url, json=data, headers=headers)
    Result = r.json()
    if 'result' in Result:
        return Result['result'][0]
    else:
        return Result


# 使用百度语音，baidu-aip,生成mp3
def Create_Mp3(content):

    client = AipSpeech(APP_ID, APIKey, SecretKey)            # 获取一个在线请求的client
    result = client.synthesis(content, 'zh', 1, {'spd':4,'vol': 6})  # 设置并获取返回语音的二进制文件流

    if not isinstance(result, dict):                           # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        with open('audio.mp3', 'wb') as f:
            f.write(result)




def openbrowser(text):
    maps = {
        '百度': ['百度', 'baidu'],
        '腾讯': ['腾讯', 'tengxun'],
        '网易': ['网易', 'wangyi']


    }
    if text in maps['百度']:
        webbrowser.open_new_tab('https://www.baidu.com')
    elif text in maps['腾讯']:
        webbrowser.open_new_tab('https://www.qq.com')
    elif text in maps['网易']:
        webbrowser.open_new_tab('https://www.163.com/')
    else:
        webbrowser.open_new_tab('https://www.baidu.com/s?wd=%s' % text)

def jarvis(text):
    a='贾维斯'
    b='播放'
    c='天气'
    d='NBA'
    if a in text:
        print("success")
        text = text.replace(a, '')
        print("主人我在")
        Create_Mp3('主人我在')
        pronounce()
        if b in text:
            print("好的，播放音乐")
            Create_Mp3('好的，播放音乐')
            pronounce()
            name = text.replace(b,'')
            music(name);
        if c in text:
            text = text.replace(c,'')
            resp = getWeather_infor(text)
            resp = select_info(resp)
            Create_Mp3(resp)
            pronounce()
        if d in text:
            text = text.replace(d,'')
            text = text.replace('今天','')
            text = text.replace('怎么样','')
            resp = getNBA_infor()
            resp = select_info2(text,resp)
            Create_Mp3(resp)
            pronounce()
    else:
        print("fail")
        Create_Mp3('我睡觉去了')

if __name__ == '__main__':
    flag = 'y'
    while flag.lower() == 'y':
        print('请输入数字选择语言：')
        devpid = input('1536：普通话(简单英文),1537:普通话(有标点),1737:英语,1637:粤语,1837:四川话\n')
        my_record()
        TOKEN = getToken(HOST)
        speech = get_audio(FILEPATH)
        result = speech2text(speech, TOKEN, int(devpid))
        print(result)
        # if type(result) == str:
        #     openbrowser(result.strip('，'))
        if type(result) == str:
            jarvis(result.strip('，'))
        flag = input('Continue?(y/n):')