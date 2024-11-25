# Author: Gabby Schwalm
import time

def print_dialogue(dialogue):
    for c in dialogue:
        print(c, end='', flush=True)
        time.sleep(0.05)
    print('')

def scene_zero():
    # expository dialouge
    line_1 = "Professor Quampbell: Hello and welcome! I am so glad you could make it."
    
    #
    print_dialogue(line_1)



if __name__ == "__main__":
    print("main start")
    scene_zero()
    print("main end")