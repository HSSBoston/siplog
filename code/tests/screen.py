import board, displayio, busio, terminalio
from adafruit_display_text import label
from fourwire import FourWire
from adafruit_st7789 import ST7789

BORDER = 20
FONTSCALE = 2
BACKGROUND_COLOR = 0x00FF00  # Bright Green
FOREGROUND_COLOR = 0xAA0088  # Purple
TEXT_COLOR = 0xFFFF00

displayio.release_displays()
# dir(board)
spi = busio.SPI(clock=board.LCD_CLK,
                MOSI =board.LCD_MOSI)

# while not spi.try_lock():
#     pass
# spi.configure(baudrate=24000000) # Configure SPI for 24MHz
# spi.unlock()

display_bus = FourWire(spi, command=board.LCD_DC, chip_select=board.LCD_CS, reset=board.LCD_RST)
display = ST7789(display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53)

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(display.width - BORDER * 2, display.height - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = FOREGROUND_COLOR
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER)
splash.append(inner_sprite)


# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
    x=display.width // 2 - text_width // 2,
    y=display.height // 2,
)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

while True:
    pass