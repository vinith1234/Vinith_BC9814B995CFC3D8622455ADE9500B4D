def linear_search_product(products,target_product):
 indices =[]
 for i, product in enumerate(products):
    if products[i] == target_product: indices.append(i)
 return indices


#eg input values
products = ["apple", "orange", "grapes", "apple", "banana", "papaya", "appel"]
target_product = "apple"
result = linear_search_product(products, target_product)
print(result)