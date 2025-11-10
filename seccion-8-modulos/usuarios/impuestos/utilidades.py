if __name__ != "__main__":
    # from ..gestion.crud import guardar # import relativo (v94)
    from usuarios.gestion.crud import guardar  # import absoluto (v94)

    print(__name__)

    def pagar_impuestos():
        print("pagando impuestos")
        guardar()


if __name__ == "__main__":
    # from usuarios.gestion.crud import guardar  # import absoluto (v94)
    print("ejecutar tareas de mantenimiento")
