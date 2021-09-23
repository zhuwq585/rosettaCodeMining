from urllib import request
from bs4 import BeautifulSoup

ROOT_URL = "http://www.rosettacode.org"
TASKS_LIST_URL = "http://www.rosettacode.org/wiki/Category:Programming_Tasks"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "host": "www.rosettacode.org"
}


req = request.Request(url=TASKS_LIST_URL, headers=HEADERS, method="POST")
res = request.urlopen(req)
htmlContent = res.read()

bs = BeautifulSoup(htmlContent, "html.parser")
taskList = []
for aTag in bs.select("#mw-pages a"):
    taskList.append(ROOT_URL + aTag.attrs['href'])

file = open("allTasks.txt","w")
for taskUrl in taskList:
    file.write(taskUrl+"\n")

