#===========================================================================================
#===EL JARDIN
#===========================================================================================
label auto_chapter_save:
    $ renpy.take_screenshot()
    $ renpy.save(renpy.newest_slot(), save_name)
    return
# Declara los personajes usados en el juego como en el ejemplo:

define car = Character("Carmen", color="#aa2525")
define carp = Character("Pensamientos de Carmen", color="#aa2525")
define papa = Character("Papá", color="#007a33")
define raul = Character("Don Raul", color="#000000")
define mama = Character("Mamá", color="#7108ad")
define m_raul = Character("Ex-mujeres de Don Raul", color="#666666")
define hermanos = Character("Hermanos de Carmen", color="#d44706")
define tia = Character("Tia", color="#22a707")
define alvaro = Character("Alvaro", color="#7861ca")
define cura = Character("Cura", color="#a19100")
define chofer= Character("Chofer", color="#424242")
define burro = Character("El Burro", color="#498daf")
define d_finca = Character("Dueña de la finca", color="#224422")

# El juego comienza aquí.

label start:
    camera:
        perspective True
#Primera parte
    #Acto 1, de la primera parte
    call p1_a1 from _call_p1_a1
    #Acto 2, de la primera parte
    call p1_a2 from _call_p1_a2
    #Acto 3, de la primera parte
    call p1_a3 from _call_p1_a3
    #Minijuego clicker
    window hide
    show screen mini_clicker_explain
    pause
    hide screen mini_clicker_explain
    call mini_clicker from _call_mini_clicker
    call mini_clicker_win from _call_mini_clicker_win
    
    
    
    #Acto 4, de la primera parte
    call p1_a4 from _call_p1_a4
    #Acto 5, de la primera parte
    call p1_a5 from _call_p1_a5
    #Acto 6, de la primera parte
    call p1_a6 from _call_p1_a6

#Segunda parte
    #Acto 1, de la segunda parte
    call p2_a1 from _call_p2_a1
    #Minijuego de buscar el objeto
    window hide
    show screen mini_finder_explain
    pause
    hide screen mini_finder_explain
    call mini_finder from _call_mini_finder
  
    #Acto 2, de la segunda parte
    call p2_a2 from _call_p2_a2
    #Acto 3, de la segunda parte
    call p2_a3 from _call_p2_a3
    #Acta 4, de la segunda parte
    call p2_a4 from _call_p2_a4

#Tercera parte
    #Acto 1, de la tercera parte
    call p3_a1 from _call_p3_a1
    #Minijuego carrera
    window hide
    show screen mini_runner_explain
    pause
    hide screen mini_runner_explain
    call mini_runner from _call_mini_runner
    #Acto 2, de la tercera parte
    call p3_a2 from _call_p3_a2
    #Acto 3, de la tercera parte
    call p3_a3 from _call_p3_a3
    #Acto 4, de la tercera parte
    call p3_a4 from _call_p3_a4
    #Acto 5 de la tercera parte
    call p3_a5 from _call_p3_a5
    #Acto 6, de la tercera parte
    call p3_a6 from _call_p3_a6
    #Acto 7, de la tercera parte
    call p3_a7 from _call_p3_a7
    #Acto 8, de la tercera parte
    call p3_a8 from _call_p3_a8
    #Acto 9, de la tercera parte
    call p3_a9 from _call_p3_a9
    #Acto 10, de la tercera parte
    call p3_a10 from _call_p3_a10
    #Acto 11, de la tercera parte
    call p3_a11 from _call_p3_a11
    #Minijuego memoria

    window hide
    show screen mini_memory_explain
    pause
    hide screen mini_memory_explain
    call mini_memoria from _call_mini_memoria
    # Finaliza el juego:

    label fin:
    scene bg_fin
    "..."

    return

return
