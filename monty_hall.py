import random


class Simulation:
    """
    Class for simulating the Monty Hall problem.
    """

    def __init__(self, num_doors, switch):
        """
        Initialize the Simulation object.

        Args:
            num_doors (int): Number of doors in the Monty Hall problem.
            switch (bool): Flag indicating whether the player switches doors.
        """
        self.num_doors = num_doors
        self.switch = switch
        self.wins = 0
        self.losses = 0

    def run(self):
        """
        Run a single simulation of the Monty Hall problem.

        This method randomly chooses the door with the prize, the door the player picks,
        reveals a door, and determines the final outcome based on the switching strategy.
        """
        # Randomly choose the door with the prize
        prize_door = random.randint(1, self.num_doors)

        # Randomly choose the door the player picks
        player_pick = random.randint(1, self.num_doors)

        # Determine which door to reveal
        reveal_doors = [i for i in range(1, self.num_doors + 1) if i != prize_door and i != player_pick]
        revealed_door = random.choice(reveal_doors)

        # Switch if specified
        if self.switch:
            player_pick = [i for i in range(1, self.num_doors + 1) if i != player_pick and i != revealed_door][0]

        # Check if the player won
        if player_pick == prize_door:
            self.wins += 1
        else:
            self.losses += 1


if __name__ == "__main__":
    num_doors = 3
    switch = True
    num_simulations = 1000

    sim = Simulation(num_doors, switch)
    for i in range(num_simulations):
        sim.run()

    print(f"Win percentage with {num_doors} doors and switching: {sim.wins / num_simulations:.2%}")

    switch = False

    sim = Simulation(num_doors, switch)
    for i in range(num_simulations):
        sim.run()

    print(f"Win percentage with {num_doors} doors and not switching: {sim.wins / num_simulations:.2%}")
