inventario = [
     {"producto" : "camisa","precio":25900,"stock":"11"},
     {"producto":"pantalon","precio":39900,"stock":"23"},
      ]
inventario.append({
    "producto":"abrigo",
    "precio":50000,
    "stock":"2"
    })
for producto in inventario:
    producto ["stock"] = int(producto ["stock"])
for producto in inventario: 
    producto["precio"]= producto["precio"] + 10000
for producto in inventario: 
    print(f"Hay {producto['stock']} unidades del producto {producto['producto']}. Su precio por unidad es de {producto['precio']}")


