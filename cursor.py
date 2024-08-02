import math
import pygame

class Cursor:
    def __init__(self, screen_height, screen_width):
        self.angle = 90
        self.radius = 50
        self.size = 10
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.left = None
        self.top = None
        self.right = None
        self.height = self.size*math.sin(60*math.pi/180)
    
    def update_cursor_points(self):
        base_point = (
            self.screen_width/2 + (self.radius*math.cos((self.angle)*math.pi/180)),
            self.screen_height/2 + (self.radius*math.sin((self.angle)*math.pi/180))
        )
        self.left = (
                        base_point[0] + ((self.size/2)*math.cos((90+self.angle)*math.pi/180)),
                        base_point[1] + ((self.size/2)*math.sin((90+self.angle)*math.pi/180))
                    )
        self.right = (
                        base_point[0] + ((self.size/2)*math.cos((-90+self.angle)*math.pi/180)),
                        base_point[1] + ((self.size/2)*math.sin((-90+self.angle)*math.pi/180))
                    )
        self.top = (
                        base_point[0] + (self.height*math.cos((self.angle)*math.pi/180)),
                        base_point[1] + (self.height*math.sin((self.angle)*math.pi/180))
                    )     

    def draw_cursor(self, gamedisplay):
            pygame.draw.polygon(gamedisplay,
                                (0,0,255,1),
                                [
                                    self.left,
                                    self.top,
                                    self.right
                                ],
                                0
                                )
            pygame.draw.line(
                gamedisplay,
                (0,255,255,1),
                self.left,
                self.right,
                width=1
            )

    def is_point_in_polygon(self, list_of_points):
        n = len(list_of_points)
        inside = False

        for x,y in [self.top, self.left, self.right]:
            p1x, p1y = list_of_points[0]
            for i in range(n + 1):
                p2x, p2y = list_of_points[i % n]
                if y > min(p1y, p2y):
                    if y <= max(p1y, p2y):
                        if x <= max(p1x, p2x):
                            if p1y != p2y:
                                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                            if p1x == p2x or x <= xinters:
                                inside = not inside
                p1x, p1y = p2x, p2y

        return inside