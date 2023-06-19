from code.globals.constanst import EXIT_PROGRAM
from code.states.stateRule import StateRule
from code.states.menuState import MenuState
from code.states.Game.stateGameLevels import StateGameLevels

dict_name_status = {
    'Play': StateGameLevels,
    'Menu': MenuState,
    'Rules': StateRule,
    'Exit': EXIT_PROGRAM
}

