from algoritmos import merge_count, mediana_das_medianas, par_mais_proximo

def menu():
    print("\n=== Visualizador de Algoritmos de Dividir e Conquistar ===")
    print("1. Contagem de Inversões")
    print("2. Mediana das Medianas")
    print("3. Par de Pontos Mais Próximos")
    print("0. Sair")
    return input("Escolha uma opção: ")

def ler_lista():
    entrada = input("Digite uma lista de números separados por espaço: ")
    return list(map(int, entrada.strip().split()))

def ler_pontos():
    print("Digite os pontos no formato x y, um por linha. Linha vazia para terminar.")
    print("Exemplo: 1.5 2.3")
    pontos = []
    while True:
        linha = input()
        if not linha.strip():
            break
        try:
            partes = linha.strip().split()
            if len(partes) != 2:
                print("Erro: Digite exatamente dois números (x y). Tente novamente.")
                continue
            x, y = map(float, partes)
            pontos.append((x, y))
        except ValueError:
            print("Erro: Digite números válidos. Tente novamente.")
            continue
    return pontos

def main():
    while True:
        opcao = menu()
        if opcao == '1':
            lista = ler_lista()
            print("\nPasso a passo da contagem de inversões:")
            _, inversoes = merge_count(lista)
            print(f"\nTotal de inversões: {inversoes}\n")
        elif opcao == '2':
            lista = ler_lista()
            print("\nPasso a passo da Mediana das Medianas:")
            mediana = mediana_das_medianas(lista)
            print(f"\nMediana das Medianas: {mediana}\n")
        elif opcao == '3':
            pontos = ler_pontos()
            print("\nPasso a passo do Par de Pontos Mais Próximos:")
            par, dist = par_mais_proximo(pontos)
            print(f"\nPar mais próximo: {par} com distância {dist:.2f}\n")
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
