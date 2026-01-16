#Set Comprehension
messages = {'welcome', 'to', 'rns'}
capital = {message.capitalize() for message in messages}
print(capital)
uppercase = {message.upper() for message in messages}
print(uppercase)

#Dictionary Comprehension
tesla_models = {'released_year': 2012, 'price': 70000, 'range': 400}
print(tesla_models)

tesla_new_model = {key:val + 5 for key, val in tesla_models.items()}
print(tesla_new_model)

