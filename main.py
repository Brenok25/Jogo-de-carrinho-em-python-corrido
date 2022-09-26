import timeit
import random
import time

from ursina import *

app = Ursina()
camera.orthographic = True
camera.fov = 10

def action():
    b = Button(scale=(.5, .25), text=' Presta atenção na estrada boy')
    destroy(b, delay=0.7)

def action2():
    b = Button(scale=(.5, .25), text=' Se me atacr eu vou atacar ')
    destroy(b, delay=0.7)


#cria o  carro
car = Entity(
    model='quad',
    texture='./hero.png',
    collider='box',
    scale=(2, 1),
    rotation_z=-90,
    on_click=action
)

road1 = Entity(
    model='quad',
    texture='./finali',
    scale=15,
    z=1
)
road2 = duplicate(road1, y=15)
pair = [road1, road2]

morte = ['Você morreu dolorosamente',
         'Papai do céu ama papai do céu leva',
         'Tu é ruim até aqui boy',
         'Num joguinho facil desse?',
         'Um beijo da Anita',
         'Vlw flw',
         'Não siga a luz']
frase = random.choice(morte)


enemies = []
import random
def newEnemy():
    val = random.uniform(-7,7) #onde os carros spawnan distancia e tals
    new = duplicate(
        car,
        texture='./enemy2.png',
        x = 1*val,
        y = 20, #distancia q eles spawnam ou seja q demora pra aparecer na tela
        color = color.random_color(),
        on_click=action2,
        rotation_z=
        90 if val < 0
            else -90
    )
    enemies.append(new)
    invoke(newEnemy, delay=0.5)
newEnemy()

#faz mexer
def update():
    car.x -=held_keys['a']*5*time.dt
    car.x += held_keys['d']*5*time.dt

    for road in pair:
        road.y -= 6*time.dt
        if road.y < -15:
            road.y +=30
    for enemy in enemies:
        if enemy.x <0:
            enemy.y -= 10*time.dt #velocidade dos inimigos
        else:
            enemy.y -= 5*time.dt
        if enemy.y <-10:
            enemies.remove(enemy)
            destroy(enemy)


    if car.intersects().hit:
        #car.shake()
        if frase == 'Papai do céu ama papai do céu leva':
            b = Button(scale=(.5, .25), text=frase)
            destroy(b, delay=1)
            destroy(car, delay=2)

        else:
            b = Button(scale=(.5, .25), text=frase)
            destroy(b, delay=1)
            destroy(car, delay=1)


app.run()