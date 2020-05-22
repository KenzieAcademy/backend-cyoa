"""Choose Your Own Adventure - Random Portal Edition!

The choices you make will either end the game immediately (-1),
cause you to pass through another portal to a random point in
the story (0), or advance you to the next level (1).
"""

import random
import textwrap


with open('levels.txt', 'r') as f:
    levels = eval(f.read())  # TODO: Unsafe! Refactor this!
with open('endgames.txt', 'r') as f:
    endgames = eval(f.read())  # TODO: Unsafe! Refactor this!

level = 0
game_over = False
while not game_over:
    current_level = levels[level]
    # set the stage
    print(textwrap.dedent(current_level['description']))

    # present choices
    options = []
    for i, option in enumerate(current_level['options']):
        text, progress = option
        options.append(progress)
        print(f"{i}. {text}")

    # collect user's choice
    choice = int(input('Time to decide: '))

    # act based on the user's choice
    if options[choice] == -1:
        # end game
        print(random.choice(endgames))
        game_over = True
    elif options[choice] == 0:
        # move on to a random level
        level = random.choice(range(1, len(levels)))
    elif options[choice] == 1:
        # move on to the next level
        level += 1
        if level == len(levels) - 1:
            print("Congratulations! You've made it to the end!")
            game_over = True
    else:
        # an invalid option was entered
        # TODO: create more messages to choose from randomly
        print('I DON\'T THINK YOU UNDERSTAND...')
        continue

print('THE END')
