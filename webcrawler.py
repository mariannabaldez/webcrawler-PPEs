import datetime
from datetime import date
from distutils.util import execute
import requests
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
names = ['ROBERTO FURIAN ARDENGHY',
         'NICOLAS SIMONE',
         'JOAQUIM SILV E LUNA',
         'CLAUDIO ROGERIO LINASSI MASTELLA',
         'RODRIGO ARAUJO ALVES',
         'FERNANDO ASSUMPCAO BORGES',
         'JOAO HENRIQUE RITTERSHAUSSEN',
         'RODRIGO COSTA LIMA E SILVA',
         'SALVADOR DAHAN']

pep = {}
for name_in_column in column_names:
    for name in names:
        if name == name_in_column:
            name.append(pep)










