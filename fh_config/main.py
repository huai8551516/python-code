# -*- coding: gbk -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget
 
 
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
 
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
     
    sys.exit(app.exec_())

# #打开复合程序配置文件
# file = open('FHFH.exe.config', "r", encoding="utf-8")
# file_content = file.read()
# file.close()

# p = '<add key="AccessWebsiteUrl" value="http://124.160.226.98:8081/D:/shipin" />'

