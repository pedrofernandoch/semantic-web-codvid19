import pygame
import os
from iaButton import IaButton


#
#
#
# LOAD IMAGE #
def load_image(image_name, p):
    image_path = os.path.join("assets", image_name)
    try:
        image = p.image.load(image_path)
        return image, image.get_rect()
    except p.error:
        print("Problema ao carregar imagem")


#
#
#
# CONFIG SCREEN #
def config_screen():
    # init
    pygame.init()
    # create the screen
    width, height = 600, 600
    scr = pygame.display.set_mode((width, height))
    # title
    pygame.display.set_caption("COVID DADOS")
    # screen color
    scr.fill("gray")
    image, rect = load_image("logo.png", pygame)
    rect.center = width // 2, (height // 2) - 100
    scr.blit(image, rect)

    buttons = [IaButton(scr, 'Grafico geral', 0), IaButton(scr, 'Grafico por area', 1)]

    pygame.display.flip()

    return pygame, buttons


#
#
#
# GAME LOOP #
def game_loop():
    py_game, buttons = config_screen()

    running = True
    # game loop
    while running:
        for event in py_game.event.get():
            if event.type == py_game.QUIT:
                running = False

            # buttons event listeners
            buttons[0].button.listen(event)
            buttons[1].button.listen(event)


#
#
#
# MAIN FUNCTION #

if __name__ == "__main__":
    game_loop()
