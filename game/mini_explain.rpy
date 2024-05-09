 

# Define la pantalla para mostrar la explicación de los controles del minijuego.
screen mini_clicker_explain():
    # Fondo
    add "images/explain_mini/explain_mini_clicker.jpg" xpos 0 ypos 0
    
    # Botón para continuar al minijuego
    textbutton "Continuar" action Hide("mini_clicker_explain")


screen mini_finder_explain():
    # Fondo
    add "images/explain_mini/explain_mini_finder.jpg" xpos 0 ypos 0
    
    # Botón para continuar al minijuego
    textbutton "Continuar" action Hide("mini_finder_explain")

screen mini_runner_explain():
    # Fondo
    add "images/explain_mini/explain_mini_runner.jpg" xpos 0 ypos 0
    
    # Botón para continuar al minijuego
    textbutton "Continuar" action Hide("mini_runner_explain")


screen mini_memory_explain():
    # Fondo
    add "images/explain_mini/explain_mini_memory.jpg" xpos 0 ypos 0
    
    # Botón para continuar al minijuego
    textbutton "Continuar" action Hide("mini_memory_explain")