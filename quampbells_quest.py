# Author: Gabby Schwalm
import time

def print_dialogue(dialogue: str, speed: int):
    for c in dialogue:
        print(c, end='', flush=True)
        time.sleep(speed)
    print('')

def scene_zero():
    print("You are in Presser Hall because you recieved an email from Professor Quampbell asking if you could help him with something.")
    time.sleep(4)
    print("You are waiting outside of his office on the second floor.")
    print("You admire his poster of conductors and wondering how some of those positions could be possible when . . . ")
    time.sleep(4)
    print("")

    # expository dialouge
    prof_quampbell = "Professor Quampbell: "
    pq_line_1 = "Hello and welcome! I am so glad you could make it."
    pq_line_2 = "I wanted to program a new piece for this upcoming cycle, but the parts are pretty difficult."
    pq_line_3 = "I asked different faculty to take a look at the parts and give me their thoughts."
    pq_line_4 = "I forgot that I need to bring the music with me on my trip to conduct the Hawaii-Alaska Biannual Youth Band!"
    pq_line_5 = "Could you do me a favor and gather the different parts and bring them back to my office before my flight tomorrow?"
    pq_line_6 = "I would do it myself, but I have a meeting with the President to discuss where we will erect the statue of Dr. Ponce"
    pq_line_7 = "Thanks!"
    
    # output dialogue
    print(prof_quampbell, end='')
    print_dialogue(pq_line_1, 0.05)
    time.sleep(0.5)
    print(prof_quampbell, end='')
    print_dialogue(pq_line_2, 0.05)
    time.sleep(0.5)
    print(prof_quampbell, end='')
    print_dialogue(pq_line_3, 0.05)
    time.sleep(0.5)
    print(prof_quampbell, end='')
    print_dialogue(pq_line_4, 0.05)
    time.sleep(0.5)
    print(prof_quampbell, end='')
    print_dialogue(pq_line_5, 0.05)
    time.sleep(0.5)
    print(prof_quampbell, end='')
    print_dialogue(pq_line_6, 0.05)
    time.sleep(0.5)
    print(prof_quampbell, end='')
    print_dialogue(pq_line_7, 0.05)


if __name__ == "__main__":
    # introduction to game
    print("Welcome to Quampbells Quest! - a text based adventure game\n")
    time.sleep(1)
    print_dialogue("Scene one: \n", 0.2)
    time.sleep(0.5)

    scene_zero()
