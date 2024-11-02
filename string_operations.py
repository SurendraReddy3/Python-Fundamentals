def string_operations():
    sample_string = "  Hello, World! Welcome to TJS - Python programming.  "

    # Using strip to remove leading and trailing whitespaces
    stripped_string = sample_string.strip()
    print("Original:", repr(sample_string))
    print("Stripped:", repr(stripped_string))

    # Using find to locate a substring
    find_result = stripped_string.find("World")
    print("Find 'World':", find_result)

    # Using replace to replace substrings
    replace_result = stripped_string.replace("World", "Universe")
    print("Replace 'World' with 'Universe':", replace_result)

    # Using count to count occurrences of a substring
    count_result = stripped_string.count("o")
    print("Count 'o':", count_result)

    # Converting string to upper case
    upper_result = stripped_string.upper()
    print("Upper case:", upper_result)

    # Converting string to lower case
    lower_result = stripped_string.lower()
    print("Lower case:", lower_result)

    # Using split to split the string at each space
    split_result = stripped_string.split()
    print("Split:", split_result)

    # Using join to join elements of a list into a single string
    join_result = ", ".join(split_result)
    print("Join elements:", join_result)

    # Using slice to get a substring
    slice_result = stripped_string[7:12]
    print("Slice from 7 to 12:", slice_result)

    # Check if string starts with a substring
    starts_with = stripped_string.startswith("Hello")
    print("Starts with 'Hello':", starts_with)

    # Check if string ends with a substring
    ends_with = stripped_string.endswith("programming.")
    print("Ends with 'programming.':", ends_with)

    # Using format to insert variables into strings
    name = "Alice"
    age = 30
    formatted_string = "Name: {}, Age: {}".format(name, age)
    print("Formatted string:", formatted_string)

    f_string_result = f"Name: {name}, Age: {age}"
    print("F-string result:", f_string_result)

string_operations()
