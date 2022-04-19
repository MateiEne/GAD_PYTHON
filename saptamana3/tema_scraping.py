from bs4 import BeautifulSoup
import requests
import pandas as pd
dataset = []

for x in range(20, 28):
    r = requests.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{x}-ianuarie-ora-13-00/")
    link = BeautifulSoup(r.text, "html.parser")
    #print(link)

    table = link.find_all('table', attrs={'width': '710'})
    #print(table)
    header = []

    for i in table:
        for tbody in i.find_all('tbody'):
            td_list = []
            for tr in tbody.find_all('tr'):
                if tr.find_all('td'):
                    header = [td.get_text() for td in tr.find_all('td')]
                    for cnt in range(0, len(header)):
                        transTable = header[cnt].maketrans("ăîâșț", "aiast")
                        header[cnt] = header[cnt].translate(transTable)
                    dataset.append(header)
    dataset[-1].insert(0, f"{x}-ian")

df = pd.DataFrame(dataset)
df.to_csv('Tabel-date-COVID-BS.csv')