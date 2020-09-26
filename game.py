import turtle
import random
wn=turtle.Screen()
wn.title('game')
wn.tracer(1)
wn.bgcolor('black')
player=turtle.Turtle()
player.color('red')
player.shape('triangle')
player.penup()
player.goto(-300,0)
speed=10
#bullet
bullet=turtle.Turtle()
bullet.color('green')
bullet.penup()
bullet.goto(-280,0)
def control_up():
    if player.ycor()>290 and bullet.ycor()>290:
        player.sety(290)
        bullet.sety(290)
    bullet.sety(player.ycor()+speed)
    player.sety(player.ycor()+speed)

def control_down():
    if player.ycor()<-280 and bullet.ycor()<-280:
        player.sety(-280)
        bullet.sety(-280)
    bullet.sety(player.ycor()-speed)
    player.sety(player.ycor()-speed)
def bullet_shot():
    bullet.setx(bullet.xcor()+2)
    return bullet.xcor()
wn.listen()
wn.onkeypress(control_up,'Up')
wn.onkeypress(control_down,'Down')
wn.onkeypress(bullet_shot,'Right')
wn.delay(1)
#enemy
color=['cyan','red','blue','white','green']
enemy=turtle.Turtle()
enemy.color('cyan','blue')
enemy.penup()
enemy.shape('circle')
enemy.pensize(20)
enemy.goto(200,0)
score=0
#score
text=turtle.Turtle()
text.color('yellow')
text.hideturtle()
text.penup()
text.goto(10,250)
text.write(score,font=('Arial',30,'bold'))
run=True
k=1
while run:
    wn.update()
    if bullet.xcor()>500:
        bullet.setpos(player.xcor()+20,player.ycor())
    if bullet.xcor()>=-278:
        bullet.speed(0)
        bullet.setx(bullet.xcor()+speed)
    if bullet.distance(enemy.xcor(),enemy.ycor())<15:
        x=random.randint(0,200)
        y=random.randint(-290,280)
        enemy.setpos(x,y)
        text.clear()
        score+=1
        text.write(score,font=('Arial',30,'bold'))
wn.mainloop()