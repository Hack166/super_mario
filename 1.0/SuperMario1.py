import pygame
pygame.init()

width, height = 640, 480
pygame.display.set_mode((width, height))
screen = pygame.display.get_surface()
pygame.display.set_caption("SuperMarioTest1")


# Load images
mario_image = pygame.image.load("mario.png")
mario_image = pygame.transform.scale(mario_image, (40, 40))
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (width, height))

# Set up variables
mario = pygame.sprite.Sprite()
mario.image = mario_image
mario.rect = mario.image.get_rect()

player_group = pygame.sprite.Group()
player_group.add(mario)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                mario.rect.y += 10
            if keys[pygame.K_UP]:
                mario.rect.y -= 10
            if keys[pygame.K_LEFT]:
                mario.rect.x -= 10
            if keys[pygame.K_RIGHT]:
                mario.rect.x += 10
    screen.blit(background,(0, 0))
    player_group.draw(screen)
    pygame.display.update()