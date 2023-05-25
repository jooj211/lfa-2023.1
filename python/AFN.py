class AFN:
    def __init__(self, simbolos, estados, funcaoPrograma, estadoInicial, estadosFinais):
        """
        Metodo construtor de um Automato finito deterministico

        :param simbolos: ConjuntoSimbolo que representa o alfabeto do automato finito deterministico
        :param estados: ConjuntoEstados que representa o conjunto de estados do automato finito determinostico
        :param funcaoPrograma: ConjuntoTransicaoD que representa a funcao programa do automato finito deterministico
        :param estadoInicial: Estado que representa o estado inicial do automato finito deterministico
        :param estadosFinais: ConjuntoEstados que representa o conjunto de estados finais do automato finito nao-deterministico
        """
        self.simbolos = simbolos.clonar()
        self.estados = estados.clonar()
        self.funcaoPrograma = funcaoPrograma.clonar()
        self.estadoInicial = estadoInicial.clonar()
        self.estadosFinais = estadosFinais.clonar()

    def __init__(self):
        self.simbolos = ConjuntoSimbolo()
        self.estados = ConjuntoEstados()
        self.estadosFinais = ConjuntoEstados()
        self.funcaoPrograma = ConjuntoTransicaoN()

    def getEstadoInicial(self):
        """
        Obtem o estado inicial do automato finito nao-deterministico

        :return: estadoInicial - Estado que representa o estado inicial do automato finito nao-deterministico
        """
        return self.estadoInicial.clonar()

    def setEstadoInicial(self, estadoInicial):
        """
        Ajusta o estado inicial do automato finito nao-deterministico para o
        valor passado como parametro

        :param estadoInicial: um Estado a ser definido como estado inicial do automato
                              finito nao-deterministico
        """
        self.estadoInicial = estadoInicial.clonar()

    def getEstados(self):
        """
        Obtem o conjunto de estados finais do automato finito nao-deterministico

        :return: estados - ConjuntoEstados que representa o conjunto de estados
                 finais do automato finito nao-deterministico
        """
        return self.estados.clonar()

    def setEstados(self, estados):
        """
        Ajusta o conjunto de estados do automato finito nao-deterministico para o
        valor passado como parametro

        :param estados: um ConjuntoEstados a ser definido como o conjunto de estados
                        do automato finito nao-deterministico
        """
        self.estados = estados.clonar()

    def getEstadosFinais(self):
        """
        Obtem o conjunto de estados finais do automato finito nao-deterministico

        :return: estadosFinais - ConjuntoEstados que representa o conjunto de
                 estados finais do automato finito nao-deterministico
        """
        return self.estadosFinais.clonar()

    def setEstadosFinais(self, estadosFinais):
        """
        Ajusta o conjunto de estados finais do autômato finito não-determinístico
        para o valor passado como parâmetro

        :param estadosFinais: um ConjuntoEstados a ser definido como o conjunto de
                              estados finais do autômato finito não-determinístico
        """
        self.estadosFinais = estadosFinais.clonar()

    def getFuncaoPrograma(self):
        """
        Obtém a função programa do autômato finito não-determinístico

        :return: funcaoPrograma - ConjuntoTransicaoN que representa a função
                 programa do autômato finito não-determinístico
        """
        return self.funcaoPrograma.clonar()

    def setFuncaoPrograma(self, funcaoPrograma):
        """
        Ajusta a função programa do autômato finito não-determinístico para o
        valor passado como parâmetro

        :param funcaoPrograma: um ConjuntoTransicaoN a ser definido como a função
                               programa do autômato finito não-determinístico
        """
        self.funcaoPrograma = funcaoPrograma.clonar()

    def getSimbolos(self):
        """
        Obtém o alfabeto do autômato finito não-determinístico

        :return: simbolos - ConjuntoSimbolo que representa o alfabeto do autômato
                 finito não-determinístico
        """
        return self.simbolos.clonar()

    def setSimbolos(self, simbolos):
        """
        Ajusta o alfabeto do autômato finito não-determinístico para o valor
        passado como parâmetro

        :param simbolos: um ConjuntoSimbolo a ser definido como o alfabeto do
                         autômato finito não-determinístico
        """
        self.simbolos = simbolos.clonar()

    def clonar(self):
        """
        Cria e retorna uma cópia do objeto AFN

        :return: um clone desse AFN
        """
        return AFN(self.simbolos, self.estados, self.funcaoPrograma,
                   self.estadoInicial, self.estadosFinais)

    def __str__(self):
        """
        Retorna a representação em string deste AFN

        :return: uma string que representa este AFN
        """
        s = "("
        s += str(self.simbolos)
        s += ","
        s += str(self.estados)
        s += ","
        s += str(self.getFuncaoPrograma())
        s += ","
        s += str(self.estadoInicial)
        s += ","
        s += str(self.estadosFinais)
        s += ")"
        return s

    """
    Funcao Programa

    Retorna conjunto de estados alcancaveis depois de processar o Simbolo s a partir de estados e

    @param Estado: estado onde iniciara o processamento
    @param Simbolo: simbolo a ser processado
    @return: ConjuntoEstados
    """

    def p(self, e, s):
        fp = self.getFuncaoPrograma()
        for t in fp.getElementos():
            if t.getOrigem().igual(e) and t.getSimbolo().igual(s):
                return t.getDestino()

        cevazio = ConjuntoEstados()
        return cevazio

    def pe(self, e, p):
        if p == "":
            return e
        else:
            enovo = self.ConjuntoEstados()
            s = Simbolo(p[0])
            for est in e:
                enovo = enovo.uniao(self.p(est, s))
            return self.pe(enovo, p[1:])

    def Aceita(self, p):
        cestadoInicial = ConjuntoEstados()
        cestadoInicial.inclui(self.getEstadoInicial())
        cestadoFinal = self.getEstadosFinais()
        for e in self.pe(cestadoInicial, p).iterator():
            if cestadoFinal.pertence(e):
                return True
        return False

    def toAFD(self):
        # Parameters to create the new AFD
        novoCsi = self.getSimbolos().clonar()
        novoCe = ConjuntoEstados()
        novoCtD = ConjuntoTransicaoD()
        # "<" and ">" used to make the state name look like <states>
        novoEi = Estado("<" + self.getEstadoInicial().toString() + ">")
        novoCef = ConjuntoEstados()
        novoE = Estado()
        novaTD = TransicaoD()

        # Current set of final states
        atualCef = self.getEstadosFinais()

        # Parameters to control the algorithm's flow
        cceAtual = ConjuntoConjuntoEstados()
        ceAtual = ConjuntoEstados()
        eAtual = self.getEstadoInicial().clonar()
        siAtual = Simbolo()

        # Temporary parameter necessary for creating the new state
        ceTemp = ConjuntoEstados()

        # Add the initial state
        ceAtual.inclui(eAtual)
        cceAtual.inclui(ceAtual)

        # Add to the set of final states
        if atualCef.pertence(eAtual):
            novoCef.inclui(novoEi)

        novoCe.inclui(novoEi)

        # Iterate over the sets of states that will be analyzed
        iterCce = cceAtual.iterator()
        # While there is a state to analyze
        while iterCce.hasNext():
            ceAtual = iterCce.next()
            # Remove the element from the set of analyzables as it will be analyzed
            cceAtual.removerElemento(ceAtual)
            # Renew the temporary parameter
            ceTemp = ConjuntoEstados()

            # Parameter to check if the state will belong to the set of final states
            efinal = False

            # Iteration over the alphabet's set of symbols
            for iterSi in novoCsi.iterator():
                siAtual = iterSi.next()

                # Iteration over the states that form the current state
                ceTemp = ConjuntoEstados()
                for iterCe in ceAtual.iterator():
                    eAtual = iterCe.next()
                    # The new state will be the union of all the returns from the
                    # program function for a given symbol
                    ceTemp = ceTemp.uniao(p(eAtual, siAtual))

                # Check if the union is empty
                if not ceTemp.vazio():
                    # Name of the new state
                    novoNome = ceTemp.toString()
                    # Removes the { } present at the beginning and end of the name
                    novoNome = novoNome[1:len(novoNome) - 1]
                    # Inserts < and >
                    novoE = Estado("<" + novoNome + ">")

                    # Verifies if the state will belong to the set of final states
                    for iterCef in atualCef.iterator():
                        if ceTemp.pertence(iterCef.next()):
                            efinal = True

                    # If there is no state with the same name
                    # it is added to the set of states and a new transition is created
                    if not novoCe.pertence(novoE):
                        novoCe.inclui(novoE)
                        novoCtD.inclui(novaTD)
                        # If the state is final, it is added to the set of final states
                        if efinal:
                            novoCef.inclui(novoE)
                        # Creates a new transition
                        novaTD = TransicaoD(novoEi, siAtual, novoE)
                        nomeOrigem = ceAtual.toString()
                        nomeOrigem = "<" + \
                            nomeOrigem[1:len(nomeOrigem) - 1] + ">"

                        # Searches already existing transitions in the new set of states
                        novaOrigem = novoCe.retornaIgual(Estado(nomeOrigem))
                        novaTD.setOrigem(novaOrigem)
                        novaTD.setSimbolo(siAtual)
                        novaTD.setDestino(novoE)

                        novoCtD.inclui(novaTD.clonar())

                        cceAtual.inclui(ceTemp)

                    else:
                        # If the state already exists, it is only added to the set of transitions
                        # Creates only a new transition

                        novaTD = TransicaoD()
                        nomeOrigem = ceAtual.toString()
                        nomeOrigem = "<" + \
                            nomeOrigem[1:len(nomeOrigem) - 1] + ">"
                        novaOrigem = novoCe.retornaIgual(Estado(nomeOrigem))
                        novaTD.setOrigem(novaOrigem)
                        novaTD.setSimbolo(siAtual)
                        novaTD.setDestino(novoE)

                        novoCtD.inclui(novaTD.clonar())

            # Updates the iterator because the set of analyzables has changed
            iterCce = cceAtual.iterator()

        # Creates the new AFD
        novoAFD = AFD(novoCsi, novoCe, novoCtD, novoEi, novoCef)
        return novoAFD
    
    
