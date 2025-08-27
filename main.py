def main():
  print("Hello learners!")

if __name__=="__main__":
  main()
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Number Trivia API", version="1.0.0")

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def trivia_fetch(num: int) -> dict:
    return {
        "number": num,
        "is_even": (num % 2 == 0),
        "is_prime": is_prime(num),
        "square": num ** 2,
        "fact": f"El número {num} es {'par' if num % 2 == 0 else 'impar'}."
    }

@app.get("/")
def root():
    return {"message": "Bienvenido/a a Number Trivia API"}

@app.get("/trivia/{num}")
def get_trivia(num: int):
    return trivia_fetch(num)

def main():
    print("Hello learners!")
    num = int(input("Ingresa un número: "))
    print(trivia_fetch(num))

if __name__ == "__main__":
    main()
num = int(input("Ingresa un número: "))
{'number': 42, 'is_even': True, 'is_prime': False, 'square': 1764, 'fact': 'El número 42 es par.'}
def main():
    print("Hello learners!")
    try:
        num = int(input("Ingresa un número: "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        return

    resultado = trivia_fetch(num)
    print("Resultados de la trivia:")
    for k, v in resultado.items():
        print(f"{k}: {v}")

