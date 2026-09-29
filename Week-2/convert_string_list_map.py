
def convert_string_list_to_list_of_lists(string_list):
    list_of_lists = list(map(list, string_list))
    return list_of_lists

if __name__ == "__main__":
    string_list = ["hello", "world", "python"]
    
    result = convert_string_list_to_list_of_lists(string_list)
    
    print(result)