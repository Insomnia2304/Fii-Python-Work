from main import *

"""
Check if the circle is held inside the traingle
It has to be above the support rectangle of the triangle to be considered inside the triangle
(Larger margin so it is easier to move)
Args:
    circle: Circle object
    triangle: Triangle object
"""
def circle_fit_into_triangle(circle, triangle):
    if triangle.z[1] > triangle.y[1]:
        if circle.x >= triangle.x[0] and circle.x <= triangle.y[0] and circle.y >= triangle.y[1] and circle.y <= triangle.z[1]:
            return True
        return False
    return circle.x >= triangle.x[0] and circle.x <= triangle.y[0] and circle.y >= triangle.z[1] and circle.y <= triangle.y[1]
    
"""
Check if the circle is held inside the finish rectangle
Args:
    circle: Circle object
    finish_rectangle: pygame.Rect object
"""
def circle_fit_into_finish_rectangle(circle, finish_rectangle):
    return circle.x >= finish_rectangle.x and circle.x <= finish_rectangle.x + finish_rectangle.width and circle.y >= finish_rectangle.y and circle.y <= finish_rectangle.y + finish_rectangle.height
