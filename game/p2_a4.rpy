label p2_a4:
    scene bg_casa_papa

    "Desde ahi el ya me habló seriamente, y entonces las conversaciones se volvieron visitas de todos los días."
    stop music
    play music"audio/drama.mp3"
    show car_n_-18
    show car_n_-18:
        subpixel True pos (0.2, 1.1) xzoom 0.9 yzoom 0.9 
    with dissolve

    show alvaro
    
    show alvaro:
        subpixel True pos (0.7, 1.5) zpos 0.0 xzoom 1.5 yzoom 1.5 
    hide alvaro
    with dissolve


    "Cuando empezaron a preguntarme en la casa que si yo me había cuadrado con Álvaro, yo decía que eso era por molestar un rato" 
    "pero hoy en dia ese rato se convirtió en diecisiete años y seis hijos."

    "el un dia me propuso algo un poco esperado para mi"    

    show alvaro
    
    show alvaro:
        subpixel True pos (0.7, 1.5) zpos 0.0 xzoom 1.5 yzoom 1.5
    "Nos volamos?" 

    menu:
        "Si":
            jump si_me_voy

        "No":
            jump no_me_voy
    return
return

label si_me_voy:
"Yo estaba muy aburrida porque mi mamá cantaleteaba a todo momento"
"y como yo sabía vivir sola y le había perdido el misterio a irme de la casa"
"me fui con Álvaro. "
hide alvaro
with dissolve
hide car_n_-18
with dissolve

return

label no_me_voy:
car "aqui tengo las cosas medio aseguradas, es muy peligroso arriesgarnos asi, de amor no se vive"
alvaro "Que lastima, sabiendo que aqui no la dejan ser"
hide car_n_-18
with dissolve
jump fin

return






