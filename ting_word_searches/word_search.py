from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    text = txt_importer(instance.queue[0])
    if not any(word.lower() in line.lower() for line in text):
        return []
    return [
        {
            "palavra": word,
            "arquivo": instance.queue[0],
            "ocorrencias": [{"linha": text.index(d) + 1} for d in text
                            if word.lower() in d.lower()]
        }
    ]


def search_by_word(word, instance):
    text = txt_importer(instance.queue[0])
    if not any(word.lower() in line.lower() for line in text):
        return []
    return [
        {
            "palavra": word,
            "arquivo": instance.queue[0],
            "ocorrencias": [{
                "linha": text.index(d) + 1,
                "conteudo": d
            }
                            for d in text
                            if word.lower() in d.lower()]
        }
    ]
