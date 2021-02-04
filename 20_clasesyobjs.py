from lamp import Lamp, VentiladorConLampara


def run():
    #OBJETO LAMPARA
    lamp = Lamp(is_turned_on=False)
    ventilador_con_lampara=VentiladorConLampara(vent_status=True,lamp_status=True)

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
            ventilador_con_lampara.encender_ventilador(True)
            ventilador_con_lampara.turn_on()
        elif command == 'a':
            lamp.turn_off()
            ventilador_con_lampara.encender_ventilador(False)
            ventilador_con_lampara.turn_off()
        else:
            break


if __name__ == '__main__':
    run()