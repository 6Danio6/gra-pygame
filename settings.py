import pygame, os, settings, menu, time
from gra import Gra

clock = pygame.time.Clock()
Clock = pygame.time.Clock()

# display stuff

window_size = [1280,720]

Display = pygame.Surface((640,360))

screen = pygame.display.set_mode(window_size)

# extra

pygame.display.set_icon(pygame.image.load("player_animations\idle\idle_0.png"))
pygame.display.set_caption("Couch Potato")

# variables

saw_img = pygame.image.load("sawblade.png")
saw_img = pygame.transform.scale(saw_img, (32,32))
couch_img = pygame.image.load("couch.png")

angle=0
scroll = [0,0]
volume = 100

# functions

def collision_test(rect, tiles):
    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    return collisions

def move(rect,movement,tiles):
    rect.x += movement[0]
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    collisions = collision_test(rect,tiles)
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        if movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    collisions = collision_test(rect,tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

def load_tiles():
    tilepics = []
    files = os.listdir("tiles")
    files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
    for file in files:
        tilepics.append(pygame.image.load("tiles/" + file))
    return tilepics

def load_map(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    data = data.split("\n")
    game_map = []
    for row in data:
        game_map.append(row.split(" "))
    return(game_map)

def display_map(game_map, tilepics, angle):        #           1-55 = tiles        98 = saw        99 = couch
    tile_size = tilepics[0].get_width()
    tile_rects = []
    saw_rects = []
    couch_rect = []
    spike_rects = []
    y = 0
    for row in game_map:
        if row == game_map[-1]:
            break
        x = 0
        for tile in row:
            for i in range(len(tilepics)):
                if int(tile) == i+1 and i + 1 < 56:
                    Display.blit(tilepics[i],(x * tile_size - settings.scroll[0], y * tile_size - settings.scroll[1]))
                    tile_rects.append(pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
                    break
                elif int(tile) == i + 1:
                    Display.blit(tilepics[i],(x * tile_size - settings.scroll[0], y * tile_size - settings.scroll[1]))
                    spike_rects.append(pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
            if int(tile) == 98:
                saw_img_copy = pygame.transform.rotate(saw_img,angle).copy()
                Display.blit(saw_img_copy,((x*tile_size - int(saw_img_copy.get_width() / 2) + saw_img.get_width()/2) - settings.scroll[0], (y*tile_size - int(saw_img_copy.get_height() / 2)+saw_img.get_height()/2) - settings.scroll[1]))
                saw_rects.append(pygame.Rect(x*tile_size + 10 , y*tile_size + 10, tile_size - 20, tile_size - 20))
            if int(tile) == 99:
                Display.blit(couch_img,((x*tile_size+3) - settings.scroll[0] , (y*tile_size+4) - settings.scroll[1]))
                couch_rect.append(pygame.Rect(x*tile_size , y*tile_size, couch_img.get_width(), couch_img.get_height()))
            x += 1
        y += 1
    return tile_rects, saw_rects, couch_rect, spike_rects

def load_animation(path, frame_durations):
    animation_name = path.split("/")[-1]
    animation_frames = []
    n = 0
    for frame in frame_durations:
        animation_frame_id = animation_name + "_" + str(n)
        img_loc = path + "/" + animation_frame_id + ".png"
        frame_image = pygame.image.load(img_loc)
        for i in range(frame):
            animation_frames.append(frame_image)
        n += 1
    return animation_frames

def get_font(number, size):
    return pygame.font.Font(f"fonts/font{number}.ttf", size)

def load_intro(path, frame_durations):
    intro_frames = []
    n = 1
    for frame in frame_durations:
        if n < 10:
            img_loc = path + "/" + "0000" + str(n) + ".png"
        else:
            img_loc = path + "/" + "000" + str(n) + ".png"
        frame_image = pygame.image.load(img_loc)
        for i in range(frame):
            intro_frames.append(frame_image)
        n += 1
    return intro_frames

def intro():
    intro = load_intro("intro", [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])
    for frame in intro:
        Display.blit(frame, (0,0))
        screen.blit(pygame.transform.scale(Display,(window_size)),(0,0))
        pygame.display.update()
        clock.tick(60)
    menu.Menu()

def load_map_player_cords(map_num):
    file = open("maps/map" + str(map_num) +  ".txt", "r")
    data = file.read()
    file.close()
    data = data.split("\n")
    player_cords = []
    player_cords = data[-1].split(" ")
    player_x = player_cords[0]
    player_y = player_cords[1]
    return player_x, player_y

def you_dead(map_number):
    img = pygame.image.load("you_dead.png")
    maklowicz = pygame.mixer.Sound("maklowicz_i_koperkowy_pies.wav")
    Display.blit(img,(201,95))
    screen.blit(pygame.transform.scale(Display,(window_size)),(0,0))
    pygame.display.update()
    maklowicz.play()
    time.sleep(3)
    Gra(map_number)

def next_lvl(current_map_number):
    img = pygame.image.load("you_dead.png")
    Display.blit(img,(201,95))
    screen.blit(pygame.transform.scale(Display,(window_size)),(0,0))
    pygame.display.update()
    time.sleep(3)
    Gra(current_map_number + 1)