open_file = open("Cupcakeinvoices.csv")

# for name in open_file:
#     print(name)

cupcake_types = []

for line in open_file:
    line = line.strip()
    values = line.split(',')
    cupcake_types.append(values[2])

print(cupcake_types)

total_invoice = []

open_file.seek(0,0)

for line in open_file:
    line = line.strip()
    values = line.split(',')
    num_cupcakes = values[3]
    amount_cupcakes = values[4]
    total_invoice.append(num_cupcakes * amount_cupcakes)
    
print(total_invoice)
