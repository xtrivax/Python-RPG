import time

sleep = time.sleep

def printstory(story, delay=None):
    """
    Splits text into ines and then prints them with a delay if given one.

    """
    lines = story.split("\n")

    for individual_line in lines:
        print(individual_line)

        if delay:
            sleep(delay)