print("LAND VALUE AND STAMP DUTY CALCULATOR")
length = float(input("Enter Length (m): "))
width = float (input("Enter Width (m):"))
value_per_m2 = float(input("Enter Value per m2 (UGX):"))
stamp_rate = float(input("Enter Stamp Rate (%): "))

area = length * width
land_value = area * value_per_m2
stamp_duty = land_value * stamp_rate / 100
total = land_value + stamp_duty

print("\n--- RESULTS ---")
print("Land Area:", area, "m2")
print("Land Value: UGX", land_value)
print("Stamp Duty: UGX", stamp_duty)
print("Total Amount: UGX", total)