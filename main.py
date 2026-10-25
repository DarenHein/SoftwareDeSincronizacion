import os
import sys
import shutil

# aun falta el tema de la base de datos por por lo que veo no hace falta solo para tener un control en github pero de ahi en fuera se pensara

# ! ULTIMAS ADECUACIONES YA FUNCIONA ESTA VIVO EL SOFTWARE PERO LO QUE NOS FALTA EN ACTUALIZACIONES 
# QUE MOVEMOS 
# los nombres de los albumes como se mueven etc en pocas palabras mas intuitivo 
# en pasos osea de pc a sd y despues de sd a dap asi

pcPath = "/Users/luismanjarrezcarbajal/Music/Music/Media.localized/MUSIC"
sdPath = "/Volumes/MEMORIASD/MUSICA"          
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

def getCleanList(path: str, omitidos: list) -> list:
    lista_artistas = os.listdir(path)
    artistas = cleanList(lista_artistas, omitidos)
    return artistas

def sync_missing_artists(listPath: list, pathOrigen: str, pathDestino: str, modo: str = "move") -> list:
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
                    if modo == "move":
                        shutil.move(rutaOrigen, rutaDestino)
                        print(f"📦 [Artista Movido] {artista}")
                    elif modo == "copy":
                        shutil.copytree(rutaOrigen, rutaDestino)
                        print(f"📋 [Artista Copiado] {artista}")
                    
                    artistasQueExisten.append(artista) 
                except Exception as e:
                    print(f"❌ Error ha ocurrido con el artista {artista}: {e}")
            else:
                print(f"⚠️ Artista '{artista}' no se encontró en el origen.")
    return artistasQueExisten

def transferir_album(artista_album_pc : str , artista_album_sd : str , album : str , modo="move"):
    if not os.path.exists(artista_album_sd):
        try:
            if modo == "move":
                shutil.move(artista_album_pc, artista_album_sd)
                print(f"📦 [Movido] '{album}' -> Espacio liberado en PC.")
            elif modo == "copy":
                shutil.copytree(artista_album_pc, artista_album_sd)
                print(f"📋 [Copiado] '{album}' -> Música intacta en PC y SD.")
        except Exception as e:
            print(f"❌ Error con el álbum '{album}': {e}")
            
def sincronizar_albumes_artistas(artistas_pendientes, dir_origen, dir_destino, lista_omitidos, modo="move"):
    for artista in artistas_pendientes:
        artista_path_origen = os.path.join(dir_origen, artista)
        artista_path_destino = os.path.join(dir_destino, artista)
        
        if not os.path.exists(artista_path_origen):
            continue
        
        albumes_origen = getCleanList(artista_path_origen, lista_omitidos) 
        
        for album in albumes_origen:
            album_origen = os.path.join(artista_path_origen, album)
            album_destino = os.path.join(artista_path_destino, album)
            
            transferir_album(album_origen, album_destino, album, modo)
            
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
        
        artistasPc = getCleanList(pcPath, listaOmitidos)
        artistasSD = getCleanList(sdPath, listaOmitidos)
        artistasPcPath = joinPathArtist(artistasPc, sdPath)
        artistasPc = getCleanList(pcPath, listaOmitidos)
        artistasSD = getCleanList(sdPath, listaOmitidos)
        artistasPcPath = joinPathArtist(artistasPc, sdPath)
        artistas_pendientes_pc_sd = sync_missing_artists(artistasPcPath, pcPath, sdPath , "move") 
        
        sincronizar_albumes_artistas(
            artistas_pendientes=artistas_pendientes_pc_sd,
            dir_origen=pcPath,
            dir_destino=sdPath,
            lista_omitidos=listaOmitidos,
            modo="move"
        )
                
        if flagHost: 
            print("Dispositivo conectado ... ")
            artistasDap = getCleanList(hostPath,listaOmitidos)
            artistasSD = getCleanList(sdPath,listaOmitidos)
            artistasDapPath = joinPathArtist(artistasSD,hostPath) 
            artistas_pendientes_sd_dap =  sync_missing_artists(artistasDapPath,sdPath,hostPath , "copy") 
            sincronizar_albumes_artistas(
                artistas_pendientes=artistas_pendientes_sd_dap,
                dir_origen=sdPath,
                dir_destino=hostPath,
                lista_omitidos=listaOmitidos,
                modo="copy"
            )
            
        else: 
            print("Favor de conectar el dispositivo ... ")
            pass 
        
    else: 
        if flagLocal == False:
            print("no existe el directorio donde se ecnutra la musica local ... ") 
            pass 
        elif flagSD == False: 
            print("No se encuntra el directorio de la memoria SD ...")
            pass