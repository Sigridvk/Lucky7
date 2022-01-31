"""
save_data.py

Programmeertheorie
Sigrid van Klaveren, Vanja Misuric-Ramljak and Luna Ellinger

- Contains the function save_data which writes information from the games to outputfiles.
"""

import csv

def save_data(steps_from_smallest_game, solved_games, game, algorithm):
    """
    Saves the the steps from the smallest game, and the number of steps taken per game (solved_games) to an output file.
    Takes a list with the steps from te smallest game, and a list with the number of steps per game as parameters.
    Returns nothing.
    """

    # Write moves to an output file
    with open(f'output/{algorithm}/output_moves_{algorithm}_{game}.csv','a') as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['car','move'])
        for row in steps_from_smallest_game:
            csv_out.writerow(row)
    
    # Write total steps to an output file
    with open(f'output/{algorithm}/amount_steps_{algorithm}_{game}.csv','a') as out2:
        write = csv.writer(out2)
        for val in solved_games:
            write.writerow([val])