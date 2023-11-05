from fastapi import FastAPI
app = FastAPI(
    title = "Calculator"
)
@app.get("/sum")
def sum(a: int, b: int):
    """Сложение"""
    return a + b

@app.get("/difference")
def difference(a: int, b: int):
    """Вычитание"""
    return a - b

@app.get("/multiplication")
def multiplication(a: int, b: int):
    """Умножение"""
    return a * b

@app.get("/division")
def division(a: int, b: int):
    """Деление"""
    if b == 0:
        return "Делить на 0 нельзя!"
    else:
        return a / b
