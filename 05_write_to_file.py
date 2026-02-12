from datetime import date

calculations = [
            '-40.0C is -40F', '100.0C is 212F', '32.0F is 0C',
            '-273.0C is -459F', '400.0C is 752F', '-40.0F is -40C']

# **** Get current date for heading and filename ****
today = date.today()

# get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

file_name = f"temperature_{year}_{month}_{day}"
write_to = f"{file_name}.txt"

with open(write_to, "w") as text_file:

    text_file.write("***** Temperature Calculations *****\n")
    text_file.write(f"Generated: {day}/{month}/{year}\n\n")
    text_file.write("Here is your calculation history (oldest to newest)...\n")

    # write the item to file
    for item in calculations:
        text_file.write(item)
        text_file.write("\n")