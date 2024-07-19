from address import Address
from mailing import Mailing

to_address = Address("453645", "Казань", "Ленина", "10", "1")
from_address = Address("764352", "Ижевск", "Комсомольская", "5", "3")
cost = 1300
track = "Track475768"

mailing = Mailing(from_address, to_address, cost, track)
print(mailing)
