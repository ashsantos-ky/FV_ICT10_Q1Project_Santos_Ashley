from pyscript import display

# the data to be displayed on intro section
restaurant_name = 'Good dough'
own_name = 'Kirsten Santos'
year_estab = 2025
products = ['Meat - ' 'Vegetables - ' 'Hawaiian - ' 'Pepperoni - ' 'Cheese']

# displayed on footer
has_delivery = 'Dine in and Take out'
business_hours = ['9am-9pm']

# display the data on index.html in the correct elements
display(restaurant_name, target="restaurant_name")
display(f"Owned by: {own_name}", target="own_name")
display(f"baked since: {year_estab}", target="year_estab")
display(has_delivery, target="has_delivery")
display(", ".join(products), target="products")
display(", ".join(business_hours), target="business_hours")
