# Graphical parameters
GAME_TITLE = "Crypto Casino"
WINDOW_HEIGHT = 1024
WINDOW_WIDTH = 1280
WHEEL_DIAMETER = 950
WHEEL_RADIUS = WHEEL_DIAMETER/2
WHEEL_SHIFT = (WINDOW_HEIGHT - WHEEL_DIAMETER)/2
ARROW_SIDE = 50

POCKET_BUTTON_WIDTH = 55
POCKET_BUTTON_HEIGHT = 35
BET_BUTTON_WIDTH = 55
BET_BUTTON_HEIGHT = 55

# Images
IMAGE_MAIN_MENU = "images/accueil.png"
IMAGE_FOND_CASINO = "images/casino.png"
IMAGE_FOND_ROULETTE = "images/fondbleu.png"
IMAGE_FOND_SIDEMENU = "images/tapis.png"
IMAGE_WHEEL = "images/BruceWheelis.png"
IMAGE_ARROW = "images/arrow.png"
IMAGE_LAUNCHBUTTON = "images/spin.png"
IMAGE_GAME_OVER = "images/gameover.png"

IMAGES_BUTTONS_NORMAL = ["images/{}.png".format(i) for i in range(16)]
IMAGES_BUTTONS_CLICKED = ["images/{}down.png".format(i) for i in range(16)]
IMAGES_MISES_NORMAL = ["images/jeton{}.png".format(i) for i in [10, 20, 50, 100]]
IMAGES_MISES_CLICKED = ["images/jeton{}light.png".format(i) for i in [10, 20, 50, 100]]
