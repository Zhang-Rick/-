
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
import requests
import time
import json

class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('UI\\Main.ui')

        self.ui.pushButton.clicked.connect(self.handleCalc)

    def DanmuSent(roomid, content):
        url = 'https://api.live.bilibili.com/msg/send'
        data = {
            'bubble': '0',
            'color': '5566168',
            'mode': '1',
            'fontsize': '25',
            'msg': content,
            'roomid': roomid,
            'csrf': '74b3d40b75e6730241b75229a3db8f5f',
            'csrf_token': '74b3d40b75e6730241b75229a3db8f5f'
        }
        #data['msg'] = content
        #data['roomid'] = roomid
        cookie = {'cookie': 自己输入}#...我刚上传，b站昵称就被改了。。。
        danmuSent = requests.post(url, cookies=cookie, data=data).text
        print((danmuSent))

    def handleCalc(self):
        roomid = self.ui.lineEdit.text()
        url = 'https://api.live.bilibili.com/xlive/web-room/v1/dM/gethistory'
        data = {
            'bubble': '0',
            'color': '5566168',
            'mode': '1',
            'fontsize': '25',
            'roomid': roomid,
            'csrf': '74b3d40b75e6730241b75229a3db8f5f',
            'csrf_token': '74b3d40b75e6730241b75229a3db8f5f'
        }
        #data['roomid'] = roomid
        req = requests.post(url, data=data)
        room = json.loads(req.text)['data']['room']
        filename = 'danmu' + roomid + '.log'
        file = open(filename, mode='a')
        lines = ['']

        for element in room:
            text = element['text']
            timeline = element['timeline']
            nickname = element['nickname']

            msg = "{}: {}: {}.".format(timeline, nickname, text)
            with open(filename) as f:
                lines = f.read().splitlines()
            # print(lines[0])
            # print(lines)
            if msg not in lines:
                file.write(msg)
                file.write('\n')
  #                if text == '你是左手写字吗？':
  #                   # print(text, '你是左手写字吗？', text == '你为啥这么早毕业？')
  #                   DanmuSent(roomid, "因为手机镜像!")
  #              elif text == '主播好帅？':
  #                  # print(text, '你是左手写字吗？', text == '你为啥这么早毕业？')
  #                  DanmuSent(roomid, "你也帅")
  #              elif text == '你为啥这么早毕业？':
  #                  # print(text, '你是左手写字吗？', text == '')
  #                  DanmuSent(roomid, "因为我帅!")
            # print(msg)




app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
