import pygame
from obstacle import convert_offset_from_center_to_coords, Obstacle
from cursor import Cursor
import time
import json

pygame.init()

config = json.load(open("config.json","r"))

width = config["screen_width"]
height = config["screen_height"]

gamedisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("OpenHexagon")

clock = pygame.time.Clock()

level_data = [
    Obstacle("top-left", 40, 10, height, width),
    Obstacle("top-right",40, 100, height, width)
]

scroll_speed = config["scroll_speed"]
cursor_speed = config["cursor_speed"]

cursor = Cursor(height, width)
start = time.time()

while True:
    gamedisplay.fill((255,255,255))

    for obstacle in level_data:
        obstacle.update_current_points()
        obstacle.draw_polygon(gamedisplay)
        obstacle.distance -= scroll_speed

    pygame.draw.polygon(gamedisplay,
                        (0,255,0,1),
                        [
                            convert_offset_from_center_to_coords(30,40, height, width),
                            convert_offset_from_center_to_coords(90,40, height, width),
                            convert_offset_from_center_to_coords(150,40, height, width),
                            convert_offset_from_center_to_coords(210,40, height, width),
                            convert_offset_from_center_to_coords(270,40, height, width),
                            convert_offset_from_center_to_coords(-30,40, height, width)
                        ],
                        0
                        )

    cursor.update_cursor_points()
    cursor.draw_cursor(gamedisplay)
    for obstacle in level_data:
        if(cursor.is_point_in_polygon(obstacle.points)):
            print("You FAILED !")
            print(f"You lasted: {time.time()-start} seconds !")
            pygame.quit()
            quit()
    

    keys=pygame.key.get_pressed()
    if(keys[pygame.K_LEFT]):
        cursor.angle -= cursor_speed
    if(keys[pygame.K_RIGHT]):
        cursor.angle += cursor_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()           

    pygame.display.update()
    clock.tick(config["framerate"])