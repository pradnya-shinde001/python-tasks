
def sort_tuples_by_last_element(tuples_list):   
    sorted_list = sorted(tuples_list, key=lambda x: x[-1])
    return sorted_list




if __name__ == "__main__":
    tuples_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    sorted_list = sort_tuples_by_last_element(tuples_list)
    print(sorted_list)