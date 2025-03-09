class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triangulo de pascal etc.
    """
    
    def fibonacci(self, n):
        """
        Calcula el n-ésimo número de la secuencia de Fibonacci.
        """
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def secuencia_fibonacci(self, n):
        """
        Genera los primeros n números de la secuencia de Fibonacci.
        """
        seq = [0, 1]
        for _ in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq[:n]
    
    def es_primo(self, n):
        """
        Verifica si un número es primo.
        """
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        """
        Genera una lista de números primos hasta n.
        """
        return [i for i in range(2, n + 1) if self.es_primo(i)]
    
    def es_numero_perfecto(self, n):
        """
        Verifica si un número es perfecto.
        """
        return sum(i for i in range(1, n) if n % i == 0) == n
    
    def triangulo_pascal(self, filas):
        """
        Genera las primeras n filas del triángulo de Pascal.
        """
        triangulo = [[1]]
        for i in range(1, filas):
            fila = [1]
            for j in range(1, i):
                fila.append(triangulo[i - 1][j - 1] + triangulo[i - 1][j])
            fila.append(1)
            triangulo.append(fila)
        return triangulo[:filas]
    
    def factorial(self, n):
        """
        Calcula el factorial de un número.
        """
        return 1 if n == 0 else n * self.factorial(n - 1)
    
    def mcd(self, a, b):
        """
        Calcula el máximo común divisor de dos números.
        """
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo de dos números.
        """
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        """
        Calcula la suma de los dígitos de un número.
        """
        return sum(int(d) for d in str(abs(n)))
    
    def es_numero_armstrong(self, n):
        """
        Verifica si un número es de Armstrong.
        """
        num_str = str(n)
        return sum(int(d) ** len(num_str) for d in num_str) == n
    
    def es_cuadrado_magico(self, matriz):
        """
        Verifica si una matriz es un cuadrado mágico.
        """
        if not matriz:
            return False
        n = len(matriz)
        suma_objetivo = sum(matriz[0])
        
        # Verificar filas y columnas
        for i in range(n):
            if sum(matriz[i]) != suma_objetivo or sum(matriz[j][i] for j in range(n)) != suma_objetivo:
                return False
        
        # Verificar diagonales
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo or sum(matriz[i][n - i - 1] for i in range(n)) != suma_objetivo:
            return False
        
        return True
