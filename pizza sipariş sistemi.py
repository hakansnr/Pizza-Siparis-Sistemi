import csv
import datetime

with open("Menu.txt", "w") as f:
    f.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n1: Klasik\n2: Margarita\n3: TürkPizza\n4: Sade Pizza\n")
    f.write("* ve seçeceğiniz sos:\n11: Zeytin\n12: Mantarlar\n13: Keçi Peyniri\n14: Et\n15: Soğan\n16: Mısır\n")
    f.write("* Teşekkür ederiz!")

class Pizza:
    def __init__(self):
        self.description = "Pizza"
        self.cost = 0.0
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

class KlasikPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik pizza"
        self.cost = 67.0

class MargaritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita Pizza"
        self.cost = 62.0

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turk Pizza"
        self.cost = 75.0

class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Sade Pizza"
        self.cost = 60.0

class Decorator(Pizza):
    def __init__(self, pizza):
        self.component = pizza
    
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin"
        self.cost = 2.0

class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar"
        self.cost = 3.0

class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi Peyniri"
        self.cost = 5.0

class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Etli"
        self.cost = 4.0

class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Soğanlı"
        self.cost = 2.5

class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mısır"
        self.cost = 2.5 

def main():
    # Menüyü ekrana yazdırma
    with open('Menu.txt', 'r') as file:
        print(file.read())

# Pizza seçimi
pizza = None
while not pizza:
    try:
        pizza_choice = int(input("Lütfen bir pizza tabanı seçiniz (1-4): "))
        if pizza_choice == 1:
            pizza = KlasikPizza()
        elif pizza_choice == 2:
            pizza = MargaritaPizza()
        elif pizza_choice == 3:
            pizza = TurkPizza()
        elif pizza_choice == 4:
            pizza = SadePizza()
        else:
            print("Geçersiz seçim. Lütfen 1-4 arasında bir seçim yapınız.")
    except ValueError:
        print("Geçersiz seçim. Lütfen 1-4 arasında bir seçim yapınız.")

# Sos seçimi
sos = None
while not sos:
    try:
        sos_choice = int(input("Lütfen bir sos seçiniz (11-16): "))
        if sos_choice == 11:
            sos = Zeytin(pizza)
        elif sos_choice == 12:
            sos = Mantar(pizza)
        elif sos_choice == 13:
            sos = KeciPeyniri(pizza)
        elif sos_choice == 14:
            sos = Et(pizza)
        elif sos_choice == 15:
            sos = Sogan(pizza)
        elif sos_choice == 16:
            sos = Misir(pizza)
        else:
            print("Geçersiz seçim. Lütfen 11-16 arasında bir seçim yapınız.")
    except ValueError:
        print("Geçersiz seçim. Lütfen 11-16 arasında bir seçim yapınız.")

# Sipariş toplamının hesaplanması
total_cost = sos.get_cost()
print("Sipariş toplamı: {} TL".format(total_cost))

# Müşteri bilgiler
customer_name = input("Lütfen adınızı giriniz: ")
customer_address = input("Lütfen adresinizi giriniz: ")
customer_phone = input("Lütfen telefon numaranızı giriniz: ")

# Siparişin onaylanması
confirm = None
while not confirm:
    try:
        confirm_choice = int(input("Siparişinizi onaylamak için 1'e, iptal etmek için 2'ye basınız: "))
        if confirm_choice == 1:
            confirm = True
        elif confirm_choice == 2:
            confirm = False
        else:
            print("Geçersiz seçim. Lütfen 1 veya 2'ye basınız.")
    except ValueError:
        print("Geçersiz seçim. Lütfen 1 veya 2'ye basınız.")

if confirm:
    print("Siparişiniz onaylandı. Teşekkür ederiz, {}!".format(customer_name))
else:
    print("Siparişiniz iptal edildi. İyi günler dileriz, {}.".format(customer_name))













