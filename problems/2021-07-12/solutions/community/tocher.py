"""
Solution by John Tocher, https://github.com/JohnTocher
"""

import random

def create_border_data():
    """ Returns a dictionary describing the borders of the provided geography

        key:state   value:list of bordering states
    """

    border_dict = dict()

    border_dict["NE"] = ["SD", "WY"]
    border_dict["SD"] = ["ND", "NE", "WY", "MT"]
    border_dict["ND"] = ["SD", "MT"]
    border_dict["WY"] = ["MT", "SD", "NE", "ID"]
    border_dict["MT"] = ["ND", "SD", "WY", "ID"]
    border_dict["ID"] = ["MT", "WY", "OR", "WA"]
    border_dict["OR"] = ["WA", "ID"]
    border_dict["WA"] = ["ID", "OR"]

    return border_dict

def bad_random_solution(starting_state="NE", max_tries=10):
    """ Terrible method, pick randomly from available options!
    """

    border_lookup = create_border_data()  # Get the dictionary of border data
    set_of_borders = set()

    for each_state, bordering_states in border_lookup.items():
        for each_border in bordering_states:
            # Generate tuple of borders (A,B), sorted so that (B,A) isn't counted as different
            this_pair = tuple(sorted([each_state, each_border]))
            set_of_borders.add(this_pair)

    border_count = len(set_of_borders)
    print(f"There are {len(border_lookup)} states and {border_count} unique borders")

    try_count = 0
    solution_found = False

    while try_count < max_tries and not solution_found:
        try_count += 1
        print(f"\nAttempt {try_count} of {max_tries}")
        state_we_are_in = starting_state
        this_journey = list()
        this_journey.append(starting_state)
        borders_still_to_cross = list(set_of_borders)
        still_on_our_journey = True # Still have borders to try

        while still_on_our_journey:
            #print(f"Journey so far: {this_journey}")
            states_we_can_see = border_lookup[state_we_are_in]
            list_of_borders_here = list()
            for each_state in states_we_can_see:
                border_pair = [each_state, state_we_are_in]
                list_of_borders_here.append(tuple(sorted(border_pair)))
            random.shuffle(list_of_borders_here)

            still_on_our_journey = False
            for each_border in list_of_borders_here:
                if each_border in borders_still_to_cross:
                    if each_border[0] == state_we_are_in:
                        new_state = each_border[1]
                    else:
                        new_state = each_border[0]
                    this_journey.append(new_state)
                    borders_still_to_cross.pop(borders_still_to_cross.index(each_border))
                    state_we_are_in = new_state
                    still_on_our_journey = True
                    if not borders_still_to_cross:
                        print(f"Solution found!: {this_journey}")
                        solution_found = True
                        still_on_our_journey = False
                    break  # Don't need to look at any more borders, we're moving
            else:
                still_on_our_journey = False # None of the available borders are unvisited!
                print(f"Stranded at the end of journey: {this_journey}")
                print(f"Still to cross {borders_still_to_cross}")

    return solution_found

def setup_and_solve():
    """ Main routine to run the solving algorithms"""
    result = bad_random_solution()
    print(f"Result was {result}")

if __name__ == "__main__":
    setup_and_solve()
    print("Finished")
