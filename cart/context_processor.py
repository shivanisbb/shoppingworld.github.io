from .cart import cart

def cart(request):
    return{'cart':cart(request)}
