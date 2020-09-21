import turtle
import random
clr_list = ['red', 'blue', 'gold', 'brown', 'violet', 'pink', 'orange', 'yellow']
def pinwheel(num_branch, size, backup):
    """ draw polagon
    """
    turtle.penup()
    turtle.goto(random.randint(-200,200), random.randint(-200, 200))
    
    turtle.pendown()
    for i in range(num_branch):
        turtle.forward(size)
        turtle.backward(backup)
        turtle.right(360/num_branch)
    
    
    

for i in range(10):
    turtle.pensize(random.randint(2, 20))
    turtle.color(random.choice(clr_list))
    pinwheel(random.randrange(3,9), random.randrange(30, 100), random.randrange(30, 100))
    
