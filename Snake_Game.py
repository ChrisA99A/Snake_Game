import pygame
import sys
import random
import time

# Inicializar Pygame
pygame.init()

# 1. Operadores relacionales y lógicos
# Configuración del juego
ANCHO, ALTO = 800, 600
TAMANO_CELDA = 30
FILAS, COLUMNAS = ALTO // TAMANO_CELDA, ANCHO // TAMANO_CELDA
FPS = 10

# Colores (RGB)
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
GRIS = (40, 40, 40)

# Crear ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Serpiente")
reloj = pygame.time.Clock()

# 2. Condicional IF y funciones clave
def inicializar_serpiente():
    """Inicializa la serpiente en posición central con 3 segmentos"""
    cabeza = [COLUMNAS // 2, FILAS // 2]
    return [cabeza, [cabeza[0] - 1, cabeza[1]], [cabeza[0] - 2, cabeza[1]]]

def generar_comida(serpiente):
    """Genera comida en posición aleatoria no ocupada por la serpiente"""
    while True:
        # 3. Operadores lógicos en condición compuesta
        comida = [
            random.randint(0, COLUMNAS - 1),
            random.randint(0, FILAS - 1)
        ]
        
        # 4. Bucle FOR y operadores relacionales
        if all(comida != segmento for segmento in serpiente):
            return comida

def dibujar_elementos(serpiente, comida, puntuacion):
    """Dibuja todos los elementos del juego"""
    ventana.fill(NEGRO)
    
    # Dibujar cuadrícula
    for x in range(0, ANCHO, TAMANO_CELDA):
        pygame.draw.line(ventana, GRIS, (x, 0), (x, ALTO))
    for y in range(0, ALTO, TAMANO_CELDA):
        pygame.draw.line(ventana, GRIS, (0, y), (ANCHO, y))
    
    # Dibujar serpiente
    for i, segmento in enumerate(serpiente):
        color = VERDE if i == 0 else AZUL  # Cabeza verde, cuerpo azul
        pygame.draw.rect(
            ventana, 
            color, 
            pygame.Rect(
                segmento[0] * TAMANO_CELDA,
                segmento[1] * TAMANO_CELDA,
                TAMANO_CELDA,
                TAMANO_CELDA
            )
        )
    
    # Dibujar comida
    pygame.draw.rect(
        ventana, 
        ROJO, 
        pygame.Rect(
            comida[0] * TAMANO_CELDA,
            comida[1] * TAMANO_CELDA,
            TAMANO_CELDA,
            TAMANO_CELDA
        )
    )
    
    # Mostrar puntuación
    fuente = pygame.font.SysFont(None, 36)
    texto = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    ventana.blit(texto, (10, 10))

def mostrar_game_over(puntuacion):
    """Muestra mensaje de Game Over y opciones"""
    ventana.fill(NEGRO)
    fuente_titulo = pygame.font.SysFont(None, 72)
    fuente_texto = pygame.font.SysFont(None, 36)
    
    titulo = fuente_titulo.render("GAME OVER", True, ROJO)
    texto_puntos = fuente_texto.render(f"Puntuación final: {puntuacion}", True, BLANCO)
    texto_reinicio = fuente_texto.render("Presiona R para reiniciar", True, VERDE)
    texto_salir = fuente_texto.render("Presiona ESC para salir", True, BLANCO)
    
    ventana.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, ALTO // 3))
    ventana.blit(texto_puntos, (ANCHO // 2 - texto_puntos.get_width() // 2, ALTO // 2))
    ventana.blit(texto_reinicio, (ANCHO // 2 - texto_reinicio.get_width() // 2, ALTO // 2 + 50))
    ventana.blit(texto_salir, (ANCHO // 2 - texto_salir.get_width() // 2, ALTO // 2 + 100))
    
    pygame.display.update()

def main():
    # Inicializar estado del juego
    serpiente = inicializar_serpiente()
    direccion = "DERECHA"
    nueva_direccion = direccion
    comida = generar_comida(serpiente)
    puntuacion = 0
    game_over = False
    
    # 5. Bucle WHILE principal
    while True:
        for evento in pygame.event.get():
            # 6. Condicionales anidados
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # 7. Operadores lógicos en condiciones
            if evento.type == pygame.KEYDOWN and not game_over:
                if (evento.key == pygame.K_UP and direccion != "ABAJO"):
                    nueva_direccion = "ARRIBA"
                elif (evento.key == pygame.K_DOWN and direccion != "ARRIBA"):
                    nueva_direccion = "ABAJO"
                elif (evento.key == pygame.K_LEFT and direccion != "DERECHA"):
                    nueva_direccion = "IZQUIERDA"
                elif (evento.key == pygame.K_RIGHT and direccion != "IZQUIERDA"):
                    nueva_direccion = "DERECHA"
            
            # Manejar reinicio y salida
            if evento.type == pygame.KEYDOWN and game_over:
                if evento.key == pygame.K_r:  # Reiniciar
                    return main()
                elif evento.key == pygame.K_ESCAPE:  # Salir
                    pygame.quit()
                    sys.exit()
        
        if not game_over:
            # Actualizar dirección
            direccion = nueva_direccion
            
            # Calcular nueva posición de la cabeza
            cabeza = serpiente[0].copy()
            if direccion == "ARRIBA":
                cabeza[1] -= 1
            elif direccion == "ABAJO":
                cabeza[1] += 1
            elif direccion == "IZQUIERDA":
                cabeza[0] -= 1
            elif direccion == "DERECHA":
                cabeza[0] += 1
            
            # 8. Detección de colisiones con bordes
            if (cabeza[0] < 0 or cabeza[0] >= COLUMNAS or 
                cabeza[1] < 0 or cabeza[1] >= FILAS):
                game_over = True
            
            # Detección de colisiones con el cuerpo
            # 9. Bucle FOR con alterador CONTINUE
            for segmento in serpiente:
                # Evitar comparar la cabeza consigo misma
                if segmento == cabeza:
                    continue
                if cabeza == segmento:
                    game_over = True
                    break
            
            # Mover serpiente
            serpiente.insert(0, cabeza)
            
            # Verificar si comió
            if cabeza == comida:
                comida = generar_comida(serpiente)
                puntuacion += 1
            else:
                serpiente.pop()  # Eliminar cola si no comió
        
        # Dibujar elementos
        if game_over:
            mostrar_game_over(puntuacion)
        else:
            dibujar_elementos(serpiente, comida, puntuacion)
        
        pygame.display.update()
        reloj.tick(FPS)

if __name__ == "__main__":
    main()