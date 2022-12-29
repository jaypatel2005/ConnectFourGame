RED = (255 , 0, 0)
DARK_RED = (139, 0, 0)
BLUE = (0, 0, 255)
LIME = (0, 255, 0)
GREEN = (0, 128, 0)
DARK_GREEN = (0, 100, 0)
YELLOW = (255, 255, 0)
GOLDEN = (255, 215, 0)
NAVY = (0, 0, 128)
PURPLE = (128, 0, 128)
LIGHT_GREEN = (144, 238, 144)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BROWN = (58, 29, 0)
BROWN = (164, 116, 73)
GREY = (128, 128, 128)
AQUA = (255, 255, 255)
PINK = (255, 0, 255)
ORANGE = (255, 165, 0)
LIGHT_BLUE = (173, 216, 230)
WHEAT = (245, 222, 179)
SILVER = (192, 192, 192)
DARK_BLUE = (0, 0, 139)
AZURE = (240, 255, 255)
CHOCOLATE = (210, 105, 30)

all_vars = dir()
all_colors = []

for var in all_vars:
    if not var.startswith('__'):
        all_colors.append(eval(var))

