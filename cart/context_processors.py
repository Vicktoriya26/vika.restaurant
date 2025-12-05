def cart(request):
    # Якщо ти зберігаєш кошик у сесії
    cart = request.session.get('cart', {})
    return {'cart': cart}
