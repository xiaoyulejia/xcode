import requests
import sys
import os
import json  

n = 1
m = int(input("抓取次数:"))
def get_content (url):
   resp = requests.get(url)
   resp.encoding="utf-8"
   return resp.text
url = "https://v1.hitokoto.cn"

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")
 
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
 
    def flush(self):
        pass
 

path = os.path.abspath(os.path.dirname(__file__))
type = sys.getfilesystemencoding()
sys.stdout = Logger('a.txt')
 

while n <= m:
   content = get_content(url)
   load_data = json.loads(content)
   print (load_data['hitokoto'] + '-- ' +  load_data['from'])
   n = n+1
