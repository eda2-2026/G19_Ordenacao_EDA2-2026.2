## 💻 Sobre o Projeto

Este projeto criado para aplicar fundamentos de orientação a objetos, no qual consiste no desenvolvimento de um site de vendas de miniaturas de carros. O objetivo principal do desenvolvimento foi aplicar conceitos acadêmicos de Estruturas de Dados e Algoritmos de Ordenação em um cenário prático, utilizando uma arquitetura brutas para demonstrar o domínio da lógica de programação.

## 👥 Alunos Integrantes

*   **[Cauã Nicolas Pereira de Oliveira]** - *231026670*
*   **[João Lucas Ramos dos Reis]** - *211061930*


## 🎥 Vídeo de Apresentação do Projeto

Produzimos um vídeo demonstrativo detalhando o funcionamento prático da nossa loja *Garage Models*, o reaproveitamento da estrutura criada em Orientação a Objetos e a explicação da lógica brute do algoritmo **Insertion Sort** aplicada aos filtros de preço.

▶️ **[Clique aqui para assistir](LINK_DO_VIDEO_AQUI)**

> 💡 *Nota: Caso o link acima não funcione diretamente, você também pode copiar e colar a seguinte URL no seu navegador:*  
> `LINK_DO_VIDEO_AQUI`

## 🚀 Funcionalidades do Sistema

• Catálogo Dinâmico: Exibição modular de miniaturas separadas automaticamente entre categorias (Carros e Motos).
• Filtro e Ordenação Bruta: Mecanismo integrado na interface que reordena os produtos dinamicamente a partir da escolha do usuário.


## 🧠 O Algoritmo: Insertion Sort

Para a ordenação do catálogo (**menor e maior preço**), foi implementado o algoritmo Insertion Sort (Ordenação por Inserção) de forma totalmente artesanal no backend, sem o uso de funções nativas de ordenação da linguagem Python (como .sort() ou sorted()). 

Justificativa de Escolha Econômica e Técnica

Para a banca examinadora e avaliação acadêmica, a escolha do Insertion Sort fundamentou-se nos seguintes pilares da ciência da computação:
1. Alta Eficiência Prática para Pequenos Volumes: Embora o algoritmo possua complexidade assintótica de pior caso (O(n²)), para coleções pequenas de dados (como o catálogo inicial de treino), ele apresenta constantes de tempo menores e supera algoritmos avançados (como o Quick Sort) por evitar o overhead de pilhas de chamadas recursivas.
2. Estabilidade Garantida: O Insertion Sort é um algoritmo estável. No contexto de um e-commerce, isso garante que se dois produtos possuírem exatamente o mesmo preço, eles manterão estritamente a ordem de relevância ou ID original em que foram cadastrados, prevenindo comportamentos imprevisíveis na interface do usuário.
3. Complexidade de Espaço Extra O(1): A ordenação opera diretamente sobre as referências da lista (in-place), economizando recursos de memória do servidor de aplicação.



# 📄 Merge Sort — Documentação da Execução

**Projeto:** Garage Models | **Disciplina:** ED2 — Estrutura de Dados e Algoritmos 2

---

## 🧠 O que é o Merge Sort?
O Merge Sort é um algoritmo de ordenação baseado na estratégia de **Dividir para Conquistar** (*Divide and Conquer*).

A ideia principal é simples:
> *"Se eu não consigo ordenar uma lista grande de uma vez, eu divido ela em partes menores até chegar em pedaços tão pequenos que já estejam ordenados por natureza — e aí eu junto tudo na ordem certa."*

---

## ⚙️ Como funciona: as 3 Fases

### Fase 1 — DIVISÃO 🔪
A função divide a lista ao meio recursivamente até que cada sublista tenha apenas 1 elemento (um elemento sozinho está sempre "ordenado").

```python
meio = len(lista) // 2
esquerda = lista[:meio]
direita  = lista[meio:]

merge_sort_miniaturas(esquerda, sentido)  # recursão
merge_sort_miniaturas(direita,  sentido)  # recursão
```

### Fase 2 — CONQUISTA (Mesclagem) 🔀
Depois de dividir, ele mescla as sublistas comparando os elementos e colocando-os em ordem.

```python
while i < len(esquerda) and j < len(direita):
    nome_esq = esquerda[i]['nome'].lower()
    nome_dir = direita[j]['nome'].lower()

    if sentido == "crescente":
        condicao = nome_esq <= nome_dir   # A → Z
    else:
        condicao = nome_esq >= nome_dir   # Z → A

    if condicao:
        lista[k] = esquerda[i]
        i += 1
    else:
        lista[k] = direita[j]
        j += 1
    k += 1
```

### Fase 3 — COLETA DOS RESTOS 🧹
Após a mesclagem, elementos que sobraram de um dos lados são copiados para a lista final.

```python
while i < len(esquerda):     # sobras da esquerda
    lista[k] = esquerda[i]
    i += 1
    k += 1

while j < len(direita):      # sobras da direita
    lista[k] = direita[j]
    j += 1
    k += 1
```

---

## 🎬 Execução Passo a Passo — Exemplo Real com Miniaturas

Usando 4 carros do catálogo como exemplo:
**Lista inicial:** `["Porsche 911", "BMW M5", "Audi A4", "Honda NSX"]`

### 🔪 FASE 1: Divisões

```text
Nível 0 (lista completa):
["Porsche 911", "BMW M5", "Audi A4", "Honda NSX"]
                    ↓ meio = 2
         ┌──────────────────────┐
         ↓                      ↓
["Porsche 911", "BMW M5"]   ["Audi A4", "Honda NSX"]
        ↓ meio = 1                   ↓ meio = 1
   ┌─────────┐                  ┌─────────┐
   ↓         ↓                  ↓         ↓
["Porsche"] ["BMW"]          ["Audi"]  ["Honda"]
      ↑           ↑               ↑         ↑
   tamanho 1  tamanho 1       tamanho 1  tamanho 1
   (base da recursão — parar aqui!)
```

### 🔀 FASE 2: Mesclagens (subindo a recursão)

**Mesclagem 1: `["Porsche"]` + `["BMW"]`**

| Passo | Compara | Resultado |
| :---: | :--- | :--- |
| **1** | `"porsche"` vs `"bmw"` | `"bmw"` < `"porsche"` → BMW vai primeiro |
| **2** | Só sobrou `"porsche"` | Porsche vai por último |

✅ **Resultado:** `["BMW M5", "Porsche 911"]`

**Mesclagem 2: `["Audi"]` + `["Honda"]`**

| Passo | Compara | Resultado |
| :---: | :--- | :--- |
| **1** | `"audi"` vs `"honda"` | `"audi"` < `"honda"` → Audi vai primeiro |
| **2** | Só sobrou `"honda"` | Honda vai por último |

✅ **Resultado:** `["Audi A4", "Honda NSX"]`

**Mesclagem Final: `["BMW M5", "Porsche 911"]` + `["Audi A4", "Honda NSX"]`**

| Passo | Compara | Vencedor | Lista até agora |
| :---: | :--- | :---: | :--- |
| **1** | `"bmw"` vs `"audi"` | `audi` | `[Audi A4]` |
| **2** | `"bmw"` vs `"honda"`| `bmw` | `[Audi A4, BMW M5]` |
| **3** | `"porsche"` vs `"honda"`| `honda`| `[Audi A4, BMW M5, Honda NSX]` |
| **4** | Só sobrou `"porsche"` | `porsche`| `[Audi A4, BMW M5, Honda NSX, Porsche 911]` |

✅ **Resultado Final:** `["Audi A4", "BMW M5", "Honda NSX", "Porsche 911"]`

---

## 🔤 Por que funciona com letras?

O Python compara strings letra por letra usando a tabela Unicode. Cada letra tem um número (ex: `'a'=97`, `'b'=98`, `'z'=122`). A comparação é feita assim:

```python
"audi" < "bmw"      # True → 'a'(97) < 'b'(98) ✅
"bmw"  < "honda"    # True → 'b'(98) < 'h'(104) ✅
"honda" < "porsche" # True → 'h'(104) < 'p'(112) ✅
```

Se a primeira letra for igual, vai para a segunda:
```python
"honda" < "hyundai" # 'h'=='h' → compara 'o'(111) vs 'y'(121) → True ✅
```

O `.lower()` garante que `"BMW"` e `"bmw"` sejam tratados igual:
```python
"BMW".lower()   == "bmw"   # 'b'=98
"Audi".lower()  == "audi"  # 'a'=97  →  'a' < 'b'  →  Audi vem primeiro ✅
```

---

## 📊 Complexidade

| Métrica | Merge Sort (você) | Insertion Sort (amigo) |
| :--- | :---: | :---: |
| **Pior caso** | $O(N \log N)$ | $O(N^2)$ |
| **Melhor caso** | $O(N \log N)$ | $O(N)$ |
| **Caso médio** | $O(N \log N)$ | $O(N^2)$ |
| **Memória extra** | $O(N)$ | $O(1)$ |
| **Estável?** | ✅ Sim | ✅ Sim |

**Por que $O(N \log N)$?**
A cada nível de recursão, o algoritmo processa $N$ elementos no total.
E o número de níveis é $\log_2(N)$ — porque dividimos ao meio sempre.
Então: $N$ elementos $\times \log_2(N)$ níveis = $O(N \log N)$

---

## 🔗 Integração no Projeto Flask

```text
Usuário clica "Ordem Alfabética (A→Z)" no site
            ↓
HTML envia: GET /?ordem=alfabetica_az
            ↓
routes.py captura: ordem = request.args.get('ordem')
            ↓
if ordem == "alfabetica_az":
    merge_sort_miniaturas(lista_produtos, sentido="crescente")
            ↓
ordenacao_merge.py executa o Merge Sort na lista
            ↓
Flask renderiza o index.html com os produtos já ordenados
```

---

## 📁 Arquivos do Projeto

| Arquivo | Função |
| :--- | :--- |
| `ordenacao_merge.py` | Implementação do Merge Sort |
| `ordenacao_insertion.py` | Implementação do Insertion Sort (amigo) |
| `routes.py` | Rotas Flask que chamam os algoritmos |
| `templates/index.html` | Interface com o `<select>` de ordenação |

> *Documentação gerada para apresentação da disciplina ED2 — Estrutura de Dados e Algoritmos 2.*

## 🛠️ Tecnologias Utilizadas

* **Python** (Versão 3.x ou superior)
* **Flask** (Framework Web micro)

## 🔧 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação na sua máquina local:

### 1. Clonar o repositório
```bash
git clone https://github.com/CauaNicolas/Garage_Models
```

### 2. Criar e ativar um ambiente virtual (Recomendado)
```bash
# No Windows:
python -m venv venv
.\venv\Scripts\activate

# No Linux/macOS:
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar o Flask
```bash
pip install flask
```

### 4. Rodar a aplicação
Você pode iniciar o servidor utilizando o comando oficial do Flask:
```bash
flask --app app run --debug
ou
python app.py

```

### 5. Acessar no navegador
Abra o seu navegador e acesse o endereço local gerado:
```text
http://127.0.0.1:5000
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
