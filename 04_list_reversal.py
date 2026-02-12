all_calculations = ['-40.0C is -40F', '100.0C is 212F',
                    '32.0F is 0C', '-273.0C is -459F',
                    '400.0C is 752F', '60.0F is 16C']

newest_first = list(reversed(all_calculations))

print("==== Oldest to Newest for calc idk ====")
for item in all_calculations:
    print(item)

print()

print("==== Now the reversed ====")
for item in newest_first:
    print(item)