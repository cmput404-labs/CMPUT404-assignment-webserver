#  coding: utf-8 
import socketserver
import os.path
from os import path

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/


BASE_URL = "http://127.0.0.1:8080"

STR_TO_SEND = ""
END_LINE_STR = "\r\n"

class MyWebServer(socketserver.BaseRequestHandler):

    # def setup(self):

    
    def handle(self):
        self.clear()
        
        self.data = self.request.recv(1024).strip()
        print ("Got a request of: %s\n" % self.data)
        # self.request.sendall(bytearray("OK",'utf-8'))
       
        self.extract()        

        self.do_send()

            
    def clear(self):
        global STR_TO_SEND
        STR_TO_SEND = "HTTP/1.1 " 
        

    def extract(self):
        #convert into string
        data_array = self.data.decode("utf-8").split(' ')

        method_str =  data_array[0]
        print("method: " + method_str + '\n')

        dir_str = data_array[1]
        print("dir: " + dir_str + '\n')

        # check request method type
        if method_str == "GET":            
            self.GET(dir_str)
        else:
            self.not_GET()

    
    # complete status code of GET
    def GET(self, dir_str):
        global STR_TO_SEND
        print("in get")

        if self.exist_end_slash(dir_str):
            print("have slash")
            #check path
            if self.legal_path(dir_str):
                STR_TO_SEND += "200 OK" + END_LINE_STR
                self.load_content(dir_str)
            else:
                STR_TO_SEND += "404 Not Found" + END_LINE_STR
        else:
            print("dont have slash")
            #check availability
            if self.legal_path(dir_str):
                STR_TO_SEND += "301 Moved Permanently" + END_LINE_STR
                STR_TO_SEND += "Location: " + BASE_URL + dir_str + '/' + END_LINE_STR
            else:
                STR_TO_SEND += "404 Not Found" + END_LINE_STR
            

    
    def legal_path(self, dir_str):
        base_folder_str = 'www'
        norm_path_str = path.normpath(base_folder_str + dir_str)
        path_seq = [norm_path_str, base_folder_str]
        
        # the path exist AND path under 'www' folder
        return path.exists(norm_path_str) and (path.commonpath(path_seq) == base_folder_str)

    def load_content(self, dir_str):
        pass


    def not_GET(self):
        global STR_TO_SEND
        STR_TO_SEND += "405 Method Not Allowed" + END_LINE_STR


    def exist_end_slash(self, dir_str):
        return dir_str[-1] == '/'


    def do_send(self):
        global STR_TO_SEND
        self.request.sendall(bytearray(STR_TO_SEND,'utf-8'))


if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    socketserver.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = socketserver.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
