# Definir la función para esperar a que termine el audio en el canal de voz
label _wait_for_voice_end:
    python:
        def on_voice_end():
            renpy.music.register_channel_finish_callback("voice", None)  # Eliminar el callback después de que se llame una vez

        renpy.music.register_channel_finish_callback("voice", on_voice_end)  # Registrar la función de callback

        renpy.pause(lambda: renpy.music.get_playing(channel="voice") == [])  # Pausar hasta que no haya más audio en el canal de voz
