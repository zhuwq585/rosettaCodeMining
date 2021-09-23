from urllib import request
from bs4 import BeautifulSoup
import time
ROOT_URL = "http://www.rosettacode.org"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "host": "www.rosettacode.org"
}
TARGET_LANGUAGE_SET = {"Python","Java","JavaScript","C sharp","PHP","C","C++","R","TypeScript","Swift","Objective-C","Kotlin","MATLAB","Go","VBA","Rust","Ruby","Scala","Visual Basic","Dart"}
taskList = []
for line in open("taskList.txt","r").readlines():
    taskList.append(line[:-1])

# testurl = "http://www.rosettacode.org/wiki/Abundant_odd_numbers"
passedTask = []
mostSupported = (0,"")
for url in taskList:
    req = request.Request(url=url, headers=HEADERS, method="POST")
    res = request.urlopen(req)
    htmlContent = res.read()
    bs = BeautifulSoup(htmlContent, "html.parser")
    languageSet = set()
    for languageNameTag in bs.select("#toc .toclevel-1 a .toctext"):
        languageSet.add(languageNameTag.string)

    if TARGET_LANGUAGE_SET.issubset(languageSet):
        passedTask.append(url)
        print(url + "--" + 'pased')
    else:
        if len(languageSet.intersection(TARGET_LANGUAGE_SET)) > mostSupported[0]:
            mostSupported = (len(languageSet.intersection(TARGET_LANGUAGE_SET)), url)
            print("mostSupported:" + str(mostSupported) + "length: " + str(mostSupported[0]))
        elif len(languageSet.intersection(TARGET_LANGUAGE_SET)) == mostSupported[0]:
            mostSupported = mostSupported + (len(languageSet.intersection(TARGET_LANGUAGE_SET)), url)

    time.sleep(0.1)

file = open("result.txt","w")
if len(passedTask) != 0:
    for line in passedTask:
        file.write(line + "\n")
else:
    file.write(str(mostSupported))
pass