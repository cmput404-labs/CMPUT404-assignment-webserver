# import requests

# r = requests.get('http://127.0.0.1:8080/')

# print(r.text)

import os.path
from os import path

def main():
    norm_path_str = path.normpath('www/../../../../../../../../../../../../etc/group')
    print(norm_path_str)
    a = [norm_path_str,'www/deep/index.html']

#    print ("File exists:"+str(path.exists('www/index.html/../')))
#    print ("Is it File?" + str(path.isfile('www/index.html/../')))
#    print ("File exists:" + str(path.exists('career.guru99.txt')))
    print ("directory exists:" + str(path.basename('www/deep/index.html')))
    print ("common path: " + path.commonpath(a))
#    print ("same file: " + path.samefile('www/index.html/../','/'))

if __name__== "__main__":
   main()