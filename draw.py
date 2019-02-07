from display import *

def draw_line( x0, y0, x1, y1, screen, color ):


    a = (y1-y0)
    b = -1 * (x1-x0)

    if(y0 <= y1):
        if(abs(a) <= abs(b)): # IF dy <= dx, slope <= 1
            #Octant I, V
            d = 2*a+b

            while x0 <= x1:

                #PLOT
                plot(screen, color, x0, y0)
                if d > 0:
                    y0+=1
                    d += 2*b

                x0+=1
                d += 2*a
        else:

            #Octant II, VI
            d = a+2*b

            while y0 <= y1:

                #PLOT
                plot(screen, color, x0, y0)
                if d < 0:
                    x0+=1
                    d += 2*a

                y0+=1
                d += 2*b

    else:
        if(abs(a) <= abs(b)): # IF dy <= dx, slope <= 1
            #Octant IV, VIII
            d = 2*a-b

            while x0 <= x1:

                #PLOT
                plot(screen, color, x0, y0)
                if d < 0:
                    y0-=1
                    d -= 2*b

                x0+=1
                d += 2*a
        else:
            #Octant III, VII
            d = a-2*b

            while y0 >= y1:

                #PLOT
                plot(screen, color, x0, y0)
                if d > 0:
                    x0+=1
                    d += 2*a

                y0-=1
                d -= 2*b
