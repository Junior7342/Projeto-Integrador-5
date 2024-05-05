## CONEXÃO COM SQL
## VARIÁVEIS USADAS NESTE BLOCO: dados_conexao; conexao
import pyodbc
dados_conexao = (
    ## não alterar DRIVER={SQL SERVER} --- padrão utilizado
    "Driver={SQL SERVER};"
    ## LAPTOP-U3965MMQ deve ser substituído para localização do futuro servidor
    "Server=LAPTOP-U3965MMQ;"
    "Database=PYTHON_SQL;"
)

## conexão com o PYODBC
conexao = pyodbc.connect(dados_conexao)
# TESTE CONEXÃO
print("Conexão bem sucedida!")
## FIM DO BLOCO CONEXÃO


#####
#####


## VARIÁVEIS USADAS NESTE BLOCO: cursor, qtag1, nome_arquivo, comando, lista_exibicao, qtag2

## FUNCOES USADAS NESTE BLOCO: buscar_banda_artista(), sql_consulta_banda_artista(qtag1), ...
## ...
cursor = conexao.cursor()


def buscar_banda_artista():

    #o SQL não é case sensitive
    qtag1 = input("\t\tInforme o nome da banda ou artista que deseja localizar: ")
    print("\n")
    sql_consulta_banda_artista(qtag1)
    print("\t\tTudo certo até aqui")


def sql_consulta_banda_artista(qtag1):

    cursor = conexao.cursor()
    nome_arquivo = 'bd_cademeuvinil_teste'
    comando = f"""SELECT banda, album, estado, preco FROM {nome_arquivo}
where banda = '{qtag1}' or banda like '{qtag1}%' or banda like '%{qtag1}'"""
    #print(len(cursor.execute(comando).fetchall()))
    lista_exibicao = list(cursor.execute(comando).fetchall())
    n = 0
    while n < len(lista_exibicao):
        print(f"\t\t{lista_exibicao[n]}")
        n += 1
    print("\t\tTodos os resultados da busca exibidos.")

    texto_qtag2 = f"""Digite 1(Hum) para prosseguir na compra... Digite 2 (Dois) para... """
    print(f"\n\t\t{texto_qtag2}")
    qtag2 = input("\n\t\tInforme agora sua opção: ")
    qtag2 = int(qtag2)
    fluxo_de_acoes(cursor, nome_arquivo, qtag2)


def fluxo_de_acoes(cursor, nome_arquivo, qtag2):

    if qtag2 == 1:
        while qtag2 == 1:
            if qtag2 == 1:
                qtag3 = input("\t\tQual o nome do álbum que deseja adquirir: ")


                ## Imprime o nome da banda
                banda = f"""SELECT banda FROM {nome_arquivo}
                where album = '{qtag3}' or album like '{qtag3}%' or album like '%{qtag3}'"""
                nome_banda = cursor.execute(banda).fetchone()
                nome_banda = str(nome_banda)
                print(f"\t\tBanda: {nome_banda}")


                ## Imprime o nome do álbum
                album = f"""SELECT album FROM {nome_arquivo}
                where album = '{qtag3}' or album like '{qtag3}%' or album like '%{qtag3}'"""
                album_nome = cursor.execute(album).fetchone()
                album_nome = str(album_nome)
                print(f"\t\tAlbum: {album_nome};")


                ## Imprime o estado 'novo'/'seminovo'/'usado'
                estado = f"""SELECT estado FROM {nome_arquivo}
                where album = '{qtag3}' or album like '{qtag3}%' or album like '%{qtag3}'"""
                album_estado = cursor.execute(estado).fetchone()
                album_estado = str(album_estado)
                print(f"\t\tEstado: {album_estado};")


                ## Imprime o preço
                preco = f"""SELECT preco FROM {nome_arquivo}
                where album = '{qtag3}' or album like '{qtag3}%' or album like '%{qtag3}'"""
                album_preco = cursor.execute(preco).fetchone()
                album_preco = str(album_preco)
                print(f"\t\tPreço: {album_preco}")


                carrinho_de_compras(cursor, nome_arquivo, qtag3)

                texto_qtag4 = f"""Digite 1(Hum) para continuar comprando... 2(Dois) para finalizar a compra..."""
                print(f"\n\t\t{texto_qtag4}")
                qtag4 = input("\n\t\tInforme agora sua opção: ")
                qtag4 = int(qtag4)

                print("Teste qtag 4 ok!!!")



## Função 'carrinho_de_compras(cursor, nome_arquivo, qtag3):' salva em um outro banco de dados...
## ... o álbum/vinil, mas não exclui do primeiro banco o álbum selecionado/reservado
def carrinho_de_compras(cursor, nome_arquivo, qtag3):

    ## Comando que envia para um segundo banco de dados o álbum reservado
    reservar_album = f"""INSERT INTO bd_cademeuvinil_reserva SELECT * FROM {nome_arquivo}
                    where album = '{qtag3}' or album like '{qtag3}%' or album like '%{qtag3}'"""
    cursor.execute(reservar_album)
    conexao.commit()
    #verif = f"""select * from bd_cademeuvinil_teste"""
    #print(cursor.execute(verif).fetchone())
    print("\n\t\tÁlbum reservado.")




                ####################

                #album = f"""SELECT album FROM {nome_arquivo}
                #where album = '{qtag3}' or album like '{qtag3}%' or album like '%{qtag3}'"""
                #album_nome = cursor.execute(album).fetchone()
                #album_nome = str(album_nome)
                #print(type(album_nome))
                #print(f"\t\tAlbum: {album_nome}")

                #estado = f"""SELECT estado FROM {nome_arquivo}
                #where album = '{qtag3}' or album like '{qtag3}%' or album like '%{qtag3}'"""
                #album_estado = cursor.execute(estado).fetchone()
                #album_estado = str(album_estado)
                #print(type(album_estado))
                #print(f"\t\tEstado: {album_estado}")

                #preco = f"""SELECT preco FROM {nome_arquivo}
                #where album = '{qtag3}' or album like '{qtag3}%' or album like '%{qtag3}'"""
                #album_preco = cursor.execute(preco).fetchone()
                #album_preco.connection.setdecoding(float)
                #print(type(album_preco))
                #print(f"\t\tPreço: {album_preco}")


######


texto1 = """\n\t\tDigite 'B' para buscar pela Banda/Artista ou;
\t\tDigite 'A' para buscar pelo nome do Álbum;"""
print(texto1)
qtag = input("\t\tDigite agora sua opção: ")
qtag = qtag.upper()
buscar_banda_artista()