from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.file_management import txt_importer
import pytest


def mock():
    path_files = [
        "statics/arquivo_teste.txt",
        "statics/novo_paradigma_globalizado-min.txt",
    ]
    return [{
            "nome_do_arquivo": p,
            "qtd_linhas": len(txt_importer(p))
            } for p in path_files]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    files_mocked = mock()
    for f in files_mocked:
        priority_queue.enqueue(f)
    assert len(priority_queue.high_priority.queue) == 1

    searched = priority_queue.search(1)

    assert searched == {
        'nome_do_arquivo': 'statics/novo_paradigma_globalizado-min.txt',
        'qtd_linhas': 19}

    priority_queue.dequeue()

    assert len(priority_queue.high_priority.queue) == 0

    with pytest.raises(
        IndexError
    ):
        priority_queue.search(99)
