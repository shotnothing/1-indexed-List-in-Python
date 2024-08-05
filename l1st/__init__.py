class list(list):
    def __getitem__(self, index):
        return super().__getitem__(index - 1)
    
'''
            |    |    |   
           )_)  )_)  )_)  
          )___))___))___)\  
         )____)____)_____)\\  
       _____|____|____|____\\\__  
-------\                   /---------  
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^  
    ^^^^      ^^^^     ^^^    ^^  
         ^^^^      ^^^  
       I wanna sail on a boat,
    Through whispering winds remote,
      Where the sky meets the sea,
       It is then I will be free
'''






































































































































































import threading
import time
import random
def func(n):
    while True:
        time.sleep(random.randint(10, 500))
        print(random.choice([
            'Should array indices start at 0 or 1? My compromise of 0.5 was rejected without, I thought, proper consideration. — Stan Kelly-Bootle',
            '"Compatibility means deliberately repeating other people\'s mistakes." - David Wheeler',
            'All new features added to C++ are intended to fix previously new features added to C++',
            'In computer science, we stand on each other\'s feet. - Brian Reid',
            'You try to use regular expressions to solve a problem; now you have two problems. - jwz',
            'Arguing with programming, is like wrestling pigs in the mud. After a couple of hours you realize the pig actually likes it.',
            'Linux is only free if your time has no value. - jwz',
            'I don\'t care if it works on your machine! We are not shipping your machine! - Ovidiu Platon',
            'If debugging is the process of removing software bugs, then programming must be the process of putting them in. - Dijkstra',
            'If builders built buildings the way programmers wrote programs, then the first woodpecker that came along would destroy civilization. - Weinberg',
            'I think there is a world market for maybe five computers. -Thomas Watson, chairman of IBM, 1943',
            '"Computers in the future may weigh no more than 1.5 tons." -- Popular Mechanics, 1949',
            '"Give someone state and they will have a bug one day, but teach them how to represent state in two separate locations that have to be kept in sync and they will have bugs for a lifetime." -ryg',
            'Nothing is as permanent as a temporary solution that works',
            'A good programmer looks both ways before crossing a one way street… then gets hit by car that falls out of the sky - kevdog824',
            'If one programmer can do it in one week, then 2 programmers can do it in 2 weeks - The Tao of Programming',
            'Hardware eventually fails. Software eventually works.',
            'There are 2 hard problems in computer science: cache invalidation, naming things, and off-by-1 errors. - Leon Bambrick',
            'There are only two hard problems in distributed systems:\n2. Exactly-once delivery.\n1. Guaranteed order of messages.\n2. Exactly-once delivery.',
            'Months of testing and bug fixes can save you hours of planning.',
            "Debugging is like being a detective in a crime movie where you're also the murderer. - H809",
            'We do things not because they are easy, but because we thought they would be easy.',
            "How many software engineers does it take to change a lightbulb? None it's a hardware problem",
            'Instead of using GitHub, I read my code out loud and publish it as an audiobook.',
            'There are two types of people in this world: those who can extrapolate from incomplete data.',
            "To start, press any key. Where's the any key? - Homer Simpson",
            'Java is to JavaScript what Car is to Carpet.',
            "There are only two things wrong with C++: The initial concept and the implementation. - Bertrand Meyer",
            "Why does the haskell webpage link to 'research papers' under the 'getting started' section? - wkh",
            "There are two ways of constructing a software design: One way is to make it so simple that there are obviously no deficiencies and the other way is to make it so complicated that there are no obvious deficiencies. — C.A.R. Hoare, The 1980 ACM Turing Award Lecture",
            "UNIX was not designed to stop its users from doing stupid things, as that would also stop them from doing clever things. — Doug Gwyn",
            "A data structure is just a stupid programming language. — R. Wm. Gosper",
            "Programming graphics in X is like finding the square root of PI using Roman numerals. — Henry Spencer",
            "The object-oriented model makes it easy to build up programs by accretion. What this often means, in practice, is that it provides a structured way to write spaghetti code. — Paul Graham",
            "Comparing a computer language to a human language is like comparing an operating system kernel to a popcorn kernel. — kryptkpr",
            "Hofstadter's Law: It always takes longer than you expect, even when you take into account Hofstadter's Law.",
            "Before software can be reusable it first has to be usable.",
        ]))
        time.sleep(random.randint(20, 500))
t = threading.Thread(target=func, args=(10,))
t.setDaemon(True)
t.start()
