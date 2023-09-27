import tomli

# imports the tomli library
# nessesary to parse any toml files

with open("data1.toml", "rb") as toml_file:
    data1 = tomli.load(toml_file)

# parses the actual toml file and asigns the data variable to it

print(data1["things_about_yourself"]["name"])
print("\n", data1["fun_facts"])

# prints out the info in each section

# you can also get the whole file printed
# instead of printing it here, it has only been asigned to a variable


with open("data2.toml", "rb") as toml_file:
    data2 = tomli.load(toml_file)
