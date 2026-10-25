graph TD
    A[Inicio del Script] --> B[Validar Rutas: sdPath, pcPath, hostPath, dbPath]
    B --> C{¿Existe Base de Datos?}
    
    C -->|No| D[Crear Carpeta Base y Archivo DB] --> E
    C -->|Sí| E
    
    E{¿Existen SD y PC Local?} -->|No| F[Imprimir Error: Falta Local o SD] --> Z[Fin]
    E -->|Sí| G[Obtener Listas Limpias de Artistas: PC y SD]
    
    G --> H[Sincronizar Artistas Faltantes PC -> SD]
    H --> I[Sincronizar Álbumes Pendientes PC -> SD: move]
    I --> J{¿Existe Dispositivo DAP / Host?}
    
    J -->|No| K[Imprimir: Conectar Dispositivo] --> Z
    J -->|Sí| L[Obtener Listas Limpias: SD y DAP]
    
    L --> M[Sincronizar Artistas Faltantes SD -> DAP]
    M --> N[Sincronizar Álbumes Pendientes SD -> DAP: copy]
    N --> Z
    