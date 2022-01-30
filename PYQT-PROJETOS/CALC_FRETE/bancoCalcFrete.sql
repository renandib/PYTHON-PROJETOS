### CRIANDO BANCO PRO TRABALHO DE QTS 

## ENTREGAR DIA 03/11 > TENQ TA PRONTO E PODE SER EM GRUPO 

#Desenvolver uma interface para que seja possível calcular o valor de frete para um pedido baseado no local de entrega, peso transportado, valor da mercadoria. O desenvolvimento dessa aplicação deve seguir os requisitos a seguir:

# VALOR / PESO / #TBL DE UFS > REGIAO SUDESTE > MG/SP/RJ/ES

# valor do produto > pede pro usuario digitar 

# peso do produto > tbl_peso e preço 


# DEIXEI UM SLIDE NA PASTA DE QTS ( ESBOCO CALC FRETE ) EM POWER POINT > OLHAR ELE E COMEÇAR A CRIAR O BANCO E DPS O FRONT 

## OBS >ESSA AULA VAI AJUDAR MUITO NO FRONT > https://www.youtube.com/watch?v=ufb8a6ZztOM
#https://www.youtube.com/watch?v=Uv4h8IJhQUg

CREATE DATABASE calcFrete;

drop database calcFrete;
use calcFrete;

# CRIANDO TABELA DE UF + REGIAO

CREATE TABLE tbl_uf (
	id int(6) primary key not null,
    uf varchar(2) not null
);

select * from tbl_uf;

select uf from tbl_uf where id = 1;
drop table tbl_uf;
INSERT INTO tbl_uf (id,uf)
	VALUES (1,"ES"),
    (2,"MG"),
    (3,"RJ"),
    (4,"SP");
    
    
## CRIANDO TABELA DAS CIDADES E LIGANDO COM AS REGIOES DA 1° TABELA
CREATE TABLE tbl_cidades(
	id int(11) primary key not null auto_increment,
    cidade varchar(25) not null,
    regiao varchar(25) not null,
    fk_id_uf int,
    
    constraint fk_id_uf foreign key (fk_id_uf) references tbl_uf (id)
);

INSERT INTO tbl_cidades (cidade,regiao,fk_id_uf)

VALUES ("VITORIA","CAPITAL",1),
("SERRA","INTERIOR",1),
("BELO HORIZONTE","CAPITAL",2),
("CONTAGEM","INTERIOR",2),
("RIO DE JANEIRO","CAPITAL",3),
("ANGRA DOS REIS","INTERIOR",3),
("SÃO PAULO","CAPITAL",4),
("TABOAO DA SERRA","CAPITAL",4),
("SOROCABA","INTERIOR",4);

select * from tbl_cidades;

drop table tbl_pesoUf;

# CRIANDO TABELA DE PESO POR UF E REGIAO 
CREATE TABLE tbl_pesoUf (
	id int(11) primary key auto_increment,
    uf_peso varchar(8) not null,
    regiao_peso varchar(12) not null,
    ate_10_kg decimal(5,2) not null,
    ate_20_kg decimal(5,2) not null,
    kg_excedente decimal (5,2) not null,
    pedagio decimal (4,2) not null,
    vigencia date
);

select uf_peso,regiao_peso,ate_10_kg,ate_20_kg,kg_excedente,pedagio,vigencia from tbl_pesoUf;

select * FROM tbl_pesouf;

INSERT INTO tbl_pesoUf (uf_peso,regiao_peso,ate_10_kg,ate_20_kg,kg_excedente,pedagio,vigencia)


VALUES ("ES","CAPITAL",16.22,24.01,0.26,4.20,"2021-06-15"),
("ES","INTERIOR",12.50,18.50,0.20,4.20,"2021-08-25"),
("MG","CAPITAL",13.81,20.43,0.22,4.20,"2021-07-23"),
("MG","INTERIOR",17.95,26.56,0.29,4.20,"2022-05-23"),
("RJ","CAPITAL",11.75,17.39,0.19,4.20,"2022-08-11"),
("RJ","INTERIOR",15.28,22.61,0.25,4.20,"2022-09-10"),
("SP","CAPITAL",10.00,14.80,0.16,4.20,"2022-04-15"),
("SP","INTERIOR",13.81,20.43,0.22,4.20,"2021-07-23");


## 1° tela vai mostrar essa tabela de preço por PESO DA UF E REGIAO 
## 2° vai ter um list box > pra selecionar a UF 
## 3° vai ter um list box > pra selecionar a cidade 
## 4° vai ter um input pra colocar o peso 
## 5° vai ter um input pra colocar qnts pedagios tem no percurso
## 6° vai ter um input > pra pessoa colocar o percentual > q ela viu na tbl de icms 
## 7° botao pra calcular frete 

## LABEL FINAL DE RESPOSTA > FAZENDO O CALCULO E MOSTRANDO SE VALE A PENA OU N 


## TIVE UMAS DUVIDAS DE LOGICA > PERGUNTEI PRO PROF NO TEAMS > ESPERANDO ELE DAR A RESPOSTA PRA DAR CONTINUIDADE AQUI.. 