import requests
import time
from win11toast import toast

url = "http://query.bjeea.cn/queryService/rest/score/103"

music_src = "D:\\PythonProjects\\NEMT_2024_check_score\\思接千载 Cogitation of Epochs-HOYO-MiX.mp3"

cnt = 0

if __name__ == '__main__':
    while 1:
        response = requests.get(url)
        cnt += 1
        if cnt >= 30:
            # 通知当前status
            toast('当前 status：', str(response.status_code), icon = 'D:\\PythonProjects\\NEMT_2024_check_score\\心海_摸鱼.png')
            cnt = 0
        if response.status_code == 200:
            # 通知当前status
            # toast('当前 status：', str(response.status_code), icon = 'D:\\PythonProjects\\NEMT_2024_check_score\\心海_能量上升_4x.png')
            # toast('可以查了！','好运！', icon = 'D:\\PythonProjects\\NEMT_2024_check_score\\心海_能量上升_4x.png', audio = music_src, on_click = url)
            toast('可以查了！','好运！', icon = 'D:\\PythonProjects\\NEMT_2024_check_score\\心海_能量上升.png', audio = music_src, on_click = url, scenario='incomingCall', duration='long')

            # print(response.text)
            break
        time.sleep(60)