import pygame
import math

def convert_offset_from_center_to_coords(angle, distance, height, width):
    finalx = height/2 + (distance*math.cos((90+angle)*math.pi/180))
    finaly = width/2 + (distance*math.sin((90+angle)*math.pi/180))
    return (finaly, finalx)

class Obstacle:
    def __init__(self,direction,width, distance, screen_height, screen_width):
        self.direction = direction
        self.width = width
        self.distance = 1000 + distance
        self.direction_map = {
            "top-left": [150, 90],
            "top-right": [90, 30],
            "right": [30, -30],
            "left": [150, 210],
            "bottom-right": [-30, -90],
            "bottom-left": [-90, -150]
        }
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.points = None

    def draw_polygon(self, gamedisplay):
        if(self.distance > 0):
            pygame.draw.polygon(gamedisplay,
                                (255,0,0,1),
                                self.points,
                                0
                                )
    def update_current_points(self):
        self.points = [
            convert_offset_from_center_to_coords(self.direction_map[self.direction][0], self.distance+self.width, self.screen_height, self.screen_width),
            convert_offset_from_center_to_coords(self.direction_map[self.direction][0], self.distance, self.screen_height, self.screen_width),
            convert_offset_from_center_to_coords(self.direction_map[self.direction][1], self.distance, self.screen_height, self.screen_width),
            convert_offset_from_center_to_coords(self.direction_map[self.direction][1], self.distance+self.width, self.screen_height, self.screen_width)
        ]