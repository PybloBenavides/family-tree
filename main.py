import networkx as nx
import pandas as pd

data = pd.read_csv(r"C:\Users\pablo\Desktop\moctezuma\arbol_granaino.csv")




def read_data(data):
    people = {}
    person_number = 0
    for j, row in data.iterrows():

        father = None
        mother = None

        name = row[NAME]
#         if not isinstance(name,str):
#             print(name)
#         print(name)
        father_name = row[FATHER]
        mother_name = row[MOTHER]
        branch = row[BRANCH]
        born = row[BORN]

        if name in people.keys():
            previous = people[name]
            previous_father = previous.father
            previous_mother = previous.mother
            if previous_father.name == father_name and previous_mother.name == mother_name:
#                 print(f"{name} persona repetido")
                continue

        if father_name != np.nan and father_name is not None:
            if father_name in people.keys():
                father = people[father_name]
                father.male = True
            else:
                father = Person(father_name, person_number,branch)
                person_number+=1
                people[father_name] = father
        if mother_name != np.nan and mother_name is not None:
            if mother_name in people.keys():
                mother = people[mother_name]
                mother.male = False
            else:
                mother = Person(mother_name, person_number, branch)
                person_number+=1
                people[mother_name] = mother
        person = Person(name, person_number, branch, father=father, mother=mother, born=born )
        person_number += 1
        people[name] = person
        if father is not None and mother is not None:
            father.add_couple(mother)
            mother.add_couple(father)
    return people
        

def assign_fake_birthdays(people):
    for j in [0,1]:
        for name, person in people.items():
            if person.needs_birthday:
                person.find_birthday()


def assign_positions(families_dict):
	#     last_occupied_pos = 0
    counter = 0
    for brotherhood in families_dict.values():
        counter += 1
        if counter%2==0:
            left_or_right = -1
        else:
            left_or_right = 1
        brotherhood.position =  10 * left_or_right * int(counter/2)
        
#         last_occupied_pos+=10
        for brother in brotherhood.brothers:
            brotherhood.father.x_position = brotherhood.position + 5 * left_or_right
            brother.x_position = brotherhood.position + 2 * left_or_right
            brotherhood.mother.x_position = brotherhood.position + 5 * left_or_right
        
def gather_couples(people):
    for person in people.values():
        if person.brotherhood is None:
            if person.couple != {}:
#                 print(person.couple)
                mate = person.couple[1]
#                 if mate.brotherhood is not None:
                person.x_position = mate.x_position - 2.5
#                     print("asercando a shu husbnad")
                
def gather_families(people):
    families_dict = {}
    for person in people.values():
        father = person.father
        mother = person.mother
        if father is not None and mother is not None:
            if (father,mother) in families_dict.keys():
                person.brotherhood = families_dict[(father,mother)]
                brotherhood.brothers.append(person)
            else:
                brotherhood = Brotherhood(father,mother)
                brotherhood.brothers.append(person)
                families_dict[(father,mother)] = brotherhood
    assign_positions(families_dict)
    gather_couples(people)

