
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
        cookie = {'cookie': '_uuid=F4632D84-4AF9-A4E4-6EA4-9F494013965A67449infoc; buvid3=34CC82F6-6D68-4D26-A6C9-B3613B62307513439infoc; fingerprint=a36c0698c02fc7b82454285fb7ebad2e; buvid_fp=34CC82F6-6D68-4D26-A6C9-B3613B62307513439infoc; buvid_fp_plain=CAF2852A-5B2C-4DC4-9B62-B0AC1FB3F0B334777infoc; SESSDATA=edf48872%2C1637584882%2C9de74%2A51; bili_jct=74b3d40b75e6730241b75229a3db8f5f; DedeUserID=1063023997; DedeUserID__ckMd5=f1370fd7a98e5081; sid=alfhcb21; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(k|YkRlY)km0JuYkk|JJul); LIVE_BUVID=AUTO6816222028739495; CURRENT_QUALITY=80; bp_t_offset_1063023997=535026683109037144; bp_video_offset_1063023997=535786694761180219; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1623593021,1623642052,1623650554,1623652515; _dfcaptcha=ef73066ac2a8633493b9bf73d95661f4; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1623658405; PVID=3'}
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