#Read csv files and display all user names;
import csv
fp = open('emp.csv','r')
csv_obj =csv.reader(fp)
user_list=list(csv_obj)


for user in user_list:
    print(user[1])
    """ i=0
    while i<len(user):
        print(user[1])
        i=i+1 """
    '''
    Vivianne
Lind
Ame
Traver
Morena
Phaidra
Neddy
Cosimo
Truda
Juliet
Benoite
Alair
Carlee
Michel
Billie
Giacomo
Carlynne
Caspar
Ekaterina
Willie
Nonie
Mason
Mace
Shirlene
Brooke
Gilberto
Otho
Kathlin
Nissie
Carlita
Burlie
Lynde
Garrard
Andy
Georges
Allin
Wyn
Ronald
Gunilla
Chev
Berti
Camella
Albie
Loretta
Cazzie
Brinna
Raye
Georgiana
Susannah
Terrijo
Con
Althea
Marwin
Lyon
Bram
Micheil
Bernhard
Owen
Shadow
Shannan
Toby
Darleen
Tamma
Estell
Basil
Lynnet
Kerry
Brita
Zaccaria
Etienne
Osbourne
Alayne
Ker
Sterne
Kendrick
Mose
Jedd
Constancia
Riva
Thor
Candice
Burl
Ted
Chickie
Ceciley
Codi
Kelila
Lisbeth
Ave
Alec
Paul
Carlee
Jay
Doy
Puff
Jerrine
Randell
Cesya
Seana
Kennedy
    '''


fp.close()