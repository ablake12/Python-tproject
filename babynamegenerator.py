#import random module
import random

#create a main function to ask the user for their input
def main():
    #user input
    usrInput=input('Do you want a girl name, a boy name, or a unisex name? ')
    #call babyName function
    babyName(usrInput)
    
#create babyName function 
def babyName(i):
    #create a list of names with a girl category, boy category, and unisex category
    #create a list of list which has 15 list of names in each category
    names=[
        [['Andrea', 'Kayla', 'Naomi', 'Ashley', 'Paula', 'Alexis', 'Alina', 'Julienna', 'Sierra', 'Diamond'],#girl row 1
         ['Emma', 'Olivia', 'Ava', 'Sophie', 'Abigail', 'Isabella', 'Grace', 'Chloe', 'Victoria', 'Vanessa'],#girl row 2
         ['Natalie', 'Hannah', 'Zoey', 'Nora', 'Claire', 'Aaliyah', 'Kennedy', 'Lucy', 'Ariana', 'Maya'],#girl row 3
         ['Hailey', 'Willow', 'Piper', 'Gianna', 'Nia', 'Julia', 'Valentina', 'Vivian', 'Reagan', 'Mackenzie'],#girl row 4
         ['Lydia', 'Isa', 'Ivy', 'Lillian', 'Avani', 'Paulette', 'Pauline', 'Faith', 'Briana', 'Jasmine'],#girl row 5
         ['Alyssa', 'Mary', 'Ashlee', 'Sydney', 'Lauren', 'Trinity', 'Kimberly', 'Valerie', 'Fiona', 'Mya'],#girl row 6
         ['Paige', 'Elyse', 'Georgina', 'Amaya', 'Laila', 'Harmony', 'Payton', 'Angelina', 'Catherine', 'Malia'],#girl row 7
         ['Malia', 'Michelle', 'Alana', 'Juliette', 'Rebecca', 'Adrienna', 'Adrienne', 'Sawyer', 'Destiny', 'Alivia'],#girl row 8
         ['Toni', 'Selena', 'Lola', 'Remy', 'Imani', 'Camille', 'Melissa', 'Thea', 'Lea', 'Mia'],#girl row 9
         ['Amiyah', 'Journey', 'Kaya', 'Kiana', 'Kiara', 'Brooke', 'Kristen', 'Bria', 'Courtney', 'Kylie'],#girl row 10un
         ['Dana', 'Laura', 'Myra', 'Maliah', 'Karlie', 'Kaiya', 'Desiree', 'Cristina', 'Renee', 'Allison'],#girl row 11
         ['Florence', 'Emerald', 'Sonya', 'Yara', 'Jazmine', 'Jasmin', 'Jazmin', 'Alisa', 'Samira', 'Jennifer'],#girl row 12
         ['Zendaya', 'Rihanna', 'Layla', 'Audrey', 'Stella', 'Savannah', 'Hazel', 'Leah', 'Elianna', 'Melanie'],#girl row 13
         ['Madeline', 'Josephine', 'Brielle', 'Ximena', 'Mary', 'Margaret', 'Arya', 'Eliza', 'Valeria', 'Cecilia'],#girl row 14
         ['Nicole', 'Amara', 'Lola', 'Janelle', 'Lola', 'Ciara', 'Danielle', 'Gabrielle', 'Keisha', 'Kenya']#girl row 15
         ],#girl list
        [['Aiden', 'Darius', 'Michael', 'Booker', 'Amari', 'Jamir', 'Zaire', 'Christopher', 'Odell', 'Xavier'],#boy row 1
         ['Liam', 'William', 'Harry', 'Mason', 'Elijah', 'Jacob', 'James', 'Lucas', 'Daniel', 'Matthew'],#boy row 2
         ['Malcolm', 'Jackson', 'Luke', 'Wyatt', 'Joseph', 'Samuel', 'Henry', 'David', 'Owen', 'Julian'],#boy row 3
         ['Levi', 'Issac', 'Joshua', 'Anthony', 'Lincoln', 'Andrew', 'Mateo', 'Ryan', 'Isaiah', 'Nathaniel'],#boy row 4
         ['Lawrence', 'Thomas', 'Caleb', 'Cordell', 'Josiah', 'Jonathan', 'Connor', 'Eli', 'Leo', 'Asher'],#boy row 5
         ['Theodore', 'Adrian', 'Jeremiah', 'Robert', 'Ezra', 'Nicholas', 'Nolan', 'Austin', 'Adam', 'Carson'],#boy row 6
         ['Kevin', 'Axel', 'Brandon', 'Cole', 'Wesley', 'Luis', 'Ryder', 'George', 'Emmett', 'Finn'],#boy row 7
         ['Antonio', 'Beau', 'Tobias', 'Jude', 'Amir', 'Marvin', 'Akil', 'Gregory', 'Brody', 'Rowan'],#boy row 8
         ['Ivan', 'Stephen', 'Maxwell', 'Carlos', 'Justin', 'Timothy', 'Bryce', 'Clay', 'Edward', 'Kyrie'],#boy row 9
         ['Peter', 'Brian', 'Paul', 'Kenneth', 'Andre', 'Milo', 'Corbin', 'Zack', 'Sean', 'Eric'],#boy row 10
         ['Martin', 'Rafael', 'Cash', 'Raymond', 'Connor', 'Mario', 'Cesar', 'Cohen', 'Seth', 'Jeffrey'],#boy row 11
         ['Tyreese', 'Tyrone', 'Tyson', 'Jase', 'Zayn', 'Collin', 'Marshall', 'Romeo', 'Trevor', 'Warren'],#boy row 12
         ['Grady', 'Solomon', 'Malik', 'Harvey', 'Porter', 'Sullivan', 'Allen', 'Kendrick', 'Russell', 'Nasir'],#boy row 13
         ['Winston', 'Cyrus', 'Phillip', 'Khalil', 'Bruce', 'Franklin', 'Derrick', 'Jonas', 'Tate', 'Hank'],#boy row 14
         ['Drake', 'Mohammad', 'Jason', 'Frederick', 'Keith', 'Scott', 'Rowen', 'Davis', 'Roland', 'Roy']#boy row 15
         ],#boy list
        [['Jordan', 'Alex', 'Angel', 'Avery', 'Charlie', 'Cameron', 'Taylor', 'Tony', 'Jalen', 'Carter'],#unisex row 1
         ['Riley', 'Kendall', 'Blake', 'Zion', 'Jaiden', 'Amani', 'Casey', 'Iman', 'Noah', 'Logan'],#unisex row 2
         ['Dylan', 'Tyler', 'Miles', 'Andy', 'Drew', 'Chris', 'Jessie', 'Jackie', 'Justice', 'Jody'],#unisex row 3
         ['Jamie', 'Sasha', 'Shawn', 'Tory', 'Tracy', 'Amari', 'Peyton', 'Reese', 'Marley', 'Quinn'],#unisex row 4
         ['Hayden', 'Spencer', 'Elliott', 'Lennox', 'Blair', 'Cleo', 'Miller', 'Baker', 'Milan', 'Ocean'],#unisex row 5
         ['Frankie', 'Shay', 'Jules', 'Wren', 'Armani', 'Royal', 'Perry', 'Blue', 'Campbell', 'Clarke'],#unisex row 6
         ['Robin', 'Rumi', 'Honor', 'Jazz', 'Kirby', 'Marlo', 'Devin', 'Dakota', 'Adrian', 'Addison'],#unisex row 7
         ['Briley', 'Corey', 'Montana', 'Pat', 'Kelsey', 'Shannon', 'Harley', 'Micah', 'Kyle', 'River'],#unisex row 8
         ['Harper', 'Phoenix', 'Jaden', 'Nico', 'Gray', 'Reagan', 'Alby', 'Ali', 'Alexis', 'Ashely'],#unisex row 9
         ['Billy', 'Brady', 'Bobby', 'Brook', 'Carmen', 'Cody', 'Emery', 'Francis', 'Fabian', 'Glenn'],#unisex row 10
         ['Rory', 'Harley', 'Hunter', 'Jade', 'Kadin', 'Kerry', 'Carry', 'Jalin', 'Jaden', 'Lee'],#unisex row 11
         ['London', 'Linden', 'Lane', 'Lonnie', 'Lumi', 'Moriah', 'Noel', 'Raphael', 'Sage', 'Sam'],#unisex row 12
         ['Sunny', 'Scout', 'Tristin', 'Terry', 'True', 'Toby', 'Unique', 'Wallace', 'West', 'Winter'],#unisex row 13
         ['Zen', 'Benny', 'Christian', 'Clare', 'Connie', 'Darcy', 'Danny', 'Denny', 'Izzy', 'Gene'],#unisex row 14
         ['Jerry', 'Jo', 'Kelly', 'Lou', 'Max', 'Nicky', 'Mel', 'Ruby', 'Reggie', 'Ray']#unisex row 15
         ]#unisex list
        ]#list of names
    a=random.randint(0, 14)#list within the girl list
    b=random.randint(0, 9)#random numbers for the names
    #quits if the user input doesn't contain none of the options given
    #create conditional statement that determines which category you should get the name from based off the user's input
    if 'girl' in i:#if the user enters girl
        babyName=names[0][a][b]#use the girl list of names
    elif 'boy' in i:#if the user enters boy
        babyName=names[1][a][b]#use the boy list of names 
    elif 'unisex' in i:#if the user enters unisex
        babyName=names[2][a][b]#use the unisex list of names
    #print(babyName)#prints gender name for user
    ask='noNo'#initializing the variable ask
    #newList=[]
    #while the user keeps saying they don't like the name
    #while loop will stop if user types in yes or anything other than no/No
    while 'no' in ask:
        a=random.randint(0, 14)#random numbers for the names
        b=random.randint(0, 9)#random numbers for the names
        #newList.append(babyName)
        print(babyName)
        #print(newList)
        #a=random.randint(0, 9)#random numbers for the names
        if 'girl' in i:#if the user enters girl
            babyName=names[0][a][b]#use the girl list of names
        elif 'boy' in i:#if the user enters boy
            babyName=names[1][a][b]#use the boy list of names 
        elif 'unisex' in i:#if the user enters unisex
            babyName=names[2][a][b]#use the unisex list of names 
        ask=input('Do you like this name? ')#enter user input
        #a=random.randint(0, 9)#random numbers for the names
        
    #if 'yes' in ask:


main()#call the main function