"""Choose Your Own Adventure - Random Portal Edition!

The choices you make will either end the game immediately (-1),
cause you to pass through another portal to a random point in
the story (0), or advance you to the next level (1).
"""

import random
import textwrap


levels = [
    [
        """
        You find yourself in a room containing two portals
        leading to other worlds that are constantly transforming.
        You don't know how you got here, but you know you've
        never stepped through a portal before, so you just HAVE
        to find out what it's like!
        Which portal will you step through?
        """,
        [
            ('red', -1),
            ('blue', 0)
        ],
    ],
    [
        """
        The walls shift and unfold around you as a figure appears
        from another portal across the room. It welcomes you to the
        Mirror Dimension and warns you that things get a little
        "strange" around here.
        What will you do?
        """,
        [
            ('Make a run for the portal across the room.', 0),
            ('Try to snatch the fancy-looking ring from the person.', -1)
        ]
    ],
    [
        """
        You have divided by zero! The world is ending!
        """,
        """
        The evil mumble rapper takes over the world and drives
        people insane with his terrible rapping skills. You are
        now deaf.
        """,
        """
        The cake was a lie. Go find some real cake.
        """,
        """
        The ring glows, and suddenly you find yourself back at
        the beginning.
        """,
        """
        You tried to steal the wizard's ring and he blasted you
        with a fireball.
        """,
        """
        The last portal has dissipated. You have nowhere to go.
        """,
        """
        The evil weiner dog robots eat you alive on the other
        side of the matrix.
        """,
        """
        A loud snap is heard. Moments later, you don't feel so
        good as dust begins falling all around.
        """,
        """
        You are swallowed whole by a Demogorgon.
        """
    ]
]

level = 0
game_over = False
while not game_over:
    current_level = levels[0]
    # set the stage
    print(textwrap.dedent(current_level[0]))

    # present choices
    options = []
    for i, option in enumerate(current_level[1]):
        text, progress = option
        options.append(progress)
        print(f"{i}. {text}")

    # collect user's choice
    choice = int(input('Time to decide: '))

    # act based on the user's choice
    if options[choice] == -1:
        # end game
        print(random.choice(levels[-1]))
        game_over = True
    elif options[choice] == 0:
        # move on to a random level
        pass
    elif options[choice] == 1:
        # move on to the next level
        pass
    else:
        # an invalid option was entered
        print('I DON\'T THINK YOU UNDERSTAND...')
        continue

    # end the game
    game_over = True

print('THE END')
