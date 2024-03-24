def towers_of_hanoi(n, source, target, auxiliary):
    """
    Solves the Towers of Hanoi problem recursively.

    Parameters:
        n (int): Number of disks.
        source (str): Name of the source peg.
        target (str): Name of the target peg.
        auxiliary (str): Name of the auxiliary peg.
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    towers_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    towers_of_hanoi(n - 1, auxiliary, target, source)


def main():
    while True:
        # Taking input for the number of disks
        try:
            num_disks = int(input("Enter the number of disks: "))
            if num_disks < 1:
                print("Number of disks should be a positive integer.")
            else:
                # Calculate the minimum number of moves
                min_moves = 2 ** num_disks - 1
                print(f"Minimum number of moves required: {min_moves}")

                # Ask if the user wants to see the solution
                choice = input("Do you want to see the solution? (yes/no): ")
                if choice.lower() in ["yes", "y"]:
                    # Calling the Towers of Hanoi function
                    towers_of_hanoi(num_disks, 'A', 'C', 'B')

                # Ask if the user wants to continue
                choice = input("Do you want to solve again? (yes/no): ")
                if choice.lower() not in ["yes", "y"]:
                    break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
