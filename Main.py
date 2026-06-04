Main.py
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso de {monto}. Saldo actual: {self.saldo}")
        else:
            print("El monto debe ser positivo.")

    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro exitoso de {monto}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes o monto inválido.")

    def mostrar_info(self):
        print(f"Titular: {self.titular}, Saldo: {self.saldo}")

# Ejemplo de uso
cuenta1 = CuentaBancaria("Elvira", 100)
cuenta1.mostrar_info()
cuenta1.depositar(50)
cuenta1.retirar(30)
cuenta1.mostrar_info()
