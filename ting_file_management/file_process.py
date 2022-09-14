from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Pre-processando o arquivo """
    file = txt_importer(path_file)

    if path_file not in instance._data:
        instance.enqueue(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    return sys.stdout.write(str(result))


def remove(instance):
    """Removendo arquivo"""
    if len(instance) == 0:
        return sys.stdout.write(f"Não há elementos\n")

    removed_file = instance.dequeue()
    return sys.stdout.write(str(f"Arquivo {removed_file} removido com sucesso\n"))


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
