class Lamp:
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


class VentiladorConLampara(Lamp):
    def __init__(self, vent_status,lamp_status):
        self._status=vent_status
        self._is_turned_on=lamp_status

    def encender_ventilador(self, interruptor):
        self._status=interruptor
        if self._status:
            print('VENTILADOR ENCENDIDO')
        else:
            print('VENTILADOR APAGADO')
