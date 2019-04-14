#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import floor
import sys

from PIL import Image, ImageOps

# CLI input parsing
line_length = int(sys.argv[1])
input_text = sys.argv[2].lower()

# Size formatting
print('Input analysis')
print('==============')
length_of_input = len(input_text)
print(f'Length of input: {length_of_input} characters.')
complete_lines = floor(length_of_input / line_length)
print(f'Complete lines: {complete_lines}.')
final_line_length = length_of_input % line_length
print(f'Final line length: {final_line_length} characters.')

# Image dimension calculation.
glyph_size = 400
width = glyph_size * line_length
print(f'Setting width to {width}.')

if final_line_length == 0:
    height = glyph_size * complete_lines
else:
    height = (glyph_size * complete_lines) + glyph_size
print(f'Setting height to {height}.')

# Create the image.
image = Image.new('RGBA', (width, height))

coords = [0, 0]
for character in input_text:
    if character == ' ':
        character = 'space'
    elif character == '.':
        character = 'period'
    elif character == ',':
        character = 'comma'
    elif character == ':':
        character = 'colon'
    elif character == ';':
        character = 'sim'

    glyph = Image.open(f'glyphs/{character}.png')

    image.paste(glyph, (coords[0], coords[1]))

    if coords[0] == width - glyph_size:
        coords[1] += glyph_size
        coords[0] = 0
    else:
        coords[0] += glyph_size

# Save the image.
image.save('output.png')
