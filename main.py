#!/usr/bin/env python3
from __future__ import annotations

import tcod.console
import tcod.context
import tcod.event
import tcod.tileset

from engine import Engine
from entity import Entity
from input_handlers import EventHandler

def main() -> None:
    """Show "Hello World" until the window is closed."""

    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "Alloy_curses_12x12.png",
        columns=16,
        rows=16,
        charmap=tcod.tileset.CHARMAP_CP437,
    )
    tcod.tileset.procedural_block_elements(tileset=tileset)

    event_handler = EventHandler()
    
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    console = tcod.console.Console(screen_width, screen_height)
    console.print(
        0, 0, "Hello World"
    )  # Test text by printing "Hello World" to the console
    with tcod.context.new(console=console, tileset=tileset) as context:
        while True:  # Main loop
            engine.render(console=console, context=context)
            #context.present(console)  # Render the console to the window and show it
            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
