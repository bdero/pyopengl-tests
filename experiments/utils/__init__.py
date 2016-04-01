import sys
from time import time

from contextlib import contextmanager
from vispy.gloo.context import FakeCanvas
import OpenGL.GL as gl
import OpenGL.GLUT as glut


clock = 0.0
initial_time = None
previous_time = None

display_callbacks = []
update_callbacks = []


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


def timer(fps):
    # Update the clock
    global previous_time, clock
    dt = time() - previous_time
    clock += dt
    previous_time = initial_time + clock

    for callback in update_callbacks:
        callback(dt)

    glut.glutTimerFunc(int(1000/fps), timer, fps)
    glut.glutPostRedisplay()


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

    global initial_time, previous_time
    initial_time = previous_time = time()

    glut.glutTimerFunc(int(1000/60), timer, 60)

    yield

    canvas = FakeCanvas()

    glut.glutMainLoop()
