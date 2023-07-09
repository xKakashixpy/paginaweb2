from decimal import Decimal

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carrito = self.session.get('carrito', {})
        if not self.carrito:
            self.session['carrito'] = {}
            self.carrito = self.session['carrito']

    def agregar(self, producto):
        id = str(producto.id)
        item = self.carrito.setdefault(id, {
            "producto_id": producto.id,
            "nombre": producto.nombre,
            "total": producto.precio,
            "cantidad": 0,
        })
        item["cantidad"] += 1
        item["total"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            self.carrito.pop(id)
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            item = self.carrito[id]
            item["cantidad"] -= 1
            item["total"] -= producto.precio
            if item["cantidad"] <= 0:
                self.eliminar(producto)
            else:
                self.guardar_carrito()

    def limpiar(self):
        self.session['carrito'] = {}
        self.session.modified = True



