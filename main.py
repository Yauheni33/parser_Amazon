from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Cookie': 'session-id=145-8795564-8065136; session-id-time=2082787201l; csm-hit=5PFT7TFM7JVB716M9NFS+s-VQBEPCMMM485XW9M9N36|1518875748401; x-wl-uid=1toMjpvuG1H2WqSdM3xo6LTl1y6zu4+I4mGNoxcDURWr0N+XEJx3NjyqkCeOFDDAjtD/TTSknzmg=; ubid-main=130-5951734-2759747; session-token=iQ2sfWqeYRhqgWa09gCRVYaLlMF8PlxNN4nmYOC4NyQ6aQaK1zhK/Nf/uFRtPXmZ+Ya6oHSO/c7gC7HeyY7DSuEc6lI42nOnQ64gNZ5AS7iJtwVkb40MJTY3esM73x6SKSgz0tUBNvPWVW1JggS2kps/UbHfb7egAGH386C4RowEK64ldJ9XYqT7cu4KrL4une9Zs8NpVx9qgUebE/sxy6Z06MICwIKduvNnu8kFKxOmWz/hWLOjGjTghw5eVojg',
    "session-token": "iQ2sfWqeYRhqgWa09gCRVYaLlMF8PlxNN4nmYOC4NyQ6aQaK1zhK/Nf/uFRtPXmZ+Ya6oHSO/c7gC7HeyY7DSuEc6lI42nOnQ64gNZ5AS7iJtwVkb40MJTY3esM73x6SKSgz0tUBNvPWVW1JggS2kps/UbHfb7egAGH386C4RowEK64ldJ9XYqT7cu4KrL4une9Zs8NpVx9qgUebE/sxy6Z06MICwIKduvNnu8kFKxOmWz/hWLOjGjTghw5eVojg",
    "Connection": "keep-alive",
    "bbn":	"2350149011",
    "ie":	"UTF8",
    "qid":	"1518858846",
    "rh":	"n:2350149011,p_36:100-99999999",
}

cookies = dict(head)
main = "https://www.amazon.com"
page = "https://www.amazon.com/s/ref=sr_pg_1?rh=n%3A2350149011%2Cp_36%3A100-99999999&bbn=2350149011&ie=UTF8&qid=1518858846"
#page = "https://www.amazon.com/s/ref=sr_pg_2?rh=n%3A2350149011%2Cp_36%3A100-99999999&page=2&bbn=2350149011&ie=UTF8&qid=1519036423"

for count in range(400):

    r = requests.get(page, headers=cookies)
    text = BeautifulSoup(r.text, "html.parser")

    print("page = ", count)
    listPage = text.findAll("a", {"class": "a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})
    index = 1
    for i in listPage:
        new_page = BeautifulSoup((requests.get(i['href'], headers=cookies)).text, "html.parser")
        n = new_page.findAll("span", {"id": "btAsinTitle"})
        print("game = ", index)
        print((n[0]).text)
        n = new_page.find("div", {"class": "buying"}).find('a')
        print(n.text)
        n = new_page.find("div", {"id": "mas-developer-info"}).findAll("a", {"class": "a-link-normal"})
        for j in range(len(n)):
            if ((n[j])['href'])[0] == '/':
                print("https://www.amazon.com" + (n[j])['href'])
            else:
                print((n[j])['href'])
        print()
        index += 1

    q = text.find("span", {"class": "pagnLink"}).find("a")
    page = main + q['href']