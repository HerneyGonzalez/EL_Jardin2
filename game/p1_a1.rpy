
label p1_a1:
    voice "voz1.mpeg"
    play music "audio/triste.mp3"
    "Cuando tierno uno cree que la vida son puras rosas, pero cuando va creciendo y viviendo, entiende que sólo son puras espinas. "
    voice "voz2.mpeg"
    car "(Cuando llegué al uso de razón mataron a don Raúl. Nunca lo olvidaré.)"
    play sound "audio/disparo.mp3"
    "*sonido de disparo*"
    stop sound

    scene bg_iglesia

    show car_n_bestido
    
    show car_n_bestido:
        subpixel True pos (0.2, 1.1) xzoom 0.9 yzoom 0.9 
    with dissolve

    voice "voz3.mp3"
    car "(Yo había hecho ese día por la mañana mi primera comunión, y a pesar de que mi vestido blanco con azahares era alquilado, no me lo había dejado quitar.)"
    voice "voz4.mp3"
    car "(Yo me sentía como un alma pura con ese vestido, tal como el padre Aniceto nos lo había explicado una y otra vez durante los cuarenta días de cuaresma,"
    voice "voz5.mp3"
    car "Que fueron los de la preparación para recibir en mi alma el cuerpo de Jesús.)"
    stop music
    show papa_formal
    
    show papa_formal:
        subpixel True pos (0.7, 2.0) zpos 0.0 xzoom 2.0 yzoom 2.0 



    #show papa_formal:
        #subpixel True pos (0.75, 2.0) xzoom 2.0 yzoom 2.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 


    voice "voz6.mp3"
    papa "Que bendición, que pude traer musicos desde Chaparral"
    play music "feliz.mp3"
    hide papa_formal
    "*se escucha musica alegre*"
    voice "voz7.mp3"
    raul "Mire mijita, aqui le traje algo"
    voice "voz8.mp3"
    car "(Él estaba dándome un regalo, un libro llamado La imitación de Cristo, de Kempis, del que nunca leí más que el título porque tenía una letra apretada.)"

    play sound "audio/corriendo.mp3"
    "*sonidos de gente corriendo*"
    voice "voz9.mp3"
    raul "No me mate.."
    play sound "audio/disparo.mp3"
    "*sonido de disparo*"
    stop sound
    stop music

    play music "audio/triste.mp3"
    voice "voz10.mp3"
    car "(Entraron unos hombres armados y le dispararon a don Raúl)"
    voice "voz11.mp3"
    car "(El tiro le estalló en la cara y su sangre me saltó encima como un animal asustado y me manchó todo el vestido con había recibido al niño Jesús.)"
    voice "voz12.mp3"
    car "(Una sangre caliente y olorosa a cobre, que aún no me he podido quitar de encima.)"
    voice "voz13.mp3"
    car "( Los ojos le quedaron disparados en sentidos opuestos, como si hubiera querido buscar a los asesinos y entre tanta gente no hubiera acertado a saber quiénes eran.)"

return


