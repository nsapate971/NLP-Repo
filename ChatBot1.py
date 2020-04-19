
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
[
        r"what is your name ?",
        ["I am a Chatbot crafted by Nikkhil  !",]
    ],
[
        r"how are you ?",
        ["I'm doing good and at home \n How about You ?",]
    ],
[
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
[
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
[
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
[
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
[
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
[
        r"(.*) created ?",
        [" A man on earth top secret ;)",]
    ],
[
        r"(.*) (location|city) ?",
        ['ceatul, US',]
    ],
[
        r"how is status of corona in (.*)?",
        ["Weather in %1 is dangerous due to corona, Too many people losing lives :(","Todays numbers : Cases : 23, Deaths : 2 , Recovered: Updating !!"]
    ],
[
        r"where does (.*) work?",
        ["%1 is a big guy, I heard he is learning new recepies, started drinking less tea, and also coding better these days.",]
    ],[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its too much hot here in %2"]
    ],
[
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
[
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of WWE",]
    ],
[
        r"who (.*) sportsperson ?",
        ["Goldberg","Rhea Reply","Moday Night Mesaaeh"]],
[
        r"who (.*) (moviestar|actor)?",
        ["Hrithik Roshan"]],
[
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]],
]
my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}
chat = Chat(pairs, my_dummy_reflections)

def chatty():
    print("Hi, I'm Nikkhil's Chatbot  Wassup ? ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start    chat = Chat(pairs, reflections)
    chat.converse()
if __name__ == "__main__":
    chatty()
