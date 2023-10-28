import io

def write_to_latexfile(f:io.TextIOBase, s:str):
    contents_before = f.read()
    contents_after = s+contents_before
    f.write(contents_after)
    