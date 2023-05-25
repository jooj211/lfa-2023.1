class Main:
    def main(self):
        t = Main()
        t.faca1("ababa")
        # t.faca2()

    def faca1(self, w):
        a = AFD()
        try:
            a.ler("./AFD.XML")
            print("AFD M = ", a)
            if a.Aceita(w):
                print("Aceitou ", w)
            print("Pe(q0, ", w, "):", a.pe(a.getEstadoInicial(), w))
        except Exception as e:
            print(e)

    def faca2(self):
        a = AFN()
        try:
            a.ler("./AFN01.XML")
            print("AFN M = ", a)
            print("AFD M' = ", a.toAFD())
        except Exception as e:
            print(e)


if __name__ == '__main__':
    m = Main()
    m.main()
