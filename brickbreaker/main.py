from tkinter import *
import time
import random

blockId = 4
donotgamestart = True
rotationslistx = [-20,-10,0,10,15]
rotationx = rotationslistx[2]
rotationslisty = [7,-7]
rotationy = rotationslisty[0]
del rotationslistx[2]

def create_block(color,x,y,width,height):
    global blockId
    global rotationx
    global rotationslistx
    global rotationslisty
    global rotationy
    canvas.create_rectangle(x,y,x+width,y+height,fill=color,outline=color)
    blockpos = canvas.coords(blockId)
    blockId += 1
    return blockpos


def movepaddle(event):
    global paddlepos
    notx = event.x
    paddlepos = canvas.coords(paddle)
    x = paddlepos[0] - notx
    if paddlepos[2] < 785:
        canvas.move(paddle,x*-1,0)
        root.update()
        root.update_idletasks()
    else:
        x = 0
        canvas.move(paddle, -5, 0)

bricksDestroyed = 0
def moveball():
    global block1
    global block2
    global block3
    global block4
    global block5
    global block6
    global bricksDestroyed
    global block
    global ballpos
    global paddlepos
    global rotationx
    global rotationslistx
    global rotationslisty
    global rotationy
    global startext
    canvas.move(ball,0,rotationy-3)
    if ballpos[3] >= paddlepos[3] and ballpos[2] > paddlepos[0] and ballpos[0] < paddlepos[2] and ballpos[1] < paddlepos[1]:
        random.shuffle(rotationslistx)
        rotationx = rotationslistx[0]
        rotationy = rotationslisty[1]
    if ballpos[1] > 800:
        canvas.itemconfig(startext, state='normal', text='Вы проиграли :(', fill='red')
        root.update()
        root.update_idletasks()
        time.sleep(1)
        root.destroy()
    if ballpos[0] <= 0:
        rotationx = rotationx * -1
    if ballpos[2] >= 800:
        rotationx = rotationx * -1
    if ballpos[1] <= 0:
        rotationy = rotationslisty[0]
    if ballpos[3] >= block1[3] and ballpos[2] > block1[0] and ballpos[0] < block1[2] and ballpos[1] < block1[1] or ballpos[1] <= block1[1] and ballpos[2] > block1[0] and ballpos[0] < block1[2] and ballpos[3] > block1[1]:
        canvas.itemconfig(4,state='hidden')
        rotationy = rotationy * -1
        bricksDestroyed += 1
        block1 = [0,0,0,0]

    if ballpos[3] >= block2[3] and ballpos[2] > block2[0] and ballpos[0] < block2[2] and ballpos[1] < block2[1] or ballpos[1] <= block2[1] and ballpos[2] > block2[0] and ballpos[0] < block2[2] and ballpos[3] > block2[1]:
        canvas.itemconfig(5,state='hidden')
        rotationy = rotationy * -1
        bricksDestroyed += 1
        block2 = [0, 0, 0, 0]
    if ballpos[3] >= block3[3] and ballpos[2] > block3[0] and ballpos[0] < block3[2] and ballpos[1] < block3[1] or ballpos[1] <= block3[1] and ballpos[2] > block3[0] and ballpos[0] < block3[2] and ballpos[3] > block3[1]:
        canvas.itemconfig(6,state='hidden')
        rotationy = rotationy * -1
        bricksDestroyed += 1
        block3 = [0, 0, 0, 0]
    if ballpos[3] >= block4[3] and ballpos[2] > block4[0] and ballpos[0] < block4[2] and ballpos[1] < block4[1] or ballpos[1] <= block4[1] and ballpos[2] > block4[0] and ballpos[0] < block4[2] and ballpos[3] > block4[1]:
        canvas.itemconfig(7,state='hidden')
        rotationy = rotationy * -1
        bricksDestroyed += 1
        block4 = [0, 0, 0, 0]
    if ballpos[3] >= block5[3] and ballpos[2] > block5[0] and ballpos[0] < block5[2] and ballpos[1] < block5[1] or ballpos[1] <= block5[1] and ballpos[2] > block5[0] and ballpos[0] < block5[2] and ballpos[3] > block5[1]:
        canvas.itemconfig(8,state='hidden')
        rotationy = rotationy * -1
        bricksDestroyed += 1
        block5 = [0, 0, 0, 0]
    if ballpos[3] >= block6[3] and ballpos[2] > block6[0] and ballpos[0] < block6[2] and ballpos[1] < block6[1] or ballpos[1] <= block6[1] and ballpos[2] > block6[0] and ballpos[0] < block6[2] and ballpos[3] > block6[1]:
        canvas.itemconfig(9,state='hidden')
        rotationy = rotationy * -1
        bricksDestroyed += 1
        block6 = [0, 0, 0, 0]
    if bricksDestroyed >= 6:
        canvas.itemconfig(startext,state='normal',text='Вы выиграли!',fill='green')
        root.update()
        root.update_idletasks()
        time.sleep(1)
        root.destroy()

    canvas.move(ball,rotationx,rotationy)
    root.update()
    root.update_idletasks()


def startgame(event):
    global donotgamestart
    donotgamestart = False




root = Tk()
root.title('Арканоид')
canvas = Canvas(root,width=800,height=800,bg='dark blue')
canvas.grid(row=0,column=0)
startext = canvas.create_text(400,500,text='Нажмите Enter чтобы начать',font=('Helvetica',20))
root.bind('<KeyPress-Return>',startgame)
while donotgamestart:
    root.update()
    root.update_idletasks()

canvas.itemconfig(startext,state='hidden')

root.unbind('<KeyPress-Return>')
root.bind('<Motion>',movepaddle)
ball = canvas.create_oval(400,600,425,625,fill='red',outline='red')
paddle = canvas.create_rectangle(335,740,400,750,fill='green',outline='green')
colors = ['red','blue','green','yellow','aqua','pink',"orange","cyan",'purple']
block1 = create_block(colors[random.randint(0,8)],random.randint(120,670),random.randint(20,610),100,10)
block2 = create_block(colors[random.randint(0,8)],random.randint(120,670),random.randint(20,610),100,10)
block3 = create_block(colors[random.randint(0,8)],random.randint(120,670),random.randint(20,610),100,10)
block4 = create_block(colors[random.randint(0,8)],random.randint(120,670),random.randint(20,610),100,10)
block5 = create_block(colors[random.randint(0,8)],random.randint(120,670),random.randint(20,610),100,10)
block6 = create_block(colors[random.randint(0,8)],random.randint(120,670),random.randint(20,610),100,10)
while True:
    paddlepos = canvas.coords(paddle)
    ballpos = canvas.coords(ball)
    root.update()
    root.update_idletasks()
    time.sleep(0.05)
    moveball()