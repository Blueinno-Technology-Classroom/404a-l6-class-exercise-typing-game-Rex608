import pgzrun
from pgzhelper import*

WIDTH = 1000
HEIGHT = 800

run_imgs = ['zombies/run/tile002','zombies/run/tile003','zombies/run/tile003','zombies/run/tile005']
zombie = Actor(run_imgs[0])
zombie.fps = 10
zombie.images = run_imgs
zombie.scale = 1
zombie.right = WIDTH
zombie.bottom = HEIGHT-200
zombie.fps = 10
question = 'hello'
typed=''

idle_imgs = ['wizard/idle/tile000','wizard/idle/tile001','wizard/idle/tile002','wizard/idle/tile003','wizard/idle/tile004','wizard/idle/tile005']
wizard = Actor(idle_imgs[0])
wizard.images = idle_imgs
wizard.scale = 1
wizard.right = WIDTH/2
wizard.bottom = HEIGHT-100
wizard.fps = 10

def update():
    zombie.animate()
    wizard.animate()
    

def draw():
    screen.clear()
    screen.draw.text(question,(WIDTH/3,HEIGHT/10),color='white',fontsize=60)
    screen.draw.text(typed,(WIDTH/3,HEIGHT/10),color='white',fontsize=60)
    zombie.draw()
    wizard.draw()

def on_key_down(key):
    global typed
    print(f'keycode:{key}')
    if key == keys.SPACE or key in range(97,122+1):
        typed += chr(key)
        if typed == question:
            typed=''

pgzrun.go()