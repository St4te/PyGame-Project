from Earthworm import Earthworm
from Kirpich import *
from Pepelny_demon import Pepelny_demon
from qw1 import *
from qw2 import *
from qw3 import *
from qw4 import *
from random import randint

def get_enemy(enemy_id,  curse, artifacts, element):
    if enemy_id == 1:
        return Kirpich(curse, artifacts, element)
    if enemy_id == 2:
        return qw1(curse, artifacts, element)
    if enemy_id == 3:
        return qw2(curse, artifacts, element)
    if enemy_id == 4:
        return qw3(curse, artifacts, element)
    if enemy_id == 5:
        return qw4(curse, artifacts, element)
    if enemy_id == -1:
        return Pepelny_demon(curse, artifacts, element)
    if enemy_id == -2:
        return Earthworm(curse, artifacts, element)


def det_rand_enemy_id(a, is_boss):
    if not is_boss:
        b = randint(1, 5)
        while b in a:
            b = randint(1, 5)
        return b
    else:
        return randint(-2, -1)


