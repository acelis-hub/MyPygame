import pygame # importa pygame
import sys # importa sys para identificar ventana
pygame.init() # inicializa la libreria

size = (800, 500) # tamaño de ventana
screen = pygame.display.set_mode(size) # crea la ventana

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()