def sort_list(input_list):
    """
    Sorts a list in ascending order.

    Args:
        input_list (list): The list to be sorted.

    Returns:
        list: A new list sorted in ascending order.
    """
    return sorted(input_list)

# Example usage
if __name__ == "__main__":
    sample_list = [5, 2, 9, 1, 5, 6]
    sorted_list = sort_list(sample_list)
    print("Original List:", sample_list)
    print("Sorted List:", sorted_list)