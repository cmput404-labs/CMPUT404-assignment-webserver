# import requests

# r = requests.get('http://127.0.0.1:8080/')

# print(r.text)

import os.path
from os import path

def legal_path(dir_str):
        base_folder_str = 'www'
        norm_path_str = path.normpath(base_folder_str + dir_str)
        path_seq = [norm_path_str, base_folder_str]
        
        # the path exist AND path under 'www' folder
        return path.exists(norm_path_str) and (path.commonpath(path_seq) == base_folder_str)

def main():
    # norm_path_str = path.normpath('www/../../../../../../../../../../../../etc/group')
    # print(norm_path_str)
    # a = [norm_path_str,'www/deep/index.html']

   print ("File exists:"+str(path.exists('www/deep')))
   print ("Is it File?" + str(path.isfile('www/deep')))
#    print ("File exists:" + str(path.exists('career.guru99.txt')))
    # print ("directory exists:" + str(path.basename('www/deep/index.html')))
    # print ("common path: " + path.commonpath(a))
#    print ("same file: " + path.samefile('www/index.html/../','/'))

    # print(legal_path("/base.css"))

if __name__== "__main__":
   main()