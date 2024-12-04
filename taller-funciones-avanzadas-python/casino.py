def el_ganador(total_perdidas):
    def calcular_ganancias():
        if(total_perdidas < 1000000):
            return total_perdidas * 0.1
        if(total_perdidas >= 1000000 and total_perdidas <= 5000000):
            return total_perdidas * 0.2
        if(total_perdidas > 5000000):
            return total_perdidas * 0.3
    return calcular_ganancias

bonificacion1 = el_ganador(1500000)

print(f"Recibe una bonificacion de {bonificacion1()}")



    