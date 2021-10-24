# with open('binaries', 'bw') as bin_files:
#     for i in range(17):
#         bin_files.write(bytes([i]))

with open('binaries', 'bw') as bin_files:
    bin_files.write(bytes(range(17)))

with open('binaries', 'br') as bins:
    for b in bins:
        print(b)

