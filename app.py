"""Quote board — local quotes, small web UI."""

import json
import random

from flask import Flask, Response, render_template

from quotes import QUOTES

app = Flask(__name__)


@app.get("/")
def index() -> str:
    return render_template(
        "index.html",
        quotes_json=json.dumps(QUOTES),
        quote_count=len(QUOTES),
    )


@app.get("/health")
def health() -> tuple[str, int]:
    return "ok", 200


@app.get("/api/quotes")
def list_quotes() -> Response:
    return Response(json.dumps(QUOTES), mimetype="application/json")


@app.get("/api/quotes/random")
def random_quote() -> Response:
    return Response(json.dumps(random.choice(QUOTES)), mimetype="application/json")


def main() -> None:
    app.run(host="0.0.0.0", port=8080)


if __name__ == "__main__":
    main()
