import os
import random
from flask import Flask, render_template

app = Flask(__name__)

def get_sides():
    """Return how many sides the die should have based on the DICE_SIDES env var."""
    env_value = os.getenv("DICE_SIDES", "6")

    try:
        sides = int(env_value)
        if sides >= 2:
            return sides
        else:
            print(f"[WARN] DICE_SIDES inválido ({env_value}), usando 6.")
            return 6
    except ValueError:
        print(f"[WARN] DICE_SIDES no es un número válido ({env_value}), usando 6.")
        return 6


@app.route("/")
def index():
    sides = get_sides()
    result = random.randint(1, sides)
    return render_template("index.html", result=result, sides=sides)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
