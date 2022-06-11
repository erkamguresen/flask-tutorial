from src import create_app, db, feed_db

app = create_app()


# @app.route("/health", methods=["GET"])
# def health_check():
#     return "ok"

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    feed_db()
    app.run(host="0.0.0.0")


