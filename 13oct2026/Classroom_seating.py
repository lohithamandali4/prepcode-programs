students = 73
bench_capacity = 3

benches = students // bench_capacity
remaining_students = students % bench_capacity

print("completely occupied benches:",
benches)
print("remaining students:",
remaining_students)