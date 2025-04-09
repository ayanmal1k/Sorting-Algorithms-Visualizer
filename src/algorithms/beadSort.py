def beadSort(array, *args):
    """
    Bead Sort (also known as Gravity Sort) is a natural sorting algorithm inspired by
    beads falling under gravity on parallel vertical rods.
    
    For each number in the input array, imagine a row of beads on vertical rods.
    The number of beads in each row corresponds to the value of the number.
    When gravity is applied, beads fall down as far as possible, naturally sorting the array.
    
    This algorithm only works on positive integers.
    
    Time complexity: O(n + m), where n is the number of elements and m is the maximum value
    Space complexity: O(n*m) for the beads matrix
    """
    
    if not array:
        return

    if any(not isinstance(x, int) or x < 0 for x in array):
        raise ValueError("Bead sort only works with non-negative integers.")

    n = len(array)
    max_val = max(array)

    beads = [[0 for _ in range(n)] for _ in range(max_val)]

    # Drop beads (setup)
    for col in range(n):
        for row in range(array[col]):
            beads[row][col] = 1
            yield array[:], -1, col, row, -1  # Visual feedback when placing beads

    # Simulate gravity
    for row in range(max_val):
        count = 0
        for col in range(n):
            if beads[row][col]:
                count += 1
                beads[row][col] = 0
        for col in range(n - count, n):
            beads[row][col] = 1

        # Reconstruct a temporary array to show progress visually
        temp_array = [sum(beads[i][j] for i in range(max_val)) for j in range(n)]
        yield temp_array, -1, -1, row, -1  # Show current state during gravity fall

    # Final update to actual array
    for col in range(n):
        array[col] = sum(beads[row][col] for row in range(max_val))
        yield array[:], -1, col, -1, -1 