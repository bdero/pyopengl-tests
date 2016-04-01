#!/usr/bin/python3

import numpy
import OpenGL.GL as gl
from vispy.gloo import Program

import utils


VERT = """
uniform float scale;
attribute vec2 position;
attribute vec4 color;
varying vec4 v_color;

void main()
{
    gl_Position = vec4(position*scale, 0.0, 1.0);
    v_color = color;
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
    with utils.init_window(title='Simple shader'):
        program = Program(VERT, FRAG, count=4)
        program['color'] = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1), (1, 1, 0, 1)]
        program['position'] = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
        program['scale'] = 1.0

        def render():
            program.draw(gl.GL_TRIANGLE_STRIP)
        utils.display_callbacks.append(render)

        def update(dt):
            program['scale'] = (1.5 + numpy.cos(utils.clock))/4.0
        utils.update_callbacks.append(update)
