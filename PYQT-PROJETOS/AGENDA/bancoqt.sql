-- ESSE BANCO EU TO CRIANDO PRA USAR NA AULA DA ALINE DE DS - PYQT5 > FAZENDO RELACAO COM PYCHARM+ DESIGNER 

create database agenda;
use agenda;

create table contatos(
	id int not null auto_increment primary key,
    nome varchar(150),
    email varchar(150),
    telefone varchar(11),
    tipoTelefone varchar(11)
    
);

