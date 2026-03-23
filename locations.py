location = {
    "velvet_room": {
    "name": "The Velvet Room",
    "description": "You find yourself in a strange blue limousine. There is a man with a long nose sitting infront of you, next to him there seems to be a woman on his left.",
    "actions": ["Talk to Igor", "Talk to Margaret"],
    "connected_to": ["TBC"]
    },
    "yasoinaba_station": {
        "name": "Yasoinaba Station",
        "description": "It's the only train station in Inaba.",
        "actions": ["Take the train"],
        "connected_to": ["central_sd_south"]
    },
    "central_sd_south": {
        "name": "Central Shopping District",
        "description": "The street where most of Inaba's family businesses are located, but the majority of the shops are closed, due to the overwhelming success of Junes.",
        "actions": ["Wait at bus stop", "Talk to gas station attendant", "Enter The Velvet Room"],
        "shops": ["Yomenaido Bookstore", "Daidara Metalworks", "Marukyu Tofu", "Shiroku Store"],
        "connected_to": ["central_sd_north", "dojima_residence"]
    },
    "dojima_residence": {
        "name": "Dojima Residence",
        "description": "Your temporary home in the town where Nanako Dojima and Ryotaro Dojima reside at with you.",
        "actions": ["Enter Dojima Residence"],
        "connected_to": ["central_sd_south"]
    }
}