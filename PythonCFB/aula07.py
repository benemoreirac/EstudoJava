texto = "Curso de Python"
palavra = "Python"
curso = "CFB Cursos"

res= palavra.upper() in texto.upper()
print(res)
#sensitive case

res_concat = texto+ " do canal "+ curso
print(res_concat)

cidade = "Patrocinio"
dia =15
mes ="Dezembro"
ano=2019
data = "{}, {} de {} de {} \n \"{}"

print(cidade + ", " + str(dia) + " de " + mes + " de " + str(ano))
print(data.format(cidade, dia, mes, ano,curso))

# \'   \"   \n   \r    \t     \b