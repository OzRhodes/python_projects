
m random import randrange


stages_str=[
"  __________",
" |          |",
" |          |",
" |          0",
" |         /|\ ",
" |          |",
" |         / \ ",
"---"]


wordlist = ["other","there","which","their","about","write","would","these","thing","could","number","sound","people","water","first","place","where","after","little","round","every","under","through","sentence","great","think","differ","cause","before","right","three","small","large","spell","follow","change","light","house","picture","again","animal","point","mother","world","build","earth","father","stand","should","country","found","answer","school","study","still","learn","plant","cover","between","state","never","thought","cross","start","might","story","while","press","close","night","north","together","white","children","begin","example","paper","group","always","music","those","often","letter","until","river","second","carry","science","friend","began","mountain","horse","watch","color","enough","plain","usual","young","ready","above","though","family","direct","leave","measure","product","black","short","numeral","class","question","happen","complete","order","south","problem","piece","since","whole","space","heard","better","during","hundred","remember","early","ground","interest","reach","listen","table","travel","morning","simple","several","vowel","toward","against","pattern","center","person","money","serve","appear","govern","notice","voice","power","certain","machine","figure","field","correct","pound","beauty","drive","stood","contain","front","teach","final","green","quick","develop","ocean","minute","strong","special","behind","clear","produce","street","multiply","nothing","course","wheel","force","object","decide","surface","island","system","record","common","possible","plane","stead","wonder","laugh","thousand","check","shape","equate","brought","bring","distant","paint","language","among","grand","heart","present","heavy","dance","engine","position","material","settle","speak","weight","general","matter","circle","include","divide","syllable","perhaps","sudden","count","square","reason","length","represent","subject","region","energy","probable","brother","believe","fraction","forest","window","store","summer","train","sleep","prove","exercise","catch","mount","board","winter","written","instrument","glass","grass","visit","bright","weather","month","million","finish","happy","flower","clothe","strange","eight","village","raise","solve","metal","whether","seven","paragraph","third","shall","describe","floor","either","result","century","consider","coast","phrase","silent","temperature","finger","industry","value","fight","excite","natural","sense","quite","broke","middle","moment","scale","spring","observe","child","straight","consonant","nation","dictionary","speed","method","organ","section","dress","cloud","surprise","quiet","stone","climb","design","experiment","bottom","single","stick","twenty","smile","crease","trade","melody","office","receive","mouth","exact","symbol","least","trouble","shout","except","wrote","suggest","clean","break","blood","touch"]

word = wordlist[randrange(len(wordlist))]

letters_remaining =list(word)
panel=["_"]*len(word)
win = False

print("Welcome to hangman\n\n")

wrong_guesses=0
# game loop

while True:
    print("\n")
    print ("\n")
    for letter in panel:
        print(letter, end=' ')
    print ("\n")
    guess = input("Guess a letter : ")
    
    if guess in letters_remaining:
        index = letters_remaining.index(guess)
        panel[index]=guess  
        letters_remaining[index] = "*"
    else:
        wrong_guesses +=1
        if wrong_guesses > len(stages_str):
            print("\nThe word is {}\n".format(word))
            print("\n\n YOU'RE A LOSER!")
            break
            
            
    if '_' in panel:
        for i in range(wrong_guesses-1):
            print(stages_str[i])
        print("\n")
    else:
        print("\nThe word is {}\n".format(word))
        print("\n\n YOU'RE A WINNER!")
        break
        
