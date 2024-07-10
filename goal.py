import tkinter as tk

class GoalCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Goal Calculator")

        self.goals_performed_a = 0
        self.goals_reached_a = 0
        self.goals_performed_b = 0
        self.goals_reached_b = 0

        self.create_widgets()

    def create_widgets(self):
        # Labels and entry fields for Team A
        self.label_team_a = tk.Label(self.root, text="Team A")
        self.label_team_a.grid(row=0, column=0, padx=10, pady=10)

        self.label_goals_performed_a = tk.Label(self.root, text="Goals Performed:")
        self.label_goals_performed_a.grid(row=1, column=0, padx=10, pady=10)
        self.entry_goals_performed_a = tk.Entry(self.root)
        self.entry_goals_performed_a.grid(row=1, column=1, padx=10, pady=10)

        self.label_goals_reached_a = tk.Label(self.root, text="Goals Reached:")
        self.label_goals_reached_a.grid(row=2, column=0, padx=10, pady=10)
        self.entry_goals_reached_a = tk.Entry(self.root)
        self.entry_goals_reached_a.grid(row=2, column=1, padx=10, pady=10)

        # Labels and entry fields for Team B
        self.label_team_b = tk.Label(self.root, text="Team B")
        self.label_team_b.grid(row=0, column=2, padx=10, pady=10)

        self.label_goals_performed_b = tk.Label(self.root, text="Goals Performed:")
        self.label_goals_performed_b.grid(row=1, column=2, padx=10, pady=10)
        self.entry_goals_performed_b = tk.Entry(self.root)
        self.entry_goals_performed_b.grid(row=1, column=3, padx=10, pady=10)

        self.label_goals_reached_b = tk.Label(self.root, text="Goals Reached:")
        self.label_goals_reached_b.grid(row=2, column=2, padx=10, pady=10)
        self.entry_goals_reached_b = tk.Entry(self.root)
        self.entry_goals_reached_b.grid(row=2, column=3, padx=10, pady=10)

        # Calculate button
        self.button_calculate = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.button_calculate.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        # Result labels
        self.label_result_a = tk.Label(self.root, text="Total Goals for Team A: ")
        self.label_result_a.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.label_result_b = tk.Label(self.root, text="Total Goals for Team B: ")
        self.label_result_b.grid(row=4, column=2, columnspan=2, padx=10, pady=10)
        self.label_winner = tk.Label(self.root, text="Winner: ")
        self.label_winner.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    def calculate(self):
        try:
            self.goals_performed_a = int(self.entry_goals_performed_a.get())
            self.goals_reached_a = int(self.entry_goals_reached_a.get())
            self.goals_performed_b = int(self.entry_goals_performed_b.get())
            self.goals_reached_b = int(self.entry_goals_reached_b.get())

            total_goals_a = self.goals_performed_a + self.goals_reached_a
            total_goals_b = self.goals_performed_b + self.goals_reached_b

            self.label_result_a.config(text=f"Total Goals for Team A: {total_goals_a}")
            self.label_result_b.config(text=f"Total Goals for Team B: {total_goals_b}")

            if total_goals_a > total_goals_b:
                winner = "Team A advances to the next game"
            elif total_goals_a < total_goals_b:
                winner = "Team B advances to the next game"
            else:
                if self.goals_performed_a > self.goals_performed_b:
                    winner = "Team A advances to the next game"
                elif self.goals_performed_a < self.goals_performed_b:
                    winner = "Team B advances to the next game"
                else:
                    winner = "It's a tie! Both teams advance to the next game"

            self.label_winner.config(text=f"Winner: {winner}")

        except ValueError:
            print("Please enter valid numbers for goals.")

if _name_ == "_main_":
    root = tk.Tk()
    app = GoalCalculator(root)
    root.mainloop()