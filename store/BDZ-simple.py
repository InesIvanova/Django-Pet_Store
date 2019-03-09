def get_name(first_name, last_name):
    return f'{first_name} {last_name}'


def is_card_num_valid(card_number):
    sum_card = sum(list(map(int, card_number)))
    if sum_card % 7 == 0:
        return True
    return False


class ExistingCard:
    def __init__(self, first_name, last_name, card_number):
        self.name = get_name(first_name, last_name)
        self.card_number = card_number


class Destination:
    def __init__(self, location, card_number=None):
        self.location = location
        self.price = self.__get_price()
        self.card_number = card_number

    def __get_price(self):
        return sum([ord(l) for l in self.location]) / 100

    def make_discount(self):
        self.price = self.price * 0.50


class Passenger:
    def __init__(self, first_name, last_name):
        self.name = get_name(first_name, last_name)
        self.destinations = []
        self.total_sum = None

    def assign_total_sum(self):
        self.total_sum = sum(list(map(lambda d: d.price, self.destinations)))


number_of_cards = int(input())
existing_cards_list = []

for _ in range(0, number_of_cards):
    data = input()
    splitted_data = data.split()
    first_name, last_name, ticket_num = splitted_data
    existing_card = ExistingCard(first_name, last_name, ticket_num)
    existing_cards_list.append(existing_card)

data = input()
passengers_list = []

while not data == 'time to leave!':
    splitted_data = data.split()
    _, first_name, last_name, destination, card_number = splitted_data
    name = get_name(first_name, last_name)

    existing_cards_nums_list = list(map(lambda c: c.card_number, existing_cards_list))
    names_list = list(map(lambda c: c.name, existing_cards_list))

    destination = Destination(location=destination)

    if card_number in existing_cards_nums_list:
        card = list(filter(lambda c: c.name == name, existing_cards_list))

        if card and name == card[0].name:
            card = card[0]
            destination.make_discount()
            destination.card_number = card_number
        else:
            print(f'card {card_number} already exists for another passenger!')
    else:
        if is_card_num_valid(card_number):
            card = ExistingCard(first_name, last_name, card_number)
            existing_cards_list.append(card)
            print(f'issuing card {card_number}')
            destination.make_discount()
            destination.card_number = card_number
        else:
            print(f'card {card_number} is not valid!')

    if name not in list(map(lambda p: p.name, passengers_list)):
        passenger = Passenger(first_name, last_name)
    else:
        passenger = list(filter(lambda p: p.name == name, passengers_list))[0]
    passenger.destinations.append(destination)
    passenger.assign_total_sum()
    passengers_list.append(passenger)

    data = input()

passengers_list = list(set(passengers_list))
ordered_passengers_list = sorted(passengers_list, key=lambda p: -p.total_sum)

for passenger in ordered_passengers_list:
    print(f'{passenger.name}:')
    ordered_destinations_list = sorted(passenger.destinations, key=lambda d: -d.price)
    for destination in ordered_destinations_list:
        if destination.card_number:
            used_card = f'(using card {destination.card_number})'
            print(f'--{destination.location}: {destination.price:.2f}lv {used_card}')
        else:
            print(f'--{destination.location}: {destination.price:.2f}lv')
    print(f'total: {passenger.total_sum:.2f}lv')