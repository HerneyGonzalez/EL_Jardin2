label p3_a9:
    scene bg_casa_papa

    show mama_formal
    
    show mama_formal:
        subpixel True pos (0.7, 1.6) zpos 0.0 xzoom 1.5 yzoom 1.5
    voice "voz188.mp3"
    mama "Aunque me cueste todos mis esfuerzo, voy a seguir luchando con lo que ha quedado en la finca"
    voice "voz189.mp3"
    carp "y nosotros en Chaparral tuvimos que entregarle a mi hermano el carro de mi papá."
    hide mama_formal
    with dissolve
    voice "voz190.mp3"
    carp "Mis hermanos se volvieron hombres agrios y empezaron a mandar como si todo lo que el viejo dejó fuera de ellos."
    voice "voz191.mp3"
    carp "Para evitar enfrentamientos con la familia, llego un señor al que llamaban El Burro"
    show burro
    
    show burro:
        subpixel True pos (0.2, 1.1) xzoom 0.9 yzoom 0.9 
    voice "voz192.mp3"
    burro "Venga Alvaro, coja el Nissan y haga una línea entre La Marina y Río Blanco"
    show alvaro
    show alvaro:
        subpixel True pos (0.7, 1.1) zpos 0.0 xzoom 1 yzoom 1
    with dissolve
    
    voice "voz193.mp3"
    "pero un día tuvo un accidente y se salió de la carretera."
    play sound "audio/auto.mp3" volume 0.3
    "*sonido de accidente automovilistico*"
    stop sound
    voice "voz194.mp3"
    carp "No fue muy grave, aunque tocó pagar todo y nosotros empeñar lo que teníamos." 
    voice "voz195.mp3"
    carp "Quedamos amarrados de pies y manos con quien nos prestó para tapar la deuda que nos dejó el accidente."
    voice "voz196.mp3"
    carp "¡Tocó! ¿Qué podíamos hacer?"
    voice "voz197.mp3"
    carp "Teníamos que pagar las raspaduras de los pasajeros y la mercancía que se dañó"
    voice "voz198.mp3"
    carp "y como le quitaron el derecho a ganarse la vida, ya que no podía volver a manejar ni zorra"

return





