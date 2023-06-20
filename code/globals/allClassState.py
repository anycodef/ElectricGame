from code.globals.constanst import EXIT_PROGRAM
from code.states.stateRule import StateRule
from code.states.menuState import MenuState
from code.states.Game.stateGameLevels import StateGameLevels
from code.states.Game.Level1.Level1 import StateLevel1

dict_name_status = {
    'Play': StateLevel1,
    'Levels': StateGameLevels,
    'Menu': MenuState,
    'Rules': StateRule,
    'Exit': EXIT_PROGRAM
}

