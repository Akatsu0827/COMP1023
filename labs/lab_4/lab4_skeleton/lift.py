def main():

    # Get user input
    # lift_1_floor, lift_2_floor and lift_3_floor can be either G or 10
    # lift_1_status, lift_2_status and lift_3_status can be moving up, moving down or stopped
    # The strip() method removes spaces or other characters from the start and end of a string. For example:
    # text = "   COMP 1023   "
    # cleaned_text = text.strip()
    # print(cleaned_text)  # Output: "COMP 1023"
    lift_1_floor = input("Current floor of lift 1 (G/10): ").strip()
    lift_1_status = input("Status of lift 1 (moving up/moving down/stopped): ").strip()
    lift_2_floor = input("Current floor of lift 2 (G/10): ").strip()
    lift_2_status = input("Status of lift 2 (moving up/moving down/stopped): ").strip()
    lift_3_floor = input("Current floor of lift 3 (G/10): ").strip()
    lift_3_status = input("Status of lift 3 (moving up/moving down/stopped): ").strip()

    print("Result: ")

    # NOTE: Please do not modify any code above this line.

    # === TODO BELOW ===
    from typing import Self

    class Lift:
        floor: str
        status: str
        
        def __lt__(self, other: Self) -> bool:
            distance = [("G", "moving down"), ("G", "stopped"), ("10", "moving down"), ("10", "stopped"), ("10", "moving up"), ("G", "moving up")]
            return distance.index((self.floor, self.status)) > distance.index((other.floor, other.status))

        def __gt__(self, other: Self) -> bool:
            distance = [("G", "moving down"), ("G", "stopped"), ("10", "moving down"), ("10", "stopped"), ("10", "moving up"), ("G", "moving up")]
            return distance.index((self.floor, self.status)) < distance.index((other.floor, other.status))

        def __eq__(self, other: Self) -> bool: # type: ignore
            distance = [("G", "moving down"), ("G", "stopped"), ("10", "moving down"), ("10", "stopped"), ("10", "moving up"), ("G", "moving up")]
            return distance.index((self.floor, self.status)) == distance.index((other.floor, other.status))

        @property
        def distance(self):
            return [("G", "moving down"), ("G", "stopped"), ("10", "moving down"), ("10", "stopped"), ("10", "moving up"), ("G", "moving up")].index((self.floor, self.status))


    lift_1 = Lift()
    lift_1.floor = lift_1_floor
    lift_1.status = lift_1_status

    lift_2 = Lift()
    lift_2.floor = lift_2_floor
    lift_2.status = lift_2_status

    lift_3 = Lift()
    lift_3.floor = lift_3_floor
    lift_3.status = lift_3_status

    import numpy as np
    distance_array = np.array([lift_1.distance, lift_2.distance, lift_3.distance])
    print(f"Lift {distance_array.argmin()+1} will come to pick you up.")
    
    # These are the print statements that you will need to use in your solution.
    # The expected output of your program must be exactly the same as these print statements, which is "Lift X will come to pick you up."
    # You can uncomment and then move or copy them to anywhere in your code as you like.

    # print("Lift 1 will come to pick you up.")
    # print("Lift 2 will come to pick you up.")
    # print("Lift 3 will come to pick you up.")

    # === TODO ABOVE ===


if __name__ == "__main__":
    main()
