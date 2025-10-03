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
        idx: int
        
        def __lt__(self, other: Self) -> bool:
            distance = [("G", "moving down"), ("G", "stopped"), ("10", "moving down"), ("10", "stopped"), ("10", "moving up"), ("G", "moving up")]
            return distance.index((self.floor, self.status)) > distance.index((other.floor, other.status))

        def __gt__(self, other: Self) -> bool:
            distance = [("G", "moving down"), ("G", "stopped"), ("10", "moving down"), ("10", "stopped"), ("10", "moving up"), ("G", "moving up")]
            return distance.index((self.floor, self.status)) < distance.index((other.floor, other.status))

        def __eq__(self, other: Self) -> bool: # type: ignore
            distance = [("G", "moving down"), ("G", "stopped"), ("10", "moving down"), ("10", "stopped"), ("10", "moving up"), ("G", "moving up")]
            return distance.index((self.floor, self.status)) == distance.index((other.floor, other.status))
        
        def __ge__(self, other: Self) -> bool:
            return self > other or self == other
        
        def __le__(self, other: Self) -> bool:
            return self < other or self == other
        
        def __str__(self):
            return f"{self.__class__.__name__}({', '.join([f'{key}={value}'for key, value in self.__dict__.items()])})"

        def __repr__(self):
            return f"{self.__class__.__name__}({', '.join([f'{key}={value}'for key, value in self.__dict__.items()])})"

        @property
        def distance(self):
            return [("G", "moving down"), ("G", "stopped"), ("10", "moving down"), ("10", "stopped"), ("10", "moving up"), ("G", "moving up")].index((self.floor, self.status))

    lift_1 = Lift()
    lift_1.floor = lift_1_floor
    lift_1.status = lift_1_status
    lift_1.idx = 1

    lift_2 = Lift()
    lift_2.floor = lift_2_floor
    lift_2.status = lift_2_status
    lift_2.idx = 2

    lift_3 = Lift()
    lift_3.floor = lift_3_floor
    lift_3.status = lift_3_status
    lift_3.idx = 3

    lifts = [lift_1, lift_2, lift_3]
    
    def compare(lifts: list[Lift], highest_priority_idx: int = 0, current_comparing_idx: int = 1) -> Lift:
        if lifts[highest_priority_idx] < lifts[current_comparing_idx]:
            highest_priority_idx = current_comparing_idx
        current_comparing_idx += 1
        if current_comparing_idx >= len(lifts):
            return lifts[highest_priority_idx]
        else:
            return compare(lifts, highest_priority_idx, current_comparing_idx)
        
    print(f"Lift {compare(lifts).idx} will come to pick you up.")

            

                
        




    # idx = sorted([lift_1, lift_2, lift_3], key=lambda x: x.distance)[0].idx
    # print(f"Lift {idx} will come to pick you up.")


    
    # These are the print statements that you will need to use in your solution.
    # The expected output of your program must be exactly the same as these print statements, which is "Lift X will come to pick you up."
    # You can uncomment and then move or copy them to anywhere in your code as you like.

    # print("Lift 1 will come to pick you up.")
    # print("Lift 2 will come to pick you up.")
    # print("Lift 3 will come to pick you up.")

    # === TODO ABOVE ===


if __name__ == "__main__":
    main()
