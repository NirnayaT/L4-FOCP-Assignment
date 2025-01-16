sweets = int(input("How many sweets are there? "))
pupils = int(input("How many pupils are present? "))
sweets_per_pupil = sweets // pupils
leftover_sweets = sweets % pupils
print(
    f"Each pupil will receive {sweets_per_pupil} sweet(s), and there will be {leftover_sweets} sweet(s) left over."
)
