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
