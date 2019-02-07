from display import *
from draw import *
from subprocess import Popen, PIPE

screen = new_screen()

# Horizontal + Vertical Line Tests
color = [ 255, 255, 255 ]
draw_line( 250, -500, 250, 500, screen, color)
color = [ 255, 255, 0 ]
draw_line( -500, 250, 500, 250, screen, color)




# OCTANT 1,5 TEST
color = [ 0, 255, 0 ]
draw_line( 0, 0, 1000, 250, screen, color)
draw_line( 0, 0, 1000, 500, screen, color)

# OCTANT 2, 6 TEST
color = [ 255, 0, 0 ]
draw_line( 0, 0, 250, 1000, screen, color)
draw_line( 0, 0, 500, 1000, screen, color)

# OCTANT 3, 7 TEST
color = [0, 122, 255 ]
draw_line( 0, 500, 250,0, screen, color)
draw_line( 250, 500, 500,100, screen, color)

# OCTANT 4, 8 TEST
color = [ 255, 122, 0 ]
draw_line( 250, 500, 500, 0, screen, color)
draw_line( 0, 400, 500, 0, screen, color)



display(screen)
save_extension(screen, 'img.png')
# p = Popen( ['open', "img.png"], stdin=PIPE, stdout = PIPE )
# p.communicate()
