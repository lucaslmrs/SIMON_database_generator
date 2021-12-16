import random
import string

from dados.dados_em_lista import cursos
from dados.dados_em_lista import disciplinas
from dados.Aluno_cod_matricula import lista_codMatricula
from dados.Disciplina_codDisciplina import lista_codDisciplina
from dados.Turma_codTurma import lista_codTurma
from dados.Professor_codProfessor import lista_codProfessor
from dados.Certificado_codCertificado import lista_codCertificado
from dados.Monitor_codMonitor import lista_codMonitor
from dados.Sala_codSala import lista_codSala

import names
from cpf_generator import CPF
from random_username.generate import generate_username


class InsertGenerator:
    
    def __init__(self) -> None:
        self.cursos = cursos
        self.disciplinas = disciplinas
        self.lista_codMatricula = lista_codMatricula
        self.lista_codDisciplina = lista_codDisciplina
        self.lista_codTurma = lista_codTurma
        self.lista_codProfessor = lista_codProfessor
        self.lista_codCertificado = lista_codCertificado
        self.lista_codMonitor = lista_codMonitor
        self.lista_codSala = lista_codSala

    def __generator_CPF(self):
        cpf = CPF.generate() 
        return cpf

    def __generator_name(self):
        name = names.get_full_name()
        return name
    
    def __generator_curso(self):
        return self.cursos[random.randint(0, 5)]

    def __generator_cod(self, digitos):
        cod = ''
        for i in range(digitos):
            cod += str(random.randint(0, 9))
        return cod

    def __generator_ranking(self):
        ranking = random.random() * 10
        return ranking

    def __generator_Login(self):
        login = generate_username()
        return login[0]

    def __generator_Senha(self):
        characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        length = random.randint(5, 20)

        random.shuffle(characters)
        password = list()
        for i in range(length):
            password.append(random.choice(characters))
        random.shuffle(password)
        return "".join(password)

    def __generator_nomeDisciplina(self, i:int):
        return self.disciplinas[i]

    def __generator_cargaHoraria_disciplina(self):
        carga_horaria = [30, 60, 90, 120]
        return carga_horaria[random.randint(0, 3)]

    def __generator_Vagas(self):
        vagas = [20, 30, 40, 50, 60, 70, 80, 90, 100]
        return vagas[random.randint(0, 8)]

    def __generator_Ano(self):
        ano = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
        return ano[random.randint(0, 8)]


    def __generator_Periodo(self):
        periodo = [1, 2]
        return periodo[random.randint(0, 1)]

    def __generator_siglaTurma(self):
        characters = list(string.ascii_letters)
        length = random.randint(5, 20)

        random.shuffle(characters)
        password = list()
        for i in range(length):
            password.append(random.choice(characters))
        random.shuffle(password)
        return "".join(password)

    def __generator_Capacidade(self):
        vagas = [40, 50, 60, 70, 80]
        return vagas[random.randint(0, 4)]

    def __generator_TipoSala(self):
        tipo = ['LIP', 'normal']
        return tipo[random.randint(0, 1)]

    def __generator_Disponibilidade(self):
        tipo = [True, False]
        return tipo[random.randint(0, 1)]

    def __generator_caminhoImagem(self, disciplina:str):
        path = f"C:/simon/disciplinas/{disciplina}.png"
        return path

    def __generator_cargaHoraria_disciplina(self):
        carga_horaria = [30, 60, 90, 120]
        return carga_horaria[random.randint(0, 3)]

    def __generator_Datahora(self):
        hora = str(random.randint(8, 18))
        minuto = ['00', '15', '']
        return True

    def __generator_codMatricula(self):
        qtd_alunos = len(lista_codMatricula)
        return lista_codMatricula[random.randint(0, qtd_alunos-1)]

    def __generator_codDisciplina(self):
        qtd_Disciplina = len(self.lista_codDisciplina)
        return self.lista_codDisciplina[random.randint(0, qtd_Disciplina-1)] 

    def __generator_codTurma(self):
        qtd_turma = len(self.lista_codTurma)
        return self.lista_codTurma[random.randint(0, qtd_turma-1)] 

    def __generator_codMonitor(self):
        qtd_monitor = len(self.lista_codMonitor)
        return self.lista_codMonitor[random.randint(0, qtd_monitor-1)] 

    def __generator_codProfessor(self):
        qtd_Professor = len(self.lista_codProfessor)
        return self.lista_codProfessor[random.randint(0, qtd_Professor-1)] 
    
    def __generator_codSala(self):
        qtd_Sala = len(self.lista_codSala)
        return self.lista_codSala[random.randint(0, qtd_Sala-1)] 

    def __generator_codCertificado(self):
        qtd_Certificado = len(self.lista_codCertificado)
        return self.lista_codCertificado[random.randint(0, qtd_Certificado-1)] 

    def insert_aluno(self, qtd):
        lista_codMatricula = list()
        with open('inserts/Aluno.txt', 'w') as file:
            file.write("INSERT INTO Aluno VALUES\n")
            for i in range(qtd):
                codmatricula = self.__generator_cod(9)
                lista_codMatricula.append(codmatricula)
                cpf = self.__generator_CPF()
                curso = self.__generator_curso()
                nome = self.__generator_name()
                ranking = self.__generator_ranking()
                login = self.__generator_Login()
                senha = self.__generator_Senha()
                if i == qtd-1: 
                    file.write(f"('{codmatricula}', '{cpf}', '{nome}', '{curso}', {ranking}, '{login}', '{senha}');\n")
                else: 
                    file.write(f"('{codmatricula}', '{cpf}', '{nome}', '{curso}', {ranking}, '{login}', '{senha}'),\n")
                
        with open('dados/Aluno_cod_matricula.py', 'w') as file:
            file.write(f"lista_codMatricula = {lista_codMatricula}")

    def insert_disciplina(self):
        qtd = len(self.disciplinas)
        lista_codDisciplina = list()
        with open('inserts/Disciplina.txt', 'w') as file:
            file.write("INSERT INTO Disciplina VALUES\n")
            for i in range(qtd):
                codDisciplina = self.__generator_cod(9)
                lista_codDisciplina.append(codDisciplina)
                nomeDisciplina = self.__generator_nomeDisciplina(i)
                cargaHoraria = self.__generator_cargaHoraria_disciplina()
                if i == qtd-1: 
                    file.write(f"('{codDisciplina}', '{nomeDisciplina}', {cargaHoraria});\n")
                else: 
                    file.write(f"('{codDisciplina}', '{nomeDisciplina}', {cargaHoraria}),\n")
        with open('dados/Disciplina_codDisciplina.py', 'w') as file:
            file.write(f"lista_codDisciplina = {lista_codDisciplina}")

    def insert_aluno_disciplina(self, qtd):
        with open('inserts/AlunoDisciplina.txt', 'w') as file:
            file.write("INSERT INTO AlunoDisciplina VALUES\n")
            for i in range(qtd):
                codAluno = self.__generator_codMatricula()
                codDisciplina = self.__generator_codDisciplina()
                if i == qtd-1: 
                    file.write(f"('{codAluno}', '{codDisciplina}');\n")
                else: 
                    file.write(f"('{codAluno}', '{codDisciplina}'),\n")

    def insert_turma(self, qtd):
        lista_codTurma = list()
        with open('inserts/Turma.txt', 'w') as file:
            file.write("INSERT INTO Turma VALUES\n")
            for i in range(qtd):
                codTurma = self.__generator_cod(9)
                lista_codTurma.append(codTurma)
                codDisciplina = self.__generator_codDisciplina()
                vagas = self.__generator_Vagas()
                ano = self.__generator_Ano()
                periodo = self.__generator_Periodo()
                sigla = self.__generator_siglaTurma()
                if i == qtd-1: 
                    file.write(f"('{codTurma}', '{codDisciplina}', {vagas}, {ano}, {periodo}, '{sigla}');\n")
                else: 
                    file.write(f"('{codTurma}', '{codDisciplina}', {vagas}, {ano}, {periodo}, '{sigla}'),\n")
        with open('dados/Turma_codTurma.py', 'w') as file:
            file.write(f"lista_codTurma = {lista_codTurma}")

    def insert_monitor(self, qtd):
        lista_codMonitor = list()
        with open('inserts/Monitor.txt', 'w') as file:
            file.write("INSERT INTO Monitor VALUES\n")
            for i in range(qtd):
                codMonitor = self.__generator_cod(9)
                lista_codMonitor.append(codMonitor)
                codTurma = self.__generator_codTurma()
                codMatricula = self.__generator_codMatricula()
                if i == qtd-1: 
                    file.write(f"('{codMonitor}', '{codTurma}', '{codMatricula}');\n")
                else: 
                    file.write(f"('{codMonitor}', '{codTurma}', '{codMatricula}'),\n")
        with open('dados/Monitor_codMonitor.py', 'w') as file:
            file.write(f"lista_codMonitor = {lista_codMonitor}")

    def insert_sala(self, qtd):
        lista_codSala = list()
        with open('inserts/Sala.txt', 'w') as file:
            file.write("INSERT INTO Sala VALUES\n")
            for i in range(qtd):
                codSala = self.__generator_cod(9)
                lista_codSala.append(codSala)
                capacidade = self.__generator_Capacidade()
                tipo = self.__generator_TipoSala()
                disponibilidade = self.__generator_Disponibilidade()
                if i == qtd-1: 
                    file.write(f"('{codSala}', '{capacidade}', '{tipo}', {disponibilidade});\n")
                else: 
                    file.write(f"('{codSala}', '{capacidade}', '{tipo}', {disponibilidade}),\n")
        with open('dados/Sala_codSala.py', 'w') as file:
            file.write(f"lista_codSala = {lista_codSala}")

    def insert_professor(self, qtd):
        lista_codProfessor = list()
        with open('inserts/Professor.txt', 'w') as file:
            file.write("INSERT INTO Professor VALUES\n")
            for i in range(qtd):
                codProfessor = self.__generator_cod(9)
                lista_codProfessor.append(codProfessor)
                cpf = self.__generator_CPF()
                nome = self.__generator_name()
                login = self.__generator_Login()
                senha = self.__generator_Senha()
                if i == qtd-1: 
                    file.write(f"('{codProfessor}', '{cpf}', '{nome}', '{login}', '{senha}');\n")
                else: 
                    file.write(f"('{codProfessor}', '{cpf}', '{nome}', '{login}', '{senha}'),\n")
        with open('dados/Professor_codProfessor.py', 'w') as file:
            file.write(f"lista_codProfessor = {lista_codProfessor}")

    def insert_turma_professor(self, qtd):
        with open('inserts/TurmaProfessor.txt', 'w') as file:
            file.write("INSERT INTO TurmaProfessor VALUES\n")
            for i in range(qtd):
                codProfessor = self.__generator_codProfessor()
                codTurma = self.__generator_codTurma()
                if i == qtd-1: 
                    file.write(f"('{codProfessor}', '{codTurma}');\n")
                else: 
                    file.write(f"('{codProfessor}', '{codTurma}'),\n")

    def insert_certificado(self):
        qtd = len(self.disciplinas)
        lista_codCertificado = list()
        with open('inserts/Certificado.txt', 'w') as file:
            file.write("INSERT INTO Certificado VALUES\n")
            for i in range(qtd):
                codCertificado = self.__generator_cod(9)
                lista_codCertificado.append(codCertificado)
                codDisciplina = self.lista_codDisciplina[i]
                caminhoImagem = self.__generator_caminhoImagem(self.__generator_nomeDisciplina(i))
                if i == qtd-1: 
                    file.write(f"('{codCertificado}', '{codDisciplina}', '{caminhoImagem}');\n")
                else: 
                    file.write(f"('{codCertificado}', '{codDisciplina}', '{caminhoImagem}'),\n")
        with open('dados/Certificado_codCertificado.py', 'w') as file:
            file.write(f"lista_codCertificado = {lista_codCertificado}")

    def insert_certificado_monitor(self, qtd):
        with open('inserts/CertificadoMonitor.txt', 'w') as file:
            file.write("INSERT INTO CertificadoMonitor VALUES\n")
            for i in range(qtd):
                codCertificado = self.__generator_codCertificado()
                codMonitor = self.__generator_codMonitor()
                if i == qtd-1: 
                    file.write(f"('{codCertificado}', '{codMonitor}');\n")
                else: 
                    file.write(f"('{codCertificado}', '{codMonitor}'),\n")

    def insert_reserva(self, qtd):
        with open('inserts/Reserva.txt', 'w') as file:
            file.write("INSERT INTO Reserva VALUES\n")
            for i in range(qtd):
                codReserva = self.__generator_cod(9)
                codSala = self.__generator_codSala()
                codMonitor = self.__generator_codMonitor()
                if i == qtd-1: 
                    file.write(f"('{codReserva}', '{codSala}', '{codMonitor}');\n")
                else: 
                    file.write(f"('{codReserva}', '{codSala}', '{codMonitor}'),\n")

    def run(self):
        self.insert_aluno(1000)
        self.insert_disciplina()
        self.insert_sala(20)
        self.insert_professor(50)
        self.insert_aluno_disciplina(40000)
        self.insert_turma(80)
        self.insert_monitor(100)
        self.insert_turma_professor(250)
        self.insert_certificado()
        self.insert_certificado_monitor(400)
        self.insert_reserva(4000)
