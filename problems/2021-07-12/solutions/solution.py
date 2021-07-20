"""
Solution to the Border Crossing #1 problem.

By David Amos
July 18, 2021
"""

import random

STATES = {
    "A": "Nebraska",
    "B": "South Dakota",
    "C": "North Dakota",
    "D": "Wyoming",
    "E": "Montana",
    "F": "Idaho",
    "G": "Oregon",
    "H": "Washington",
}

BORDERS = [
    "AaB",
    "AbD",
    "BcD",
    "BdE",
    "BeC",
    "CfE",
    "EgD",
    "EiF",
    "DhF",
    "FjG",
    "FkH",
    "GlH",
]

def get_trips_starting_from(state, borders=BORDERS):
    trips = []

    def make_trips(state, driven=None, borders_crossed=None):
        driven = driven or state
        borders_crossed = borders_crossed or ()
        # Get all of the borders connected to `state`
        # that haven't been crossed
        available_borders = [
            border
            for border in borders
            if state in border and border not in borders_crossed
        ]

        # Determine if the trip has ended
        if not available_borders:
            trips.append(driven)

        # Cross the border to the adjacent state and recurse
        for border in available_borders:
            crossing = border[1:] if border[0] == state else border[1::-1]
            make_trips(
                state=crossing[-1],
                driven=driven + crossing,
                borders_crossed=(border, *borders_crossed),
            )

    make_trips(state)
    return trips


def get_route_string(route):
    states_in_route = [
        STATES[label]
        for label in random_route
        if label.upper() == label
    ]
    return " - ".join(states_in_route)

# Determine how many routes there are that cross each border exactly once.
# This can be done using the length of a trip. Since there are 12 total
# borders, the trip string should have twelve lower case letters. But the
# trip string also contains upper case letters for the states on either side
# of a border. Each lower case letter has one upper case letter on to its
# left in the string, plus on addition upper case letter at the end of the
# string. This gives a total of 13 upper case letters in a string for a
# solutions, so the the total length of a solution string is 12 + 13 = 25.
trips = get_trips_starting_from("A")
solutions = [trip for trip in trips if len(trip) == 25]
print(f"There are {len(solutions)} possible routes.")


# If there are any solutions, print a random one using the state names.
if len(solutions) != 0:
    print("\nHere's a random solution:")
    random_route = random.choice(solutions)
    print(get_route_string(random_route))
