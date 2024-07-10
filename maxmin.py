import tkinter as tk
from tkinter import ttk


class MaxMinSliderApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MaxMin Slider Application")

        self.create_widgets()

    def create_widgets(self):
        # X Min Slider
        self.x_min_label = ttk.Label(self, text="X Min:")
        self.x_min_label.grid(row=0, column=0, padx=10, pady=10)

        self.x_min_value = tk.IntVar()
        self.x_min_slider = ttk.Scale(self, from_=0, to=100, orient='horizontal', variable=self.x_min_value)
        self.x_min_slider.grid(row=0, column=1, padx=10, pady=10)

        self.x_min_display = ttk.Label(self, textvariable=self.x_min_value)
        self.x_min_display.grid(row=0, column=2, padx=10, pady=10)

        # X Max Slider
        self.x_max_label = ttk.Label(self, text="X Max:")
        self.x_max_label.grid(row=1, column=0, padx=10, pady=10)

        self.x_max_value = tk.IntVar()
        self.x_max_slider = ttk.Scale(self, from_=0, to=100, orient='horizontal', variable=self.x_max_value)
        self.x_max_slider.grid(row=1, column=1, padx=10, pady=10)

        self.x_max_display = ttk.Label(self, textvariable=self.x_max_value)
        self.x_max_display.grid(row=1, column=2, padx=10, pady=10)

        # Y Min Slider
        self.y_min_label = ttk.Label(self, text="Y Min:")
        self.y_min_label.grid(row=2, column=0, padx=10, pady=10)

        self.y_min_value = tk.IntVar()
        self.y_min_slider = ttk.Scale(self, from_=0, to=100, orient='horizontal', variable=self.y_min_value)
        self.y_min_slider.grid(row=2, column=1, padx=10, pady=10)

        self.y_min_display = ttk.Label(self, textvariable=self.y_min_value)
        self.y_min_display.grid(row=2, column=2, padx=10, pady=10)

        # Y Max Slider
        self.y_max_label = ttk.Label(self, text="Y Max:")
        self.y_max_label.grid(row=3, column=0, padx=10, pady=10)

        self.y_max_value = tk.IntVar()
        self.y_max_slider = ttk.Scale(self, from_=0, to=100, orient='horizontal', variable=self.y_max_value)
        self.y_max_slider.grid(row=3, column=1, padx=10, pady=10)

        self.y_max_display = ttk.Label(self, textvariable=self.y_max_value)
        self.y_max_display.grid(row=3, column=2, padx=10, pady=10)


if _name_ == "_main_":
    app = MaxMinSliderApp()
    app.mainloop()