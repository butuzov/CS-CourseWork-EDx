# Note -> Logic in application isn't right.
# test cases ignore facts about white and black.
# everything in same number is treated as gray.




#This one is a challenge. There's a lot going on: splitting
#up strings, removing unnecessary characters, converting to
#integers, and running a big conditional. You can do it!
#
#In web development, it is common to represent a color like
#this:
#
#  rgb(red_val, green_val, blue_val)
#
#where red_val, green_val and blue_val would be substituted
#with values from 0-255 telling the computer how much to
#light up that portion of the pixel. For example:
#
# - rgb(255, 0, 0) would make a color red.
# - rgb(255, 255, 0) would make yellow, because it is equal
#   parts red and green.
# - rgb(0, 0, 0) would make black, the absence of all color.
# - rgb(255, 255, 255) would make white, the presence of all
#   colors equally.
#
#Don't let the function-like syntax here confuse you: here,
#these are just strings. The string "rgb(0, 255, 0)"
#represents the color green.
#
#Write a function called "find_color" that accepts a single
#argument expected to be a string as just described. Your
#function should return a simplified version of the color
#that is represented according to the following rules:
#
# If there is more red than any other color, return "red".
# If there is more green than any other color, return "green".
# If there is more blue than any other color, return "blue".
# If there are equal parts red/green, return "yellow".
# If there are equal parts red/blue, return "purple".
# If there are equal parts green/blue, return "teal".
# If there are equal parts red/green/blue, return "gray".


#Write your function here!
def find_color( rgb_string ):
    v_s = rgb_string.find("(")
    v_e = rgb_string.find(")")
    rgb = [int(v) for v in rgb_string[v_s+1:v_e].split(", ")];
    max_value = max(rgb);

    if rgb[0] == rgb[1] == rgb[2]:
        return 'gray'

    else:

        rgb = "".join(['ff' if color == max_value else '00' for color in rgb])
        RGBs = {
            'ff0000':'red',
            '00ff00':'green',
            '0000ff':'blue',

            'ff00ff':'purple',
            'ffff00':'yellow',
            '00ffff':'teal',

            'ffffff':'white',
            '000000':'black',
        }
        return RGBs[rgb]

#You can test your function with the cases below. If your
#code is working correctly, these should print "red",
#"purple", and "gray". Remember to comment these lines
#back out before submitting your code.
print(find_color("rgb(125, 50, 75)"))
print(find_color("rgb(125, 17, 125)"))
print(find_color("rgb(217, 217, 217)"))
