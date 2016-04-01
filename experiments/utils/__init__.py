import sys

from contextlib import contextmanager
import OpenGL.GL as gl
import OpenGL.GLUT as glut


display_callbacks = []


def _display():
    for callback in display_callbacks:
        callback()
    glut.glutSwapBuffers()


def _reshape(width, height):
    gl.glViewport(0, 0, width, height)


def _keyboard(key, x, y):
    # CTRL+C or ESCAPE
    if key in [b'\x03', b'\x1b']:
        sys.exit()


def _mouse(button, state, x, y):
    if button == glut.GLUT_LEFT_BUTTON:
        if not state:
            print('Mouse clicked')
        else:
            print('Mouse released')


@contextmanager
def init_window(width=1600, height=900, title='OpenGL'):
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)

    glut.glutCreateWindow(title)
    glut.glutReshapeWindow(width, height)

    glut.glutReshapeFunc(_reshape)
    glut.glutDisplayFunc(_display)

    glut.glutKeyboardFunc(_keyboard)
    glut.glutMouseFunc(_mouse)

    yield

    glut.glutMainLoop()


def build_program(vertex_string, fragment_string):
    program = gl.glCreateProgram()

    vertex = gl.glCreateShader(gl.GL_VERTEX_SHADER)
    fragment = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)

    gl.glShaderSource(vertex, vertex_string)
    gl.glShaderSource(fragment, fragment_string)

    gl.glCompileShader(vertex)
    gl.glCompileShader(fragment)

    gl.glAttachShader(program, vertex)
    gl.glAttachShader(program, fragment)
    gl.glLinkProgram(program)

    gl.glDetachShader(program, vertex)
    gl.glDetachShader(program, fragment)

    return program
