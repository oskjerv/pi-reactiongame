from gpiozero import LED, Button
from gpiozero import Buzzer
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
from time import time
from random import randint
from random import choice
from string import ascii_letters
from string import digits

from os import _exit
import pygame
import writetodb
from writetodb import main_game
from writetodb import main_round


def get_random_string(length):
    # choise from all lowercase letters
    chars = ascii_letters + digits
    result_str = ''.join(choice(chars) for i in range(length))
    return result_str
    
game_id = get_random_string(15)

print(game_id)

# for pi setup and wiring, see Raspberry pi beginners guide page 144


pygame.init()

bell = pygame.mixer.Sound("/home/pi/gpio-music-box/elec_blip2.wav")

led = LED(4)
player2_button = Button(15)
player1_button = Button(14)

#buzzer = Buzzer(18)
buzzer = TonalBuzzer(18)

n_games = int(input("How many rounds do you want to play? "))
round = 0

player1_name = input("player1 player name is ")
player2_name = input("player2 player name is ")

player1_score = 0
player2_score = 0

reactiontime = 0

input("Press enter to start the game ...")

while n_games:
    round = round + 1
    n_games = n_games-1

    print(player1_name + " vs " + player2_name)
    print("Round " + str(round) + "/" + str(n_games))

    sleep(2)

    countdown = 3
    while countdown:
        print (countdown)
        #bell.play()
        #buzzer.beep(on_time = 1)
        buzzer.play(Tone(60))
        sleep(1)
        countdown -= 1
    print("Go!")

    led.on()
    light = randint(2, 15)
    sleep(light)
    led.off()
    
    start = time()
    
    while True:
        
        if player1_button.is_pressed:
            end = time()
            reactiontime = end - start
            main_round(game_id, round, light, 1, 0, reactiontime)
            
            print(player1_name + " vant!\n")
            player1_score = player1_score + 1
            sleep(1)
            print("Score: \n"+ player1_name + ":" + str(player1_score) + "\n" + str(player2_name) + ": " + str(player2_score) + "\n")
            sleep(1)
            break
        if player2_button.is_pressed:
            end = time()
            reactiontime = end - start
            
            main_round(game_id, round, light, 0, 1, reactiontime)
            print(player2_name + " vant!\n")
            player2_score = player2_score + 1 
            sleep(1)
            print("Score: \n"+ player1_name + ":" + str(player1_score) + "\n" + str(player2_name) + ": " + str(player2_score) + "\n")
            sleep(1)
            break
        
        

    #def pressed(button):
    #    if button.pin.number == 14:
    #        print(player1_name + " vant!")
    #    else:
    #       print(player2_name + " vant!")
    #    #_exit(0)
        
    #player2_button.when_pressed = pressed
    #player1_button.when_pressed = pressed
    
if player1_score > player2_score:
    print(player1_name + " wins " + str(player1_score) + ":" + str(player2_score))
if player1_score < player2_score:
    print(player2_name + " wins " + str(player1_score) + ":" + str(player2_score))
if player1_score == player2_score:
    print("Its a tie! Score: " + str(player1_score) + ":" + str(player2_score))

main_game(game_id, player1_name, player2_name, player1_score, player2_score, round)

_exit(0)

