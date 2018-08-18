# -*- coding: utf-8 -*-

import os
import sys
reload(sys)
sys.setdefaultencoding('gbk')

def findFile(fname, path='.'):
    basePath = os.path.abspath(path)
    dirlst = os.listdir(path)
    for file in dirlst:
        try:
            newPath = os.path.join(basePath, file)
            if os.path.isdir(newPath):
                findFile( fname, newPath)
            else:
                if fname in file:
                    print newPath
        except:
            continue


if __name__ == '__main__':
    findFile('.zip', 'd:\\')
