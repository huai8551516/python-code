#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar,QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QFile, QStandardPaths
from PyQt5.QtGui import QTextCursor
import PyQt5.sip
import sys,os,shutil
from threading import Thread
#窗口类

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        #self.progress_bar = QProgressBar()
        self.setWindowTitle("一键自动化部署复核程序环境")
        self.setGeometry(200, 200, 200, 200)
        self.setFixedSize(200, 250)
        self.start_btn = QPushButton("启动", self)
        self.start_btn.clicked.connect(self.start)
        self.textEdit = QTextEdit(self)
        self.textEdit_content = ''
        self.textEdit.setEnabled(False);

        self.update_timer = QTimer()
        self.update_timer.setInterval(1000)
        self.update_timer.start()
        self.update_timer.timeout.connect(self.updateEdt)


        # t_updateEdt = Thread(target=self.updateEdt)
        # t_start.setDaemon(True)
        # t_start.start() # start thread
        # threads.append(t_updateEdt)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_btn)
        vbox = QVBoxLayout(self)
        vbox.addLayout(hbox)
        vbox.addWidget(self.textEdit)
        #self.start_btn.resize(40, 80)
        self.show()
    def start(self):
        self.textEdit_content = ''
        #多线程
        self.threads = []
        self.t_start = Thread(target=self.do_auto)
        self.t_start.setDaemon(True)

        self.t_start.start() # start thread
        self.threads.append(self.t_start)
    
    def do_auto(self):
        dir_list = ['D:\\摄像头视频', 'D:\\摄像头视频临时',
                    'D:\\摄像头视频错误', 'D:\\摄像头视频本机备份']
        for d in dir_list:
            if not os.path.exists(d):
                os.makedirs(d)
                self.textEdit_content += d + "创建成功\n"
            else:
                self.textEdit_content += d + "已经存在\n"
        try:
            #移动文件夹
            video_path = "C:\\Program Files (x86)\\Bandicam"
            fh_path = "Y:\\111\\Debug"
            dest_file = "D:\\Debug"
            if os.path.exists(video_path):
                if not os.path.exists("C:\\Bandicam"):
                    shutil.move(video_path, "C:\\")
                else:
                    self.textEdit_content += "C:\\Bandicam " + "已经存在\n"
            else:
                self.textEdit_content += video_path + "不存在，请安装Bandicam\n"
            if os.path.exists(dest_file):
                self.textEdit_content += "正在删除老版复核程序....\n"
                shutil.rmtree(dest_file)
                self.textEdit_content += "D:\\Debug 已删除\n"

            if os.path.exists(fh_path):                    
                self.textEdit_content += "正在复制新版复核程序....\n"
                shutil.copytree(fh_path, dest_file)
                self.textEdit_content += "新版复核程序已经复制完成\n"
                self.createDesktopLnk("D:\\Debug\\FHFH.exe", "复核程序")
                self.textEdit_content += "桌面快捷方式创建成功,可以关闭程序了\n"

            else:
                self.textEdit_content += fh_path + "目录不存在"
                self.textEdit_content += "请查看Y盘是否打开，或文件是否存在"
        except Exception as e:
            print(e)

    def updateEdt(self):
        #self.textEdit.clear()	
        self.textEdit.setText(self.textEdit_content)
        #保持编辑器在光标最后一行
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.textEdit.setTextCursor(cursor)
    #创建快捷方式
    def createDesktopLnk(self, filename, lnkname):
        """Create Application lnk to Desktop"""
        if os.path.splitext(lnkname)[-1] != ".lnk":
            lnkname += ".lnk"
        lnkname = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation)+"/"+lnkname
        if os.path.exists(lnkname):
            os.remove(lnkname)
        QFile.link(filename, lnkname)



def main():
    app = QApplication(sys.argv)
    screen = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
	main()