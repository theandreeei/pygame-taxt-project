import pygame as pg
import random


width, height = 700, 450
FPS = 60
BLACK = (0, 0, 0)
IMAGES_DICT = {
    'bg': pg.image.load('img/Background.png'),
    'player': {
        'rear': pg.image.load('img/cab_rear.png'),
        'left': pg.image.load('img/cab_left.png'),
        'front': pg.image.load('img/cab_front.png'),
        'right': pg.image.load('img/cab_right.png'),
    },
    'hole': pg.image.load('img/hole.png'),
    'hotel': pg.transform.scale(pg.image.load('img/hotel.png'), (62, 62)),
    'passenger': pg.image.load('img/passenger.png'),
    'parking': pg.transform.scale(pg.image.load('img/parking.png'), (80, 45)),
}
x_direction = 0
y_direction = 0
player_speed = 2

# player
player_view = 'rear'
player_rect = IMAGES_DICT['player'][player_view].get_rect()
player_rect.x, player_rect.y = 300, 300

# hotel
hotel_img = IMAGES_DICT['hotel']
hotel_rect = hotel_img.get_rect()
hotel_positions = [
    (60, 30),
    (555, 30), 
    (64, 336 - 62),  
    (555, 250), 
] 
hotel_rect.x, hotel_rect.y = random.choice(hotel_positions)

# parking
parking_img = IMAGES_DICT['parking']
parking_rect = parking_img.get_rect()
parking_rect.x, parking_rect.y = hotel_rect.x, hotel_rect.y + 80

# passenger
passenger_img = IMAGES_DICT['passenger']
passenger_rect = passenger_img.get_rect()
# (passenger_rect.x, passenger_rect.y) = (hotel_rect.x, hotel_rect.y + hotel_rect.height)
(passenger_rect.x, passenger_rect.y) = random.choice(hotel_positions)
passenger_rect.y += hotel_rect.height


def is_crash():
    for x in range(player_rect.x, player_rect.topright[0], 1):
        for y in range(player_rect.y, player_rect.bottomleft[1], 1):
            try: 
                if screen.get_at((x, y)) == (209, 204, 173):
                    return True
            except IndexError:
                pass
    if hotel_rect.colliderect(player_rect):
        return True
    return False


def draw_message(text, color):
    font = pg.font.SysFont(None, 36, True)
    message = font.render(text, True, color)
    screen.blit(message, (width / 2 - 50, height / 2 - 15))
    pg.display.flip()
    pg.time.delay(1000)


pg.init()

screen = pg.display.set_mode([width, height])

timer = pg.time.Clock()

run = True
while run:
    timer.tick(FPS)
    # Events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys_pressed = pg.key.get_pressed()

    # V. 1
    # if keys_pressed[pg.K_RIGHT] and player_rect.x < width - player_rect.width:
    #     x_direction = 1
    #     player_view = 'right'
    # elif keys_pressed[pg.K_LEFT] and player_rect.x > 0:
    #     x_direction = -1
    #     player_view = 'left'
    # elif keys_pressed[pg.K_UP] and player_rect.y > 0:
    #     y_direction = -1
    #     player_view = 'rear'
    # elif keys_pressed[pg.K_DOWN] and player_rect.y <= height - player_rect.height:
    #     y_direction = 1
    #     player_view = 'front'

    # V. 2
    if keys_pressed[pg.K_RIGHT]:
        x_direction = 1
        player_view = 'right'
    elif keys_pressed[pg.K_LEFT]:
        x_direction = -1
        player_view = 'left'
    elif keys_pressed[pg.K_UP]:
        y_direction = -1
        player_view = 'rear'
    elif keys_pressed[pg.K_DOWN]:
        y_direction = 1
        player_view = 'front'
    
    # Updating
    player_rect.x += x_direction * player_speed
    player_rect.y += y_direction * player_speed
    x_direction = 0
    y_direction = 0

    if player_rect.x > width - player_rect.width:
        player_rect.x = 0
    elif player_rect.x < 0:
        player_rect.x = width - player_rect.width
    elif player_rect.y > height - player_rect.height:
        player_rect.y = 0
    elif player_rect.y < 0:
        player_rect.y = height - player_rect.height
    
    if is_crash():
        print('IS CRASH')
        # run = False
        player_view = 'rear'
        player_rect.x = 300
        player_rect.y = 300
        (parking_rect.x, parking_rect.y) = random.choice(hotel_positions)
        passenger_rect.y += hotel_rect.height
        continue

    if parking_rect.contains(player_rect):
        passenger_rect.x, passenger_rect.y = player_rect.x, player_rect.y + player_rect.height
        draw_message('Перемога!!!', pg.Color('green'))
        player_view = 'rear'
        player_rect.x = 300
        player_rect.y = 300

        (hotel_rect.x, hotel_rect.y) = random.choice(hotel_positions)
        (passenger_rect.x, passenger_rect.y) = hotel_rect.x, hotel_rect.y + hotel_rect.height
        (parking_rect.x, parking_rect.y) = random.choice(hotel_positions)
        passenger_rect.y += hotel_rect.height
        continue

    if player_rect.colliderect(passenger_rect):
        passenger_rect.x, passenger_rect.y = player_rect.x, player_rect.y

    # Visualization
    screen.fill(BLACK)
    screen.blit(IMAGES_DICT['bg'], (0, 0))
    
    screen.blit(hotel_img, hotel_rect)
    screen.blit(parking_img, parking_rect)
    screen.blit(passenger_img, passenger_rect)
    screen.blit(IMAGES_DICT['player'][player_view], player_rect)

    pg.display.flip()

pg.quit()