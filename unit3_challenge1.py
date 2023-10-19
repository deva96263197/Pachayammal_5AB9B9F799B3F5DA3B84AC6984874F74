def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices

products = ["shoes", "boot", "shoes", "loafer", "sandal", "shoes"]
target = "shoes"
target2 = 'slipper'
result = linearSearchProduct(products, target)
print(result)
result = linearSearchProduct(products, target2)
print(result)