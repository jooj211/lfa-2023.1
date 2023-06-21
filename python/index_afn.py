from AFN import AFN
from AFD import AFD

afn = AFN()

afn.from_xml("AFN01.XML")

print(afn)

afd = afn.toAFD()

print(str(afd))