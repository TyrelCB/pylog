# Write Variable from another script to OUtput.txt

def write_to_file(filename, self):
    with open(filename, "w") as text_file:
        text_file.write("%s" % self)
def append_to_file(filename, self):
    with open(filename, "a") as text_file:
        text_file.write("\n%s" % self)
def append_to_file2(filename, self): # Don't write as new line
    with open(filename, "a") as text_file:
        text_file.write("%s" % self)
def append_to_file3(filename, self):
    with open(filename, "a") as text_file:
        for i in self:
            #print('writing', i)
            text_file.write(i)
def read_file(self):
    with open(self) as text_file:
        return text_file.read()
def read_file_lines(self):
    with open(self) as text_file:
        return text_file.readlines()
def delete_last_line(filename):
    lines = read_file_lines(filename)
    print(len(lines))
    lines = lines[:-1]
    print(len(lines))
    write_to_file(filename, '')
    for i in lines:
        print('appending', i)
        append_to_file2(filename, i)

if __name__ == '__main__':
    f = 'search_output.txt'
    #print(read_file(f))
    lines = read_file_lines(f)
    lines = lines[:-1]
    print(lines)
    write_to_file(f, '')
    for i in lines:
        append_to_file2(f, i)
''' How to Call examples
Import write_output

# write
t = 'write test'
write_to_file(t)

# append
a = 'append test'
append_to_file(a)

# read
f = 'Output.txt'
print(read_file(f))
'''
