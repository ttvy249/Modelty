def rotate_sparse_array(arr, steps):
    non_none_elements = [val for val in arr if val is not None]
    steps = steps % len(non_none_elements)
    rotated_non_none_elements = non_none_elements[-steps:] + non_none_elements[:-steps]
    result = []
    non_none_index = 0
    for val in arr:
        if val is not None:
            result.append(rotated_non_none_elements[non_none_index])
            non_none_index += 1
        else:
            result.append(None)
    return result


if __name__ == "__main__":
    array_input = input("Enter the array (elements separated by commas, use 'None' for None values): ")
    steps = int(input("Enter the number of steps to rotate: "))

    # Convert input string to list
    array = [None if x.strip() == 'None' else int(x.strip()) for x in array_input.split(',')]

    # Perform the rotation
    rotated_array = rotate_sparse_array(array, steps)

    # Print the result
    print(f"Original array: {array}")
    print(f"Rotated array: {rotated_array}")
