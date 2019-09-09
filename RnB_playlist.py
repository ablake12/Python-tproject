#Alanza Blake
#Cis 215

import time#import module
import random#import module


#A Playlist should store a list of songs, and provide a method for you to, add songs to a playlist, play your playlist and shuffle it. 
#The Playlist should also be able to produce (via a method called runtime) the total running time of your list of songs. 
#For example, if youve added three songs that are three seconds each, your runtime method should return 9.
#Playing will be accomplished by printing out the songs in the order prescribed by your playlist. 
#Shuffled playlists should not repeat a song that has already been played.

class Song:#class 
    def __init__(self, artist, title, album, time, genre):#constructor includes artist/band(string), song title(string), album/mixtape(string), running time(float), genre(string)
        self.artist=artist#initializing artist/band name
        self.title=title#initializing song title 
        self.album=album#initializing album/mixtape name
        self.time=time#initializing running time
        self.genre=genre#initializing genre
    #Create accessor methods to set the artist name, song title, and album title
    def get_artist(self):#pre:self is a rational object
        return self.artist#post:returns self's artist string 
    def get_title(self):#pre:self is a rational object
        return self.title#post:returns self's song title string
    def get_album(self):#pre:self is a rational object
        return self.album#post:returns self's album title string 
    def get_time(self):#pre:self is a rational object
        return self.time#post:returns self's time float
    def __str__(self):#pre:self is a rational object
        return self.title+" by "+self.artist+" - "+self.album#post:returns self's value which is a string

class Playlist:#class
    def __init__(self):#constructor consists of object
        self.tracklist = []#initialize tracklist with empty list
        self.shufflelist = []#initialize shuffledlist with empty list
        #shuffle list is used to prevent shuffling the list permanently because random.shuffle() will keep the list shuffled
    def add_song(self, track):#pre:self is a rational object and track is a string
        self.tracklist.append(track)#post:the string track is appended to the list tracklist
        self.shufflelist.append(track)#post:the string track is appended to shuffle list
    def play(self):#pre:self is a rational object
        for i in self.tracklist:#for elements in the list
            time.sleep(1)#so the elements won't print all at once
            print(i)#post:prints strings
    def shuffle_play(self):#pre:self is a rational object
        random.shuffle(self.shufflelist)#use random module method to shuffle playlist
        #random.shuffle()shuffles the list completely
        for j in range(len(self.shufflelist)):#for the range from 0 to the length of the shuffled list
            time.sleep(1)#so the elements won't print all at once
            print(self.shufflelist[j])#post:prints strings
    #create method called running time
    def running_time(self):#pre:self is a rational object
        self.tracktime = 0#initialize the duration times with empty list
        for k in self.tracklist:#for the objects placed in the tracklist
            self.tracktime = self.tracktime + k.get_time()#use the get_time method from the song class to add to the track time
        print("%.2f minutes" % (self.tracktime))#post:prints a float which is the sum of the duration of every song
            
                   
ari=Song("Ari Lennox", "Facetime", "Shea Butter Baby", 2.32, "R&B")#create ari object
bey=Song("Beyonce", "Sorry", "Lemonade", 3.53, "R&B")#create beyonce object
key=Song("Keyshia Cole", "Love", "The Way It Is", 4.15, "R&B")#create keyshia object
sza=Song("SZA", "The Weekend", "Ctrl", 4.32, "R&B")#create sza object
#just print elements of list since each song has an str
rnb=Playlist()#call playlist constructor
rnb.add_song(ari)#call add song method for default song
rnb.add_song(bey)#call add song method for default song
rnb.add_song(key)#call add song method for default song
rnb.add_song(sza)#call add song method for default song

#Create menu for user

print("Welcome to your R&B playlist!")
print()#space
print("1.Add+ a song")#menu option 1
print("2.Play")#menu option 2
print("3.Shuffle Play")#menu option 3
print("4.Running Time")#menu option 4
print("5.Quit")#menu option
print()#space
option = int(input("Please choose a number: "))#user input 
print()#space
while option != 5:#while the user doesn't choose integer 5/quit
    if option == 1:#pre:user chooses the integer 1
        print()#space
        song_title=input("Enter the song title: ")#user input for song title string
        song_artist=input("Enter the artist: ")#user input for artist string
        song_album=input("Enter the album/Mixtape name: ")#user input for album string
        song_time=float(input("Enter the song duration: "))#user input for time float
        new_song=Song(song_artist, song_title, song_album, song_time, "R&B")#call Song object using the user inputs
        rnb.add_song(new_song)#post:the object is appended to the list for playlist
    if option == 2:#pre:user chooses the integer 2
        print()#space
        rnb.play()#post:method play prints strings 
    if option == 3:#pre:user chooses the integer 3
        rnb.shuffle_play()#post:method shuffle_play prints strings unsorted
    if option == 4:#pre:user chooses the integer 4
        rnb.running_time()#post: print the method running time to give the user the running time
    print()#space
    time.sleep(1)#so everything doesn't print all at once
    print("1.Add+ a song")#menu option 1
    print("2.Play")#menu option 2
    print("3.Shuffle Play")#menu option 3
    print("4.Running Time")#menu option 4
    print("5.Quit")#menu option
    print()#space
    option = int(input("Please choose a number: "))#user input    
    print()#space
