import csv
import webbrowser

# Path de instalacion de chrome
CHROME_PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# Numero maximo de enlaces lanzados en cada ejecucion del programa
NUM_LINKS = 8
FICHEROS = ["ListaVacas - Hoja 1.csv", "S1.txt"]
# FICHEROS = ["ListaVacas - Hoja 2.csv", "S2.txt"]


class Coordenada():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __eq__(self, other):
        return self.x == other.x

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return "[" + self.x + "," + self.y + "]"


def readCsv(fileName):
    firstRow = True
    toret = set()
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if firstRow:
                firstRow = False
            else:
                x = row[0].split(" ")[1]
                y = row[0].split(" ")[3]
                toret.add(Coordenada(x, y))
    return toret


def readTxt(fileName):
    toret = set()
    f = open(FICHEROS[1], "r")
    for linea in f:
        x = linea[1:].split(",")[0]
        y = linea.split(",")[1].split("]")[0]
        toret.add(Coordenada(x, y))
    return toret


def lanzarEnlaces(coordenadas):
    cont = 0
    for i in coordenadas:
        url = "https://ts20.hispano.travian.com/karte.php?x=" + i.x + "&y=" + i.y
        webbrowser.get(CHROME_PATH).open(url)
        print(url)
        antiguasCoordenadas.add(i)
        cont += 1
        if cont >= NUM_LINKS:
            break


# Leo coordenadas de los 2 ficheros
nuevasCoord = readCsv(FICHEROS[0])
antiguasCoordenadas = readTxt(FICHEROS[1])

# genero coordenadas para meter en la lista de vacas
resta = nuevasCoord.difference(antiguasCoordenadas)
lanzarEnlaces(resta)

# Añado todas las coordendas al registro
f = open(FICHEROS[1], "w")
for i in antiguasCoordenadas:
    f.write(str(i) + "\n")
