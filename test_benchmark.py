import sys
import os
import copy
import timeit
import random
import string

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ordenacao_merge import merge_sort_miniaturas
from ordenacao_insertion import insertion_sort_miniaturas

# ──────────────────────────────────────────────
# Dataset real do projeto (N=27)
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

# Marcas e modelos base para gerar mocks realistas
MARCAS = [
    "Audi", "BMW", "Chevrolet", "Dodge", "Ferrari", "Ford", "Honda",
    "Hyundai", "Jaguar", "Kawasaki", "Kia", "Lamborghini", "Lexus",
    "Mazda", "Mercedes", "Mitsubishi", "Nissan", "Peugeot", "Porsche",
    "Renault", "Subaru", "Suzuki", "Toyota", "Volkswagen", "Volvo",
    "Yamaha", "Ducati", "Triumph", "Harley", "Royal Enfield",
]
MODELOS = [
    "GT-R", "Turbo", "Sport", "RS", "AMG", "M3", "Type-R", "GTI",
    "Nismo", "Shelby", "Cobra", "Viper", "Hellcat", "STI", "EVO",
    "Z06", "Cayman", "Boxster", "Supra", "NSX", "Civic", "Corolla",
    "Ninja", "CBR", "YZF", "GSX", "Hayabusa", "Panigale", "Fireblade",
]

def gerar_mock(n_total):
    """Gera uma lista de n_total produtos com nomes e preços aleatórios."""
    random.seed(42)  # Seed fixo para resultados reproduzíveis
    base = list(MINIATURAS_BD)  # começa com os 27 reais
    extra_necessario = max(0, n_total - len(base))
    for i in range(extra_necessario):
        marca  = random.choice(MARCAS)
        modelo = random.choice(MODELOS)
        ano    = random.randint(2000, 2024)
        preco  = round(random.uniform(29.90, 499.90), 2)
        base.append({
            "id":    len(base) + 1,
            "nome":  f"{marca} {modelo} {ano}",
            "tipo":  random.choice(["carro", "moto"]),
            "preco": preco,
        })
    random.shuffle(base)  # embaralha para o pior caso
    return base[:n_total]


# ──────────────────────────────────────────────
# Algoritmos auxiliares para comparação justa
# ──────────────────────────────────────────────
def insertion_sort_por_nome(lista, sentido="az"):
    n = len(lista)
    for i in range(1, n):
        atual = lista[i]
        chave = atual["nome"].lower()
        j = i - 1
        if sentido == "az":
            while j >= 0 and lista[j]["nome"].lower() > chave:
                lista[j + 1] = lista[j]; j -= 1
        else:
            while j >= 0 and lista[j]["nome"].lower() < chave:
                lista[j + 1] = lista[j]; j -= 1
        lista[j + 1] = atual

def merge_sort_por_preco(lista, sentido="crescente"):
    if len(lista) > 1:
        meio = len(lista) // 2
        esq, dir_ = lista[:meio], lista[meio:]
        merge_sort_por_preco(esq, sentido)
        merge_sort_por_preco(dir_, sentido)
        i = j = k = 0
        while i < len(esq) and j < len(dir_):
            cond = esq[i]["preco"] <= dir_[j]["preco"] if sentido == "crescente" else esq[i]["preco"] >= dir_[j]["preco"]
            if cond: lista[k] = esq[i]; i += 1
            else:    lista[k] = dir_[j]; j += 1
            k += 1
        while i < len(esq):  lista[k] = esq[i];  i += 1; k += 1
        while j < len(dir_): lista[k] = dir_[j]; j += 1; k += 1


# ──────────────────────────────────────────────
# Função de benchmark por tamanho de dataset
# ──────────────────────────────────────────────
def benchmark_escala(tamanho, fn_merge, fn_insertion, extra_merge, extra_insertion, repeticoes):
    dataset = gerar_mock(tamanho)
    t_merge = timeit.timeit(
        lambda: fn_merge(copy.deepcopy(dataset), **extra_merge),
        number=repeticoes
    )
    t_insertion = timeit.timeit(
        lambda: fn_insertion(copy.deepcopy(dataset), **extra_insertion),
        number=repeticoes
    )
    media_m = t_merge     / repeticoes
    media_i = t_insertion / repeticoes
    vencedor = "🔵 Merge" if media_m < media_i else "🟠 Insertion"
    diff_pct = abs(media_m - media_i) / max(media_m, media_i) * 100
    return media_m, media_i, vencedor, diff_pct


def imprimir_tabela_escala(titulo, fn_merge, fn_insertion, extra_merge, extra_insertion):
    print(f"\n  {'─' * 57}")
    print(f"  📊 {titulo}")
    print(f"  {'─' * 57}")
    print(f"  {'N':>8}  │  {'Merge Sort (s)':>16}  │  {'Insertion (s)':>16}  │  Vencedor")
    print(f"  {'─'*8}──┼──{'─'*16}──┼──{'─'*16}──┼──{'─'*20}")

    tamanhos = [27, 100, 300, 500, 1000, 2000, 5000]
    for n in tamanhos:
        reps = max(100, 10_000 // n)  # menos repetições para N grande
        m, i, venc, pct = benchmark_escala(n, fn_merge, fn_insertion, extra_merge, extra_insertion, reps)
        print(f"  {n:>8}  │  {m:>16.8f}  │  {i:>16.8f}  │  {venc}  ({pct:.1f}%)")

    print(f"  {'─' * 57}")


# ══════════════════════════════════════════════════════════
#  INÍCIO
# ══════════════════════════════════════════════════════════
print()
print("╔════════════════════════════════════════════════════════════╗")
print("║       COMPARAÇÃO DE ALGORITMOS — GARAGE MODELS ED2        ║")
print("║              Merge Sort  vs  Insertion Sort                ║")
print("║       Múltiplos tamanhos de dataset  |  Unidade: segundos  ║")
print("╚════════════════════════════════════════════════════════════╝")
print()
print("  ⏳ Aguarde — rodando testes com múltiplos N...")

print()
print("=" * 62)
print("  ESCALA: ORDENAÇÃO ALFABÉTICA (por nome)  A → Z")
print("=" * 62)
imprimir_tabela_escala(
    "Merge Sort vs Insertion Sort — A → Z",
    fn_merge=merge_sort_miniaturas,
    fn_insertion=insertion_sort_por_nome,
    extra_merge={"sentido": "crescente"},
    extra_insertion={"sentido": "az"},
)

print()
print("=" * 62)
print("  ESCALA: ORDENAÇÃO NUMÉRICA (por preço)  Crescente")
print("=" * 62)
imprimir_tabela_escala(
    "Merge Sort vs Insertion Sort — Menor → Maior preço",
    fn_merge=merge_sort_por_preco,
    fn_insertion=insertion_sort_miniaturas,
    extra_merge={"sentido": "crescente"},
    extra_insertion={"sentido": "menor"},
)

# ──────────────────────────────────────────────
# RESUMO TEÓRICO
# ──────────────────────────────────────────────
print()
print("=" * 62)
print("  POR QUE O INSERTION GANHA EM N PEQUENO?")
print("=" * 62)
print("""
  O Merge Sort tem um CUSTO FIXO maior por execução:
    • Cria sublistas novas (esquerda / direita) na memória
    • Faz chamadas recursivas (overhead de função)
    • Copia elementos de volta para a lista original

  O Insertion Sort é mais simples:
    • Trabalha no lugar (in-place), sem alocar memória extra
    • Sem recursão — só um while simples
    • Com N pequeno, esse "trabalho extra" do Merge domina o tempo

  O PONTO DE VIRADA acontece quando N cresce o suficiente
  para que O(N²) do Insertion supere O(N log N) do Merge.
  Na tabela acima você consegue ver exatamente onde isso ocorre!

  Complexidade comparada:
  ┌──────────────┬────────────────┬──────────────────────┐
  │      N       │  Merge (N logN)│  Insertion Sort (N²) │
  ├──────────────┼────────────────┼──────────────────────┤
  │           27 │            135 │                  729 │
  │          100 │            700 │               10.000 │
  │          500 │          4.500 │              250.000 │
  │        1.000 │         10.000 │            1.000.000 │
  │        5.000 │         60.000 │           25.000.000 │
  └──────────────┴────────────────┴──────────────────────┘
""")
print("=" * 62)
print()
