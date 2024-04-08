label p1_a5:
    stop music
    play music "audio/triste.mp3"
    scene bg_casa_papa_gris
    show car_n_bestido
    show car_n_bestido:
        subpixel True pos (0.2, 1.1) xzoom 0.9 yzoom 0.9 
    with dissolve
    
    hermanos "Papá esa niña la tiene que poner es a trabajar y que deje de comer tanto libro"

    "Por ese tipo de comentarios me empece a aburrir en el Tolima."

    "Eso de aprender en los libros sí era muy importante para mí"

    "Yo quería ser más persona. Para mí ellos eran unos burros"

    show papa_formal
    
    show papa_formal:
        subpixel True pos (0.7, 2.0) zpos 0.0 xzoom 2.0 yzoom 2.0

    papa "Sabe mija, mejor la saco de aqui de Ortega y la mando para Armenia con su tía."

    menu:
        "Irse a vivir con la tia":
            jump irse

        "Quedarse en Chaparral":
            jump quedarse
    return


return

label irse:
"Yo sé que eso le dolió, porque cuando se despidió no me quería mirar, y cuando al final le tocó, le vi una apagadera en los ojos."
hide papa_formal
with dissolve
hide car_n_bestido
with dissolve

return

label quedarse:
car "no soy la persona mas feliz aqui, pero mejor me quedo, me eso que andar de paticaliente en otro lado"
hide car_n_bestido
with dissolve
jump p2_a2



