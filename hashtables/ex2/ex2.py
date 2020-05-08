#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    trips_dict = {}
    route = []

    for ticket in tickets:
        trips_dict[ticket.source] = ticket.destination

    index = 0
    current_destination = "NONE"

    while index < length:
        current_destination = trips_dict.get(current_destination)
        route.append(current_destination)
        index += 1

    return route
