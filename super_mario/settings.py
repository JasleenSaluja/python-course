# general setup
TILE_SIZE = 64
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
ANIMATION_SPEED = 8

# editor graphics 
EDITOR_DATA = {
	0: {'style': 'player', 'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None, 'graphics': 'super_mario/graphics/player_1/idle_right'},
	1: {'style': 'sky',    'type': 'object', 'menu': None, 'menu_surf': None, 'preview': None, 'graphics': None},
	
	2: {'style': 'terrain', 'type': 'tile', 'menu': 'terrain', 'menu_surf': 'super_mario/graphics/menu/land_1.png',  'preview': 'super_mario/graphics/preview/land_1.png',  'graphics': None},
	3: {'style': 'water',   'type': 'tile', 'menu': 'terrain', 'menu_surf': 'super_mario/graphics/menu/water.png', 'preview': 'super_mario/graphics/preview/water.png', 'graphics': 'super_mario/graphics/terrain/water/animation'},
	
	4: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'super_mario/graphics/menu/gold.png',    'preview': 'super_mario/graphics/preview/gold.png',    'graphics': 'super_mario/graphics/items/gold'},
	5: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'super_mario/graphics/menu/silver.png',  'preview': 'super_mario/graphics/preview/silver.png',  'graphics': 'super_mario/graphics/items/silver'},
	6: {'style': 'coin', 'type': 'tile', 'menu': 'coin', 'menu_surf': 'super_mario/graphics/menu/diamond.png', 'preview': 'super_mario/graphics/preview/diamond.png', 'graphics': 'super_mario/graphics/items/diamond'},

	7:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'super_mario/graphics/menu/spikes.png',      'preview': 'super_mario/graphics/preview/spikes.png',      'graphics': 'super_mario/graphics/enemies/spikes'},
	8:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'super_mario/graphics/menu/zombie.png',       'preview': 'super_mario/graphics/preview/zombie.png',       'graphics': 'super_mario/graphics/enemies/zombie/idle'},
	9:  {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'super_mario/graphics/menu/shell_left.png',  'preview': 'super_mario/graphics/preview/shell_left.png',  'graphics': 'super_mario/graphics/enemies/shell_left/idle'},
	10: {'style': 'enemy', 'type': 'tile', 'menu': 'enemy', 'menu_surf': 'super_mario/graphics/menu/shell_right.png', 'preview': 'super_mario/graphics/preview/shell_right.png', 'graphics': 'super_mario/graphics/enemies/shell_right/idle'},
	
	11: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'super_mario/graphics/menu/small_fg.png', 'preview': 'super_mario/graphics/preview/small_fg.png', 'graphics': 'super_mario/graphics/terrain/palm/small_fg'},
	12: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'super_mario/graphics/menu/large_fg.png', 'preview': 'super_mario/graphics/preview/large_fg.png', 'graphics': 'super_mario/graphics/terrain/palm/large_fg'},
	13: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'super_mario/graphics/menu/left_fg.png',  'preview': 'super_mario/graphics/preview/left_fg.png',  'graphics': 'super_mario/graphics/terrain/palm/left_fg'},
	14: {'style': 'palm_fg', 'type': 'object', 'menu': 'palm fg', 'menu_surf': 'super_mario/graphics/menu/right_fg.png', 'preview': 'super_mario/graphics/preview/right_fg.png', 'graphics': 'super_mario/graphics/terrain/palm/right_fg'},

	15: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'super_mario/graphics/menu/small_bg.png', 'preview': 'super_mario/graphics/preview/small_bg.png', 'graphics': 'super_mario/graphics/terrain/palm/small_bg'},
	16: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'super_mario/graphics/menu/large_bg.png', 'preview': 'super_mario/graphics/preview/large_bg.png', 'graphics': 'super_mario/graphics/terrain/palm/large_bg'},
	17: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'super_mario/graphics/menu/left_bg.png',  'preview': 'super_mario/graphics/preview/left_bg.png',  'graphics': 'super_mario/graphics/terrain/palm/left_bg'},
	18: {'style': 'palm_bg', 'type': 'object', 'menu': 'palm bg', 'menu_surf': 'super_mario/graphics/menu/right_bg.png', 'preview': 'super_mario/graphics/preview/right_bg.png', 'graphics': 'super_mario/graphics/terrain/palm/right_bg'},
}

NEIGHBOR_DIRECTIONS = {
	'A': (0,-1),
	'B': (1,-1),
	'C': (1,0),
	'D': (1,1),
	'E': (0,1),
	'F': (-1,1),
	'G': (-1,0),
	'H': (-1,-1)
}

LEVEL_LAYERS = {
	'clouds': 1,
	'ocean': 2,
	'bg': 3,
	'water': 4,
	'main': 5
}

# colors 
SKY_COLOR = '#041E5A'
SEA_COLOR = '#75BDBC'
HORIZON_COLOR = '#0470A7'
HORIZON_TOP_COLOR = '#67BFC7'
LINE_COLOR = 'black'
BUTTON_BG_COLOR='#33323d'
BUTTON_LINE_COLOR='#f5f1de'