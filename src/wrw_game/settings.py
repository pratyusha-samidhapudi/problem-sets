"""
Game settings

"""

# general configuration
GAME_TITLE = "WARRIORS, ROBBERS AND WIZARDS GAME"

# initial settings
INITIAL_PLAYER_HEALTH = 5
INITIAL_ENEMY_LEVEL = 1

# score assignment options
SCORE_SUCCESS_ATTACK = 1
SCORE_ENEMY_DOWN = 5

# fight choices
WARRIOR = 1
ROBBER = 2
WIZARD = 3

# fight results
SUCCESS_ATTACK = WARRIOR - ROBBER, ROBBER - WIZARD, WIZARD - WARRIOR
FAILURE_ATTACK = WARRIOR - WIZARD, ROBBER - WARRIOR, WIZARD - ROBBER
SUCCESS = 1
FAILURE = -1
DRAW = 0

# messages
MSG_SUCCESS_ATTACK = "YOUR ATTACK IS SUCCESSFUL!"
MSG_SUCCESS_DEFENCE = "YOUR DEFENCE IS SUCCESSFUL!"
MSG_FAILURE_ATTACK = "YOUR ATTACK IS FAILED!"
MSG_FAILURE_DEFENCE = "YOUR DEFENCE HAS BEEN BREACHED!"
MSG_DRAW = "IT'S A DRAW!"
