# Engeto-pa-3-project

Third project to ENGETO Python academy.

## Project description

This project is used to extract results from the 2017 Czech parliamentary elections, link [here](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Libraries
Libraries used in the code are stored in a file `requirements.txt`. It's recommended to use a new virtual environment and install the libraries using pip as follows:

```
$ pip3 --version                   # check pip version
$ pip3 install -r requirements.txt # install libraries
```

## Project execution

To execute the file `election_scraper.py` in terminal, two arguments are required:
```
python3 election_scraper.py <city-name> <output-file> 
```

where `<city-name>` can be one of the following:

```
Praha, Benešov, Beroun, Kladno, Kolín, Kutná Hora, Mělník, Mladá Boleslav, 
Nymburk, Praha-východ, Praha-západ, Příbram, Rakovník, Zahraničí, 
České Budějovice, Český Krumlov, Jindřichův Hradec, Písek, Prachatice, 
Strakonice, Tábor, Domažlice, Klatovy, Plzeň-město, Plzeň-jih, Plzeň-sever, 
Rokycany, Tachov, Cheb, Karlovy Vary, Sokolov, Děčín, Chomutov, Litoměřice, 
Louny, Most, Teplice, Ústí nad Labem, Česká Lípa, Jablonec nad Nisou, Liberec, 
Semily, Hradec Králové, Jičín, Náchod, Rychnov nad Kněžnou, Trutnov, Chrudim, 
Pardubice, Svitavy, Ústí nad Orlicí, Havlíčkův Brod, Jihlava, Pelhřimov, Třebíč, 
Žďár nad Sázavou, Blansko, Brno-město, Brno-venkov, Břeclav, Hodonín, Vyškov, 
Znojmo, Jeseník, Olomouc, Prostějov, Přerov, Šumperk, Kroměříž, Uherské Hradiště, 
Vsetín, Zlín, Bruntál, Frýdek-Místek, Karviná, Nový Jičín, Opava, Ostrava-město
```

Consequently, the results will be saved into a `.csv` file.

## Project execution example

Results of elections in Prague:
1. argument ```Praha```
2. argument ```results_praha```

Code execution:
```
python3 election_scraper.py Praha results_praha
```

Data extraction process:

```
Extracting data from: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100
Saving data to file: results_praha.csv
Finishing
```

Partial output:

```
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Volte Pr.Blok www.cibulka.net,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Společ.proti výst.v Prok.údolí,Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,OBČANÉ 2011-SPRAVEDL. PRO LIDI,Unie H.A.V.E.L.,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,Česká strana národně sociální,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
500054,Praha 1,21 556,14 167,14 036,2 770,9,13,657,12,1,774,392,514,41,6,241,14,44,2 332,5,0,12,2 783,1 654,1,7,954,3,133,11,2,617,34
500224,Praha 10,79 964,52 277,51 895,8 137,40,34,3 175,50,17,2 334,2 485,1 212,230,15,1 050,35,67,9 355,9,8,30,6 497,10 856,37,53,2 398,12,477,69,53,2 998,162
547034,Praha 11,58 353,39 306,39 116,5 100,48,18,2 513,30,17,1 548,2 310,757,192,13,846,29,57,6 763,11,5,23,3 598,10 213,31,35,1 622,14,373,86,53,2 674,137
```

