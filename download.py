import requests, time
from pathlib import Path


for i in range(1, 635):

    filename = 'katalog/'+str(i)+'.pdf'
    my_file = Path(filename)
    if my_file.is_file():
        print("exists", filename)
        continue


    #time.sleep(1)
    lenn = str(i)
    page = "0" * (4 - len(lenn)) + str(i)
    print(page)
    url = 'https://www.ssb.gov.tr/urunkatalog/tr/files/assets/common/downloads/page'+page+'.pdf'
    print(url)
    try:
        resp = requests.get(url)
        with open('katalog/'+str(i)+'.pdf', 'wb') as f:
            f.write(resp.content)
    except:
        print("error")
