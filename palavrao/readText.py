def read_text():
    citacoes = open("C:\Phyton\palavrao\txt\SAFIRA_01_01042017_30042017_EFD_ICMSIPI.txt")
    conteudoTexto = citacoes.read()
    print(conteudoTexto)
    citacoes.close()

read_text()
