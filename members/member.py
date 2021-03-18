


class Person():
    def __init__(self, name, number, branch, father=None, mother=None, born=1100, male=None):
        self.brotherhood = None
        self.name = name
        self.born = born
        self.children = []
        self.father = father
        self.mother = mother
        self.couple = {} # Pueden ser multiples matrimonios
        self.male = male
        self.number = number
        self.calculated_birthday = False
        self.needs_birthday=True
        self.branch = branch
        self.x_position = 0
        self.changed_pos = False
        if born == 1100:
            self.needs_birthday = True
            
        else:
            self.needs_birthday = False
        if father is not None:
            father.add_child(self)
        if mother is not None:
            mother.add_child(self)
    
    def add_child(self, child):
        self.children.append(child)
        if self.needs_birthday: # No sabemos fecha de este tipo
            if not child.needs_birthday:
                self.birthday_from_other(child, child=True)
        else: #Sabemos fecha de este tipo
            if child.needs_birthday:
                child.birthday_from_other(self,parent=True)

    def add_couple(self, mate):
        if self.needs_birthday:
            if not mate.needs_birthday:
                self.birthday_from_other(mate)

        else:
            if mate.needs_birthday:
                mate.birthday_from_other(self)
            
        if self.couple.keys():
            self.couple[max(self.couple.keys()) +1 ] = mate
            
        else:
            self.couple[1] = mate
    def birthday_from_other(self, other, child=False,parent=False):
#         print("birthdayy!!")
        if self.needs_birthday:
            difference = 0
            if child:
                difference -=24
            elif parent:
                difference += 24
            self.born = other.born + difference
            self.needs_birthday = False
            self.calculated_birthday = True
        
    def find_birthday(self):
        if self.father is not None:
            if not self.father.needs_birthday:
                self.birthday_from_other(father, parent=True)
        if self.mother is not None:
            if not self.mother.needs_birthday:
                self.birthday_from_other(mother, parent=True)
        if self.children:
            for child in self.children:
                if not child.needs_birthday:
                    self.birthday_from_other(child, child=True)
        if self.couple:
            for mate in self.couple.values():
                if not mate.needs_birthday:
                    self.birthday_from_other(mate)
            
    def __str__(self):
        return self.name
    def info(self):
        print(f"{self.name} hija de {self.father} y {self.mother} nacio en el {self.born}, caso con {self.couple} y tuvo hijos {[child.name for child in self.children]}")




class Brotherhood():
    def __init__(self, father, mother):
        self.mother = mother
        self.father = father
        self.position = None
        self.brothers = []