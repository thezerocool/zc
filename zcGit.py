#!/usr/bin/python3

import requests
from os import getcwd

def updateGitFiles():
    files = ['testDownload.txt','volCtrl.py']
    for fileS in files:
        print(fileS)
        url = "https://raw.githubusercontent.com/thezerocool/zc/master/" + fileS
        directory = getcwd()
        print(directory)
        filename = directory + "\\" + fileS           # first \ escapes
        print(filename)
        r = requests.get(url)

        f = open(filename,'wb')
        f.write(r.content)
        f.close()
    # git_url = ("https://github.com/thezerocool/zc.git")

if __name__ == '__main__':
    updateGitFiles()
    print("zc success")
    #input()
