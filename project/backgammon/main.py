import pygame
import sys
import random

from constants import *
from utils import *

shapes = {}

class Circle:
    is_dragging = False
    def __init__(self, color):
        self.color = color
        self.dragging = False
        self.on_top = False
        self.finish = False
    def set_father(self, father):
        self.father = father
    def set_center(self, center):
        self.x = center[0]
        self.y = center[1]
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), CIRCLE_RADIUS)
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.on_top:
            dist = ((self.x - event.pos[0])**2 + (self.y - event.pos[1])**2) ** 0.5
            if dist <= CIRCLE_RADIUS:
                Circle.dragged = self
                self.dragging = Circle.is_dragging = True
                self.offset_x = self.x - event.pos[0]
                self.offset_y = self.y - event.pos[1]
                self.original_x = self.x
                self.original_y = self.y

        elif event.type == pygame.MOUSEBUTTONUP and self.dragging:
            self.dragging = Circle.is_dragging = False

            found = False
            for triangle in shapes['triangles']:
                if circle_fit_into_triangle(self, triangle):
                    self.father.remove_circle()
                    triangle.add_circle(self)
                    found = True
            
            if circle_fit_into_finish_rectangle(self, shapes['finish_rect']):
                self.father.remove_circle()
                self.finish = True
                if self.color == WHITE:
                    shapes['finish_white'] += 1
                else:
                    shapes['finish_red'] += 1
                found = True

            if not found:
                self.x = self.original_x
                self.y = self.original_y

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.x = event.pos[0] + self.offset_x
                self.y = event.pos[1] + self.offset_y
    def draw(self, screen):
        if not self.finish:
            pygame.draw.circle(screen, self.color, (self.x, self.y), CIRCLE_RADIUS)

class Triangle:
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.circles = []
    def add_circle(self, circle):
        circle.set_father(self)
        circle.on_top = True
        if len(self.circles) > 0:
            self.circles[-1].on_top = False
        self.circles.append(circle)
        self.compute_circles_positions()
    def remove_circle(self):
        circle = self.circles.pop()
        if len(self.circles) > 0:
            self.circles[-1].on_top = True
        self.compute_circles_positions()
        return circle
    def compute_circles_positions(self):
        circles_number = len(self.circles)
        if circles_number == 0:
            return
        
        max_height = abs(self.z[1] - self.x[1])   
        if self.z[1] > self.x[1]:
            center = (self.x[0] + ((self.y[0] - self.x[0]) / 2), self.x[1] + CIRCLE_RADIUS)
        else:
            center = (self.x[0] + ((self.y[0] - self.x[0]) / 2), self.x[1] - CIRCLE_RADIUS)

        if 2 * CIRCLE_RADIUS * circles_number > max_height:
            offset = max_height / circles_number
            for circle in self.circles:
                circle.set_center(center)
                if self.z[1] > self.x[1]:
                    center = (center[0], center[1] + offset)
                else:
                    center = (center[0], center[1] - offset)
        else:
            for circle in self.circles:
                circle.set_center(center)
                if self.z[1] > self.x[1]:
                    center = (center[0], center[1] + 2 * CIRCLE_RADIUS)
                else:
                    center = (center[0], center[1] - 2 * CIRCLE_RADIUS)
            
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [self.x, self.y, self.z])

def init():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Backgammon')

    prep_dices()
    build_shapes()

    return screen

def prep_dices():
    dice_images = {
    1: pygame.image.load('img/dice_1.png'),
    2: pygame.image.load('img/dice_2.png'),
    3: pygame.image.load('img/dice_3.png'),
    4: pygame.image.load('img/dice_4.png'),
    5: pygame.image.load('img/dice_5.png'),
    6: pygame.image.load('img/dice_6.png')
}
    dice_size = (SCREEN_WIDTH // 15, SCREEN_WIDTH // 15)
    for i in range(1, 7):
        dice_images[i] = pygame.transform.scale(dice_images[i], dice_size)
    
    shapes['dice_images'] = dice_images

def build_shapes():
    global shapes

    median_width = SCREEN_WIDTH * 0.003

    border_width = (SCREEN_WIDTH * 0.85 - median_width) / 2
    border_height = SCREEN_HEIGHT * 0.90

    left_border_x = SCREEN_WIDTH * 0.03
    left_border_y = SCREEN_HEIGHT * 0.05

    right_border_x = SCREEN_WIDTH * 0.03 + border_width + median_width
    right_border_y = SCREEN_HEIGHT * 0.05
    
    shapes['left_border'] = pygame.Rect(left_border_x, left_border_y, border_width, border_height)
    shapes['right_border'] = pygame.Rect(right_border_x, right_border_y, border_width, border_height)
    shapes['finish_rect'] = pygame.Rect(right_border_x + border_width + 0.02 * SCREEN_WIDTH, right_border_y, SCREEN_WIDTH * 0.06, border_height)
    shapes['finish_red'] = shapes['finish_white'] = 0

    rect_width = border_width * 0.922
    rect_height = border_height * 0.94

    left_rect_x = left_border_x + border_width * 0.04
    left_rect_y = left_border_y + border_height * 0.03

    rigth_rect_x = right_border_x + border_width * 0.04
    right_rect_y = left_border_y + border_height * 0.03

    shapes['left_rect'] = pygame.Rect(left_rect_x, left_rect_y, rect_width, rect_height)
    shapes['right_rect'] = pygame.Rect(rigth_rect_x, right_rect_y, rect_width, rect_height)

    hinge_width = median_width + (left_rect_x - left_border_x) * 2
    hinge_height = border_height * 0.15

    top_hinge_x = left_rect_x + rect_width
    top_hinge_y = left_border_y + border_height * 0.15

    bot_hinge_x = left_rect_x + rect_width
    bot_hinge_y = SCREEN_HEIGHT - left_border_y - border_height * 0.15 - hinge_height
    
    shapes['top_hinge'] = pygame.Rect(top_hinge_x, top_hinge_y, hinge_width, hinge_height)
    shapes['bot_hinge'] = pygame.Rect(bot_hinge_x, bot_hinge_y, hinge_width, hinge_height)



    shapes['triangles'] = []

    x = (rigth_rect_x, left_rect_y)
    y = (rigth_rect_x + rect_width / 6, left_rect_y)
    z = (x[0] + rect_width / 12, left_rect_y + rect_height / TRIANGLE_RATIO)

    shapes['triangles'].insert(0, Triangle(x, y, z, DARK_TRIANGLE))
    for i in range(5):
        x = (x[0] + rect_width / 6, x[1])
        y = (y[0] + rect_width / 6, y[1])
        z = (z[0] + rect_width / 6, z[1])
        shapes['triangles'].insert(0, Triangle(x, y, z, DARK_LIGHT[i % 2 == 0]))

    x = (left_rect_x, left_rect_y)
    y = (left_rect_x + rect_width / 6, left_rect_y)
    z = (x[0] + rect_width / 12, left_rect_y + rect_height / TRIANGLE_RATIO)

    shapes['triangles'].insert(6, Triangle(x, y, z, DARK_TRIANGLE))
    for i in range(5):
        x = (x[0] + rect_width / 6, x[1])
        y = (y[0] + rect_width / 6, y[1])
        z = (z[0] + rect_width / 6, z[1])
        shapes['triangles'].insert(6, Triangle(x, y, z, DARK_LIGHT[i % 2 == 0]))

    x = (left_rect_x, left_rect_y + rect_height)
    y = (left_rect_x + rect_width / 6, left_rect_y + rect_height)
    z = (x[0] + rect_width / 12, left_rect_y + rect_height - rect_height / TRIANGLE_RATIO)

    shapes['triangles'].append(Triangle(x, y, z, LIGHT_TRIANGLE))
    for i in range(5):
        x = (x[0] + rect_width / 6, x[1])
        y = (y[0] + rect_width / 6, y[1])
        z = (z[0] + rect_width / 6, z[1])
        shapes['triangles'].append(Triangle(x, y, z, DARK_LIGHT[i % 2]))

    x = (rigth_rect_x, left_rect_y + rect_height)
    y = (rigth_rect_x + rect_width / 6, left_rect_y + rect_height)
    z = (x[0] + rect_width / 12, left_rect_y + rect_height - rect_height / TRIANGLE_RATIO)

    shapes['triangles'].append(Triangle(x, y, z, LIGHT_TRIANGLE))
    for i in range(5):
        x = (x[0] + rect_width / 6, x[1])
        y = (y[0] + rect_width / 6, y[1])
        z = (z[0] + rect_width / 6, z[1])
        shapes['triangles'].append(Triangle(x, y, z, DARK_LIGHT[i % 2]))
    
    shapes['circles'] = []
    for i in range(len(INIT_CIRCLES)):
        shapes['circles'].append(Circle(INIT_CIRCLES[i][1]))
        shapes['triangles'][INIT_CIRCLES[i][0]].add_circle(shapes['circles'][-1])

    shapes['left_dice'] = shapes['dice_images'][1].get_rect()
    shapes['left_dice'].center = (shapes['right_border'].x + shapes['right_border'].width / 3, shapes['right_border'].centery)

    shapes['right_dice'] = shapes['dice_images'][1].get_rect()
    shapes['right_dice'].center = (shapes['left_dice'].midright[0] + shapes['left_dice'].width, shapes['right_border'].centery)

def draw_table(screen):
    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(screen, BORDER_COLOR, shapes['left_border'])
    pygame.draw.rect(screen, BORDER_COLOR, shapes['right_border'])
    draw_finish(screen)

    pygame.draw.rect(screen, TABLE_COLOR, shapes['left_rect'])
    pygame.draw.rect(screen, TABLE_COLOR, shapes['right_rect'])

    pygame.draw.rect(screen, HINGE_COLOR, shapes['top_hinge'])
    pygame.draw.rect(screen, HINGE_COLOR, shapes['bot_hinge'])

    screen.blit(shapes['dice_images'][shapes['left_dice_num']], shapes['left_dice'])
    screen.blit(shapes['dice_images'][shapes['right_dice_num']], shapes['right_dice'])

    for triangle in shapes['triangles']:
        triangle.draw(screen)

    for circle in shapes['circles']:
        circle.draw(screen)
    if hasattr(Circle, 'dragged'):
        Circle.dragged.draw(screen)

def draw_finish(screen):
    rect = shapes['finish_rect']
    pygame.draw.rect(screen, FINISH_COLOR, rect)

    max_height = rect.height / 2.2
    redcenter = (rect.x + rect.width / 2, rect.y + CIRCLE_RADIUS)
    whitecenter = (rect.x + rect.width / 2, rect.y + rect.height - CIRCLE_RADIUS)

    if 2 * CIRCLE_RADIUS * shapes['finish_red'] > max_height:
        for _ in range(shapes['finish_red']):
            offset = max_height / shapes['finish_red']
            pygame.draw.circle(screen, RED, redcenter, CIRCLE_RADIUS)
            redcenter = (redcenter[0], redcenter[1] + offset)
    else:
        for _ in range(shapes['finish_red']):
            pygame.draw.circle(screen, RED, redcenter, CIRCLE_RADIUS)
            redcenter = (redcenter[0], redcenter[1] + 2 * CIRCLE_RADIUS)

    if 2 * CIRCLE_RADIUS * shapes['finish_white'] > max_height:
        for _ in range(shapes['finish_white']):
            offset = max_height / shapes['finish_white']
            pygame.draw.circle(screen, WHITE, whitecenter, CIRCLE_RADIUS)
            whitecenter = (whitecenter[0], whitecenter[1] - offset)
    else:
        for _ in range(shapes['finish_white']):
            pygame.draw.circle(screen, WHITE, whitecenter, CIRCLE_RADIUS)
            whitecenter = (whitecenter[0], whitecenter[1] - 2 * CIRCLE_RADIUS)

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def main():
    screen = init()

    rolling = False
    shapes['left_dice_num'], shapes['right_dice_num'] = (6, 6)

    while True:
        draw_table(screen)

        mouse_pos = pygame.mouse.get_pos()
        if not Circle.is_dragging:
            if shapes['left_dice'].collidepoint(mouse_pos) or shapes['right_dice'].collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if shapes['left_dice'].collidepoint(event.pos) or shapes['right_dice'].collidepoint(event.pos):
                    rolling = True
                    start_time = pygame.time.get_ticks()
            for circle in shapes['circles']:
                circle.handle_event(event)

        if rolling:
            elapsed_time = pygame.time.get_ticks() - start_time
            if elapsed_time < DICE_ROLL_TIME_MS:
                dice1, dice2 = roll_dice()
                shapes['left_dice_num'], shapes['right_dice_num'] = (dice1, dice2)
            else:
                rolling = False

        pygame.display.flip()

if __name__ == '__main__':
    main()
