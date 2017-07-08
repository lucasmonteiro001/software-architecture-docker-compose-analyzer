def salvar_dados(dados, nome_arquivo_saida, nome_coluna_csv):
    lista = []

    # gera a lista com os dados de servico
    for valor, quantidade_com_esse_numero in dados:
        lista += [valor] * quantidade_com_esse_numero

    # salva os valores no arquivo

    f = open("dados_para_script_R/%s.csv" % nome_arquivo_saida, "w")

    f.write("%s\n" % nome_coluna_csv)

    for val in lista:
        f.write("%s\n" % val)

    f.close()


dados_servicos = [
    (1.0, 8678),
    (2.0, 8650),
    (3.0, 5041),
    (4.0, 2482),
    (5.0, 1242),
    (8.0, 1031),
    (6.0, 833),
    (7.0, 476),
    (9.0, 328),
    (10.0, 208),
    (11.0, 64),
    (13.0, 57),
    (12.0, 49),
    (18.0, 44),
    (15.0, 33),
    (16.0, 22),
    (20.0, 20),
    (17.0, 17),
    (14.0, 14),
    (19.0, 12),
    (24.0, 11),
    (22.0, 9),
    (21.0, 8),
    (25.0, 7),
    (29.0, 4),
    (33.0, 4),
    (66.0, 4),
    (36.0, 3),
    (38.0, 2),
    (26.0, 2),
    (28.0, 2),
    (27.0, 2),
    (23.0, 2),
    (30.0, 1),
    (35.0, 1),
    (58.0, 1),
    (382.0, 1),
    (219.0, 1)
]

dados_redes = [
    (0.0, 27874),
    (1.0, 1208),
    (2.0, 252),
    (3.0, 16),
    (4.0, 9),
    (5.0, 5),
    (6.0, 2)
]

dados_portas = [
    (0, 42256),
    (1, 34999),
    (2, 6335),
    (3, 1325),
    (4, 479),
    (5, 162),
    (13, 149),
    (7, 82),
    (19, 71),
    (18, 68),
    (6, 62),
    (8, 27),
    (9, 20),
    (11, 13),
    (12, 12),
    (10, 11),
    (15, 6),
    (17, 3),
    (21, 2),
    (16, 2),
    (20, 2),
    (14, 1),
    (106, 1)
]

dados_dependencias = [
    (0, 79232),
    (1, 4672),
    (2, 1331),
    (3, 447),
    (4, 204),
    (5, 109),
    (6, 48),
    (7, 39),
    (11, 3),
    (13, 2),
    (8, 1)
]

salvar_dados(dados_servicos, "servicos", "stars")
salvar_dados(dados_redes, "redes", "stars")
salvar_dados(dados_portas, "portas", "stars")
salvar_dados(dados_dependencias, "dependencias", "stars")
