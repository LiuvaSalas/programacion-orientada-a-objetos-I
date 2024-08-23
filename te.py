class Te:
    duracion = 365

    @staticmethod
    def retorna_tiempo_y_recomendacion(sabor: int):
        if sabor == 1:
            tiempo = 3
            recomendacion = "al desayuno"
            return (
                tiempo,
                recomendacion
            )
        elif sabor == 2:
            tiempo = 5
            recomendacion = "al medio dia"
            return (
                tiempo,
                recomendacion
            )
        elif sabor == 3:
            tiempo = 6
            recomendacion = "al atardecer"
            return (
                tiempo,
                recomendacion
            )
        else:
            return "El sabor no se encuentra en el listado"

    @staticmethod
    def retorna_precio(formato: int):
        if formato == 500:
            precio = 5000
            return precio
        elif formato == 300:
            precio = 3000
            return precio
        else:
            return "Formato no valido"
