from xml.dom import minidom
from copy import deepcopy

class AFD:
    def __init__(self, simbolos=None, estados=None, funcao_programa=None, estado_inicial=None, estados_finais=None):
        if simbolos is not None and estados is not None and funcao_programa is not None and estado_inicial is not None and estados_finais is not None:
            self.simbolos = simbolos.copy()
            self.estados = estados.copy()
            self.funcao_programa = funcao_programa.copy()
            self.estado_inicial = deepcopy(estado_inicial)
            self.estados_finais = estados_finais.copy()
        else:
            self.simbolos = set()
            self.estados = set()
            self.estados_finais = set()
            self.funcao_programa = set()
            self.estado_inicial = None

    def get_estado_inicial(self):
        return deepcopy(self.estado_inicial)

    def set_estado_inicial(self, estado_inicial):
        self.estado_inicial = deepcopy(estado_inicial)

    def get_estados(self):
        return self.estados.copy()

    def set_estados(self, estados):
        self.estados = estados.copy()

    def get_estados_finais(self):
        return self.estados_finais.copy()

    def set_estados_finais(self, estados_finais):
        self.estados_finais = estados_finais.copy()

    def get_funcao_programa(self):
        return self.funcao_programa.copy()

    def set_funcao_programa(self, funcao_programa):
        self.funcao_programa = funcao_programa.copy()

    def get_simbolos(self):
        return self.simbolos.copy()

    def set_simbolos(self, simbolos):
        self.simbolos = simbolos.copy()

    def clonar(self):
        return AFD(self.simbolos, self.estados, self.funcao_programa, self.estado_inicial, self.estados_finais)

    def __str__(self):
        s = "("
        s += str(self.simbolos) + ","
        s += str(self.estados) + ","
        s += str(self.get_funcao_programa()) + ","
        s += str(self.estado_inicial) + ","
        s += str(self.estados_finais) + ")"
        return s

    def ler(self, path_arquivo):
        # Parse XML file
        doc = minidom.parse(path_arquivo)
        automato = doc.documentElement

        # Read symbols
        simbolos_element = automato.getElementsByTagName("simbolos")[0]
        simbolos = set()
        for simbolo in simbolos_element.getElementsByTagName("elemento"):
            simbolos.add(simbolo.getAttribute("valor"))
        self.set_simbolos(simbolos)

        # Read states
        estados_element = automato.getElementsByTagName("estados")[0]
        estados = set()
        for estado in estados_element.getElementsByTagName("elemento"):
            estados.add(estado.getAttribute("valor"))
        self.set_estados(estados)

        # Read final states
        estados_finais_element = automato.getElementsByTagName("estadosFinais")[0]
        estados_finais = set()
        for estado_final in estados_finais_element.getElementsByTagName("elemento"):
            estados_finais.add(estado_final.getAttribute("valor"))
        self.set_estados_finais(estados_finais)

        # Read initial state
        estado_inicial_element = automato.getElementsByTagName("estadoInicial")[0]
        self.set_estado_inicial(estado_inicial_element.getAttribute("valor"))

        # Read transitions
        funcao_programa_element = automato.getElementsByTagName("funcaoPrograma")[0]
        funcao_programa = set()
        for transicao in funcao_programa_element.getElementsByTagName("elemento"):
            origem = transicao.getAttribute("origem")
            destino = transicao.getAttribute("destino")
            simbolo = transicao.getAttribute("simbolo")
            funcao_programa.add((origem, simbolo, destino))
        self.set_funcao_programa(funcao_programa)

    def p(self, e, s):
        for origem, simbolo, destino in self.get_funcao_programa():
            if origem == e and simbolo == s:
                return destino
        return None

    def pe(self, e, p):
        e_atual = e
        for s in p:
            e_atual = self.p(e_atual, s)
            if e_atual is None:
                return None
        return e_atual

    def aceita(self, p):
        return self.pe(self.get_estado_inicial(), p) in self.get_estados_finais()

    def to_xml(self, filename):
        with open(filename + ".xml", "w") as f:
            f.write("<AFD>\n")
            f.write("\n")

            f.write("\t<simbolos>\n")
            for s in self.get_simbolos():
                f.write(f'\t\t<elemento valor="{s}"/>\n')
            f.write("\t</simbolos>\n")
            f.write("\n")

            f.write("\t<estados>\n")
            for e in self.get_estados():
                f.write(f'\t\t<elemento valor="{e}"/>\n')
            f.write("\t</estados>\n")
            f.write("\n")

            f.write("\t<estadosFinais>\n")
            for e in self.get_estados_finais():
                f.write(f'\t\t<elemento valor="{e}"/>\n')
            f.write("\t</estadosFinais>\n")
            f.write("\n")

            f.write("\t<funcaoPrograma>\n")
            for origem, simbolo, destino in self.get_funcao_programa():
                f.write(f'\t\t<elemento origem="{origem}" destino="{destino}" simbolo="{simbolo}"/>\n')
            f.write("\t</funcaoPrograma>\n")
            f.write("\n")

            f.write(f'\t<estadoInicial valor="{self.get_estado_inicial()}"/>\n')
            f.write("\n")

            f.write("</AFD>\n")