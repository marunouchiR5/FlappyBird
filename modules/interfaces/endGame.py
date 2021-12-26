# end game UI
import sys
import pygame


# show end game UI
def endGame(screen, sounds, show_score, score, number_images, bird, pipe_sprites, background_image, other_images,
            base_pos, cfg):
    sounds['die'].play()
    print("----- Game Over -----")
    clock = pygame.time.Clock()
    game_over_pos = [(cfg.SCREENWIDTH - other_images['game-over'].get_width()) / 2, cfg.SCREENHEIGHT * 0.36]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    return
        boundary_values = [0, base_pos[-1]]
        bird.update(boundary_values, float(clock.tick(cfg.FPS)) / 1000.)
        screen.blit(background_image, (0, 0))
        pipe_sprites.draw(screen)
        screen.blit(other_images['game-over'], game_over_pos)
        screen.blit(other_images['base'], base_pos)
        show_score(screen, score, number_images)
        bird.draw(screen)
        pygame.display.update()
        clock.tick(cfg.FPS)
