
# aqui leeremos la base de datos y de ahi crearemos una lista y esa lista la mandaremos a github para posteriores compras 

import os
from config import dbPath , nameDirectoryDB ,  sdPath
 
def validateDb(dvPath : str) -> bool : 
    if os.path.exists(dbPath) : 
        return True 
    else : 
        return False 
    
def getArtistList(sdPath : str) -> list : 
    artistSdList = os.listdir(sdPath)
    return artistSdList
# despues limpiar de archivos basura 


def writeDB(nameDirectoryDB : str , artistas : list) -> bool :
    try : 
        with open (nameDirectoryDB , "a" , encoding="utf-8") as db : 
                
            for artista in artistas : 
                db.write(f"{artista}\n")
        return True
    except Exception as e : 
        print(f"error al escribir en {nameDirectoryDB}")
        return False      


            