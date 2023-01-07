from gtts import gTTS
from playsound import playsound
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
my_bot=ChatBot('pybot')

#trainer  = ChatterBotCorpusTrainer(my_bot)
#trainer.train('chatterbot.corpus.english')
cnt=0
while True:
    
    query = str(input(">> "))
    var = str(my_bot.get_response(query))
    tts = gTTS(var)
    cnt= cnt+1;
    tts.save("output"+str(cnt)+ ".mp3")
    playsound("output"+str(cnt)+ ".mp3")
    print(var)
    if "exit" in query:
        break;

