from pyscript import display

#redid the things I did in index
business_hours = ['9am-9pm']
has_delivery = 'Dine in and Take out'

location = 'Makati City'
p_numb = '09123456789'
email_add = 'good!dough@gmail.com'

#to display data
display(", ".join(business_hours), target="business_hours")
display(has_delivery, target="has_delivery")
display(location, target="location")
display(p_numb, target="p_numb")
display(email_add, target="email_add")