inputFileName = 'test_hash_remover.txt'
outputFileName = 'test_hash_removed.txt'

input = open(inputFileName, "r")
output = open(outputFileName, "w")

for line in input:
    if not line.lstrip().startswith("#"):
        output.write(line)

input.close()
output.close()