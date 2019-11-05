import urllib.request
import requests
import re
from bs4 import BeautifulSoup
from village import Village


def setup():
    initCoords = [15, 15]
    range = 10
    speed = 7
    quick = 7
    tp = 5  # nivel de la plaza de torneos
    natare = False
    toret = {'xyX': initCoords[0], 'xyY': initCoords[1], 'range': range, 'maxDiff': 2, 'minSpielerCitys': 1,
             'maxSpielerCitys': 15, 'minSpielerEW': 0, 'maxSpielerEW': 10000, 'antiNoob': 'on',
             'speed': speed, 'quick': quick, 'tp': tp}
    if natare:
        toret.update({'nataren': 'on'})
    return toret


def postRequest(data):
    getterUrl = 'https://www.gettertools.com/ts15.hispano.travian.com/42-Search-inactives'
    response = requests.post(getterUrl, data)
    return BeautifulSoup(response.text, features="html.parser")


def obtainTableRows(html):
    table = html('table')[1]  # Cojo la tabla con los datos (la 0 tiene el formulario de envío)
    tableRows = table('tr')
    print(len(tableRows))
    villages = []

    for row in tableRows[1:2]:
        cells = row('td')
        # Regex para sacar coordenadas
        coords = re.findall('showOpenTipCity\((-?\d*),(-?\d*),this\)', str(cells[1]))
        coordX = coords[0][0]
        coordY = coords[0][1]

        timeCell = str(cells[9])  # la celda 9 tiene la info del viaje
        time = timeCell[4:len(timeCell) - 5]
        villages.append(Village(coordX, coordY, time))
    return villages


data = setup()
html = postRequest(data)
rows = obtainTableRows(html)
print(rows)
print(rows[0].x)
# print(soup)
