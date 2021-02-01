import argoscuolanext
import hashlib
import json
import sys

class CaricaCompiti:
    """
    Classe che scarica i compiti e legge le impostazioni 

    """
    def __init__(self,compitiObject):
        self.compitiObject=compitiObject
        # Create set     
        self.added=set()
        for obj in self.compitiObject.compiti:
            self.added.add(obj["id"])
        
    
    def downloadNewCompiti(self):
        nuovicompiti=[]
        session = argoscuolanext.Session(self.compitiObject.codscuola,self.compitiObject.username,self.compitiObject.password)
        obj=session.compiti()["dati"]
        for i in obj:
            tmphash=self.createHASH(i)
            if not (tmphash in self.added):
                i["id"]=tmphash
                createobj={}
                for key in self.compitiObject.daTenere:
                    createobj[key]=i[key]
                nuovicompiti.append(createobj) 
        return nuovicompiti


        
    def createHASH(self,obj):
        prefix=obj["datGiorno"]+obj["datCompiti"]+"-"
        has=str(hashlib.md5(bytes(prefix+obj["desMateria"]+obj["desCompiti"],'utf-8')).hexdigest());  
        return prefix+has


        





    