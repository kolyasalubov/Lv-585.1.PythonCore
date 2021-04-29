from service_api.app import db


class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    client_code = db.Column(db.String(32), unique=True, index=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(254), nullable=False, unique=True)
    passport_number = db.Column(db.String(8), nullable=False, unique=True)
    itn = db.Column(db.String(10), nullable=False, unique=True)
    orders = db.relationship('Order', backref='client', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(3), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    eta = db.Column(db.Integer, nullable=False)
    eta_type = db.Column(db.String(100), nullable=False)


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100), nullable=False)
    total = db.Column(db.Float, nullable=True)
    payment_method = db.Column(db.String(100), nullable=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.Date, nullable=False)


class OrderProduct(db.Model):
    __tablename__ = 'order_product'

    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)


class Document(db.Model):
    __tablename__ = 'document'
    __table_args__ = (
        db.UniqueConstraint('type', 'client_id', name='ux_document_type_client_id'),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    prefix = db.Column(db.String(12), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    path = db.Column(db.String(254), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)


class DocumentType(db.Model):
    __tablename__ = 'document_type'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)


class ProductDocumentType(db.Model):
    __tablename__ = 'product_document_type'

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    document_type_id = db.Column(db.Integer, db.ForeignKey('document_type.id'), primary_key=True)


models = (Client, Order, Product, OrderProduct, Document, DocumentType, ProductDocumentType)
