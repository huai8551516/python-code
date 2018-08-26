

import os,chardet
import pythoncom
from win32com.shell import shell
from win32com.shell import shellcon

def createDesktopLnk(filename, lnkname):
	"""Create Application lnk to Desktop"""
	shortcut = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink, None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IShellLink)

	shortcut.SetPath(filename)

	if os.path.splitext(lnkname)[-1] != ".lnk":
		lnkname += ".lnk"
	
	#get desktop path
	desktopPath = shell.SHGetPathFromIDList(
		shell.SHGetSpecialFolderLocation(0, shellcon.CSIDL_DESKTOP))
	desktopPath = desktopPath.decode()

	lnkname = os.path.join(desktopPath, lnkname)
	shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname, 0)

if __name__ == "__main__":
	createDesktopLnk("D:\\复核客户端RFID优化版0806\\FHFH.exe", "复核程序")