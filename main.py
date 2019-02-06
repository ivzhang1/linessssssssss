from display import *
from draw import *

screen = new_screen()

# OCTANT 1 TEST
#color = [ 0, 255, 0 ]
# draw_line( 0, 0, 1000, 250, screen, color)
# draw_line( 0, 0, 1000, 500, screen, color)
# draw_line( 0, 0, 1000, 750, screen, color)
# draw_line( 0, 0, 1000, 1000, screen, color)

# OCTANT 2 TEST
color = [ 255, 0, 0 ]
draw_line( 0, 0, 250, 1000, screen, color)
draw_line( 0, 0, 500, 1000, screen, color)
draw_line( 0, 0, 750, 1000, screen, color)
draw_line( 0, 0, 10, 1000, screen, color)



display(screen)
save_extension(screen, 'img.png')
