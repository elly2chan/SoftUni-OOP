from customer import Customer
from dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.find_customer(customer_id)
        dvd = self.find_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'
        if dvd.is_rented:
            return 'DVD is already rented'
        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id, dvd_id):
        customer = self.find_customer(customer_id)
        dvd = self.find_dvd(dvd_id)
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f'{customer.name} has successfully returned {dvd.name}'
        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        result = ''
        for customer in self.customers:
            result += f'{repr(customer)}' + '\n'
        for dvd in self.dvds:
            result += f'{repr(dvd)}' + '\n'
        return result.rstrip()

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def find_dvd(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd