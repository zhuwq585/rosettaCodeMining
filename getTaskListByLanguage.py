from urllib import request
from bs4 import BeautifulSoup

ROOT_URL = "http://www.rosettacode.org"
TASKS_LIST_URL = "http://www.rosettacode.org/wiki/Category:Programming_Tasks"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "host": "www.rosettacode.org"
}
TARGET_LANGUAGE_SET = {"Python","Java","JavaScript","C_sharp","PHP","C","C++","R","TypeScript","Swift","Objective-C","Kotlin","MATLAB","Go","VBA","Rust","Ruby","Scala","Visual_Basic","Dart"}

for language in TARGET_LANGUAGE_SET:
    url = "http://www.rosettacode.org/wiki/Category:" + language
    print(url)
    req = request.Request(url=url, headers=HEADERS, method="POST")
    res = request.urlopen(req)
    htmlContent = res.read()
    bs = BeautifulSoup(htmlContent, "html.parser")
    
    file = open(language+"Tasks.txt" ,"w")
    list = bs.select("#mw-pages a")
    for aTag in list:
        file.write( ROOT_URL + aTag.attrs['href'] + "#" + language +"\n" )
    file.close()
pass