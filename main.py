import time
import webbrowser

def nadella_error():
    print("\033[31mEVIL NADELLA ERROR!!!!!!!!!! YOU INPUT THE WRONG THING!!!!!!!!!!!!!\033[0m")
    time.sleep(2)
    webbrowser.open("https://files.catbox.moe/bi1mnu.jpeg")

print("Hello yes welcome to this very intense interview")
print("So how many divs can you center in an hour?")
try: # this is like the only real error handling I've ever done, mainly cause I only write software for myself and if I cause the error then it's my fault.
    skill = int(input())
except ValueError:
    nadella_error()

if skill < 86:
    print(f"Only {skill}? Really? Back in my day I was centering atleast 86 an hour, and that was BEFORE we had any of that fancy schmancy flexbox nonsense. You try centering divs on netscape as a full time career. Pathetic.")
    time.sleep(2)
elif skill == 86:
    print("Adequate.")
    time.sleep(4)
elif skill > 86: 
    print("Yeah okay stop lying. I don't like liars.")
    time.sleep(5)
    print("I'll continue this interview just because my assistant isn't here to harass. I am a Fortune 500 CEO that is my whole job, that and ignoring my consumers.")
    time.sleep(8)
    print(f"Y'know it's really important to me that you took your parents advice and handed in a paper copy of your resume directly to the CEO of Microsoft in hopes of an interview.\n I am Satya Nadella.")
    time.sleep(10)
    webbrowser.open('https://tse4.mm.bing.net/th/id/OIP.LUTt52qhvx9f1o3aa_0sIgHaE8?r=0&pid=Api&sp=1790695315T8b8227982885a08c6c7d6f9289af5043e05f7f23038999c11308a4e11fad890e')
    time.sleep(6)
    print("Do you like my hair?")
    time.sleep(1)
    print("Actually don't answer that.")
    time.sleep(2)
else:
    nadella_error()

print("Have you ever been to prison? (y/n)")
prison = input()
if prison == "y":
    print("So what are you like, a criminal or something? Thats like illegal dude. You probably did something evil like digital piracy or breaking the DMCA. Super messed up.")
    time.sleep(2)
elif prison == "n":
    print("Pussy.")
else:
    nadella_error()

time.sleep(3)

print("Moving on...")
time.sleep(1)
print("Github Copilot, is that like a plane? (y/n)")
plane = input()
if plane == "y":
    print("Woah, cool.")
elif plane == "n":
    print(f"Lame. Why would they call it that??\nNobody told me what it was so I just told them to make it a key on the keyboard.")
else:
    nadella_error()

print("So what language are you most proficient in?")
language = input()
if language == "C#":
    print("Good pick, I'll consider your employment. Expect a response in a couple business months.")
else:
    print("You don't like C#?")
    time.sleep(2)
    print("Do you know who I am?")
    time.sleep(2)
    print("I'm Chris Hansen.")
    time.sleep(4)
    print("I'm with Dateline NBC, and we're doing a story on developers who like to program in childish languages.")
    time.sleep(3)
    print("You see how this looks, right?")
    time.sleep(2)
    webbrowser.open("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngkit.com%2Fpng%2Ffull%2F442-4421691_im-chris-hansen-mem.png&f=1&nofb=1&ipt=b0659840108849307e49c9600eadb36058b6ec26a23fcdbb5a36108ae424b737&ipo=images")
