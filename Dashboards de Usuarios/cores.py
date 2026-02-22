
class Cores:
    # Resetar
    resetar = "\033[0m"

    # Estilos de Texto
    negrito = "\033[1m"
    italico = "\033[3m"
    sublinhado = "\033[4m"
    invertido = "\033[7m"

    # Cores de Texto Normais
    preto = "\033[30m"
    vermelho = "\033[31m"
    verde = "\033[32m"
    amarelo = "\033[33m"
    azul = "\033[34m"
    magenta = "\033[35m"
    ciano = "\033[36m"
    branco = "\033[37m"

    # Cores de Texto Brilhantes
    preto_claro = "\033[90m"
    vermelho_claro = "\033[91m"
    verde_claro = "\033[92m"
    amarelo_claro = "\033[93m"
    azul_claro = "\033[94m"
    magenta_claro = "\033[95m"
    ciano_claro = "\033[96m"
    branco_claro = "\033[97m"

    # Cores de Fundo
    fundo_preto = "\033[40m"
    fundo_vermelho = "\033[41m"
    fundo_verde = "\033[42m"
    fundo_amarelo = "\033[43m"
    fundo_azul = "\033[44m"
    fundo_magenta = "\033[45m"
    fundo_ciano = "\033[46m"
    fundo_branco = "\033[47m"

    # Cores de Fundo Brilhantes
    fundo_preto_claro = "\033[100m"
    fundo_vermelho_claro = "\033[101m"
    fundo_verde_claro = "\033[102m"
    fundo_amarelo_claro = "\033[103m"
    fundo_azul_claro = "\033[104m"
    fundo_magenta_claro = "\033[105m"
    fundo_ciano_claro = "\033[106m"
    fundo_branco_claro = "\033[107m"


# Exemplo de uso
if __name__ == "__main__":
    print(Cores.verde + "Texto em verde" + Cores.resetar)
    print(Cores.vermelho_claro + "Texto em vermelho claro" + Cores.resetar)
    print(Cores.fundo_azul + Cores.branco + "Branco com fundo azul" + Cores.resetar)
