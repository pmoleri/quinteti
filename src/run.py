from gui import GameMain

# Este modulo solo existe porque no se pudo enganchar directamente
# GameMain por estar dentro de un paquete.

# Es importante definir la funcion 'main' para que sea invocada por sugar.
# El modulo se define en activity.py con el atributo game_name.
def main():
    GameMain.main()

# Codigo para debug de este modulo:
if __name__ == "__main__":
    main()
