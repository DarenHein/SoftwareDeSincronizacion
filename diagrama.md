graph TD
    A[Inicio del Script] --> B{Validar Rutas: PC, SD, DB}
    B -->|DB no existe| C[Crear directorio y archivo database.txt]
    B -->|DB ya existe| D{¿Existen PC y SD?}
    C --> D
    
    D -->|No| E[Imprimir Error de Directorio / Fin]
    D -->|Sí| F[Obtener y limpiar listas de artistas PC y SD]
    
    F --> G[Construir rutas completas de la SD: artistasPcPath]
    G --> H[Ejecutar sync_missing_artists]
    
    subgraph Sincronización [Función: sync_missing_artists]
        H --> I{¿El artista existe en la SD?}
        I -->|Sí| J[Extraer nombre y agregar a artistasQueExisten]
        I -->|No| K{¿El artista existe en la PC?}
        K -->|Sí| L[shutil.move: PC -> SD]
        K -->|No| M[Imprimir Advertencia de Origen]
    end
    
    J --> N[Retornar lista: artistas_pendientes_de_albumes]
    L --> N
    M --> N
    
    N --> O{¿Host / DAP Conectado?}
    O -->|Sí| P[Listo para siguiente paso: Validar Álbumes]
    O -->|No| Q[Aviso: Conectar Dispositivo]