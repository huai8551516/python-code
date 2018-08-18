#-*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar,QTextEdit, QVBoxLayout, QHBoxLayout
import sys,os,shutil

#窗口类

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		#self.progress_bar = QProgressBar()
		self.setWindowTitle("一键自动化部署复核程序环境")
		self.setGeometry(200, 200, 200, 200)
		self.setFixedSize(200, 200)
		self.start_btn = QPushButton("启动", self)
		self.start_btn.clicked.connect(self.start)
		self.textEdit = QTextEdit(self)
		self.textEdit_content = ''
		hbox = QHBoxLayout()
		hbox.addWidget(self.start_btn)
		vbox = QVBoxLayout(self)
		vbox.addLayout(hbox)
		vbox.addWidget(self.textEdit)
		#self.start_btn.resize(40, 80)
		self.show()
	def start(self):
	    self.textEdit.clear()	
	    dir_list = ['D:\\摄像头视频', 'D:\\摄像头视频临时', 
	                'D:\\摄像头视频错误', 'D:\\摄像头视频本机备份']
	    for d in dir_list:
	    	if not os.path.exists(d):
	    		os.makedirs(d)
	    		self.textEdit_content += d + "创建成功\n"
	    		self.textEdit.setText(self.textEdit_content)
	    	else:
	    		self.textEdit_content += d + "已经存在\n"
	    		self.textEdit.setText(self.textEdit_content)
		#移动文件夹
	    video_path = "C:\\Program Files (x86)\\Bandicam"
	    fh_path = "Y:\\111\\复核客户端RFID优化版0806"
	    if not os.path.exists("C:\\Bandicam"):
		    shutil.move(video_path, "C:\\")
	    else:
		    self.textEdit_content += "C:\\Bandicam " + "已经存在\n"
		    self.textEdit.setText(self.textEdit_content)
	    if not os.path.exists("D:\\复核客户端RFID优化版0806"):
	    	shutil.copytree(fh_path, "D:\\复核客户端RFID优化版0806")
	    else:
		    self.textEdit_content += "D:\\复核客户端RFID优化版0806 " + "已经存在\n"
		    self.textEdit.setText(self.textEdit_content)

def main():
	app = QApplication(sys.argv)
	screen = MainWindow()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()