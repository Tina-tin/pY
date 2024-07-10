# classes1.py

class CoordinateSystem:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_distance(self):
        # Using the given formula (x2 - x1) + (y2 - y1)
        distance = abs(self.x2 - self.x1) + abs(self.y2 - self.y1)
        return distance

    def check_distance(self):
        distance = self.calculate_distance()
        if distance <= 30:
            return "You have 30 km or less to go."
        else:
            return "You have more than 30 km to go."

# Example usage
if __name__ == "__main__":
    # Initial coordinates (x1, y1) and target coordinates (x2, y2)
    coord_system = CoordinateSystem(20, 30, 50, 70)

    # Calculate and check distance
    result = coord_system.check_distance()
    print(result)
