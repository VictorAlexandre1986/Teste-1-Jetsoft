import random

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

def main():
    students = [
        Student("Alice", 20),
        Student("Bob", 22),
        Student("Charlie", 19),
        Student("David", 21),
    ]

    # Teste de operadores de comparação
    print("Teste de igualdade:")
    print(students[0] == students[1])  
    print(students[0] == students[2])  
    print(students[0] == students[0])  

    print("\nTeste de menor que:")
    print(students[2] < students[1])  
    print(students[3] < students[0])   

    print("\nTeste de maior que ou igual a:")
    print(students[1] >= students[0])  
    print(students[2] >= students[3])  

    # Embaralhar a lista de alunos
    random.shuffle(students)

    # Ordenar a lista de alunos
    students.sort()

  
    print("\nInformações dos alunos após ordenação:")
    for student in students:
        print(f"Nome: {student.name}, Idade: {student.age}")

if __name__ == "__main__":
    main()