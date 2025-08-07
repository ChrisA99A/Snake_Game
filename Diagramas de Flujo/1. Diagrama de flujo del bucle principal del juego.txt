flowchart TD
    A[Inicio] --> B[Inicializar Pygame]
    B --> C[Crear ventana 800x600]
    C --> D[Inicializar serpiente y comida]
    D --> E[Game Loop]
    E --> F[Manejar eventos teclado]
    F --> G[Actualizar posición serpiente]
    G --> H[Colisión con comida?]
    H -->|Sí| I[Crecer serpiente + nueva comida]
    I --> J[Aumentar puntuación]
    H -->|No| K[Colisión bordes/cuerpo?]
    J --> K
    K -->|Sí| L[Mostrar Game Over]
    K -->|No| M[Dibujar elementos]
    M --> N[Controlar FPS 30]
    N --> E
    L --> O[Reiniciar?]
    O -->|Sí| D
    O -->|No| P[Fin]
