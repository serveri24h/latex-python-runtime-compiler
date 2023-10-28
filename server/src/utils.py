import io
from typing import Tuple
from copy import deepcopy

def write_to_latexfile(filepath:str, s:str | None, location: int = 0):
    if s is None:
        raise Exception(f"'{s}' not allowed")
    with open(filepath, "rb+") as f:
        f.seek(location)
        contents_before = f.read(location).decode('utf')
        f.seek(location)
        contents_after = s + contents_before
        f.write(contents_after.encode("utf-8"))
        return location+len(s)


def create_equeation(s:str):
    return "\n".join([
        r"\begin{equation}",
        s,
        r"\end{equation}"
    ])

def parse_input(s:str)-> Tuple[str | None, str | None]:
    if len(s)<1:
        return None, None
    if s[0] == "%":
        print(s)
        parts = s.split(" ")
        match parts[0][1:].strip():
            case "":
                return None, None
            case "eq":
                return "write", create_equeation("".join(parts[1:]))
            case "q":
                return "quit", None
            case "c":
                return "compile", None
    return "write", s

def get_file_location(filepath:str):

    with open(filepath, "r") as f:
        lines = f.readlines()
    
    def _check(check_str: str, reverse: bool = False) -> int | None:
        n_bytes = 0
        check_len = len(check_str)
        if reverse:
            lines.reverse()
        for i,line in enumerate(lines):
            n_bytes += len(line)
            print(i,line, n_bytes)
            if len(line)>0 and line[0]=="%":
                if line[:check_len]==check_str:
                    return n_bytes

        print("täällä vitut", lines)
    
    start_check = r"%autom: first-row"
    end_check = r"%autom: last-row"
    return _check(start_check), None