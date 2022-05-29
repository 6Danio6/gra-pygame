import pygame, os

clock = pygame.time.Clock()
Clock = pygame.time.Clock()

# display stuff

window_size = [1280,720]

Display = pygame.Surface((640,360))

screen = pygame.display.set_mode(window_size)

# extra

icon = pygame.image.load("player_animations\idle\idle_0.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Couch Potato")

saw_img = pygame.image.load("sawblade.png")
saw_img = pygame.transform.scale(saw_img, (32,32))
couch_img = pygame.image.load("couch.png")
couch_img = pygame.transform.scale(couch_img, (32,32))

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

def display_map(game_map, tilepics):        #           1-53 = tiles        98 = saw        99 = couch
    tile_size = tilepics[0].get_width()
    tile_rects = []
    saw_rects = []
    couch_rect = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            for i in range(len(tilepics)):
                if int(tile) == i+1:
                    Display.blit(tilepics[i],(x * tile_size, y * tile_size))
                    tile_rects.append(pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size))
                    break
            if int(tile) == 98:
                Display.blit(saw_img,(x*tile_size, y*tile_size))
                saw_rects.append(pygame.Rect(x*tile_size + 10 , y*tile_size + 10, tile_size - 20, tile_size - 20))
            if int(tile) == 99:
                Display.blit(couch_img,(x*tile_size, y*tile_size))
                couch_rect.append(pygame.Rect(x*tile_size , y*tile_size, tile_size, tile_size))
            x += 1
        y += 1
    return [tile_rects, saw_rects, couch_rect]

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