import board, displayio, busio, terminalio, time
from fourwire import FourWire
from adafruit_st7789 import ST7789
from adafruit_display_text import label

BORDER = 20
FONTSCALE = 4
BACKGROUND_COLOR = 0x03FCC8  # light blue
FOREGROUND_COLOR = 0x305CDE  # blue
TEXT_COLOR = 0xFFFF00        # yellow

displayio.release_displays()
# print( dir(board) )
spi = busio.SPI(clock=board.LCD_CLK,
                MOSI =board.LCD_MOSI)
displayBus = FourWire(spi,
                      command=board.LCD_DC,
                      chip_select=board.LCD_CS,
                      reset=board.LCD_RST)
display = ST7789(displayBus,
                 rotation=270, width=240, height=135,
                 rowstart=40, colstart=53)
splash = displayio.Group()
display.root_group = splash

def init(demoMode=True):
    if demoMode:
        # Draw the outer most rectangle
        drawBackground(BACKGROUND_COLOR)
        
        # Draw a smaller inner rectangle
        innerBitmap = displayio.Bitmap(display.width - BORDER * 2, display.height - BORDER * 2, 1)
        innerPalette    = displayio.Palette(1)
        innerPalette[0] = FOREGROUND_COLOR
        innerSprite = displayio.TileGrid(innerBitmap,
                                         pixel_shader=innerPalette,
                                         x=BORDER, y=BORDER)
        splash.append(innerSprite)

        # Draw a label
        setText("Sip Log")
    else:
        # Draw the outer most rectangle
        drawBackground(0x000000)        
        
def drawBackground(colorHex):
    bgBitmap = displayio.Bitmap(display.width, display.height, 1)
    bgPalette    = displayio.Palette(1)
    bgPalette[0] = colorHex
    bgSprite = displayio.TileGrid(bgBitmap,
                                  pixel_shader=bgPalette,
                                  x=0, y=0)
    splash.append(bgSprite)

def setText(text):
    textArea = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
    width = textArea.bounding_box[2] * FONTSCALE
    textGroup = displayio.Group(
        scale=FONTSCALE,
        x=display.width // 2 - width // 2,
        y=display.height // 2,
    )
    textGroup.append(textArea)
    splash.append(textGroup)

def resetText(text):
    splash.pop(len(splash)-1)
    setText(text)
    
if __name__ == "__main__":
    init()
    time.sleep(3)
    init(demoMode=False)

