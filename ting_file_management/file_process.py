import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if path_file not in instance.queue:
        text_imp = txt_importer(path_file)
        instance.enqueue(path_file)
        out_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(text_imp),
            "linhas_do_arquivo": text_imp
        }
        print(out_dict, file=sys.stdout)


def remove(instance):
    try:
        path_file = instance.queue[0]
        if len(instance.queue) == 0:
            print("Não há elementos", file=sys.stdout)
        instance.dequeue()
        print(f"Arquivo {path_file} removido com sucesso", file=sys.stdout)
    except IndexError:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    try:
        path_file = instance.queue[position]
        text_imp = txt_importer(path_file)
        out_dict = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(text_imp),
            "linhas_do_arquivo": text_imp
        }
        print(out_dict, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
