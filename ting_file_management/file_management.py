import sys


def txt_importer(path_file: str):
    try:
        if not path_file.__contains__(".txt"):
            print("Formato inválido", file=sys.stderr)
        with open(path_file, "r") as file:
            return list(file.read().splitlines())
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
