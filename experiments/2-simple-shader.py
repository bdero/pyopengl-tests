#!/usr/bin/python3

import utils


VERT = """
uniform float scale;
attribute vec2 position;
attribute vec4 color;
void main()
{
    gl_Position = vec4(position*scale, 0.0, 1.0);
}
"""

FRAG = """
varying vec4 v_color;

void main()
{
    gl_FragColor = v_color;
}
"""


if __name__ == '__main__':
    utils.initWindow()
    utils.build_program(VERT, FRAG)
