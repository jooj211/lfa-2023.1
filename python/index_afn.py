from AFN import AFN

afn = AFN()

afn.from_xml("AFN01.XML")

print(afn)

afn.toXML("AFN01.XML")