from functools import lru_cache
import csv


@lru_cache
def read(path):
    list_of_jobs = []
    with open(path) as file:
        jobs = csv.DictReader(file)
        # o DictReader é um leitor baseado em dicionários
        # a linha de cabeçaçhos é utilizada como chave do dicionário
        for job in jobs:
            list_of_jobs.append(job)
    return list_of_jobs
