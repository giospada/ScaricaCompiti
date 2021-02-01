from src.CaricaCompiti import CaricaCompiti
from src.TrasformObject import TrasformObject
from src.CompitiObject import CompitiObject
from src.TUI import TUI

import json
import logging
import argparse


"""

    ┏━━━┓━━━━━━━━━━┏┓━━━━━━
    ┃┏━┓┃━━━━━━━━━━┛┗┓━━━━━
    ┃┗━┛┃━━┓━━┓┓━━┓┓┏┛━┓━━┓
    ┃┏┓┏┛┏┓┃┏┓┃┫━━┫┃┃━┏┛┏┓┃
    ┃┃┃┗┓┃━┫┗┛┃┃━━┃┃┗┓┃━┗┛┃
    ┗┛┗━┛━━┛━┓┃┛━━┛┗━┛┛━━━┛
    ━━━━━━━━━┛┃━━━━━━━━━━━━
    ━━━━━━━━━━┛━━━━━━━━━━━━

"""


settings="settings.json"
history="history.json"

paster=argparse.ArgumentParser()
paster.add_argument("-mf","--mfilter",action="store",help="filtra per materia")
paster.add_argument("-cf","--cfilter",action="store",help="filtra per il contenuto")
paster.add_argument("-s","--sethistory",action="store",help="the file that store the history")
paster.add_argument("-u","--usersettings",action="store",help="the file that store the user settings(json with n.scuola,utente and password)")
#paster.add_argument("-t","--taskwarrior",action="store_true",help="add to task worrior")
paster.add_argument("-n","--new",action="store_true",help="write only the new compiti")
paster.add_argument("-c","--current",action="store_true",help="filter by date ")
 
args=paster.parse_args();
 
 
if args.sethistory!=None:
    history=args.sethistory
 
if args.usersettings!=None:
    settings=args.usersettings

onConsole=True#not args.taskwarrior;
 
objCompiti=CompitiObject(settings,history)
cCompiti=CaricaCompiti(objCompiti)


 
tui=TUI()
 
if onConsole:
    tui.initUpdate()
 
nuovi=cCompiti.downloadNewCompiti()
objCompiti.compiti+=(nuovi)
objCompiti.saveHistory()

if onConsole:
    tui.finishUpdate()
 
trf=TrasformObject(objCompiti.compiti if not args.new else nuovi)
trf.dataMassima()
trf.ordina()
 
if args.current:
    trf.onlyNext()
 
if args.cfilter!=None:
    trf.filtra("desCompiti",args.cfilter)
 
if args.mfilter!=None:
    trf.filtra("desMateria",args.mfilter)

if onConsole:
    tui.printCompiti(trf.compiti)
else:
    print(trf.toTaskWorrior())
 