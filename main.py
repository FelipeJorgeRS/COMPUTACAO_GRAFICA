def main():
# inicia GLFW
    if not glfw.init():
        return

# Confgura os hints
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint (glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

# cria a janela
window = glfw.create_window (900, 600, "Cubo Paramétrico", None, None)
if not window:
    glfw.terminate()
    return
glfw.set_window_pos (window, 560, 250) 


# cria o contexto
glfw.make_context_current(window)

# cor de fundo da janela
glClearColor (0.2, 1.0, 0.3, 1.0)

# cria o cubo
cube = Cube (1.0)

#carrega os shaders
shader = shaders.compileProgram(
shaders.compileShader (VERTEX SHADER, GL_VERTEX SHADER),
shaders.compileShader (FRAGMENT SHADER, GL_FRAGMENT_SHADER)
)
cube.set_shader(shader)

# ativa o teste de profundidade
glEnable (GL_DEPTH_TEST)

# Render loop
while not glfw.window_should_close(window):
    # limpa as cores do buffer de profundidade e de cor
    glClear(GL_COLOR_BUFFER_BIT | GL DEPTH_BUFFER_BIT)

    # Configura as matrizes de vizualização e projeção
    view = matrix44.create_from_translation (Vector3( [0.0, 0.0, -5.0]))
    projection = matrix44.create_perspective_projection_matrix(
        45.0, #FOV
        800/600, # Aspect ratio 0.1, # Near clipping plane
        100.0 # Far clipping plane
    )

    # configura a matriz do modelo
    model= matrix44.create_from_axis_rotation (Vector3(0.5, 1.0, 0.0]), glfw.get_time())

    # desenha o cubo
    cube.draw(model, view, projection)

    # troca os buffers e o poll de events
    glfw.swap_buffers(window)
    glfw.poll_events()

# Clean up
glfw.terminate()