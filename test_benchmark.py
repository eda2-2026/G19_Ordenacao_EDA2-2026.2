import sys
import os
import copy
import timeit

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ordenacao_merge import merge_sort_miniaturas
from ordenacao_insertion import insertion_sort_miniaturas

# ──────────────────────────────────────────────
# Dataset real do projeto
# ──────────────────────────────────────────────
MINIATURAS_BD = [
    {"id": 1,  "nome": "Nissan Skyline GT-R R34 2000",  "tipo": "carro", "preco": 99.90},
    {"id": 2,  "nome": "BMW M5 F90 2022",               "tipo": "carro", "preco": 109.90},
    {"id": 3,  "nome": "Honda Acura NSX 2018",          "tipo": "carro", "preco": 99.90},
    {"id": 4,  "nome": "Porsche 911 GT3 RS 2023",       "tipo": "carro", "preco": 149.90},
    {"id": 5,  "nome": "Honda Type R 2023",             "tipo": "carro", "preco": 79.90},
    {"id": 6,  "nome": "BMW R1250 GS 2022",             "tipo": "moto",  "preco": 79.90},
    {"id": 7,  "nome": "Honda CBR1000RR-R 2022",        "tipo": "moto",  "preco": 69.90},
    {"id": 8,  "nome": "Honda Hornet 2012",             "tipo": "moto",  "preco": 89.90},
    {"id": 9,  "nome": "Yamaha YZF R1 2013",            "tipo": "moto",  "preco": 149.90},
    {"id": 10, "nome": "Renault Kwid 2019",             "tipo": "carro", "preco": 59.90},
    {"id": 11, "nome": "Volkswagen Passat 2017",        "tipo": "carro", "preco": 89.90},
    {"id": 12, "nome": "Honda CR-V 2020",               "tipo": "carro", "preco": 99.90},
    {"id": 13, "nome": "Toyota Corolla 2019",           "tipo": "carro", "preco": 79.90},
    {"id": 14, "nome": "Ford Mustang 2020",             "tipo": "carro", "preco": 149.90},
    {"id": 15, "nome": "Hyundai Elantra 2017",          "tipo": "carro", "preco": 69.90},
    {"id": 16, "nome": "Jaguar XF S-Type 2018",         "tipo": "carro", "preco": 149.90},
    {"id": 17, "nome": "Audi A1 Sportback 2018",        "tipo": "carro", "preco": 89.90},
    {"id": 18, "nome": "Audi A4 2018",                  "tipo": "carro", "preco": 109.90},
    {"id": 19, "nome": "Audi TT RS 2018",               "tipo": "carro", "preco": 109.90},
    {"id": 20, "nome": "Mercedes-Benz ML 250 2015",     "tipo": "carro", "preco": 89.90},
    {"id": 21, "nome": "Mercedes-Benz Classe C 2019",   "tipo": "carro", "preco": 109.90},
    {"id": 22, "nome": "Mercedes G63 2021",             "tipo": "carro", "preco": 149.90},
    {"id": 23, "nome": "Yamaha MT-10 2017",             "tipo": "moto",  "preco": 149.90},
    {"id": 24, "nome": "Honda CBR600RR 2019",           "tipo": "moto",  "preco": 109.90},
    {"id": 25, "nome": "Honda VFR800 2015",             "tipo": "moto",  "preco": 89.90},
    {"id": 26, "nome": "Kawasaki Ninja 300 2016",       "tipo": "moto",  "preco": 79.90},
    {"id": 27, "nome": "Yamaha FZ MT-09 2023",          "tipo": "moto",  "preco": 109.90},
]

REPETICOES = 10_000


def mostrar_resultado(lista, chave):
    valores = [item[chave] for item in lista]
    if len(valores) > 6:
        preview = valores[:3] + ["..."] + valores[-3:]
    else:
        preview = valores
    return " → ".join(str(v) for v in preview)


def separador(titulo):
    print()
    print("=" * 62)
    print(f"  {titulo}")
    print("=" * 62)


def rodar_teste(descricao, fn_merge, fn_insertion, chave, extra_merge, extra_insertion):
    print(f"\n  📌 {descricao}")
    print(f"  {'─' * 57}")

    # Mede tempo total de N repetições (em segundos)
    tempo_merge_s = timeit.timeit(
        lambda: fn_merge(copy.deepcopy(MINIATURAS_BD), **extra_merge),
        number=REPETICOES
    )
    tempo_insertion_s = timeit.timeit(
        lambda: fn_insertion(copy.deepcopy(MINIATURAS_BD), **extra_insertion),
        number=REPETICOES
    )

    # Calcula tempo médio por execução em segundos
    media_merge     = tempo_merge_s     / REPETICOES
    media_insertion = tempo_insertion_s / REPETICOES

    # Executa uma vez para pegar o resultado ordenado
    lista_merge = copy.deepcopy(MINIATURAS_BD)
    fn_merge(lista_merge, **extra_merge)
    lista_insertion = copy.deepcopy(MINIATURAS_BD)
    fn_insertion(lista_insertion, **extra_insertion)

    print(f"  🔵 Merge Sort     → Total: {tempo_merge_s:.6f}s  |  Média: {media_merge:.8f}s")
    print(f"     Resultado: {mostrar_resultado(lista_merge, chave)}")
    print()
    print(f"  🟠 Insertion Sort → Total: {tempo_insertion_s:.6f}s  |  Média: {media_insertion:.8f}s")
    print(f"     Resultado: {mostrar_resultado(lista_insertion, chave)}")

    diff = abs(media_merge - media_insertion)
    if media_merge < media_insertion:
        vencedor, perdedor = "🔵 Merge Sort", "Insertion Sort"
    else:
        vencedor, perdedor = "🟠 Insertion Sort", "Merge Sort"

    porcentagem = (diff / max(media_merge, media_insertion)) * 100
    print(f"\n  🏆 Mais rápido: {vencedor}  ({porcentagem:.1f}% mais veloz que {perdedor})")


# Insertion Sort adaptado para comparação justa na ordenação alfabética
def insertion_sort_por_nome(lista, sentido="az"):
    n = len(lista)
    for i in range(1, n):
        atual = lista[i]
        chave = atual["nome"].lower()
        j = i - 1
        if sentido == "az":
            while j >= 0 and lista[j]["nome"].lower() > chave:
                lista[j + 1] = lista[j]
                j -= 1
        else:
            while j >= 0 and lista[j]["nome"].lower() < chave:
                lista[j + 1] = lista[j]
                j -= 1
        lista[j + 1] = atual


# Merge Sort adaptado para comparação justa na ordenação numérica
def merge_sort_por_preco(lista, sentido="crescente"):
    if len(lista) > 1:
        meio = len(lista) // 2
        esq = lista[:meio]
        dir_ = lista[meio:]
        merge_sort_por_preco(esq, sentido)
        merge_sort_por_preco(dir_, sentido)
        i = j = k = 0
        while i < len(esq) and j < len(dir_):
            if sentido == "crescente":
                cond = esq[i]["preco"] <= dir_[j]["preco"]
            else:
                cond = esq[i]["preco"] >= dir_[j]["preco"]
            if cond:
                lista[k] = esq[i]; i += 1
            else:
                lista[k] = dir_[j]; j += 1
            k += 1
        while i < len(esq):
            lista[k] = esq[i]; i += 1; k += 1
        while j < len(dir_):
            lista[k] = dir_[j]; j += 1; k += 1


# ══════════════════════════════════════════════════════════
#  INÍCIO
# ══════════════════════════════════════════════════════════
print()
print("╔════════════════════════════════════════════════════════════╗")
print("║       COMPARAÇÃO DE ALGORITMOS — GARAGE MODELS ED2        ║")
print("║              Merge Sort  vs  Insertion Sort                ║")
print(f"║       Dataset: {len(MINIATURAS_BD)} produtos  |  {REPETICOES:,} repetições cada       ║")
print("║       Unidade: segundos (s)                                ║")
print("╚════════════════════════════════════════════════════════════╝")

separador("ORDENAÇÃO ALFABÉTICA (por nome)")

rodar_teste(
    descricao="A → Z (crescente)",
    fn_merge=merge_sort_miniaturas,
    fn_insertion=insertion_sort_por_nome,
    chave="nome",
    extra_merge={"sentido": "crescente"},
    extra_insertion={"sentido": "az"},
)

rodar_teste(
    descricao="Z → A (decrescente)",
    fn_merge=merge_sort_miniaturas,
    fn_insertion=insertion_sort_por_nome,
    chave="nome",
    extra_merge={"sentido": "decrescente"},
    extra_insertion={"sentido": "za"},
)

separador("ORDENAÇÃO NUMÉRICA (por preço)")

rodar_teste(
    descricao="Menor → Maior preço (crescente)",
    fn_merge=merge_sort_por_preco,
    fn_insertion=insertion_sort_miniaturas,
    chave="preco",
    extra_merge={"sentido": "crescente"},
    extra_insertion={"sentido": "menor"},
)

rodar_teste(
    descricao="Maior → Menor preço (decrescente)",
    fn_merge=merge_sort_por_preco,
    fn_insertion=insertion_sort_miniaturas,
    chave="preco",
    extra_merge={"sentido": "decrescente"},
    extra_insertion={"sentido": "maior"},
)

# ──────────────────────────────────────────────
# RESUMO TEÓRICO
# ──────────────────────────────────────────────
N = len(MINIATURAS_BD)
print()
print("=" * 62)
print("  RESUMO TEÓRICO")
print("=" * 62)
print(f"  Dataset atual:  N = {N} elementos")
print(f"  Merge Sort     → O(N log N) ≈ {N} × {N.bit_length()} = {N * N.bit_length()} operações")
print(f"  Insertion Sort → O(N²)      = {N}² = {N**2} operações (pior caso)")
print()
print("  Projeção com datasets maiores:")
print("  ┌─────────┬──────────────────┬─────────────────────┐")
print("  │    N    │  Merge (N log N) │  Insertion Sort (N²)│")
print("  ├─────────┼──────────────────┼─────────────────────┤")
print("  │      27 │              135 │                 729 │")
print("  │   1.000 │           10.000 │           1.000.000 │")
print("  │  10.000 │          130.000 │         100.000.000 │")
print("  │ 100.000 │        1.700.000 │      10.000.000.000 │")
print("  └─────────┴──────────────────┴─────────────────────┘")
print()
print("  💡 Com N=27 as diferenças são mínimas em segundos.")
print("     Em escala real, o Merge Sort é exponencialmente melhor.")
print("=" * 62)
print()
