from urllib.request as 

def read_text():
    citacoes = open(r"C:\Phyton\palavrao\txt\SAFIRA_01_01042017_30042017_EFD_ICMSIPI.txt")
    conteudoTexto = citacoes.read()
    print(conteudoTexto)
    citacoes.close()
    check_profanity(conteudoTexto)

def check_profanity(txt_para_verificar):
    s = ur.urlopen("http://www.wdylike.appspot.com/?q="+txt_para_verificar)
    sl = s.read()
    print(sl)
        
    
read_text()
