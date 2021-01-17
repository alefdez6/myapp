import sys
import uuid

def get_products():
    fake_response = [{
            "sku": uuid.uuid4(),
            "title": "Vanilla icecream",
            "long_description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "price_euro": 1.5
    },{
            "sku": uuid.uuid4(),
            "title": "Lemon icecream",
            "long_description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            "price_euro": 1.5
    }]
    return fake_response

def create_product(sku, title, long_description, price_euro):
    '''Insertar todo esto en una bbdd'''
    print(f"Crear sku={sku} y title={title}", file=sys.stderr)

