import os  # modulo estandar de py, instalado por default con el interprete

# importacion de modulo
from modulo1 import pyinfo

# importacion1 del paquete.modulo usuarios.acciones
# from usuarios.acciones import *
# from usuarios.acciones import guardar, pagar_impuestos

# importacion2 del paquete.modulo usuarios.acciones
# import usuarios.acciones

# importacion3 del paquete.modulo usuarios.acciones
from usuarios import acciones


os.system('cls' if os.name == 'nt' else 'clear')

pyinfo()

# ejecucion de funciones asociada a importacion1 de paquete.modulo
# guardar()
# pagar_impuestos()

# ejecucion de funciones asociada a importacion2 de paquete.modulo
# usuarios.acciones.guardar()
# usuarios.acciones.pagar_impuestos()

# ejecucion de funciones asociada a importacion3 de paquete.modulo
acciones.guardar()
