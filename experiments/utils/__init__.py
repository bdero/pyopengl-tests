import sys

from contextlib import contextmanager
from vispy.gloo.context import FakeCanvas
import OpenGL.GL as gl
import OpenGL.GLUT as glut


display_callbacks = []


def _display():
    gl.glClearColor(1, 1, 1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

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
    glut.glutInit(sys.argv)
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)

    glut.glutCreateWindow(title)
    glut.glutReshapeWindow(width, height)

    glut.glutReshapeFunc(_reshape)
    glut.glutDisplayFunc(_display)

    glut.glutKeyboardFunc(_keyboard)
    glut.glutMouseFunc(_mouse)

    yield

    canvas = FakeCanvas()

    glut.glutMainLoop()
