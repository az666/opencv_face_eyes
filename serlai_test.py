import easygui
import serial.tools.list_ports
# 所发十六进制字符串010591F50000F104
cmd = [0x01, 0x05, 0x91, 0xF5, 0x00, 0x00, 0xF1, 0x04]
plist = list(serial.tools.list_ports.comports())
if len(plist) <= 0:
    print("没有发现端口!")
else:
    plist_0 = list(plist[0])
    serialName = plist_0[0]
    serialFd = serial.Serial(serialName, 9600, timeout=60)
    print("可用端口名>>>", serialFd.name)
class Ser(object):
    def __init__(self):
        # 打开端口
        self.port = serial.Serial(port='COM4', baudrate=9600, bytesize=8, parity='E', stopbits=1, timeout=2)

    # 发送指令的完整流程
    def send_cmd(self, cmd):
        self.port.write(cmd)
        response = self.port.readall()
        response = self.convert_hex(response)
        return response

    # 转成16进制的函数
    def convert_hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result
while (1):
    Yes_or_No = easygui.buttonbox("是否测试成功？", choices=['Yes', 'No', '退出'])  # 提供简易UI
    if Yes_or_No == '退出': break
    if Yes_or_No == 'Yes':
        demo = b"2"  # 传入2的ASCII码 这里用b+str强制转换
    else:
        demo = b"1"  # 传入1的ASCII码 这里用b+str强制转换

   # ser.write(demo)
   # s = ser.read(1)
    #print(s)