import pygame

clock = pygame.time.Clock()

window_size = [1280,720]

Display = pygame.Surface((640,360))

screen = pygame.display.set_mode(window_size)

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
    intro = load_intro("intro", [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])
    intro_end = load_intro("intro/intro end",[6,6,6,6])
    breake = False
    i = 0
    j = 0
    for frame in intro:
        Display.blit(frame, (0,0))
        screen.blit(pygame.transform.scale(Display,(window_size)),(0,0))
        pygame.display.update()
        clock.tick(60)
    
    pygame.quit()

intro()