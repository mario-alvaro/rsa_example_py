#RSA tiny example

#//////Como crear par de claves con este script//////
#ejecutar el script dentro del intérprete de python 3
#exec(open("<scriptName>.py").read())

#obtener numeros primos (no muy grandes para ejemplo) usando numerosPrimosEntre(min, max)
#dentro de un rango, como entre 1.000.000 y 1.010.000
#multiplicar dos de los numeros obtenidos (p y q)=> p*q=n
#obtener el totient => totient(n) = (p-1)*(q-1)
#elegir e (exponente de clave pública) => numero no muy grande pero que sea coprimo con totient(n)
#por eso se coge e como primo, para asegurar que es comprimo con totient(n) (17 por ejemplo)
#solo queda d (exponente de clave privada) => se pasa a la función "posiblesPrivKeys" el totient y e
#d tiene que cumplir que: d*e%totient(n) = 1 es decir, d*e dividido por el totient = algo con resto 1
# eso significa que "d" es multiplicador modular inverso de "e"

#FORTALEZA
#el producto de los números primos es público (n)
#el exponente pequeño también es público (e)
#lo que no se conoce es el totient(n) = (p-1)*(q-1)
#Con el totient se podrían obtener claves privadas que desencriptasen
#lo encriptado con la pública.
#Obtener el totient es muy dificil con números grandes, ya que 
#factorizar el módulo "n" para obtener los dos primos grandes que lo genera
#lleva mucho tiempo computacionalmente


def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True

def numerosPrimosEntre(min, max):
    i = min
    while i <= max:
        if isPrime(i):
            print ("Primo: " + str(i))
        i+=1	
	
def posiblesPrivKeys(totient,publicKey):
    i = 1
    while i < 100000:
        privateKey = (totient*i+1)/publicKey
        "ejecutar desde el interprete el prime.py"
        if privateKey.is_integer():
            print ("posible clave privada " + str(privateKey))
        i+=1
      
def rsaEncript (numberToEncript, publicKey, prodPrimMod):
    numberEncripted = pow(numberToEncript, publicKey, prodPrimMod)
    return numberEncripted

def rsaDecript (numberToDecript, privateKey, prodPrimMod):
    numberDecripted = pow(numberToDecript, privateKey, prodPrimMod)
    return numberDecripted
