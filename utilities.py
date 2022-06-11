import turtle

screen = turtle.Screen()

def set_background_image(image):
    screen.bgpic(image)
    screen.update()

def set_image(t, image):
    screen.addshape(image)
    t.shape(image)

def point_in_rect(x, y, x1, x2, y1, y2):
    if x >= x1 and x <= x2 and y >= y1 and y <= y2:
        return True
    return False
    
