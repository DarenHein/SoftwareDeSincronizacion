import os
import sys
import shutil

# --- Configuración de Rutas ---
pcPath = "/Users/luismanjarrezcarbajal/Music/Music/Media.localized/MUSIC"
sdPath = "/Volumes/MEMORIA/MUSICA"          
hostPath = "/Volumes/MEMORIA/MUSICA"        
dbPath = "dataBase/database.txt"
nameDirectoryDB = "DataBase"

listaOmitidos = [
    ".DS_Store",
    ".AppleDouble",
    ".AppleDesktop",
    ".LSOverride",
    "Icon\r",           
    ".Spotlight-V100",
    ".Trashes",
    ".TemporaryItems",
    "Temporary Items",
    ".directory",       
    ".Trash",
    ".Trash-1000",      
    "Compilations",
    "Album Artwork",
    "Previous iTunes Libraries",
    "Automatically Add to Music",
    "Automatically Add to iTunes",
    "Unknown Artist",
    "Unknown Album"
]


# --- Funciones de Utilidad ---

def validatePath(path: str) -> bool:
    return os.path.exists(path)


def cleanList(artistas: list, omitidos: list) -> list:
    return [artista for artista in artistas if artista not in omitidos and not artista.startswith("._")]


def joinPathArtist(artistas: list, path: str) -> list:
    artistasPath = []
    for artista in artistas:
        artistasPath.append(os.path.join(path, artista))
    return artistasPath


def flagStep1(flaglocal: bool, flagSd: bool) -> bool:
    if flaglocal == True and flagSd == True:
        return True
    else:
        return False


# --- Funciones de Negocio y Sincronización ---

def getListArtist(path: str, omitidos: list) -> list:
    lista_artistas = os.listdir(path)
    artistas = cleanList(lista_artistas, omitidos)
    return artistas


def sync_missing_artists(listPath: list, pathOrigen: str, pathDestino: str) -> list:
    artistasQueExisten = [] 
    for element in listPath: 
        if os.path.exists(element):
            artista = os.path.basename(element)
            artistasQueExisten.append(artista)
        else: 
            artista = os.path.basename(element)
            rutaDestino = os.path.join(pathDestino, artista)
            rutaOrigen = os.path.join(pathOrigen, artista)
            if os.path.exists(rutaOrigen):
                try:
                    shutil.move(rutaOrigen, rutaDestino)
                except Exception as e:
                    print(f"Error a ocurrido {e}")
            else:
                print("Artista no se encontro en el origen ")
    return artistasQueExisten 


# --- Ejecución Principal ---

if __name__ == "__main__":
    
    flagSD = validatePath(sdPath)
    flagLocal = validatePath(pcPath)
    flagHost = validatePath(hostPath)
    flagDB = validatePath(dbPath)
    
    if flagDB == False: 
        os.makedirs(nameDirectoryDB, exist_ok=True)
        fd = os.open(dbPath, os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
        os.close(fd)
        
    if flagSD and flagLocal: 
        print("Ambos dispositivos concetados ...")
        print("validando Dispositivo ... ")
        
        artistasPc = getListArtist(pcPath, listaOmitidos)
        artistasSD = getListArtist(sdPath, listaOmitidos)
        artistasPcPath = joinPathArtist(artistasPc, sdPath)
        artistas_pendientes_de_albumes = sync_missing_artists(artistasPcPath, pcPath, sdPath)
        
        if flagHost: 
            print("Dispositivo conectado ... ")
        else: 
            print("Favor de conectar el dispositivo ... ")
            pass 
        
    else: 
        if flagLocal == False:
            print("no existe el directorio donde se ecnutra la musica local ... ") 
            pass 
        elif flagSD == False: 
            print("No se encuntra el directorio de la memoria microSD ...")
            pass