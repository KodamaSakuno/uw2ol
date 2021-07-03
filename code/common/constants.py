# settings
DAEMON_MODE = True
SAVE_ON_CONNECTION_LOST = False
SET_ONLINE_TO_TRUE_ON_LOGIN = False
REMOTE_ON = False
DEVELOPER_MODE_ON = True
VERSION = 0.8

# in battle
THINK_TIME_IN_BATTLE = 30
MAX_STEPS_IN_BATTLE = 6

ENGAGE_RANGE = 1 # 1
ENGAGE_DAMAGE = 0.5 # 0.5

SHOOT_RANGE_IN_BATTLE = 4 # 4
SHOOT_DAMAGE = 1 # 1

ESCAPE_DISTANCE = 20
BATTLE_MOVE_TIME_INVERVAL = 0.2
NEXT_SHIP_TIME_INVERVAL = 0.3

# world configurables
CAPTION = 'Uncharted Waters 2 Online'
FPS = 30.0
FONT_SIZE = 16
CREW_UNIT_COST = 100
SUPPLY_UNIT_COST = 5
SUPPLY_CONSUMPTION_PER_PERSON = 0.1
ONE_DAY_AT_SEA_IN_SECONDS = 3
EXP_GOT_MODIFIER = 10
EXP_PER_DISCOVERY = 500
GOLD_REWARD_FOR_HANDING_IN_QUEST = 3000
MAX_LV = 60
PORTS_ALLIED_NATION_AND_PRICE_INDEX_CHANGE_INTERVAL_SECONDS = 60 * 120
MOVE_TIME_INVERVAL = 0.01
MAX_ITEMS_IN_BAG = 30

FLEET_COUNT_PER_NATION = 6
NATION_COUNT = 6
NPC_COUNT = 36

TIME_OF_DAY_OPTIONS = ['dawn', 'day', 'dusk', 'night']
PORT_COUNT = 130

DEFECT_COST = 200000
DEFECT_LV = 15
SUPPLY_LOW_ALERT_DAYS = 10
EACH_DAY_PASS = 1
SHIP_SPEED_CUT = 5
INVEST_MIN_INGOTS = 5

EASY_MODE_OVERIDE_RATIO = 2
HARD_MODE_OVERIDE_RATIO = 5

# tiles
WALKABLE_TILES = set(range(1, 40))
SAILABLE_TILES = set(range(1, 33))
WALKABLE_TILES_FOR_ASIA = set(range(1, 47))
PARTIAL_WORLD_MAP_TILES = 73
PARTIAL_WORLD_MAP_TILES_IN_ONE_DIRECTION = 36
PORT_TILES_COUNT = 96
GRID_TILES_COUNT = 13
TILES_AROUND_PORTS = [[2, 0], [2, 1], [2, -1], [-2, 0],
                      [-2, 1], [-2, -1],[0, 2], [1, 2],
                      [-1, 2], [0, -2], [1, -2], [-1, -2]]
THREE_NEARBY_TILES_OF_UP_LEFT_TILE = [[1, 0], [0, 1], [1, 1]]

WORLD_MAP_COLUMNS = 12 * 2 * 30 * 3
WORLD_MAP_ROWS = 12 * 2 * 45
WORLD_MAP_TILE_SIZE = 16
WORLD_MAP_X_LENGTH = WORLD_MAP_COLUMNS * WORLD_MAP_TILE_SIZE

WORLD_MAP_EDGE_LENGTH = 40

WORLD_MAP_MAX_Y_TO_DRAW_NEW_PARTIAL_WORLD_MAP = WORLD_MAP_TILE_SIZE * \
                                                (WORLD_MAP_ROWS - WORLD_MAP_EDGE_LENGTH)
WORLD_MAP_MIN_Y_TO_DRAW_NEW_PARTIAL_WORLD_MAP = WORLD_MAP_TILE_SIZE * WORLD_MAP_EDGE_LENGTH
WORLD_MAP_MIN_X_TO_DRAW_NEW_PARTIAL_WORLD_MAP = WORLD_MAP_TILE_SIZE * WORLD_MAP_EDGE_LENGTH
WORLD_MAP_MAX_X_TO_DRAW_NEW_PARTIAL_WORLD_MAP = WORLD_MAP_TILE_SIZE * \
                                                (WORLD_MAP_COLUMNS - WORLD_MAP_EDGE_LENGTH)

BATTLE_TILE_SIZE = 32
PORT_MAP_SIZE = 96 * 3

# pixels
WINDOW_WIDTH = 400 + 110*2
WINDOW_HIGHT = 400
BUTTON_WIDTH, BUTTON_HIGHT = 60, 30
SELECTION_LIST_WIDTH, SELECTION_LIST_HIGHT = 225 , 250
SELECTION_LIST_X, SELECTION_LIST_Y = WINDOW_WIDTH - SELECTION_LIST_WIDTH, 120

HUD_WIDTH, HUD_HIGHT = 110, 400
BUILDING_PERSON_WIDTH, BUILDING_PERSON_HIGHT = 138, 114
BUILDING_CHAT_WIDTH, BUILDING_CHAT_HIGHT = 480, 129
BUILDING_BG_SIZE = 500
SHIP_SIZE_IN_PIXEL = 32
PERSON_SIZE_IN_PIXEL = 32
FIGURE_WIDTH = 65
FIGURE_HIGHT = 81
ITEMS_IMAGE_SIZE = 49
PIXELS_COVERED_EACH_MOVE = 16
SHIP_DOT_SIZE = 2

# IDs
DOG_FRAME_1_INDEX = 28
DOG_FRAME_2_INDEX = 29
DOG_BUILDING_ID = 2

OLD_MAN_FRAME_1_ID = 26
OLD_MAN_FRAME_2_ID = 27
OLD_MAN_BUILDING_ID = 5

AGENT_FRAME_1_ID = 24
AGENT_FRAME_2_ID = 25
AGENT_BUILDING_ID = 1

TAX_FREE_PERMIT_ID = 10
EXPENSIVE_EQUIPMENTS_IDS = {36, 37, 42, 43, 48}


# network
HOST = 'localhost'
PORT = 8082
REMOTE_HOST = '175.27.138.5'
REMOTE_PORT = 8082
HEADER_SIZE = 4
OBJECT_SIZE = 4

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 69, 0)
CRIMSON = (139, 0, 0)
BLUE = (0,0,128)
TRANS_GRAY = (50, 50, 50, 35)
TRANS_BLANK = (0, 0, 0, 0)

if __name__ == '__main__':
    print(SAILABLE_TILES)