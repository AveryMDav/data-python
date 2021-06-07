open_file = open("Cupcakeinvoices.csv")

# for name in open_file:
#     print(name)

cupcake_types = []

for line in open_file:
    line = line.strip()
    values = line.split(',')
    cupcake_types.append(values[2])

print(cupcake_types)

open_file.seek(0,0)

total_invoice = []



for line in open_file:
    line = line.strip()
    values = line.split(',')
    num_cupcakes = int(values[3])
    amount_cupcakes = float(values[4])
    total_invoice.append(amount_cupcakes * num_cupcakes)
    
print (total_invoice)
    
full_total = sum(total_invoice)

print(full_total)



open_file.close()