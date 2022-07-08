from datetime import date
import requests
from distutils.util import execute
import zipfile
import io
import warnings
import pandas as pd


# formando url, fazendo junção com a data do arquivo
def forming_url(date):
    year = date.year
    month = date.month
    if month < 10:
        month = '0' + str(month)

    file_date = str(year) + str(month)

    response = requests.get('https://www.portaldatransparencia.gov.br/download-de-dados/pep/' + file_date)
    return response
#url completa:
url = forming_url(date(2022, 5, 20))


#função que salva arquivo e faz a extração
def save_file(url):
    warnings.filterwarnings('ignore')
    file = zipfile.ZipFile(io.BytesIO(url.content))
    path = './'
    return file.extractall(path)
save_file(url)


#leitura do arquivo atravez do pandas
file = pd.read_csv('/202205_PEP.csv', sep = ';', encoding = 'ISO-8859-1')


#seleção da coluna de nomes que será verificada
column_names = pd.DataFrame(file)["Nome_PEP"]


#nomes a sereem verificados
names = {
        'ROBERTO FURIAN ARDENGHY': "NÃO É PPE",
        'NICOLAS SIMONE': "NÃO É PPE",
        'JOAQUIM SILV E LUNA': "NÃO É PPE",
        'CLAUDIO ROGERIO LINASSI MASTELLA': "NÃO É PPE",
        'RODRIGO ARAUJO ALVES': "NÃO É PPE",
        'FERNANDO ASSUMPCAO BORGES': "NÃO É PPE",
        'JOAO HENRIQUE RITTERSHAUSSEN': "NÃO É PPE",
        'RODRIGO COSTA LIMA E SILVA': "NÃO É PPE",
        'SALVADOR DAHAN': "NÃO É PPE",
         }
for name in column_names:
    for k, v in name:
        if k == name:
            v = "É PPE"

for k, v in names:
    print(f'{k} - {v}')