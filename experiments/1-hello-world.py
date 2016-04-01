#!/usr/bin/python3

import sys

import OpenGL.GL as gl
import OpenGL.GLUT as glut


def display():
    glut.glutSwapBuffers()


def reshape(width, height):
    gl.glViewport(0, 0, width, height)


def keyboard(key, x, y):
    print(key, x, y)
    if key in [b'\x03', b'\x1b']:
        sys.exit()


if __name__ == '__main__':
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA)
    glut.glutCreateWindow("Hello world")
    glut.glutReshapeWindow(1600, 900)

    glut.glutReshapeFunc(reshape)
    glut.glutDisplayFunc(display)
    glut.glutKeyboardFunc(keyboard)

    glut.glutMainLoop()
