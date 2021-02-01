import datetime as dt
import re
class TrasformObject:

    def __init__(self,compiti):
        self.today=dt.datetime.now().date()
        self.compiti=compiti

    def dataMassima(self):
        for obj in self.compiti:
            datCompiti=dt.date.fromisoformat(obj["datCompiti"])
            datGiorno=dt.date.fromisoformat(obj["datGiorno"])
            if(datCompiti<datGiorno):
                obj["datCompiti"]=datGiorno.isoformat()
                obj["datGiorno"]=datCompiti.isoformat()
    
    def ordina(self):
        self.compiti.sort(
            key=(lambda x:dt.date.fromisoformat(x["datCompiti"])),
            reverse=False)

    def filtra(self,per,dacercare):
        self.compiti=list(filter(lambda x:re.search(x[per],dacercare) ,self.compiti))

    def onlyNext(self):
        self.compiti=list(filter(lambda x: (dt.date.fromisoformat(x["datCompiti"])-self.today).days>-2,self.compiti))

    def toTaskWorrior(self):
        return
        #TODO:implementare il file per esportarlo in taskworrior