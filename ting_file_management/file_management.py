from os import path
import sys


def txt_importer(path_file):
    """Importando o arquivo em formato txt"""
    if not path.exists(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
    
    if path_file.endswith("txt"):
        with open(path_file) as file:
            return file.read().split("\n")
    return sys.stderr.write("Formato inválido\n")
