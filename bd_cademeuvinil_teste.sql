create table bd_cademeuvinil_teste (
CPF_CNPJ bigint,
BANDA VARCHAR(30),
ALBUM VARCHAR(50),
ESTADO VARCHAR(30),
USUARIO_PF_PJ VARCHAR(30),
EMAIL VARCHAR(50),
PRECO FLOAT(20)
);
insert into bd_cademeuvinil_teste (CPF_CNPJ, BANDA, ALBUM, ESTADO, USUARIO_PF_PJ, PRECO) values (11122233344,'The Who', 'Quadrophenia', 'novo', 'Cintia', 359.90);
insert into bd_cademeuvinil_teste(CPF_CNPJ, BANDA, ALBUM, ESTADO, USUARIO_PF_PJ, PRECO) values (30430430430,'The Smashing Pumpkins', 'Mellon Collie', 'novo', 'Tiago', 201.00);
select * from bd_cademeuvinil_teste
insert into bd_cademeuvinil_teste (BANDA, ALBUM, ESTADO, VENDEDOR, PRECO) values ('The Who', 'Tommy', 'usado', 'Cintia', 39.90);
insert into bd_cademeuvinil_teste (BANDA, ALBUM, ESTADO, VENDEDOR, PRECO) values ('The Who', 'Hits 50', 'novo', 'Cintia', 79.90);
insert into bd_cademeuvinil_teste(BANDA, ALBUM, ESTADO, VENDEDOR, PRECO) values ('The Smashing Pumpkins', 'Siamese Dream', 'novo', 'Tiago', 74.90);
select * from bd_cademeuvinil_teste