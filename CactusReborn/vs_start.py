﻿"""
vs-start.py

This is just a small helper file, to ensure that the
project will actually build and run in Visual Studio.
This file will not be included in the releases. This
is also where tests of the library will be performed.

FYI: I'm choosing to be explicity with the name
references, but in reality you only need to prefix
class/function names with "cactus".
"""
import sys
import cactus


FLOWCHART = cactus.game_flowchart.GameFlowchart(
    locations={
        "start": cactus.location.Location(
            title="The Shire",
            description_enter="As you enter the Shire, you are surrounded by the endless rolling hills.",
            description_exit="As you leave the Shire, you look back and wish that you could stay longer.",
            on_exit_function=None,
            locations={
                "mordor": "mordor",
                "laketown": "laketown"
            }
        ),
        "mordor": cactus.location.Location(
            title="Mordor",
            description_enter="As you enter Mordor, the Dark Lord Sauron spots you and kills you.",
            description_exit="As you pass out of Arda, you reflect on your bad decision.",
            on_exit_function=sys.exit,
            locations={}
        ),
        "laketown": cactus.location.Location(
            title="Laketown",
            description_enter="As soon as you enter Laketown, you realize that there is no Laketown.",
            description_exit="You leave Laketown, disappointed.",
            on_exit_function=sys.exit,
            locations={}
        )
    }
)

cactus.main_game.play_game(
    name="LOTR Quest",
    description="Some dumb LOTR quest.",
    prompt="> ",
    flowchart=FLOWCHART,
    case_sensitive=False,
    error_message="Enter the correct input!",
    global_commands={
        "exit": sys.exit
    }
)