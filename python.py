import turtle

def draw_petal(t):
    t.color("pink")
    t.circle(100, 60)  # Desenha metade do pétala
    t.left(120)
    t.circle(100, 60)  # Desenha a outra metade do pétala
    t.left(120)

def draw_flower(t):
    for _ in range(6):  # Desenha 6 pétalas
        draw_petal(t)
        t.left(60)  # Gira para a próxima pétala

def main():
    window = turtle.Screen()
    window.bgcolor("lightblue")

    t = turtle.Turtle()
    t.speed(10)  # Define a velocidade do desenho

    draw_flower(t)

    # Desenha o caule
    t.color("green")
    t.right(90)
    t.forward(200)

    turtle.done()

if __name__ == "__main__":
    main()

