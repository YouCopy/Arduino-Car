from pyfirmata import Arduino
import pygame

pygame.init()
sur_obj=pygame.display.set_mode((400,300))
pygame.display.set_caption("Keyboard_Input")

board = Arduino("COM4")

while(True):
    pygame.event.get()

    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_UP]:
        board.digital[9].write(1)
        board.digital[11].write(1)
    if key_input[pygame.K_DOWN]:
        board.digital[10].write(1)
        board.digital[12].write(1)
    if key_input[pygame.K_LEFT]:
        board.digital[10].write(1)
        board.digital[11].write(1)
    if key_input[pygame.K_RIGHT]:
        board.digital[9].write(1)
        board.digital[12].write(1)
    board.digital[9].write(0)
    board.digital[10].write(0)
    board.digital[11].write(0)
    board.digital[12].write(0)
