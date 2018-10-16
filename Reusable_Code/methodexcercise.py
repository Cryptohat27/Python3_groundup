"""
Methods Exercise
create a method, which takes the state and gross income as the arguments and returns the net income after deducting tax based on the state.

Assum Federal Tax: 10%

You don't have to do for all the states, just take 3-4 to solve the purpose of this exercise.
"""

def NetIncome(gross, state):
    state_tax = {'CA': 10, 'NY': 9, 'TX': 0, 'NJ': 6}

    # Calculate net income after federal tax
    net = gross - (gross * .10)
    # Calculate net income after state tax
    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
        print("Your net income after all the heavy taxes is: " + str(net))
        return net
    else:
        print("state not in the list")
        return None

NetIncome(100000, 'CA')
