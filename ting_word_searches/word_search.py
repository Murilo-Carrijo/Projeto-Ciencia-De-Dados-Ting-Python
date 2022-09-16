from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    """Verifica ocorrencia da palavra"""
    occurrences = []
    result = []
    file = txt_importer(instance._data[0])
    list = enumerate(file)

    for index, line in list:
        if word.lower() in line.lower():
            occurrences.append({'linha': index + 1})

    if occurrences != []:
        result.append({
            "palavra": word,
            "arquivo": instance._data[0],
            "ocorrencias": occurrences
        })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    occurrences = []
    result = []
    file = txt_importer(instance._data[0])
    list = enumerate(file)

    for index, line in list:
        if word.lower() in line.lower():
            occurrences.append({
                'linha': index + 1,
                'conteudo': line
            })

    if occurrences != []:
        result.append({
            "palavra": word,
            "arquivo": instance._data[0],
            "ocorrencias": occurrences
        })

    return result
