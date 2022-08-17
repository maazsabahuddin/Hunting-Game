# Local imports
import config

# Python imports
import time


LINE_BY_LINE = False


def map_view():
    print("===============\t\t\t=====================\t\t\t=================")
    print("=\t\t\t  = = = = = =\t  Hill Top\t\t= = = = = = =\t\t\t\t=")
    print("=\t\t\t  =\t\t\t=\t(Fire Weapon)\t=\t\t\t=\t\t\t\t=")
    print("=\t\t\t  =\t\t\t=====================\t\t\t=\t\t\t\t=")
    print("=\t\t\t  =\t\t\t\t\t\t\t\t\t\t\t=\t\t\t\t=")
    print("=\t\t\t  =\t\t\t=====================\t\t\t=\t\t\t\t=")
    print("=\t\t\t  = = = = = =\t  Forest\t\t= = = = = = =\t\t\t\t=")
    print("=\tVillage\t  =\t\t\t=\t(Health Kit)\t=\t\t\t=\tValley\t\t=")
    print("=\t\t\t  =\t\t\t=====================\t\t\t=\t(Tiger)\t\t=")
    print("=\t\t\t  =\t\t\t\t\t\t\t\t\t\t\t=\t\t\t\t=")
    print("=\t\t\t  =\t\t\t=====================\t\t\t=\t\t\t\t=")
    print("=\t\t\t  = = = = = =\t  River Side\t= = = = = = =\t\t\t\t=")
    print("=\t\t\t  =\t\t\t=\t(Water & Map)\t=\t\t\t=\t\t\t\t=")
    print("===============\t\t\t=====================\t\t\t=================")


def story_opinion_message():
    print("="*73)
    print(f"{'='}\t\t\t\t\t\tTHIS IS A STORY BASED GAME\t\t\t\t\t\t{'='}")
    print("=" * 73)


def story_end_message():
    print("\n")
    print("="*65)
    print(f"{'='}\t\t\t\t\t\t\t GAME ENDS \t\t\t\t\t\t\t{'='}")
    print("=" * 65)


def start_of_story():
    if LINE_BY_LINE:
        for key in config.INITIAL_MESSAGE:
            print(key, end='')
            time.sleep(0.035)
    else:
        print(config.INITIAL_MESSAGE)


def instructions_of_story():

    if LINE_BY_LINE:
        for key in config.INSTRUCTION_MESSAGE:
            print(key, end='')
            time.sleep(0.035)
    else:
        print(config.INSTRUCTION_MESSAGE)


def pickup_options():
    if LINE_BY_LINE:
        for key in config.OPTIONS_MESSAGE:
            print(key, end='')
            time.sleep(0.035)
    else:
        print(config.OPTIONS_MESSAGE)


def location_choice():
    if LINE_BY_LINE:
        for key in config.LOCATION_MESSAGE:
            print(key, end='')
            time.sleep(0.035)
    else:
        print(config.LOCATION_MESSAGE)
