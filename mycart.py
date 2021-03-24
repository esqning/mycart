from app import db, create_app
from app.model import Admin, Basket, GoodsType, Goods, User
from flask_migrate import Migrate


app = create_app()
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Admin': Admin, 'Basket': Basket, 'GoodsType': GoodsType, 'Goods': Goods}


if __name__ == '__main__':
    app.run(debug=True)
