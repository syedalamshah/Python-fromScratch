class Phone:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery

    def call(self, person):
        print(f"Calling {person} using {self.brand}")

    def battery_status(self):
        print(f"Battery is at {self.battery}%")


phone1 = Phone("Apple", 80)
phone2 = Phone("Samsung", 60)

phone1.call("Ali")
phone1.battery_status()

phone2.call("Sara")
phone2.battery_status()