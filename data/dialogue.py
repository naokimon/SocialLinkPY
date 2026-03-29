from player import Player

commandlist = {
    "Help": "List all commands",
    "Actions": "List all actions on your location.",
    "Shops": "List all available shops on your location.",
    "Clear": "Clear  screen of all commands."
}

introDialogue = [
    ("igor", '"Ah... so you have made it then, yes?"'),
    ("igor", '"My name is Igor... I am delighted to make your acquaintance."'),
    ("igor", '"This place exists between dream and reality, mind and matter..."'),
    ("igor", '"It is a room that only those who are bound by a "contract" may enter..."'),
    ("igor", '"It may be that such a fate awaits you in the near future."'),
    ("igor", '"Hm... I see."'),
    ("igor", '''"Now, let\'s take a look into your future, shall we?"\n'''
             '''Igor hovers his hand over the table, a mysterious glow appears. As the glow subsides a strange card is seen on the table.'''),
    ("igor", '"Do you believe in fortune telling?"\n'
             'Igor swipes his hand across the table, several more cards spread out evenly.'),
    ("igor", '"Each reading is done with the same cards, yet the result is always different..."'),
    ("igor", '''"*chuckle* Life itself follows the same principles, doesn\'t it?"\n'''
             '''As Igor lifts his finger upwards one of the cards flip over.'''),
    ("igor", '"Hm... The Tower in the upright position represents the immediate future. It seems a terrible catastrophe is imminent."'),
    ("igor", '"The card indicating the future beyond that is..."\n'
             'Igor lifts his finger again and another card flips over.'),
    ("igor", '"The moon, in the upright position."'),
    ("igor", '"This card represents "hesitation" and "mystery"... Very interesting indeed."'),
    ("igor", '"It seems you will encounter a misfortune at your destination, and a great mistery will be imposed upon you."'),
    ("igor", '"In the coming days, you will enter into a contract of some sort, after which you will return here."'),
    ("igor", '"The coming year is a turning point in your destiny... If the mystery goes unsolved your future may be forever lost."'),
    ("igor", '"My duty is to provide assistance to our guests to ensure that does not happen."\n'
             'Igor swipes his hand across the table one last time to disappear the cards into thin air.'),
    ("igor", '"Ah! I have neglected to introduce my assistant to you."'),
    ("igor", '"This is Margaret. She is a resident of this place, like myself."'),
    ("margaret", '"My name is Margaret. I am here to accompany you through your journey."'),
    ("igor", '"We shall attend to the details another time"'),
    ("igor", '"Until then, farewell..."'),
    ("train", '''You're now in the train on your way to Yasoinaba Station. That's where you will meet your uncle and his daughter.'''),
    ("train", '''You quickly check your phone and see a message, it reads "Meet us outside Yasoinaba Station at 4PM."'''),
    ("train", '''As you finish reading the message on your phone, someone can be heard speaking on the train's intercom.'''),
    ("train", '''"We will arrive at the Yasogami terminal in a few minutes. Passengers headed for Inaba City and Yasoinaba Station, please go to the other side of the platform."'''),
    ("train", '''You quickly grab all your belongings and head for the doors. While walking through the terminal you can hear news reports coming from tv's around the station.'''),
    ("train", '''"The scandal involves the enka star Misuzu Hiiragi, preparing to tour overseas. Tarou Namatame, a council secretary in the Inaba region whom she married just last year, is now under suspicion of having an affair."'''),
    ("train", '''"What's more, his rumored mistress is the well-known TV announcer, Ms Mayumi Yamano! The question on everyone's mind is how this love triangle will eff..."'''),
    ("train", '''The sound from the tv's slowly cease as you make your way to your final train. As your train arrives you go to collect your belongings once more and walk out of the train onto Yasoinaba Station.'''),
]

def getPlayerDialogue():
    return [
        f"You are {Player.instance.first_name + " " + Player.instance.last_name}.",
        f" Due to your parents working abroad you will be moving to Inaba to stay with your uncle and his 6 year old daughter.",
        f" You will be living with them for the next year and attending the local high school."
    ]


openingCutsceneDialogue = [
    ("dojima", '''"Hey! Over here!"\n'''
               '''You see a man with greyish black hair down the steps of the station.'''),
    ("dojima", '''"Well, you're more handsome in person than in your photo."'''),
    ("dojima", '''"Welcome to Inaba. I'm Ryotaro Dojima. I'll be looking after you."\n'''
               '''You see a little girl hiding behind him.'''),
    ("dojima", '''"Let's see... I'm your mother's younger brother... And that about sums it up."'''),
    ("dojima", '''"Heh. You probably don't remember, but we've met. I've changed your diapers before, you know."'''),
    ("dojima", '''"This here's my daughter." The shy girl finally steps up in front of him.'''),
    ("dojima", '''"Come on, Nanako, introduce yourself to your cousin."'''),
    ("nanako", '''"......"'''),
    ("nanako", '''"...'lo."\n'''
               '''Nanako blushes red and hides behind Dojima again.'''),
    ("dojima", '''"*chuckles* What're you so shy for?"\n'''
               '''Nanako hits Dojima on the rear.'''),
    ("dojima", '''"Ow, hahaha."'''),
    ("nanako", '''"......"'''),
    ("dojima", '''"Well then... Let's get going."'''),
    ("dojima", '''"My car's over there."\n'''
               '''As you walk to the car an unfamiliar girl walks in front of you. You drop a note while walking past her.'''),
    ("unfriendlylookinggirl", '''"...Hey."'''),
    ("unfriendlylookinggirl", '''"You dropped this."\n'''
                    '''She kneels down and grabs the note. She hands it to you.'''),
    ("unfriendlylookinggirl", '''"......"\n'''
                    '''You put the note back in your pocket. The unfriendly looking girl walks away.'''),
    ("dojima", '''"What's wrong?"\n'''
                    '''Dojima yells from the car. You quickly hurry towards it.\n'''
                        '''> You got in the car and header for Dojima's house.'''),
    ("attendant", '''"Hi! Welcome to Moel!"\n'''
                        '''The gas station attendant sprints towards the car.'''),
    ("dojima", '''"Can you go to the bathroom by yourself?"'''),
    ("nanako", '''"Uh-huh."\n'''
                    '''Nanako and Dojima both step out of the car. Dojima talks to the gas station attendant while Nanako is looking around aimlessly for the bathroom. The gas station attendant seems to notice.'''),
    ("attendant", '''"It's in the back, to your left. You know which way's left? The side you don't hold your chopsticks in."'''),
    ("nanako", '''"I know... Geez..."\n'''
                    "Nanako says as she looks annoyed. You too now step out of the car to stretch your legs."),
    ("attendant", '''"Are you taking a trip?"'''),
    ("dojima", '''"No, we just went to pick him up. He just moved here from the big city."'''),
    ("attendant", '''"The city, huh...?"'''),
    ("dojima", '''"Fill up my car while you're at it. Regular's fine"'''),
    ("attendant", '''"Right away, Sir!\n"'''),
    ("dojima", '''"Good a time as any for a smoke..."\n'''
                        "Dojima steps away from the car to light his cigarette."),
    ("attendant", '''"Are you in high school?\n"'''
                    "You look confused at the gas station attendant."),
    ("attendant", '''"Does it surprise a city boy to see how little there is out here?"'''),
    ("attendant", '''"There's so little to do, I'm sure you'll get bored fast. You'll either be hanging out with your friends or doing part-time jobs."'''),
    ("attendant", '''"Speaking of which, we're actually looking for part time help right now.\n"'''
                    "The gas station attendant walks closer towards you."),
    ("attendant", '''"Give it some thought, why don't you? We don't mind if you're a student."\n'''
                        "You shake his hand. You continue talking until Nanako runs back from the bathroom."),
    ("attendant", '''"Oh, I should get back to work."\n'''
                        "> Nanako is looking at you."),
    ("player", '''"Argh..."\n'''
                "Suddenly you feel a sharp pain in your head. Nanako runs up to you."),
    ("nanako", '''"...Are you okay?"'''),
    ("nanako", '''"Did you get carsick?"'''),
    ("nanako", '''"You don't look to good..."\n'''
                    "> Could it be exhaustion from the long trip...? Now that she mentions it, you feel a little dizzy..."
                    "Dojima finishes up smoking and walks back to the car."),
    ("dojima", '''"Why not take a little walk, get some fresh air? Just let me know when you're ready to go."'''),
    ("dojima", '''"I'll wait here."'''),
    ("dojima", '''"The shopping district is near the house, so you should get to know where all the stores are."'''),
    ("help", '''"Examine the blue butterfly to save your progress."''')
]

centralsdsouthintro = [
    ("Lazy Student", '''"Damn... The next bus isn't going to come for a while. And if you miss one bus, you're pretty screwed."'''),
    ("Lazy Student", '''"If only I had a motorbike, I could go anywhere I wanted, anytime I wanted."'''),
    ("Lazy Student", '''"I wonder how much they cost... Maybe I'll be able to buy myself one."'''),
    ("unfriendlylookinggirl", '''"Hm...? Have we met before?"'''),
    ("unfriendlylookinggirl", '''"Just now...? Hmm, okay."'''),
    ("unfriendlylookinggirl", '''"......"'''),
    ("unfriendlylookinggirl", '''> The girl is thinking to herself...'''),
    ("unfriendlylookinggirl", '''"Hm... I see."'''),
    ("unfriendlylookinggirl", '''"The station...? Oh, that one time."'''),
    ("unfriendlylookinggirl", '''"...Nothing I just went."'''),
    ("unfriendlylookinggirl", '''"...I don't have anywhere to go."'''),
    ("unfriendlylookinggirl", '''"......"'''),
    ("nanako", '''"Uh..."'''),
    ("nanako", '''"...Are you okay?"'''),
    ("nanako", '''> Nanako seems worried about you...''')
]

dojimasresidenceintro = [

]