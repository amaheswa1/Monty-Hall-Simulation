import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from monty_hall import Simulation


class Plot:
    """
    Class for generating a scatter plot with a line of best fit for the Monty Hall problem simulations.
    """

    def __init__(self, num_doors, num_simulations):
        """
        Initialize the Plot object.

        Args:
            num_doors (int): Number of doors in the Monty Hall problem.
            num_simulations (int): Number of simulations to run.
        """
        self.num_doors = num_doors
        self.num_simulations = num_simulations
        self.switch_wins = []
        self.no_switch_wins = []
        self.x_axis = []

    def run(self):
        """
        Run the Monty Hall simulations and collect win percentages.

        This method runs the specified number of simulations, tracking the win percentages
        for switching doors and not switching doors.
        """
        for i in range(1, self.num_simulations + 1):
            self.x_axis.append(i)

            sim = Simulation(self.num_doors, True)
            sim_wins = 0
            for j in range(i):
                sim.run()
                sim_wins += sim.wins
            self.switch_wins.append(sim_wins / i)

            sim = Simulation(self.num_doors, False)
            sim_wins = 0
            for j in range(i):
                sim.run()
                sim_wins += sim.wins
            self.no_switch_wins.append(sim_wins / i)

    def plot(self):
        """
        Generate and display the scatter plot with lines of best fit.

        This method creates a scatter plot with data points for switching doors and not switching doors,
        and adds lines of best fit using linear regression.
        """
        sns.set()
        plt.scatter(self.x_axis, self.switch_wins, label="Switching Doors")
        plt.scatter(self.x_axis, self.no_switch_wins, label="Not Switching Doors")

        # Perform linear regression to find the line of best fit
        switch_fit = np.polyfit(self.x_axis, self.switch_wins, 1)
        switch_line = np.poly1d(switch_fit)
        plt.plot(self.x_axis, switch_line(self.x_axis), color='blue', label="Line of Best Fit (Switching Doors)")

        no_switch_fit = np.polyfit(self.x_axis, self.no_switch_wins, 1)
        no_switch_line = np.poly1d(no_switch_fit)
        plt.plot(self.x_axis, no_switch_line(self.x_axis), color='orange',
                 label="Line of Best Fit (Not Switching Doors)")

        plt.xlabel("Number of Simulations")
        plt.ylabel("Win Percentage")
        plt.title(f"Monty Hall Problem with {self.num_doors} Doors")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    num_doors = 3
    num_simulations = 400

    plot = Plot(num_doors, num_simulations)
    plot.run()
    plot.plot()
