#!/usr/bin/python3

import ctypes
import numpy
import OpenGL.GL as gl

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


def load_shader(vertex, fragment):
    program = utils.build_program(vertex, fragment)
    gl.glUseProgram(program)

    data = numpy.zeros(4, dtype=[("position", numpy.float32, 2),
                                 ("color", numpy.float32, 4)])

    buffer = gl.glGenBuffers(1)

    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer)
    gl.glBufferData(gl.GL_ARRAY_BUFFER, data.nbytes, data, gl.GL_DYNAMIC_DRAW)

    stride = data.strides[0]

    offset = ctypes.c_void_p(0)
    loc = gl.glGetAttribLocation(program, "position")
    gl.glEnableVertexAttribArray(loc)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer)
    gl.glVertexAttribPointer(loc, 2, gl.GL_FLOAT, False, stride, offset)

    offset = ctypes.c_void_p(data.dtype["position"].itemsize)
    loc = gl.glGetAttribLocation(program, "color")
    gl.glEnableVertexAttribArray(loc)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer)
    gl.glVertexAttribPointer(loc, 4, gl.GL_FLOAT, False, stride, offset)

    loc = gl.glGetUniformLocation(program, "scale")
    gl.glUniform1f(loc, 1.0)

    data['color'] = [(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1), (1, 1, 0, 1)]
    data['position'] = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]


if __name__ == '__main__':
    with utils.init_window():
        load_shader(VERT, FRAG)

        def render():
            gl.glClear(gl.GL_COLOR_BUFFER_BIT)
            gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        utils.display_callbacks.append(render)
