nu1= float(input("primeira nota: "))
nu2= float(input("segunda nora: "))
media= (nu1+nu2)/2
if media >=7:
    print("PARABENS VC FOI APROVADO, com {:.1f} de nota final!!".format(media))
elif media >=5 and media <=6.9:
    print("vc ficou de RECUPARAÇÃO com {:.1f} de nota final!!".format(media))
else:
    print("PESSIMA NOTICIA, VC ESTA REPROVADO, ficou com {:.1f} de nota final!!".format(media))

