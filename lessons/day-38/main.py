from io import StringIO

sample_file = StringIO("Python makes\nsmall tools.\n")
with sample_file as file:
    contents = file.read()
print(contents, end="")
