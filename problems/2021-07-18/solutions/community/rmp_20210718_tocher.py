""" Recreational Mathematics Problems 2021-07-18

    Problem defined here:
     https://github.com/somacdivad/recreational-mathematics-problems/tree/main/problems/2021-07-18

     Solution by John Tocher,  https://github.com/JohnTocher
"""

import itertools

KNIGHTS = {"A": "Arthur", "B": "Lancelot", "C": "Kay", "D": "Bedivere", "E": "Lionel", "F": "Tristan", "G": "Gawain", "H": "Gareth", "I": "Galahad", "J": "Perceval" }

def check_the_rules(arrangement):
    """ Check the problems rules in order, return False if any rule fails
    
        Seats are numbered 0 to 9, Arthur at seat 0, 'right' will be positive, 'left' Negative
        Arrangements will come in as a list of Knight handles ["D", "E" , "F" ... "J"]
    """

    seats_by_name = dict()      # Lookup by name, e.g seat["Arthur"] = 0
    seats_by_number = dict()    # Lookup by number, e.g. seat[0] = "Arthur"

    # Arthur insists that Lancelot should sit on his right and that Kay should occupy the seat on Arthur's left
    # This first first rule defines three seats for us, if we put Arthur arbitrarily in seat 0

    seats_by_name["Arthur"] = 0
    seats_by_number[0] = "Arthur"

    seats_by_name["Lancelot"] = 1   # To Arthur's right
    seats_by_number[1] = "Lancelot"

    seats_by_name["Kay"] = 9    # To Arthur's left, also nicely covers the wrap-around case for us,
    seats_by_number[9] = "Kay"  # so we don't have to do any modulo arithmetic with keys later!

    seat_index = 2  
    for each_seat in arrangement:
        seats_by_name[KNIGHTS[each_seat]] = seat_index
        seats_by_number[seat_index] = KNIGHTS[each_seat]
        seat_index += 1

    # Bedivere refuses to sit next to anyone but Lionel and Tristan
    if seats_by_number[seats_by_name["Bedivere"] + 1 ] not in ["Lionel", "Tristan"]:
        return False

    if seats_by_number[seats_by_name["Bedivere"] - 1 ] not in ["Lionel", "Tristan"]:
        return False

    # Gawain won't sit next to Tristan, Lancelot, or Lionel
    if seats_by_number[seats_by_name["Gawain"] + 1 ] in ["Tristan", "Lancelot", "Lionel"]:
        return False
    if seats_by_number[seats_by_name["Gawain"] - 1 ] in ["Tristan", "Lancelot", "Lionel"]:
        return False

    # Gareth won't sit next to Galahad, Lancelot, or Kay
    if seats_by_number[seats_by_name["Gareth"] + 1 ] in ["Galahad", "Lancelot", "Kay"]:
        return False
    if seats_by_number[seats_by_name["Gareth"] - 1 ] in ["Galahad", "Lancelot", "Kay"]:
        return False

    # Perceval objects to sitting next to Galahad, Lancelot, or, Lionel
    if seats_by_number[seats_by_name["Perceval"] + 1 ] in ["Galahad", "Lancelot", "Lionel"]:
        return False
    if seats_by_number[seats_by_name["Perceval"] - 1 ] in ["Galahad", "Lancelot", "Lionel"]:
        return False

    # Tristan refuses to sit next to Lancelot, Perceval, or Kay
    if seats_by_number[seats_by_name["Tristan"] + 1 ] in ["Lancelot", "Perceval", "Kay"]:
        return False
    if seats_by_number[seats_by_name["Tristan"] - 1 ] in ["Lancelot", "Perceval", "Kay"]:
        return False

    # Galahad will sit next to anyone except Gawain and Kay
    if seats_by_number[seats_by_name["Galahad"] + 1 ] in ["Gawain", "Kay"]:
        return False
    if seats_by_number[seats_by_name["Galahad"] - 1 ] in ["Gawain", "Kay"]:
        return False

    # Lionel will not sit next to Galahad
    if seats_by_number[seats_by_name["Lionel"] + 1 ] in ["Galahad"]:
        return False
    if seats_by_number[seats_by_name["Lionel"] - 1 ] in ["Galahad"]:
        return False

    #The other two knights are not particular about whom they sit next to

    return seats_by_number

def solve_the_problem():
    # Main script logic goes here

    knights_to_place = ["D", "E", "F", "G", "H", "I", "J"]  # First three knights, A,B,C are fixed by first rule

    count_fail = 0
    count_ok = 0

    for each_arrangement in itertools.permutations(knights_to_place):
        result = check_the_rules(each_arrangement)

        if result:
            print(f"Everyone is happy with:\n{result}")
            count_ok += 1
            #break
        else:
            #print(f"Failed trying: {each_arrangement}")
            count_fail += 1

    print(f"All done, found {count_ok} good and {count_fail} unacceptable arrangements")

if __name__ == "__main__":
    # Running here
    solve_the_problem()
