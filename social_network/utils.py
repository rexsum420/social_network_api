def trim_and_case(input_str):
    result = []
    for char in input_str:
        if char != ' ':
            result.append(char.lower())
    return ''.join(result)