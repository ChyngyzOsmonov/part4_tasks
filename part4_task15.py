import random
from random import shuffle
del_suits = []
c_faces = []
class Desk_of_cards:

    faces = ['P-2', 'P-3', 'P-4', 'P-5', 'P-6', 'P-7', 'P-8', 'P-9', 'P-10', 'P-J','P-Q','P-K','P-A',
             'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-J','B-Q','B-K','B-A',
             'C-2', 'C-3', 'C-4', 'C-5', 'C-6', 'C-7', 'C-8', 'C-9', 'C-10', 'C-J','C-Q','C-K','C-A',
             'K-2', 'K-3', 'K-4', 'K-5', 'K-6', 'K-7', 'K-8', 'K-9', 'K-10', 'K-J','K-Q','K-K','K-A']
    
    def faces_s(self):
        shuffle(self.faces)
        #print(self.faces)

    def mixed(self):
        for j in self.faces:
            c_faces.append(j)
        print('{}'.format(c_faces[-1]))

    def del_card(self):
        c_faces.pop()
        print('Осталось карт: ', len(c_faces))

cards = Desk_of_cards()
cards.faces_s()
cards.mixed()
cards.del_card()

        
        

