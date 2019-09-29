import requests
import pandas as pd
import openpyxl


def coleta_anp(url):
    xlsx = requests.get(url)

    with open(r'/tmp/diesel.xlsx', 'wb') as f:
        f.write(xlsx.content)
        print(f.name)
    wb = openpyxl.load_workbook(f.name)
    ws = wb.active
    balde = []
    for row in ws.iter_rows():
        info = []
        if(row[4].value == 'ÓLEO DIESEL'):
            info.append(row[1].value)
            info.append(row[3].value)
            info.append(row[4].value)
            info.append(row[10].value)
            info.append(row[12].value)
            balde.append(info)
    maisatuais = []
    for b in range(len(balde) - 1, 0, -1):
        if len(maisatuais) == 27:
            break
        maisatuais.append(balde[b])
    for atual in maisatuais:
        print(atual)
            # for cell in row:
            #     print(cell.value)
            # print(' ')
        # print(row[3].value)
        # print(row[5].value)
        # print(row[7].value)
        # print(row[10].value)
        # print(row[16].value)
        # for cell in row:
        #     print (cell.value)

coleta_anp('http://www.anp.gov.br/images/Precos/Semanal2013/SEMANAL_ESTADOS-DESDE_2013.xlsx')

# df = pd.read_excel(f.name)
# for key, value in df.iterrows():
#     print(value['DATA FINAL'])
