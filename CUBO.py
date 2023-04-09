import glfw
from OpenGL.GL import *
from OpenGL.GL import shaders
from pyrr import matrix44
from pyrr import Vector3
import numpy as np

VERTEX_SHADER = """
#version 330 core
layout (location = 0) in vec3 position;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main()
{
    gl_Position = projection * view model * vec4(position, 1.0f);
}
""" 
FRAGMENT_SHADER = """
#version 330 core
out vec4 color;

void main()
{
color = vec4(1.0f, 1.0f, 1.0f, 1.0f);
}
"""

class VECTOR3:
    def init_(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
class MATRIX44:
    def _init__(self, m=None):
        if m is None:
            self.m = np.identity(4, dtype=np.float32)
        else:
            self.m = np.array(m, dtype=np.float32)
    
    def mul (self, other):
        return MATRIX44(np.dot(self.m, other.m))
    
    def translate(self, x, y, z):
        m- np.identity(4, dtype-np.float32)
        m[0, 3] = x
        m[1, 3] = y
        m[2, 3] = z
        self.m np.dot(self.m, m)

def rotate(self, angle, x, y, z):
    c =np.cos(angle)
    s = np.sin(angle)
    norm =np.sqrt(x*x + y*y + z*2)
    x /= norm
    y /= norm
    z /= norm

    m = np.identity(4, dtype= np.float32)
    m[0, 0] = x*x*(1-c)+c
    m[0, 1] = x*y*(1-c)-z*s
    m[0,2] = x*z*(1-c)+y*s
    m[1, 0] = y*x*(1-c)+z*5
    m[1, 1] = y*y*(1-c)+c
    m[1, 2] = y*z*(1-c)-x*5
    m[2, 0] = x*z*(1-c)-y*s
    m[2, 1] = y*z*(1-c)+x*s
    m[2,2] = z*z*(1-c)+c
    self.m = np.dot(self.m, m)


    def scale(self, x, y, z):
        m = np.identity(4, dtype=np.float32)
        m[0, 0] = x
        m[1, 1] = y
        m[2,2] = z
        self.m = np.dot(self.m, m)
class Cube:
    def __init__(self, size):
        self.vertices= np.array([
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ], dtype=np.float32) * size / 2
        
    self. indices = np.array([
        [0, 1, 2],
        [2, 3, 0],
        [1, 5, 6],
        [6, 2, 1],
        [7, 6, 5],
        [5, 4, 7],
        [4, 0, 3],
        [3, 7, 4],
        [4, 5, 1],
        [1, 0, 4],
        [3, 2, 6],
        [6, 7, 3]
        ], dtype=np. uint32)
    
        self.vao = g1GnVertexArrays (1)
        glBindVertexArray(self.vao)

        self.vbo glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL FALSE, 0, None)
        glEnableVertexAttribArray(0)


        self.ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)

        glBindVertexArray(0)

    def draw(self, model, view, projection):
        glUseProgram(self.shader)

        elUniformMatrix4fv(glGetUniformLocation(self.shader, "model"), 1, GL_FALSE, model)
        glUniformMatrix4fv(glGetUniformLocation(self.shader, "view"), 1, GL_FALSE, view)
        glUniformMatrix4fv(glGetUniformLocation(self.shader, "projection"), 1, GL_FALSE, projection)

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, len(self.indices) * 3, GL_UNSIGNED INT, None)
        glBindVertexArray(0)

        def set_shader(self, shader):
        self.shader = shader