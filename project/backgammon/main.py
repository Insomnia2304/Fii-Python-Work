import pygame
import sys
import random

from constants import *
from utils import *

shapes = {}
game_state = {}

"""
A class representing a circle that can be dragged and moved across the screen.

Attributes:
    color (tuple): The color of the circle.
    original_color (tuple): The original color of the circle.
    dragging (bool): A flag indicating whether the circle is being dragged.
    on_top (bool): A flag indicating whether the circle is on top of the stack.
    finish (bool): A flag indicating whether the circle is in the finish rectangle.
    eaten (bool): A flag indicating whether the circle is eaten.
    father (Triangle): The triangle that the circle is currently on.
    x (int): The x-coordinate of the circle.
    y (int): The y-coordinate of the circle.
    to_move (dict): A dictionary containing the triangles that the circle can move to.
"""
class Circle:
    is_dragging = False
    def __init__(self, color):
        self.color = self.original_color = color
        self.dragging = False
        self.on_top = False
        self.finish = False
        self.eaten = False
    """
    Sets the father of the circle.

    Args:
        father (Triangle): The triangle that the circle is currently on.
    """
    def set_father(self, father):
        self.father = father
    """
    Sets the center of the circle.

    Args:
        center (tuple): The center of the circle.
    """
    def set_center(self, center):
        self.x = center[0]
        self.y = center[1]
    """
    Handles the event.
    
    Args:
        event (pygame.event): The event to be handled.
    """
    def handle_event(self, event):
        if self.finish or self.color != GREEN:
            return
        if event.type == pygame.MOUSEBUTTONDOWN and self.on_top:
            dist = ((self.x - event.pos[0])**2 + (self.y - event.pos[1])**2) ** 0.5
            if dist <= CIRCLE_RADIUS:
                if self in shapes['eaten_red']:
                    shapes['eaten_red'].remove(self)
                    self.eaten = True
                if self in shapes['eaten_white']:
                    shapes['eaten_white'].remove(self)
                    self.eaten = True
                Circle.dragged = self
                self.dragging = Circle.is_dragging = True
                self.offset_x = self.x - event.pos[0]
                self.offset_y = self.y - event.pos[1]
                self.original_x = self.x
                self.original_y = self.y

                for index in self.to_move:
                    shapes['triangles'][index].color = GREEN

        elif event.type == pygame.MOUSEBUTTONUP and self.dragging:
            self.dragging = Circle.is_dragging = False
            finished = False
            Circle.dragged = None

            found = False
            for index in self.to_move:
                if circle_fit_into_triangle(self, shapes['triangles'][index]):
                    if len(shapes['triangles'][index].circles) == 1 and shapes['triangles'][index].circles[-1].original_color != self.original_color:
                        shapes['eaten_' + ('red' if self.original_color == WHITE else 'white')].append(shapes['triangles'][index].remove_circle())
                    self.eaten = False
                    self.father.remove_circle()
                    shapes['triangles'][index].add_circle(self)
                    found = True
                    self.color = self.original_color
                    update_moves(self.to_move[index])
                    highlight_moves()

            if circle_fit_into_finish_rectangle(self, shapes['finish_rect']) and finished:
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
                if self.eaten:
                    if self.original_color == WHITE:
                        shapes['eaten_white'].append(self)
                    else:
                        shapes['eaten_red'].append(self)
                    self.eaten = False
        
            for triangle in shapes['triangles']:
                triangle.color = triangle.original_color
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.x = event.pos[0] + self.offset_x
                self.y = event.pos[1] + self.offset_y
    """
    Draws the circle on the screen.

    Args:
        screen (pygame.Surface): The screen to draw the circle on.
    """
    def draw(self, screen):
        if not self.finish:
            pygame.draw.circle(screen, self.color, (self.x, self.y), CIRCLE_RADIUS)

"""
A class representing a triangle that can contain circles.

Attributes:
    x (tuple): The x-coordinate of the triangle.
    y (tuple): The y-coordinate of the triangle.
    z (tuple): The z-coordinate of the triangle.
    color (tuple): The color of the triangle.
    original_color (tuple): The original color of the triangle.
    circles (list): A list of circles on the triangle.
    index (int): The index of the triangle.
"""
class Triangle:
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = self.original_color = color
        self.circles = []
    """
    Sets the index of the triangle.
    
    Args:
        index (int): The index of the triangle.
    """
    def set_index(self, index):
        self.index = index
    """
    Adds a circle to the triangle.
    
    Args:
        circle (Circle): The circle to be added.
    """
    def add_circle(self, circle):
        if len(self.circles) > 0:
            self.circles[-1].on_top = False
        circle.set_father(self)
        circle.on_top = True
        self.circles.append(circle)
        self.compute_circles_positions()
    """
    Removes the top circle from the triangle.
    """
    def remove_circle(self):
        if len(self.circles) == 0:
            return
        circle = self.circles.pop()
        if len(self.circles) > 0:
            self.circles[-1].on_top = True
        self.compute_circles_positions()
        return circle
    """
    Computes the circles positions based on their number.
    """
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
    """
    Draws the triangle on the screen.
    
    Args:
        screen (pygame.Surface): The screen to draw the triangle on.
    """
    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [self.x, self.y, self.z])

"""
Initializes the game. 
"""
def init():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Backgammon')

    prep_dices()
    build_shapes()
    prep_game_state()

    return screen

"""
Prepares the dice images and loads them. 
"""
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

"""
Builds the shapes of the game.
"""
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
    shapes['eaten_red'] = []
    shapes['eaten_white'] = []

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
    
    for i in range(24):
        shapes['triangles'][i].set_index(i)
    
    shapes['circles'] = []
    for i in range(len(INIT_CIRCLES)):
        shapes['circles'].append(Circle(INIT_CIRCLES[i][1]))
        shapes['triangles'][INIT_CIRCLES[i][0]].add_circle(shapes['circles'][-1])

    shapes['left_dice_num'], shapes['right_dice_num'] = (6, 6)

    shapes['left_dice'] = shapes['dice_images'][1].get_rect()
    shapes['left_dice'].center = (shapes['right_border'].x + shapes['right_border'].width / 3, shapes['right_border'].centery)

    shapes['right_dice'] = shapes['dice_images'][1].get_rect()
    shapes['right_dice'].center = (shapes['left_dice'].midright[0] + shapes['left_dice'].width, shapes['right_border'].centery)

"""
Prepares the game state.

Args:
    game_type (str): The type of the game. Default is 'multiplayer'.
"""
def prep_game_state(game_type='multiplayer'):
    game_state['type'] = game_type
    game_state['move'] = RED
    shapes['moves'] = []

"""
Highlights the possible moves for the current player. Includes possible moves for the circles and the destination triangles.
"""
def highlight_moves():
    move_found = False
    for circle in shapes['circles']:
        circle.color = circle.original_color

    if shapes['moves'] == []:
        return
    
    if shapes['eaten_red'] != [] and game_state['move'] == RED:
        for circle in shapes['eaten_red']:
            for move in set(shapes['moves']):
                if len(shapes['triangles'][move-1].circles) == 0 or shapes['triangles'][move-1].circles[-1].original_color == game_state['move'] or (len(shapes['triangles'][move-1].circles) == 1 and shapes['triangles'][move-1].circles[-1].original_color != game_state['move']):
                    circle.color = GREEN
                    circle.to_move[move-1] = move
                    move_found = True
        if not move_found:
            shapes['moves'] = [7]
            update_moves(7)
        return
    
    if shapes['eaten_white'] != [] and game_state['move'] == WHITE:
        for circle in shapes['eaten_white']:
            for move in set(shapes['moves']):
                if len(shapes['triangles'][24 - move].circles) == 0 or shapes['triangles'][24 - move].circles[-1].original_color == game_state['move'] or (len(shapes['triangles'][24 - move].circles) == 1 and shapes['triangles'][24 - move].circles[-1].original_color != game_state['move']):
                    circle.color = GREEN
                    circle.to_move[24 - move] = move
                    move_found = True
        if not move_found:
            shapes['moves'] = [7]
            update_moves(7)
        return

    for circle in shapes['circles']:
        circle.to_move = {}
        if circle.on_top and circle.original_color == game_state['move']:
            for move in set(shapes['moves']):
                if game_state['move'] == RED:
                    if circle.father.index + move < 24:
                        if len(shapes['triangles'][circle.father.index + move].circles) == 0 or shapes['triangles'][circle.father.index + move].circles[-1].original_color == game_state['move'] or (len(shapes['triangles'][circle.father.index + move].circles) == 1 and shapes['triangles'][circle.father.index + move].circles[-1].original_color != game_state['move']):
                            circle.color = GREEN
                            circle.to_move[circle.father.index + move] = move
                            move_found = True
                elif game_state['move'] == WHITE:
                    if circle.father.index - move >= 0:
                        if len(shapes['triangles'][circle.father.index - move].circles) == 0 or shapes['triangles'][circle.father.index - move].circles[-1].original_color == game_state['move'] or (len(shapes['triangles'][circle.father.index - move].circles) == 1 and shapes['triangles'][circle.father.index - move].circles[-1].original_color != game_state['move']):
                            circle.color = GREEN
                            circle.to_move[circle.father.index - move] = move
                            move_found = True

    if not move_found:
        shapes['moves'] = [7]
        update_moves(7)


"""
Draws the table on the screen.

Args:
    screen (pygame.Surface): The screen to draw the table on.
"""
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
    if hasattr(Circle, 'dragged') and Circle.dragged is not None:
        Circle.dragged.draw(screen)
    arrange_eaten()

"""
Draws the finish rectangle on the screen.
Makes sure that circles are drawn in the finish rectangle based on their number.
"""
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

"""
Arranges the eaten circles on the screen.
"""
def arrange_eaten():
    rect1 = shapes['left_rect']
    rect2 = shapes['right_rect']

    redcenter = (rect1.right + (rect2.x - rect1.right) / 2, rect1.y + rect1.height * 1/3 - 2 * CIRCLE_RADIUS)
    whitecenter = (rect1.right + (rect2.x - rect1.right) / 2,  rect1.y + rect1.height * 2/3 + 2 * CIRCLE_RADIUS)

    for circle in shapes['eaten_red']:
        circle.set_center(redcenter)
        redcenter = (redcenter[0], redcenter[1] - 2 * CIRCLE_RADIUS)

    for circle in shapes['eaten_white']:
        circle.set_center(whitecenter)
        whitecenter = (whitecenter[0], whitecenter[1] + 2 * CIRCLE_RADIUS)

"""
Rolls the dice. Uses the random module to generate random numbers between 1 and 6.
"""
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

"""
Gets the possible moves for the current player.
"""
def get_moves():
    shapes['moves'] = []
    shapes['moves'].append(shapes['left_dice_num'])
    shapes['moves'].append(shapes['right_dice_num'])
    if shapes['left_dice_num'] == shapes['right_dice_num']:
        shapes['moves'].append(shapes['left_dice_num'])
        shapes['moves'].append(shapes['right_dice_num'])

"""
Updates the moves structure based on the move made by the player.
"""
def update_moves(move):
    shapes['moves'].remove(move)
    if len(shapes['moves']) == 0:
        # print('Switching player')
        game_state['move'] = RED if game_state['move'] == WHITE else WHITE

"""
The main function of the game. This is where magic happens.
"""
def main():
    screen = init()
    rolling = False

    while True:
        draw_table(screen)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not rolling and shapes['moves'] == []:
                if shapes['left_dice'].collidepoint(event.pos) or shapes['right_dice'].collidepoint(event.pos):
                    rolling = True
                    start_time = pygame.time.get_ticks()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    prep_game_state('singleplayer')
                    build_shapes()
                    rolling = False
                if event.key == pygame.K_m:
                    prep_game_state('multiplayer')
                    build_shapes()
                    rolling = False
                if event.key == pygame.K_z and not rolling and shapes['moves'] == []:
                    rolling = True
                    start_time = pygame.time.get_ticks()
            for circle in shapes['circles']:
                circle.handle_event(event)

        if rolling:
            elapsed_time = pygame.time.get_ticks() - start_time
            if elapsed_time < DICE_ROLL_TIME_MS:
                shapes['left_dice_num'], shapes['right_dice_num'] = roll_dice()
                # shapes['left_dice_num'], shapes['right_dice_num'] = (3, 3)
            else:
                get_moves()
                highlight_moves()
                rolling = False

        pygame.display.flip()

if __name__ == '__main__':
    main()
