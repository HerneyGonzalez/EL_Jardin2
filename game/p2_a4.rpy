label p2_a4:
    scene bg_casa_papa
    voice "voz101.mp3"
    carp "Desde ahi el ya me habló seriamente, y entonces las conversaciones se volvieron visitas de todos los días."
    stop music
    play music"audio/drama.mp3" volume 0.2
    show car_n_-18
    show car_n_-18:
        subpixel True pos (0.2, 1.1) xzoom 0.9 yzoom 0.9 
    with dissolve

    show alvaro
    
    show alvaro:
        subpixel True pos (0.7, 1.5) zpos 0.0 xzoom 1.5 yzoom 1.5 
    hide alvaro
    with dissolve

    voice "voz102.mp3"
    carp "Cuando empezaron a preguntarme en la casa que si yo me había cuadrado con Álvaro, yo decía que eso era por molestar un rato" 
    voice "voz102a.mp3"
    carp "pero hoy en dia ese rato se convirtió en diecisiete años y seis hijos."
    voice "voz103.mp3"
    carp "el un dia me propuso algo un poco esperado para mi"    

    show alvaro
    
    show alvaro:
        subpixel True pos (0.7, 1.5) zpos 0.0 xzoom 1.5 yzoom 1.5
    voice "voz104.mp3"
    "Nos volamos?" 

    menu:
        "Si":
            jump si_me_voy

        "No":
            jump no_me_voy
    return
return

label si_me_voy:
voice "voz105.mp3"
carp "Yo estaba muy aburrida porque mi mamá cantaleteaba a todo momento"
voice "voz106.mp3"
carp "y como yo sabía vivir sola y le había perdido el misterio a irme de la casa"
voice "voz107.mp3"
carp "me fui con Álvaro. "
hide alvaro
with dissolve
hide car_n_-18
with dissolve

return

label no_me_voy:
voice "voz108.mp3"
car "aqui tengo las cosas medio aseguradas, es muy peligroso arriesgarnos asi, de amor no se vive"
voice "voz109.mp3"
alvaro "Que lastima, sabiendo que aqui no la dejan ser"
hide car_n_-18
with dissolve
jump fin

return






