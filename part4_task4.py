contact_list = {'Арген': 112233, 'Дастан': 789456, 'Тилек': 112233, 'Арсен': 122112}
final = 112233
class List:
    
    def desc(self):
        print('{}'.format(contact_list))
    

class ContactList(List):
    
    def search_by_name(self):
        for key, value in contact_list.items():
            if final == value:
                print(value, key)
    

lis_num = List()
lis_num.desc()
same = ContactList()
same.search_by_name()