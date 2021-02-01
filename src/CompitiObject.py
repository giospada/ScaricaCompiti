import os
import json

class CompitiObject:
    """
    descrizione obj compiti
    "datGiorno", "desMateria", "done", "desCompiti, "datCompiti", "id"
    """
    daTenere=["datGiorno" ,"desMateria",  "desCompiti" ,"datCompiti", "id"] 
    def __init__(self,fs,fh):
        self.fs=fs
        self.fh=fh
        content=self._loadJSON(fs)
        self.username=content["utente"]
        self.codscuola=content["scuola"]
        self.password=content["password"]
        self.compiti=self._loadJSON(fh)

    def _loadJSON(self,filename):
        f=open(filename,"r")
        content=(f.read())
        f.close()
        if(content==""):
            return []
        else:
            return json.loads(content)

    def saveHistory(self):
        self._saveJSON(self.fh,self.compiti)    

    def _saveJSON(self,filename,obj):
        f=open(filename,"w")
        content=f.write(json.dumps(obj))
        f.close()

