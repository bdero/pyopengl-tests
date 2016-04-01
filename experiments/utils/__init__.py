import sys

import OpenGL.GL as gl
import OpenGL.GLUT as glut


def display_callback():
    glut.glutSwapBuffers()


def reshape_callback(width, height):
    gl.glViewport(0, 0, width, height)


def keyboard_callback(key, x, y):
    # CTRL+C or ESCAPE
    if key in [b'\x03', b'\x1b']:
        sys.exit()


def mouse_callback(button, state, x, y):
    if button == glut.GLUT_LEFT_BUTTON:
        if not state:
            print('Mouse clicked')
        else:
            print('Mouse released')


def initWindow(width=1600, height=900, title='OpenGL'):
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)

    glut.glutCreateWindow(title)
    glut.glutReshapeWindow(width, height)

    glut.glutReshapeFunc(reshape_callback)
    glut.glutDisplayFunc(display_callback)

    glut.glutKeyboardFunc(keyboard_callback)
    glut.glutMouseFunc(mouse_callback)

    glut.glutMainLoop()
