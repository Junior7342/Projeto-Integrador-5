#------------VARIAVEIS------------
lista_cpf = []
usuario_pf = dict()

usuario_pf_artista = dict()
usuario_pf_album = dict()
usuario_pf_disco_estado = dict()
usuario_pf_preco_min =  dict()
usuario_pf_preco_max = dict()

banda_registro = dict()
album_registro = dict()
estado_registro = dict()
preco_min_registro = dict()
preco_max_registro = dict()

op1 = 1
#---------------------------------


#-------------FUNÇOES-------------
def cadastrar_usuario_pf(cpf):
    nome = input("\t\t\t\tDigite aqui seu nome completo: ")
    senha = input("\t\t\t\tCrie agora uma senha com (4) quatro números: ")
    senha = int(senha)
    login = True
    lista_cpf.append(cpf)
    usuario_pf[cpf] = dict(nome=nome,cpf=cpf,senha=senha, login=login)
    print(f"\n\t\t\t\t{usuario_pf[cpf].get('nome')}, bem-vindo ao Cadê Meu Vinil?\n\t\t\t\tAproveite nosso app para achar os melhores artistas e discos de todos os tempos!")


def efetuar_login(cpf, checar_senha):

    if checar_senha == usuario_pf[cpf].get('senha'):
        login = True
        return usuario_pf[cpf].update({'login':True})

    elif checar_senha != usuario_pf[cpf].get('senha'):
        login = False


def apresentar_opcoes(cpf, login, op1):
    if login == True:
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                             Cadê Meu Vinil?                                                           ")
        print("\n")
        guardar_usuario = usuario_pf[cpf].get('nome')
        print(f"\t\t\t\t{guardar_usuario}, você está logado.\n")
        print("\t\t\t\tDigite ---- (1) caso queira procurar/adquirir um novo vinil                 2 ---- caso queira vender um vinil")
        print("\t\t\t\tDigite ---- (3) para realizar seu logout")
        op = input("\t\t\t\tDigite agora sua opção: ")
        op = int(op)

        while (op == 1 or op == 2 or op == 3) and login == True:

                    if op == 1:
                        print("\n")
                        print("\t\t\t\tDigite ---- (1) para informar a banda ou artista que deseja pesquisar       2 ---- para informar o nome do álbum ")
                        print("\t\t\t\tDigite ---- (3) para realizar seu logout")
                        op = input("\t\t\t\tDigite agora sua opção: ")
                        op = int(op)
                        if op == 2:

                                #PROCURA O ARTISTA PELO NOME DO ALBUM
                                op2 = 1
                                album = input("\t\t\t\tInforme o nome do album que deseja pesquisar: ")
                                x = 0
                                op1 = op2
                                while x < len(lista_cpf):
                                    cpf = lista_cpf[x]
                                    if album == usuario_pf_album[cpf].get(op1):
                                        print("\t\t\t\t--------------------------------------------------------------------------")
                                        print(f"\t\t\t\tO album: {usuario_pf_album[cpf].get(op1)} ---- da banda/artista: {usuario_pf_artista[cpf].get(op1)} foi encontrado!\n")
                                        print(f"\t\t\t\tO usuário do app {usuario_pf[cpf].get('nome')} tem interesse em vendê-lo pelo valor mínimo de R$ {usuario_pf_preco_min[cpf].get(op1):.2f} até o valor máximo de R$ {usuario_pf_preco_max[cpf].get(op1):.2f}.")
                                        print(f"\n\t\t\t\tDeseja contatar o usuário para fechar a transação? (S/N)")
                                        if usuario_pf[cpf].get('cpf') == cpf:
                                                            usuario_pf[cpf].update({'login':False})
                                                            break
                                    elif album != usuario_pf_album[cpf].get(op1):
                                        x+=1
                                        op1+=1
                                    else:
                                        pass

                        elif op == 2:

                                op2 = 1
                                banda = input("\t\t\t\tInforme o nome da banda ou artista que deseja pesquisar: ")

                                # --------------
                                x = 0
                                op1 = op2
                                while x < len(lista_cpf):
                                    cpf = lista_cpf[x]
                                    if banda == usuario_pf_artista[cpf].get(op1):
                                        print("\t\t\t\t--------------------------------------------------------------------------")
                                        print(f"\t\t\t\tA banda/artista: {usuario_pf_artista[cpf].get(op1)} foi encontrada!\n")
                                        print(f"\t\t\t\tO álbum disponível para venda: {usuario_pf_album[cpf].get(op1)}.")
                                        print(f"\t\t\t\tO usuário do app {usuario_pf[cpf].get('nome')} tem interesse em vendê-lo pelo valor mínimo de R$ {usuario_pf_preco_min[cpf].get(op1):.2f} até o valor máximo de R$ {usuario_pf_preco_max[cpf].get(op1):.2f}.")
                                        print(f"\n\t\t\t\tDeseja contatar o usuário para fechar a transação? (S/N)")
                                        if usuario_pf[cpf].get('cpf') == cpf:
                                                usuario_pf[cpf].update({'login': False})
                                                break
                                    elif banda != usuario_pf_artista[cpf].get(op1):
                                        x+=1
                                        op1+=1
                                    else:
                                        pass
                        elif op == 3:
                            print("\n")
                            print("\t\t\t\tLogout efetuado com sucesso.")
                            login = usuario_pf[cpf].update({'login': False})
                            return login
                        else:
                            pass


                        print("--------------------------------------------------------------------------------------------------------------------------------------")
                        print("                                                             Cadê Meu Vinil?                                                           ")
                        print("\n")
                        # print("\n")
                        print(f"\t\t\t\t{guardar_usuario}, você está logado.\n")
                        print("\t\t\t\tDigite ---- (1) caso queira procurar/adquirir um novo vinil                 2 ---- caso queira vender um vinil")
                        print("\t\t\t\tDigite ---- (3) para realizar seu logout")
                        op = int(input("\t\t\t\tDigite agora sua opção: "))
                        #--------------

                                #REGISTRA ANUNCIO DE UM ALBUM PARA A VENDA
                    elif op == 2:
                                print("\n")
                                print(f"\t\t\t\t{usuario_pf[cpf].get('nome')}, agora, você deverá preencher os dados do vinil que deseja anunciar.\n")

                                usuario_pf_artista.fromkeys([cpf])
                                banda_artista = input("\t\t\t\tQual é o nome da banda ou artista? ---- ")
                                banda_registro.fromkeys([op1])
                                banda_registro.update({op1:banda_artista})
                                usuario_pf_artista.update({cpf:banda_registro})

                                usuario_pf_album.fromkeys([cpf])
                                banda_album = input(f"\t\t\t\tQual álbum do {usuario_pf_artista[cpf].get(op1)} deseja anunciar? ---- ")
                                album_registro.fromkeys([op1])
                                album_registro.update({op1:banda_album})
                                usuario_pf_album.update({cpf:album_registro})

                                usuario_pf_disco_estado.fromkeys([cpf])
                                album_estado = input(f"\t\t\t\tQual o estado do álbum {usuario_pf_album[cpf].get(op1)}?\n\t\t\t\tExemplo: usado em bom estado; novo na embalagem, etc. ---- ")
                                estado_registro.fromkeys([op1])
                                estado_registro.update({op1:album_estado})
                                usuario_pf_disco_estado.update({cpf:estado_registro})

                                usuario_pf_preco_min.fromkeys([cpf])
                                preco_minimo = input(f"\t\t\t\tQual o valor mínimo sugerido? ---- R$ ")
                                preco_minimo = float(preco_minimo)
                                preco_min_registro.fromkeys([op1])
                                preco_min_registro.update({op1:preco_minimo})
                                usuario_pf_preco_min.update({cpf:preco_min_registro})

                                usuario_pf_preco_max.fromkeys([cpf])
                                preco_maximo = input(f"\t\t\t\tQual o valor máximo sugerido? ---- R$ ")
                                preco_maximo = float(preco_maximo)
                                preco_max_registro.fromkeys([op1])
                                preco_max_registro.update({op1:preco_maximo})
                                usuario_pf_preco_max.update({cpf:preco_max_registro})

                                print("\t\t\t\t--------------------------------------------------------------------------")
                                print("\t\t\t\tFicha técnica do álbum anunciado para venda:\n")
                                print(f"\t\t\t\tArtista: {usuario_pf_artista[cpf].get(op1)}")
                                print(f"\t\t\t\tAlbum: {usuario_pf_album[cpf].get(op1)}")
                                print(f"\t\t\t\tEstado: {usuario_pf_disco_estado[cpf].get(op1)} ")
                                print(f"\t\t\t\tPreço mínimo em R$: {usuario_pf_preco_min[cpf].get(op1):.2f} ")
                                print(f"\t\t\t\tPreço máximo em R$: {usuario_pf_preco_max[cpf].get(op1):.2f}")

                                #print("\t\t\t\t--------------------------------------------------------------------------")
                                #print("\n")
                                print("--------------------------------------------------------------------------------------------------------------------------------------")
                                #print("\n")
                                print("                                                             Cadê Meu Vinil?                                                           ")
                                print("\n")
                                #print("\n")
                                print(f"\t\t\t\t{guardar_usuario}, você está logado.\n")
                                print("\t\t\t\tDigite ---- (1) caso queira procurar/adquirir um novo vinil                 2 ---- caso queira vender um vinil")
                                print("\t\t\t\tDigite ---- (3) para realizar seu logout")
                                op = int(input("\t\t\t\tDigite agora sua opção: "))

                    #REALIZA O LOGOUT
                    elif op == 3:
                                print("\n")
                                print("\t\t\t\tLogout efetuado com sucesso.")
                                #print("\n")
                                login = usuario_pf[cpf].update({'login':False})
                                #print(f"Status: {usuario_pf[cpf].get('login')}-nome:{usuario_pf[cpf].get('nome')}")
                                return login
                    else:
                                pass


#def procurar_banda(op2, banda):
#-------------------------------

sist_op = 's'
while sist_op == 's':


    menu1 = ("                                                             Cadê Meu Vinil?                                                           ")
    menu2 = ("--------------------------------------------------------------------------------------------------------------------------------------")
    menu3 = ("                                                                                                                          ")
    menu4 = ("\t\t\t\tDigite ---- (1) para fazer login            (2) ---- para novo cadastro                     ")
    menu5 = ("\t\t\t\tDigite ---- (1) para usuário PF             (2) ---- para usuário PJ                        ")
    menu6 = ("\t\t\t\tDigite ---- (1) para informar a banda ou artista que deseja pesquisar       2 ---- para informar o nome do álbum ")
    menu7 = ("\t\t\t\tDigite ---- (3) para realizar seu logout")
    menu8 = ("\t\t\t\tDigite ---- (1) caso queira procurar/adquirir um novo vinil                 2 ---- caso queira vender um vinil")


    print("\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                             Cadê Meu Vinil?                                                           ")
    print("\n")
    #print("\n")
    print("\t\t\t\tDigite ---- (1) para fazer login            (2) ---- para novo cadastro                     ")
    op = input("\t\t\t\tDigite agora sua opção: ")
    op = int(op)

    while op == 1 or op == 2:

        #CADASTRO
        if op == 2:
            while op == 2:
                print(f"\n{menu5}")
                qt = input("\t\t\t\tDigite agora sua opção: ")
                qt = int(qt)

                #CADASTRO PF
                if qt == 1:
                    print("\n")
                    cpf = input("\t\t\t\tInforme o número completo do seu CPF sem pontos ou traços: ")
                    cpf = int(cpf)

                    #VERIFICA SE CPF JA E CADASTRADO
                    if cpf not in lista_cpf:

                        #CHAMA A FUNCAO PARA CADASTRAR NOVO USUARIO
                        cadastrar_usuario_pf(cpf)

                        login = usuario_pf[cpf].get('login')

                        #CHAMA A FUNCAO APRESENTAR OPCOES
                        apresentar_opcoes(cpf, login, op1)

                        op1 += 1
                        print("--------------------------------------------------------------------------------------------------------------------------------------")
                        print("\n")
                        print("                                                             Cadê Meu Vinil?                                                           ")
                        print("\n")
                        #print("\n")
                        print("\t\t\t\tDigite ---- (1) para fazer login            (2) ---- para novo cadastro                     ")
                        op = input("\t\t\t\tDigite agora sua opção: ")
                        op = int(op)

                    #CASO CPF ESTEJA CADASTRADO NAO PERMITE NOVO CADASTRO
                    elif cpf in lista_cpf:
                        print("\n")
                        print(f"\t\t\t\t{usuario_pf[cpf].get('nome')}, você já é cadastrado no nosso app.\n\t\t\t\tEfetue agora seu login com seu CPF ou CNPJ e senha.")
                        #print("\n")
                        print("--------------------------------------------------------------------------------------------------------------------------------------")
                        #print("\n")
                        print("                                                             Cadê Meu Vinil?                                                           ")
                        print("\n")
                        #print("\n")
                        print("\t\t\t\tDigite ---- (1) para fazer login            (2) ---- para novo cadastro                     ")
                        op = input("\n\t\t\t\tDigite agora sua opção: ")
                        op = int(op)


        elif op == 1:
            while op == 1:
                cpf = input("\n\t\t\t\tInforme o número completo do seu CPF sem pontos ou traços: ")
                cpf = int(cpf)
                checar_senha = input("\t\t\t\tInforme agora sua senha: ")
                checar_senha = int(checar_senha)
                efetuar_login(cpf, checar_senha)
                print(f"\n\t\t\t\t{usuario_pf[cpf].get('nome')}, bem-vindo novamente ao Cadê Meu Vinil!!!\n\t\t\t\tBora encontrar seu mais novo vinil???\n")
                print(menu2)
                login = usuario_pf[cpf].get('login')
                apresentar_opcoes(cpf, login, op1)
                op1 += 1
                print("--------------------------------------------------------------------------------------------------------------------------------------")
                print("                                                             Cadê Meu Vinil?                                                           ")
                print("\n")
                print("\t\t\t\tDigite ---- (1) para fazer login            (2) ---- para novo cadastro                     ")
                #print(menu3)
                op = input("\t\t\t\tDigite sua opção: ")
                op = int(op)

        #op = input("Deseja prosseguir? Digite sua opção: ")
        #op = int(op)



    sist_op = input("Deseja continuar s/n: ")
    sist_op.lower()

print("Fim do Programa.")