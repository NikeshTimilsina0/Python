def hanoi_solver(n):
    # Create the starting rod with disks stacked from largest (n) to smallest (1)
    initial_rod = list(range(n, 0, -1))
    middle_rod = [] # The auxiliary/helper rod
    target_rod = [] # The destination rod where all disks should end up
    states = []     # A list to store the string representation of rods after each move

    def record_state():
        # Captures the current look of all three rods and adds it to the states list
        states.append(f"{initial_rod} {middle_rod} {target_rod}")
    
    def move(disks, src, aux, dest):
        # Base case: if there are no disks to move, stop the recursion
        if disks == 0:
            return
        
        # Step 1: Move n-1 disks from source to the helper rod (aux)
        move(disks - 1, src, dest, aux)
        
        # Step 2: Move the remaining largest disk from source to the destination rod
        dest.append(src.pop())
        
        # Record the positions of all disks after this move
        record_state()
        
        # Step 3: Move the n-1 disks from the helper rod (aux) to the destination rod
        move(disks - 1, aux, src, dest)

    # Record the very first state (the starting position)
    record_state()
    
    # Start the recursive process for 'n' disks
    move(n, initial_rod, middle_rod, target_rod)
    
    # Join all recorded states with a newline for a clear step-by-step output
    return "\n".join(states)

# Example: Solve for 3 disks
print(hanoi_solver(3))