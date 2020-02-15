

'''
The quote_list has removed any commas in the quotes as they were causing issues in retrieveing the data as intended.  This is a temporary workaround to fix the issue.
The biggest issue with doing things this way is it makes the program run in O(N^3) time.  This must be addressed!!
'''

testing_quote_list = [
                       'nasty in the pasty', 'past nastification','bite my shiny metal ass', 'lrrr', 'Hedonismbot', 'Robot 1-X',
                       'farnsworth', 'planet express', 'boneitis', 'zoidberg', 'Perfectly symmetrical violence never solved anything'
                        ]

expanded_quote_list = [
                       'nasty in the pasty', 'past nastification','bite my shiny metal ass', 'lrrr', 'Hedonismbot', 'Robot 1-X', 'let me worry about blank',
                       'professor farnsworth', 'planet express', 'boneitis', 'zoidberg', "we can all fight when we're drunk", 'celebrated poopers', 'robot 1x'
                       'death by snu', 'i choose to believe what i was programmed to believe', 'i dont want to live on this planet anymore', 'Wernstrom',
                       "a fembot living in a manbot's manputer's world", 'i find the most erotic part of a woman is the boobies', 'shut up and take my money',
                       'Sexlexia', "zapp brannigan", "brannigan's law", "brannigans law", 'why not zoidberg', 'bender bending rodriguez', 'Cubert Farnsworth',
                       'death to all humans', "Please stop sinning while I'm singing", 'fing-longer', 'fing longer', 'shut up baby i know it', 'hookerbot',
                       'technically correct. The best kind of correct', "once ate a big heaping bowl of salt", 'good fundamentals make up for the inability to dunk',
                       'you changed the outcome by measuring it',  "once ate a big, heaping bowl of salt", 'and i have to protect my kids from understanding it',
                       'we will not give in to the thinkers', 'dr. banjo', 'doctor banjo', 'hubert farnsworth', 
                       'kill all humans', 'to shreds you say', 'bad and you should feel bad' , 'bad, and you should feel bad', 'shut up baby, i know it',
                       'my manwich', 'My god, a million years', 'now strip naked and get on the probulator', 'With blackjack! And hookers', 'turanga leela',
                       'with blackjack, and hookers', 'With blackjack and hookers', "whalers on the moon", 'but you are lazy right', 'but, you are lazy right',
                       'good news, everyone', 'good news everyone', 'Smell-o-Scope', "Just don't make me smell Uranus",'Urrectum',' jacking on', ' fun on the bun',
                       'mad rhymes with an 80%', "Captain's itch", 'the hat goes on the head', 'bending college', 'robot house', 'slurm',  'arooo',
                       'Nixon with charisma', 'Thundercougarfalconbird',  "Don't quote regulation to me", 'why is there yogurt in this cap', 'roboamerican studies',
                       'lost city of atlanta', 'harpoon my ass', 'Don-Bot', 'donbot', 'The bourgeois human', 'Popplers', 'my precious torso', 'You know, I was God once',
                       'plus some other emotions which are weird and deeply confusing', 'the flesh is spongy and bruised', "She’s got more meat than a cow",
                       'go man go', "And I'm his friend, Jesus", 'Philip J. Fry', 'hell with your spoiled baby', 'build it with 6001 hulls', 'kajigger',
                       'build it with 6,001 hulls', 'Hypnotoad', 'People said I was dumb, but I proved them', "that letter that's shaped like a man wearing a hat",
                       'Nibblonian', 'Calculon', 'Negative, bossy meat creature', 'My robotic software shall meet your calculatory needs', 'Homo farnsworth',
                       'i guess if you want children beaten, you have to do it yourself', 'Pabst Blue Robot', 'You were doing well, until everyone died',
                       'the device that lets you speed or slow the passage of time', 'Now all the planets are gonna start cracking wise', 'Futurella',
                       'I moved the stars themselves to write her a love note in the sky', 'The Scary Door', 'Your best is an idiot', 'Earthicans',
                       'Let a whole new wave of cruelty wash over this lazy land', "Bender, no! You'll make God cry", "You can't count on God for jack"
                       "When you do things right, people won't be sure you've done anything at all", 'Ask not for whom the bone bones', 'eyePhone',
                       'Why does Ross, the largest friend, not simply eat the other five', 'I feel like I was mauled by Jesus', 'freedom day', 'smelloscope',
                       'I have ridden the mighty moon worm', 'The devil take this predictable colon', 'possibly a dead weasel or a cartoon viewer',
                       'show was banned after the Star Trek wars', 'Why am I sticky and naked', 'Perfectly symmetrical violence never solved anything',
                       'Bite my glorious golden ass', "or the Mongooses, that's a good team name", 'The Fighting Mongooses', 'Robot Devil', 'scooty puff'
                       'if you want a box hurled into the sun, you got to do it yourself', "Thanks, dad. I think I'll invest it on five shares of Amazon",
                       "I never thought I'd escape with my doodle, but I pulled it out", ' looks like you get to hold onto your lower horn', 'human horn',
                       'That could be my beautiful soul sitting naked on her couch', 'Rodger your Hammerstein', "I can't believe the devil is so unforgiving",
                       "I haven't felt much of anything since my guinea pig died", 'hide in this barrel, like the wily fish', "I don't like the looks of this V-GINY", 
                       "V-GINY? Doesn't ring a bell", "we're next if we don't keep in in our collective pants", 'The only lies worth believing are the ones in the Bible',
                       'Einstein is a hard name to remember', "I’ll be a monkey’s uncle if I’m this monkey’s nephew", 'What the hoth', 'Robanukah', 'liubot', 
                       'Anything less than immortality is a complete waste of time', 'The candle that burns twice as bright burns half as long. Mmm-hmm',
                       'Probably some hogwash about the human spirit', "Time? I can't go back there", 'Sell your extra bones for cash', 'mobius dick',
                       "Something sinister won't build itself", 'evolve from filthy monkey-men', 'Like the deadly Prius', 'Give us back our genitals',
                       'Never bet against me being stupid', 'All that and a small wiener', "We've opened Pandora's fly", 'Oh, dip!', 'Except for Drugman',
                       'think you can just waltz in here with no pants and become a cop', 'What a stupid, phony, made up name', 'Mr. Peppy', 'be a prude, fry',
                       'Why, I used to smoke about four feet of rope a day',  'i hate the people that love me, and they hate me', 'blernsball', 'be a prude fry',
                       'im so embarrassed.  I wish everyone else was dead', "nature's pocket", 'natures pocket', 'i can eat.  and fertilize',
                       'have the boy lay out my formal shorts', 'i both rue and lament it', 'these balls are making me testy', 'body bags and ball sacs',
                       'War were declared', 'pimpmobile', 'fatbot', 'ask Wingus and Dingus ', 'You ever kill a man with a sock', 'werecar', 
                       'what smells like blue', 'Looks like fun on a bun',  'Please insert girder', 'hobo and a rabbit', 'robo-american studies',
                       'councel of robot elders', 'robot santa',  'ndnd', 'borax kid', "56?! Now that's all I can think about",  'to shreds, you say',
                       'if you want a box hurled into the sun you got to do it yourself', 'snoo-snoo', 'space pope',
                       ]
                       # 'Futurama', 'nibbler', 'morbo', 'meatbag', 'gender bender', 'suicide booth', 'leela', 'space pope',]

quote_list = ['nasty in the pasty', 'past nastification','bite my shiny metal ass', 'lrrr', 'Hedonismbot', 'Robot 1-X',
'hubert farnsworth',  "planet express", 'boneitis', 'zoidberg', "we can all fight when we're drunk", 'celebrated poopers', 'robot 1x'
'death by snu', 'i choose to believe what i was programmed to believe', 'i dont want to live on this planet anymore', 'Wernstrom',
"a fembot living in a manbot's manputer's world", 'i find the most erotic part of a woman is the boobies', 'shut up and take my money',
'Sexlexia', "zapp brannigan", "brannigan's law", "brannigans law", 'why not zoidberg', 'death to all humans',
"Please stop sinning while I'm singing", 'fing-longer', 'fing longer', 'shut up baby i know it', 'hookerbot', 'turanga leela',
'technically correct. The best kind of correct', "once ate a big heaping bowl of salt", 'and i have to protect my kids from understanding it',
'good fundamentals make up for the inability to dunk', 'you changed the outcome by measuring it', 'we will not give in to the thinkers', 
'dr. banjo', 'doctor banjo', 
'kill all humans', 'to shreds you say', 'bad and you should feel bad' , 'You know I was God once', 'professor farnsworth'
'my manwich', 'My god a million years',  'now strip naked and get on the probulator', 'With blackjack! And hookers', "'jacking on'"
'with blackjack and hookers', "whalers on the moon", 'but you are lazy right', 'robo-american studies', 'roboamerican studies',
'good news everyone', 'Smell-o-Scope', "Just don't make me smell Uranus",'Urrectum',' jacking on', ' fun on the bun',
'mad rhymes with an 80%', "Captain's itch", 'the hat goes on the head', 'bending college', 'robot house', 'slurm',  'arooo',
'Nixon with charisma', 'Thundercougarfalconbird', "Don't quote regulation to me", 'why is there yogurt in this cap',
'lost city of atlanta', 'harpoon my ass', 'Don-Bot', 'donbot', 'The bourgeois human', 'Popplers', 'my precious torso', 
'plus some other emotions which are weird and deeply confusing', 'the flesh is spongy and bruised', "She’s got more meat than a cow",
'go man go', "And I'm his friend Jesus", 'Philip J. Fry', 'hell with your spoiled baby', 'build it with 6001 hulls', 'kajigger',
'Hypnotoad', 'People said I was dumb but I proved them', "that letter that's shaped like a man wearing a hat", 'Cubert Farnsworth',
'Nibblonian', 'Calculon', 'Negative bossy meat creature', 'My robotic software shall meet your calculatory needs', 'Homo farnsworth',
'i guess if you want children beaten you have to do it yourself', 'Pabst Blue Robot', 'You were doing well until everyone died',
'the device that lets you speed or slow the passage of time', 'Now all the planets are gonna start cracking wise', 'Futurella',
'I moved the stars themselves to write her a love note in the sky', 'The Scary Door', 'Your best is an idiot', 'Earthicans',
'Let a whole new wave of cruelty wash over this lazy land', "Bender no! You'll make God cry", "You can't count on God for jack",
"When you do things right people won't be sure you've done anything at all", 'Ask not for whom the bone bones', 'eyePhone',
'Why does Ross the largest friend not simply eat the other five', 'I feel like I was mauled by Jesus', 'freedom day', 'smelloscope',
'I have ridden the mighty moon worm', 'The devil take this predictable colon', 'possibly a dead weasel or a cartoon viewer',
'show was banned after the Star Trek wars', 'Why am I sticky and naked', 'Perfectly symmetrical violence never solved anything',
'Bite my glorious golden ass', "or the Mongooses that's a good team name", 'The Fighting Mongooses', 'Robot Devil', 'scooty puff'
'if you want a box hurled into the sun you got to do it yourself', "Thanks dad. I think I'll invest it on five shares of Amazon",
"I never thought I'd escape with my doodle but I pulled it out", ' looks like you get to hold onto your lower horn', 'human horn',
'That could be my beautiful soul sitting naked on her couch', 'Rodger your Hammerstein', "I can't believe the devil is so unforgiving",
"I haven't felt much of anything since my guinea pig died", 'hide in this barrel like the wily fish', "I don't like the looks of this V-GINY", 
"V-GINY? Doesn't ring a bell", "we're next if we don't keep in in our collective pants", 'The only lies worth believing are the ones in the Bible',
'Einstein is a hard name to remember', "I’ll be a monkey’s uncle if I’m this monkey’s nephew", 'What the hoth', 'Robanukah', 'liubot', 
'Anything less than immortality is a complete waste of time', 'The candle that burns twice as bright burns half as long. Mmm-hmm',
'Probably some hogwash about the human spirit', "Time? I can't go back there", 'Sell your extra bones for cash', 'mobius dick',
"Something sinister won't build itself", 'evolve from filthy monkey-men', 'Like the deadly Prius', 'Give us back our genitals',
'Never bet against me being stupid', 'All that and a small wiener', "We've opened Pandora's fly", 'Except for Drugman',
'think you can just waltz in here with no pants and become a cop', 'What a stupid phony made up name', 'Mr. Peppy',
'Why I used to smoke about four feet of rope a day',  'i hate the people that love me and they hate me', 'blernsball', 'be a prude fry',
'im so embarrassed.  I wish everyone else was dead', "nature's pocket", 'natures pocket', 'i can eat.  and fertilize',
'have the boy lay out my formal shorts', 'i both rue and lament it', 'these balls are making me testy', 'body bags and ball sacs',
'War were declared', 'pimpmobile', 'fatbot', 'ask Wingus and Dingus ', 'You ever kill a man with a sock', 'werecar', 
'what smells like blue', 'Looks like fun on a bun', 'Please insert girder', 'hobo and a rabbit', 'bender bending rodriguez', 
'councel of robot elders', 'robot santa', 'ndnd', 'borax kid', "56?! Now that's all I can think about", 'snoo-snoo' ]
# 'Futurama', 'farnsworth', 'meatbag', 'nibbler', 'morbo', 'gender bender', 'suicide booth', 'leela', 'space pope',]