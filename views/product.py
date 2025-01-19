from flask import jsonify, request
from flask import Blueprint
from models import Product,db
from flask_jwt_extended import jwt_required, get_jwt_identity

product_bp = Blueprint("product_bp", __name__)

#Add Product
@product_bp.route('/add', methods=['POST'])
@jwt_required()
def add():
    data = request.get_json()
    current_user_id = get_jwt_identity()
    
    name = data['name']
    price = data['price']
    quantity = data['quantity']
    
    check_name = Product.query.filter_by(name=name).first()
    
    if check_name:
        return jsonify({'message': 'Product already exists'}), 400
    else:
        new_product = Product(name=name, price=price, quantity=quantity, user_id=current_user_id)
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully'}), 201
# Get all products
   
@product_bp.route('/getall', methods=['GET'])
def get_all():
    products = Product.query.all()
    output = []
    for product in products:
        output.append({
            'id': product.id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity
        })
        
        return jsonify(output), 200
# Update Product
@product_bp.route('/product/<int:product_id>', methods=['PUT'] )
def update_product(product_id):
    product = Product.query.get(product_id)
    if product:
        data = request.get_json()
        user_id = data.get('user_id', product.user_id)
        name = data.get("name", product.name)
        price = data.get('price', product.price)
        quantity = data.get('quantity', product.quantity)
    
    check_name = Product.query.filter_by(name=name).first()

    if check_name:
        return jsonify({'message': 'product already exists'}), 400
    else:
        product.name = name
        product.price = price
        product.quantity = quantity
        db.session.commit()
        return jsonify({'message': 'product updated successfully'}), 200

#Delete Product
@product_bp.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'product deleted successfully'}), 200
    else:
        return jsonify({'message': 'product not found'}), 404
    


