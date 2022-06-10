from flask import jsonify, request, Response

from src import create_app

app = create_app()


# @app.route("/health", methods=["GET"])
# def health_check():
#     return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
