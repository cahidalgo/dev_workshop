class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    """
    
    def es_palindromo(self, texto):
        """
        Verifica si una cadena es un palíndromo.
        """
        texto_limpio = ''.join(c.lower() for c in texto if c.isalnum())
        return texto_limpio == texto_limpio[::-1]
    
    def invertir_cadena(self, texto):
        """
        Invierte una cadena de texto sin usar slicing ni reversed().
        """
        invertida = ""
        for c in texto:
            invertida = c + invertida
        return invertida
    
    def contar_vocales(self, texto):
        """
        Cuenta el número de vocales en una cadena.
        """
        return sum(1 for c in texto.lower() if c in "aeiouáéíóú")
    
    def contar_consonantes(self, texto):
        """
        Cuenta el número de consonantes en una cadena.
        """
        return sum(1 for c in texto.lower() if c.isalpha() and c not in "aeiouáéíóú")
    
    def es_anagrama(self, texto1, texto2):
        """
        Verifica si dos cadenas son anagramas.
        """
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
    
    def contar_palabras(self, texto):
        """
        Cuenta el número de palabras en una cadena.
        """
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        """
        Pon en mayúscula la primera letra de cada palabra.
        """
        return ' '.join(p.capitalize() for p in texto.split())
    
    def eliminar_espacios_duplicados(self, texto):
        """
        Elimina espacios duplicados en una cadena.
        """
        return ' '.join(texto.split())
    
    def es_numero_entero(self, texto):
        """
        Verifica si una cadena representa un número entero sin usar isdigit().
        """
        if not texto:
            return False
        if texto[0] in ('-', '+'):
            texto = texto[1:]
        return all(c in "0123456789" for c in texto)
    
    def cifrar_cesar(self, texto, desplazamiento):
        """
        Aplica el cifrado César a una cadena de texto.
        """
        cifrado = ""
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                cifrado += chr(base + (ord(c) - base + desplazamiento) % 26)
            else:
                cifrado += c
        return cifrado
    
    def descifrar_cesar(self, texto, desplazamiento):
        """
        Descifra una cadena cifrada con el método César.
        """
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        """
        Encuentra todas las posiciones de una subcadena en un texto sin usar find() o index().
        """
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i+len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones
