import os

class Cinepolis:
    def __init__(self, nombre, num_boletos, usa_tarjeta):
        self.nombre = nombre
        self.num_boletos = num_boletos
        self.usa_tarjeta = usa_tarjeta
        self.precio_boletos = 12.00
        self.total_a_pagar = 0.0

    def calcular_descuento(self):
        if self.num_boletos > 5:
            descuento = 0.15
        elif 3 <= self.num_boletos <= 5:
            descuento = 0.10
        else:
            descuento = 0.0

        total = self.num_boletos * self.precio_boletos
        total_con_descuento = total - (total * descuento)

        if self.usa_tarjeta:
            total_con_descuento -= total_con_descuento * 0.10

        self.total_a_pagar = total_con_descuento

    def guardar_en_archivo(self, file):
        file.write(f"{self.nombre} compró {self.num_boletos} boletos, el total es de ${self.total_a_pagar:.2f}\n")


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def comprar_boletos():
    total_compras = 0
    lista_compras = []

    while True:
        try:
            num_personas = int(input("¿Cuántas personas van a comprar boletos?: "))
            if num_personas <= 0:
                print("Debe ingresar un número válido de personas.")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        for _ in range(num_personas):
            while True:
                nombre = input("Ingrese el nombre de la persona que realizará la compra: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue

                while True:
                    try:
                        num_boletos = int(input("¿Cuántos boletos quiere comprar (máximo 7)?: "))
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                        continue

                    if num_boletos > 7:
                        print("No puede comprar más de 7 boletos por persona.")
                        cambiar = input("¿Quiere cambiar el número de boletos o el número de compradores? (Boletos/Compradores): ").strip().lower()
                        if cambiar == "boletos":
                            continue
                        elif cambiar == "compradores":
                            break  
                        else:
                            print("Opción no válida. Intente nuevamente.")
                            continue
                    elif num_boletos < 1:
                        print("Debe comprar al menos 1 boleto.")
                        continue
                    else:
                        break

                if cambiar == "compradores":
                    break

                usa_tarjeta = input("¿Pagará con tarjeta Cineco? (Sí/No): ").strip().lower() == 'sí'

                compra = Cinepolis(nombre, num_boletos, usa_tarjeta)
                compra.calcular_descuento()

                lista_compras.append(compra)
                total_compras += compra.total_a_pagar
                break  

        continuar = input("¿Desea seguir comprando boletos? (Sí/No): ").strip().lower()
        if continuar == 'sí':
            limpiar_pantalla()  
        else:
            break

    with open("Compra.txt", "w", encoding="utf-8") as file:
        print("\nResumen final de compras:")
        for compra in lista_compras:
            print(f"{compra.nombre} compró {compra.num_boletos} boletos, el total es de ${compra.total_a_pagar:.2f}")
            compra.guardar_en_archivo(file)

        print(f"\nTotal a pagar por todas las compras: ${total_compras:.2f}")
        file.write(f"\nTotal a pagar por todas las compras: ${total_compras:.2f}\n")

    print("Gracias por su compra.")


if __name__ == "__main__":
    comprar_boletos()
