# %%
import os

external_result = open("../files/external-result.csv", 'r')
our_result = open("../files/analysed-java-repos.csv", 'r')
new_result = open("../files/analysed-java-repos-fixed.csv", 'w')

result = external_result.read()
external_lines = result.split("\n")
name_position = 0
loc_position = 4

old_result = our_result.read()
old_lines = old_result.split("\n")
old_name_position = 0


for i, old_line in enumerate(old_lines):
    if (i == 0):
        new_result.write(f"{old_line};loc\n")
    else:
        old_values = old_line.split(";")
        repo_name = old_values[old_name_position]

        found = False

        for i, external_line in enumerate(external_lines):
            if(i > 0):
                values = external_line.split(",")
                name = values[name_position]

                if(repo_name == name):
                    loc = values[loc_position]
                    new_result.write(f"{old_line};{loc}\n")
                    found = True
                    break

        if(not found):
            none = None
            new_result.write(f"{old_line};{none}\n")

print("Done")
