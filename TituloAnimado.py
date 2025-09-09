import time
import sys

def animate_title(title):
    try:
        while True:
            for i in range(len(title)):
                animated_title = ''
                for j in range(len(title)):
                    if i == j:
                        animated_title += title[j].upper()
                    else:
                        animated_title += title[j].lower()
                print(animated_title, end='\r')
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nAnimación detenida por el usuario.")

title = input("Escribe algo cool: ")

animate_title(title)

