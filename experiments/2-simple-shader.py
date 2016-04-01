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

    data = numpy.zeros(4, dtype=[("position", numpy.float32, 3),
                                 ("color", numpy.float32, 4)])

    buffer = gl.glGenBuffers(1)

    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer)
    gl.glBufferData(gl.GL_ARRAY_BUFFER, data.nbytes, data, gl.GL_DYNAMIC_DRAW)

    stride = data.strides[0]

    offset = ctypes.c_void_p(0)
    loc = gl.glGetAttribLocation(program, "position")
    gl.glEnableVertexAttribArray(loc)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer)
    gl.glVertexAttribPointer(loc, 3, gl.GL_FLOAT, False, stride, offset)

    offset = ctypes.c_void_p(data.dtype["position"].itemsize)
    loc = gl.glGetAttribLocation(program, "color")
    gl.glEnableVertexAttribArray(loc)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, buffer)
    gl.glVertexAttribPointer(loc, 4, gl.GL_FLOAT, False, stride, offset)


if __name__ == '__main__':
    with utils.initWindow():
        load_shader(VERT, FRAG)
