"""
    Autor: Giulliano Paz
    E-mail: giulliano94@gmail.com
    Curso: Ciência da Computação
    Inst: Universidade Federal do Pampa - UNIPAMPA
"""
# Alfabeto de caracteres para a encripitação
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789?/=][()@$# "
# Recebe fator de deslocamento
print("\n    Valores POSITIVOS para cifrar e valores NEGATIVOS para decifrar")
shift = int(input("\n ~> Fator de deslocamento: "))
# Recebe texto a ser cifrado
palavra = input("\n ~> Texto: ").lower()

# Mostra palavra cifrada
print("\n ~> Resultado: ", end=" ")
# Percorre palavra a ser cifrada, deslocando cada letra pelo fator de deslocamento
for elem in palavra:
	try:
		print(alphabet[(alphabet.index(elem)+shift) % len(alphabet)], end="")
	except Exception:
		print(elem, end="")
print("")
