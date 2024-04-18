label p1_a5:
    stop music
    play music "audio/triste.mp3" volume 0.1
    scene bg_casa_papa_gris
    show car_n_bestido
    show car_n_bestido:
        subpixel True pos (0.2, 1.1) xzoom 0.9 yzoom 0.9 
    with dissolve
    voice "voz54.mp3"
    
    hermanos "Papá esa niña la tiene que poner es a trabajar y que deje de comer tanto libro"
    voice "voz55.mp3"
    "Por ese tipo de comentarios me empece a aburrir en el Tolima."
    voice "voz56.mp3"
    "Eso de aprender en los libros sí era muy importante para mí"
    voice "voz57.mp3"
    "Yo quería ser más persona. Para mí ellos eran unos burros"

    show papa_formal
    
    show papa_formal:
        subpixel True pos (0.7, 2.0) zpos 0.0 xzoom 2.0 yzoom 2.0
    voice "voz58.mp3"
    papa "Sabe mija, mejor la saco de aqui de Ortega y la mando para Armenia con su tía."

    menu:
        "Irse a vivir con la tia":
            jump irse

        "Quedarse en Chaparral":
            jump quedarse
    return


return

label irse:
voice "voz59.mp3"
"Yo sé que eso le dolió, porque cuando se despidió no me quería mirar, y cuando al final le tocó, le vi una apagadera en los ojos."
hide papa_formal
with dissolve
hide car_n_bestido
with dissolve

return

label quedarse:
voice "voz60.mp3"
car "no soy la persona mas feliz aqui, pero mejor me quedo, me eso que andar de paticaliente en otro lado"
hide car_n_bestido
with dissolve
jump p2_a2



