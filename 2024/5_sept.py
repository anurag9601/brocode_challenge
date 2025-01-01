#Problem 1
# color_invert((255, 255, 255)) ➞ (0, 0, 0)
# (255, 255, 255) is the color white.
# The opposite is (0, 0, 0), which is black.
# color_invert((0, 0, 0)) ➞ (255, 255, 255)
# color_invert((165, 170, 221)) ➞ (90, 85, 34)
#note
# Must return a tuple.
# 255 is the max value of a single color channel.

#Solution 1
def color_invert(color):
    a,b,c = color
    inverted_color = (255 - a, 255 - b, 255 - c)
    return inverted_color
  
