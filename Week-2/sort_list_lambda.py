

def sort_dicts_by_make(dicts_list):
    sorted_list = sorted(dicts_list, key=lambda x: x['make'].strip())
    return sorted_list 

if __name__ == "__main__":
    original_list_of_dictonaries = [
        {'make': ' Google ', 'model': 216, 'color': 'Black'}, 
        {'make': 'MiMax', 'model': '2', 'color': 'Gold'}, 
        {'make': 'Samsung', 'model': 7, 'color': 'Black'}
    ]
    sorted_dictionary = sort_dicts_by_make(original_list_of_dictonaries)
    print(sorted_dictionary)
