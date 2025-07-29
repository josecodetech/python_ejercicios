class Ascensor:
    def __init__(self, planta_inicial=0, planta_maxima=10,planta_minima=0):
        """ Inicializa en la planta especificada"""
        self.planta = planta_inicial
        self.planta_maxima = planta_maxima
        self.planta_minima = planta_minima
    def subir(self):
        """ Sube una planta si no se ha alcanzado la planta máxima """
        if self.planta < self.planta_maxima:
            self.planta += 1
            print(f"Subiendo a la planta {self.planta}")
        else:
            print("Ya estás en la planta máxima.")
    def bajar(self):
        """ Baja una planta si no se ha alcanzado la planta mínima """
        if self.planta > self.planta_minima:
            self.planta -= 1
            print(f"Bajando a la planta {self.planta}")
        else:
            print("Ya estás en la planta mínima.")
    def ver_planta(self):
        """ Muestra la planta actual """
        print(f"Estás en la planta {self.planta}")