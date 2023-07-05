product= {
	"brand":"adidas",
	"category":"dress",
	"price":699,
	"size":["men", "girl"]
}

print(len(product))
print(product.get("size"))
print(product.keys())
print(product.values())
product["price"]=500
print(product)
product.update({"price":450})
product.update({"colour":"red"})
print(product)
 del product["size"] 
print(product)
for x in product:
	print(x)
for x in product:
    print(product[x])	


for x in product:
	price(x)