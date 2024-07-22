import builtins

blacklist = {';', '"', 'os', '_', '\\', '/', '`',
             ' ', '-', '!', '[', ']', '*', 'import',
             'eval', 'banner', 'echo', 'cat', '%',
             '&', '>', '<', '+', '1', '2', '3', '4',
             '5', '6', '7', '8', '9', '0', 'b', 's',
             'lower', 'upper', 'system', '}', '{'}

# Get all built-in function names from the builtins module
all_functions = dir(builtins)

# Filter out functions whose names contain any characters from the blacklist
allowed_functions = [func for func in all_functions if not any(char in func for char in blacklist)]

# Print the allowed function names
print(allowed_functions)
