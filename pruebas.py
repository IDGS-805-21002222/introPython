from io import open
class VentaDeBoletos:    
    total: float = 0.0
    texto: str = ""  
            
    def __init__(self):        
        self.nombre: str = ""
        self.personas: int = 0
        self.boletos: int = 0
        self.maxBoletos: int = 0
        self.costo: float = 0.0
        self.opciones: str = ""           
                            
    def operacion(self):
        
        print("------------------")
        self.nombre = input("Ingrese su nombre: ")    
        self.personas = int(input("Cuantas personas van a comprar: "))        
        self.boletos = int(input("Cantidad de boletos: "))
        
        self.maxBoletos = (self.personas *7)
        self.costo = (self.boletos * 12)
        
        if self.boletos <= self.maxBoletos:
            
            if self.boletos >= 6:
                self.costo = (self.costo - (self.costo*0.15))
                self.opciones = input("Se pagara con la tarjeta CINECO? si/no: ")  
                
                if self.opciones == "si":
                    self.costo = (self.costo - (self.costo*0.10))
                    print("El costo seria de: {}".format(self.costo))
                    self.opciones = input("Desea repetir la compra de boletos? si/no: ")
                    if self.opciones == "si":
                        nota=open('boletos.txt', 'a')
                        VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                        VentaDeBoletos.texto = "Nombre: {} costo: {} \n".format(self.nombre,self.costo)
                        nota.write(VentaDeBoletos.texto)
                        nota.close()            
                        self.operacion()              
                    else:
                        nota=open('boletos.txt', 'a')
                        VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                        VentaDeBoletos.texto = "Nombre: {} costo: {} \nTotal: {}\n ---------- \n".format(self.nombre,self.costo,VentaDeBoletos.total)
                        nota.write(VentaDeBoletos.texto)
                        nota.close()               
                        print("Fin")
                else:
                    print("El costo seria de: {}".format(self.costo))
                    self.opciones = input("Desea repetir la compra de boletos? si/no: ")
                    if self.opciones == "si":            
                        nota=open('boletos.txt', 'a')
                        VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                        VentaDeBoletos.texto = "Nombre: {} costo: {} \n".format(self.nombre,self.costo)
                        nota.write(VentaDeBoletos.texto)
                        nota.close()            
                        self.operacion()                
                    else:
                        nota=open('boletos.txt', 'a')
                        VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                        VentaDeBoletos.texto = "Nombre: {} costo: {} \nTotal: {}\n ---------- \n".format(self.nombre,self.costo,VentaDeBoletos.total)
                        nota.write(VentaDeBoletos.texto)
                        nota.close()                                      
                        print("Fin")
                        
            else:
                
                if self.boletos >= 3 and self.boletos <= 5:
                    self.costo = (self.costo - (self.costo*0.10))
                    self.opciones = input("Se pagara con la tarjeta CINECO? si/no: ")  
                
                    if self.opciones == "si":
                        self.costo = (self.costo - (self.costo*0.10))
                        print("El costo seria de: {}".format(self.costo))                        
                        self.opciones = input("Desea repetir la compra de boletos? si/no: ")
                        if self.opciones == "si":            
                            nota=open('boletos.txt', 'a')
                            VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                            VentaDeBoletos.texto = "Nombre: {} costo: {} \n".format(self.nombre,self.costo)
                            nota.write(VentaDeBoletos.texto)
                            nota.close()            
                            self.operacion()              
                        else:
                            nota=open('boletos.txt', 'a')
                            VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                            VentaDeBoletos.texto = "Nombre: {} costo: {} \nTotal: {}\n ---------- \n".format(self.nombre,self.costo,VentaDeBoletos.total)
                            nota.write(VentaDeBoletos.texto)
                            nota.close()                                        
                            print("Fin")
                    else:
                        print("El costo seria de: {}".format(self.costo))
                        self.opciones = input("Desea repetir la compra de boletos? si/no: ")
                        if self.opciones == "si":            
                            nota=open('boletos.txt', 'a')
                            VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                            VentaDeBoletos.texto = "Nombre: {} costo: {} \n".format(self.nombre,self.costo)
                            nota.write(VentaDeBoletos.texto)
                            nota.close()            
                            self.operacion()               
                        else:
                            nota=open('boletos.txt', 'a')
                            VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                            VentaDeBoletos.texto = "Nombre: {} costo: {} \nTotal: {}\n ---------- \n".format(self.nombre,self.costo,VentaDeBoletos.total)
                            nota.write(VentaDeBoletos.texto)
                            nota.close()              
                            print("Fin")

                else:
                    self.opciones = input("Se pagara con la tarjeta CINECO? si/no: ")  
                
                    if self.opciones == "si":
                        self.costo = (self.costo - (self.costo*0.10))
                        print("El costo seria de: {}".format(self.costo))
                        self.opciones = input("Desea repetir la compra de boletos? si/no: ")
                        if self.opciones == "si":            
                            nota=open('boletos.txt', 'a')
                            VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                            VentaDeBoletos.texto = "Nombre: {} costo: {} \n".format(self.nombre,self.costo)
                            nota.write(VentaDeBoletos.texto)
                            nota.close()            
                            self.operacion()                
                        else:
                            nota=open('boletos.txt', 'a')
                            VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                            VentaDeBoletos.texto = "Nombre: {} costo: {} \nTotal: {}\n ---------- \n".format(self.nombre,self.costo,VentaDeBoletos.total)
                            nota.write(VentaDeBoletos.texto)
                            nota.close()                                           
                            print("Fin")
                    else:
                        print("El costo seria de: {}".format(self.costo))
                        self.opciones = input("Desea repetir la compra de boletos? si/no: ")
                        if self.opciones == "si":            
                            nota=open('boletos.txt', 'a')
                            VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                            VentaDeBoletos.texto = "Nombre: {} costo: {} \n".format(self.nombre,self.costo)
                            nota.write(VentaDeBoletos.texto)
                            nota.close()            
                            self.operacion()                
                        else:
                            nota=open('boletos.txt', 'a')
                            VentaDeBoletos.total = VentaDeBoletos.total + self.costo
                            VentaDeBoletos.texto = "Nombre: {} costo: {} \nTotal: {}\n ---------- \n".format(self.nombre,self.costo,VentaDeBoletos.total)
                            nota.write(VentaDeBoletos.texto)
                            nota.close()                                       
                            print("Fin") 
                          
        else:        
            print("Demasiados boletos\nSolo se pueden comprar un\nmaximo de 7 boletos por persona")           
            self.opciones = input("Desea volver a iniciar la compra de boletos? si/no: ")
            if self.opciones == "si":            
                self.operacion()              
            else:
                print("Fin")
                     
        
def main():
    obj=VentaDeBoletos()     
    obj.operacion()
    
if __name__ == "__main__":
    main()
    