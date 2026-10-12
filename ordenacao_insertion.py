def insertion_sort_miniaturas(lista, sentido="menor"):
    """
    sentido="menor" -> Ordem Crescente (Menor para o Maior)
    sentido="maior" -> Ordem Decrescente (Maior para o Menor)
    """
    n = len(lista) # definir o tamanho
    
    for i in range(1, n): # começa a percorrer a lista a partir do 2° elemento 
        carrinho_atual = lista[i] # seleciona e isola o produto que está sendo avaliado nesta rodada
        preco_atual = carrinho_atual['preco'] # acessa e salva o valor contido na chave ['preco'] do dicionário.
        
        j = i - 1 # começa a variável j apontando p/ o índice do elem. à esquerda do carrinho_atual
        
        
        if sentido == "menor": # criamos uma condição flexível
            
            deve_deslocar = lambda preco_lista: preco_lista > preco_atual # empurra os mais caros para a direita (menor preço)
        else:  
            deve_deslocar = lambda preco_lista: preco_lista < preco_atual # empurra os mais baratos para a direita (maior preço)

        while j >= 0 and deve_deslocar(lista[j]['preco']): # Executa o deslocamento enquanto as duas regras brutas forem verdadeiras
            lista[j + 1] = lista[j]
            j -= 1
            
        lista[j + 1] = carrinho_atual