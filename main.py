import os 
import sys
import shutil 

# --- Rutas de Configuración ---
pcPath = "/Users/luismanjarrezcarbajal/Music/Music/Media.localized/MUSIC"
sdPath = "/Volumes/MEMORIA/MUSICA"          # Disco duro externo / Fuente principal 
hostPath = "/Volumes/MEMORIA/MUSICA"        # Dispositivo musical (DAP) 
dbPath = "dataBase/database.txt"
nameDirectoryDB = "DataBase"

listaOmitidos = [
    # --- macOS System & Finder ---
    ".DS_Store",
    ".AppleDouble",
    ".AppleDesktop",
    ".LSOverride",
    "Icon\r",           # Archivo invisible de iconos personalizados de Mac
    ".Spotlight-V100",
    ".Trashes",
    ".TemporaryItems",
    "Temporary Items",
    
    # --- Linux System & File Managers ---
    ".directory",       # Creado por Dolphin/KDE
    ".Trash",
    ".Trash-1000",      # Papelera genérica de Linux
    
    # --- Apple Music / iTunes (Ripping y Gestión) ---
    "Compilations",
    "Album Artwork",
    "Previous iTunes Libraries",
    "Automatically Add to Music",
    "Automatically Add to iTunes",
    "Unknown Artist",
    "Unknown Album"
]

# utilidades 
def cleanList(artistas: list, omitidos: list) -> list:
    return [artista for artista in artistas if artista not in omitidos and not artista.startswith("._")]
def joinPathArtist(artistas : list , path : str) -> list : 
    artistasPath = []
    for  artista in artistas :
        artistasPath.append(path,artista)
    return artistasPath 

def sync_missing_artists(listPath : list , pathOrigen: str , pathDestino : str) -> list :
    artistasQueExisten = [] 
    for element in listPath : 
        if os.path.exists(element) :
            artista = os.path.basename(element)
            artistasQueExisten.append(artista)
        else : 
            artista = os.path.basename(element)
            rutaDestino = os.path.join(pathDestino,artista)
            rutaOrigen = os.path.join(pathOrigen,artista)
            if os.path.exists(rutaOrigen):
                try : 
                    shutil.move(rutaOrigen,rutaDestino)
                except Exception as e : 
                    print(f"Error a ocurrido {e}")
            else : 
                print("Artista no se encontro en el origen ")
    return artistasQueExisten 
        
        

def validatePath(path):
    if os.path.exists(path) : 
        return True 
    else : 
        return False
              
def flagStep1(flaglocal : bool , flagSd : bool) -> bool : 
    if flaglocal == True and flagSd == True : 
        return True 
    else : 
        return False  

# sincronizacion de PC con SD 
# primero obtencion de artistas 
def getListArtist(path : str , omitidos : list) -> None : 
    lista_artistas = os.listdir(path)
    artistas = cleanList(lista_artistas, omitidos)
    return artistas


if __name__ == "__main__" :
    
    flagSD = validatePath(sdPath)
    flagLocal = validatePath(pcPath)
    flagHost = validatePath(hostPath)
    flagDB = validatePath(dbPath)
    
    if flagDB == False : 
        os.makedirs(nameDirectoryDB,exist_ok=True)
        fd = os.open(dbPath, os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
        os.close(fd)
        
    if flagSD and flagLocal : 
        print("Ambos dispositivos concetados ...")
        # podemos continuar con la validacion del host 
        print("validando Dispositivo ... ")
        # en este punto tenemos que sincronizar los datos dela pc en la memoriaSD 
        #
        # 
        #  
        artistasPc = getListArtist(pcPath,listaOmitidos)
        artistasSD = getListArtist(sdPath,listaOmitidos)
        artistasPcPath = joinPathArtist(artistasPc,sdPath) #paso importante por que con esto veremos si existen en el host 
        artistas_pendientes_de_albumes = sync_missing_artists(artistasPcPath,pcPath,sdPath)
        # ahora el siguiente paso es de los artiatas que existen en ambos dispositivos (local , sd) veremos si comparten los albumes relacion uno a muchos 
        
        
        if flagHost : 
            print("Dispositivo conectado ... ")
        else : 
            print("Favor de conectar el dispositivo ... ")
            pass 
        
    else : 
        if flagLocal == False :
            print("no existe el directorio donde se ecnutra la musica local ... ") 
            pass 
        elif flagSD == False : 
            print("No se encuntra el directorio de la memoria microSD ...")
            pass 
        