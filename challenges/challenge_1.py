contacts = []

def main_menu():
  global contacts

  options = {key: value for key, value in {
    1: 'Adicionar contato',
    2: 'Todos os contatos' if len(contacts) > 0 else None,
    3: 'Contatos favoritos' if any(contact['favorite'] == True for contact in contacts) else None,
    0: 'Sair'
  }.items() if value != None}

  print(f'''
---------- Gerenciador de Contatos ----------
{'\n'.join(f'({key}) {value}' for key, value in options.items())}''')

  while True:
    try:
      option = int(input('\nSelecione uma opção para prosseguir: '))

      if option not in list(options.keys()):
        print('A opção selecionada não existe, tente novamente!')
      else:
        break
    except:
      print('O valor informado não é um número, tente novamente!')

  if option == 0:
    print('\nAté a próxima!')
    return
  elif option == 1:
    return post_contact()
  elif option == 2:
    return list_contacts(contacts)
  elif option == 3:
    return list_contacts([contact for contact in contacts if contact['favorite'] == True])



def post_contact():
  print('\nDigite 0 a qualquer momento para voltar!\n')

  name = input('Digite o nome do contato: ')
  if name == '0':
    return main_menu()

  phone = input('Digite o número do contato: ')
  if phone == '0':
    return main_menu()
  
  email = input('Digite o e-mail do contato (Enter para ignorar): ')
  if email == '0':
    return main_menu()
  
  while True:
    favorite = input('Deseja adicionar o contato aos favoritos? (y/n): ')
    if favorite == 'y' or favorite == 'n' or favorite == '':
      break
    else:
      print('\nPor favor digite uma opção válida!')

  global contacts
  contacts.append({
    'name': name,
    'phone': phone,
    'email': email if email != '' else None,
    'favorite': True if favorite == 'y' else False
  })

  print(f'O contato {name} foi adicionado com sucesso!')
  return main_menu()



def list_contacts(contacts_list):
  contacts_list.sort(key=lambda contact: contact['name'])
  favorites = [contact for contact in contacts_list if contact['favorite'] == True]
  others = [contact for contact in contacts_list if contact['favorite'] == False]
  total_favorites = len(favorites)

  if total_favorites:
    print(f'''\n----- Contatos favoritos -----
{format_contacts(favorites, 1)}''')
    
  if len(others):
    print(f'''\n----- Contatos -----
{format_contacts(others, total_favorites + 1)}''')
    
  print('\nDigite 0 a qualquer momento para voltar!\n')

  while True:
    try:
      selected = int(input('Selecione um contato para modificar ou remover: '))

      if selected == 0:
        return main_menu()
      elif selected > len(contacts_list):
        print('A opção selecionada não existe, tente novamente!')
      else:
        break
    except:
      print('O valor informado não é um número, tente novamente!')
  
  selected_contact = favorites[selected - 1] if selected <= total_favorites else others[selected - total_favorites - 1]
  return contact_operations(selected_contact)



def contact_operations(contact):
  global contacts
  index = contacts.index(contact)

  print(f'''\n----- Contato selecionado -----
  Nome: {contact['name']}
  Número: {contact['phone']}
  E-mail: {contact['email']}

  (1) {'Favoritar' if contact['favorite'] == False else 'Desfavoritar'} contato
  (2) Modificar nome
  (3) Modificar número
  (4) Modificar e-mail
  (5) Remover contato
  (0) Voltar''')

  while True:
    try:
      operation = int(input('\nSelecione a opção desejada: '))

      if operation == 0:
        return main_menu()
      elif operation > 5:
        print('A opção selecionada não existe, tente novamente!')
      else:
        break
    except:
      print('O valor informado não é um número, tente novamente!')

  if operation == 1:
    return put_contact_favorite(contact, index)
  elif operation == 2:
    return put_contact_name(contact, index)
  elif operation == 3:
    return put_contact_phone(contact, index)
  elif operation == 4:
    return put_contact_email(contact, index)
  elif operation == 5:
    return delete_contact(contact, index)
  


def put_contact_favorite(contact, index):
  global contacts
  contact['favorite'] = not contact['favorite']
  contacts[index] = contact
  print(f'\n{contact['name']} foi {'adicionado aos' if contact['favorite'] == True else 'removido dos'} favoritos com sucesso!')
  return main_menu()



def put_contact_name(contact, index):
  global contacts
  new_name = input(f'\nDigite o novo nome do contato {contact['name']}: ')
  print(f'\n{contact['name']} teve seu nome alterado para {new_name} com sucesso!')
  contact['name'] = new_name
  contacts[index] = contact
  return main_menu()



def put_contact_phone(contact, index):
  global contacts
  new_phone = input(f'\nDigite o novo número do contato {contact['name']}: ')
  contact['phone'] = new_phone
  contacts[index] = contact
  print(f'\n{contact['name']} teve seu número alterado para {new_phone} com sucesso!')
  return main_menu()



def put_contact_email(contact, index):
  global contacts
  new_email = input(f'\nDigite o novo e-mail do contato {contact['name']}: ')
  contact['email'] = new_email
  contacts[index] = contact
  print(f'\n{contact['name']} teve seu e-mail alterado para {new_email} com sucesso!')
  return main_menu()



def delete_contact(contact, index):
  global contacts
  del contacts[index]
  print(f'\n{contact['name']} foi removido com sucesso!')
  return main_menu()
  


def format_contacts(contacts_list, start):
  return '\n'.join(f'({index}) | {contact['name']} | {contact['phone']} {f'| {contact['email']}' if contact['email'] != None else ''}' for index, contact in enumerate(contacts_list, start = start))



main_menu()