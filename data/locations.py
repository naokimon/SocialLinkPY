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
    "central_sd_south_intro": {
        "name": "Central Shopping District",
        "description": "The street where most of Inaba's family businesses are located, but the majority of the shops are closed, due to the overwhelming success of Junes.",
        "actions": ["Wait at bus stop", "Walk into Yomenaido Bookstore", "Walk in Daidara Metalworks", "Walk into Marukyu Tofu", "Walk into Shiroku Store", "Talk to Lazy Student","Talk to Gas Station Attendant", "Talk to Unfriendly-looking girl", "Talk to Dojima", "Talk to Nanako"],
        "shops": {
            "yomenaido bookstore": {
                "description": "Yomenaido Bookstore is a store where you can purchase books and read them to increase certain stats."
            },
            "daidara metalworks": {
                "description": "Daidara Metalworks is an equipment shop that sells weapons, armors and accessories."
            },
            "marukyu tofu": {
                "description": "Marukyu Tofu is a tofu store."
            },
            "shiroku store": {
                "description": "Shiroku Store sells expendable items. The capsule machine outside was handmade by Shiroku's deceased husband. It costs ¥200 to play and only works on rainy days."
            }
        },
        "buildings": {
            "bus_stop": {
                "description": "> It's the bus stop. You have no reason to use the bus right now."
            }
        },
        "connected_to": ["central_sd_north", "dojima_residence"]
    },
    "dojima_residence": {
        "name": "Dojima Residence",
        "description": "Your temporary home in the town where Nanako Dojima and Ryotaro Dojima reside at with you.",
        "actions": ["Enter Dojima Residence"],
        "connected_to": ["central_sd_south"]
    }
}