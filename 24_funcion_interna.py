def externa():
    def interna():
        return "Soy una funcion interna"
    print(interna())
externa()