from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

# indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("RETURN to cintinue, Ctrl-C to abort")
input()

# make the file writable as you open it
# outfile = open(to_file, 'w').write(indata)
#   ---python automatically closes it
out_file = open(to_file, 'w')
out_file.write(indata)

print("All done")

out_file.close()
in_file.close()

## copy practically overwrites everything
