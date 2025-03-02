import machine, neopixel, rp2, time, random
width = 5
height = 5
num_leds = width * height
np = neopixel.NeoPixel(machine.Pin(16), num_leds)
random.seed(2345)

buffer = [[0 for i in range(width)] for j in range(height)]
cursor = 0
todo = 2

def newline_screen():
    global height, width, buffer, cursor, todo
    for i in range(height - 1):
        for j in range(width):
           buffer[j][height - i - 1] = buffer[j][height - i - 2]
    for k in range(width):
        buffer[k][0] = 0
    cursor = 0
    todo = random.randint(0, 5)
    time.sleep_ms(100)
    
def advance_screen():
    global todo, buffer, width, cursor
    if todo >= 1:
        buffer[width - cursor - 1][0] = 1
        cursor +=1
        todo -= 1
    if todo == 0:
        newline_screen()

def print_screen(r_t, g_t, b_t, r_c, g_c, b_c):
    global np, buffer, cursor, width, height
    for i in range(num_leds):
        if buffer[i%height][int(i/width)] == 1:
            np[i] = (g_t, r_t, b_t)
        else:
            np[i] = (0, 0, 0)
        np[width - cursor - 1] = (g_c, r_c, b_c)
    np.write()
    
while True:
    advance_screen()
    print_screen(0, 10, 0, 00 , 50, 00)
    time.sleep_ms(100)
