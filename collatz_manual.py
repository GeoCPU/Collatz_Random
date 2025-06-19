def collatz_manual(n, show_sequence=False):
    steps = 0
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        sequence.append(n)
        steps += 1

    print(f"\n[✓] Reached 1 in {steps} steps.")
    if show_sequence:
        print("Sequence:")
        # Print sequence in chunks of 10 per line for readability
        for i in range(0, len(sequence), 10):
            print(sequence[i:i+10])


if __name__ == "__main__":
    print("Collatz Conjecture Explorer")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        user_input = input("Enter a positive integer to test (or 'exit' to quit): ").strip()

        if user_input.lower() in ('exit', 'quit'):
            print("Goodbye!")
            break

        try:
            number = int(user_input)
            if number <= 0:
                print("Please enter a number greater than zero.\n")
                continue
        except ValueError:
            print("That wasn't a valid number. Please enter a positive integer.\n")
            continue

        show = input("Show full sequence? (y/n): ").lower().startswith("y")
        collatz_manual(number, show_sequence=show)
        print()  # extra newline for spacing
