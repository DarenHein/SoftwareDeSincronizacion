

ES_MODO_PRUEBA =  True

if ES_MODO_PRUEBA:
    # Rutas y valores cuando estás probando localmente
    pcPath = "./test_environment/pc_mock"
    sdPath = "./test_environment/sd_mock"
    hostPath = "./test_environment/host_mock"
    dbPath = "dataBase/database_test.txt"
    nameDirectoryDB = "DataBaseTest"
else:
    # Tus rutas reales de producción
    pcPath = "/Users/luismanjarrezcarbajal/Music/Music/Media.localized/MUSIC"
    sdPath = "/Volumes/MEMORIASD/MUSICA"
    hostPath = "/Volumes/MEMORIA/MUSICA"
    dbPath = "dataBase/database.txt"
    nameDirectoryDB = "DataBase"