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


trips = get_trips_starting_from("A")
solutions = [trip for trip in trips if len(trip) == 25]
print(f"There are {len(solutions)} possible routes.")

if len(solutions) != 0:
    random_route = random.choice(solutions)
    states_in_route = [
        STATES[label]
        for label in random_route
        if label.upper() == label
    ]
    print("\nHere's a random solution:")
    print(" - ".join(states_in_route))
