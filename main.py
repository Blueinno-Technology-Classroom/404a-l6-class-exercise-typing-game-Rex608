import pgzrun, random
from pgzhelper import*

WIDTH = 1000
HEIGHT = 800

zombiie_run = ['zombies/run/tile002','zombies/run/tile003','zombies/run/tile004','zombies/run/tile005']
zombie = Actor(zombiie_run[0])
zombie.fps = 10
zombie.images = zombiie_run
zombie.scale = 5
zombie.right = WIDTH
zombie.bottom = HEIGHT-200
question = 'hello'
typed=''

wizard_idle = ['wizard/idle/tile000','wizard/idle/tile001','wizard/idle/tile002','wizard/idle/tile003','wizard/idle/tile004','wizard/idle/tile005']
wizard = Actor(wizard_idle[0])
wizard.images = wizard_idle
wizard.scale = 2
wizard.left = -100
wizard.bottom = HEIGHT-100
wizard.fps = 10

wizard_die = ['wizard/death/tile000','wizard/death/tile001','wizard/death/tile002','wizard/death/tile003','wizard/death/tile004','wizard/death/tile005','wizard/death/tile006']
wizard_attack = ['wizard/attack/tile000','wizard/attack/tile001','wizard/attack/tile002','wizard/attack/tile003','wizard/attack/tile004','wizard/attack/tile005','wizard/attack/tile006','wizard/attack/tile007']
zombie_die = ['zombies/die/tile014','zombies/die/tile015','zombies/die/tile016','zombies/die/tile017','zombies/die/tile018','zombies/die/tile019','zombies/die/tile020','zombies/die/tile021','zombies/die/tile022','zombies/die/tile023','zombies/die/tile024',]
def update():
    zombie.animate()
    wizard.animate()
    if zombie.image not in zombie_die:
        zombie.x -=1
    if zombie.image == zombie_die[-1]:
        zombie.images = zombiie_run
        reset()
    if wizard.image == wizard_die[-1] or wizard.image == wizard_attack[-1]:
        wizard.images = wizard_idle
    if zombie.collide_pixel(wizard):
        wizard.images = wizard_die
        reset()
    

def draw():
    screen.clear()
    screen.draw.text(question,(100,HEIGHT/10),color='white',fontsize=60)
    screen.draw.text(typed,(100,HEIGHT/10),color='orange',fontsize=60)
    zombie.draw()
    wizard.draw()

def on_key_down(key):
    global typed
    print(f'keycode:{key}')
    if key == keys.SPACE or key in range(97,122+1):
        typed += chr(key)
        if typed == question:
            wizard.images = wizard_attack
            zombie.images = zombie_die
    elif key == 8:
        typed = typed[:-1]

def reset():
    global typed, question
    zombie.right = WIDTH
    typed = ''
    rand_question()


def rand_question():
    global question
    num_of_text = random.randint(1,3)
    question = ''
    for i in range(num_of_text): 
        num_of_char = random.randint(2,10)
        for j in range(num_of_char):
            question += random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        question += ' '


pgzrun.go()