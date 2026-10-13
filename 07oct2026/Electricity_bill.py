unit = int(input("Enter the number of units:"))
eachgroup_units = 50
complete_units = unit // eachgroup_units
remaining_units = unit % eachgroup_units

print(f"complete_units:{complete_units},remaining_units:{remaining_units}")