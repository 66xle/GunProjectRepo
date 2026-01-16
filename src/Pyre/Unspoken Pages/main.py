from dfpyre import function, set_variable, Text, Item

PLAYER = "<gold>PLAYER <dark_gray>-<italic><gray>"
PLAYER_TALK = "<gold>PLAYER <dark_gray>-<gray>"
NPC = "<light_purple><obfuscated>Librarian</obfuscated> <dark_gray>-<white>"
UNKNOWN = "<light_purple><obfuscated>?????</obfuscated> <dark_gray>-<gray>"

Dialogue = {
"Room1.WakeUp": [
    "{PLAYER} *A cold pulse surges through your skull as you awaken*",
    "{PLAYER} Ngh... my head...",
    "{PLAYER} Where... where am I?",
    "{PLAYER} I can't seem to remember anything...",
    "{PLAYER} *You slowly rise to your feet.*"
],
"Room1.Stand": [
    "{PLAYER} What are these words that I can see?",
    "{PLAYER} They’re blurry, yet they whisper of something I’ve lost.",
    "{PLAYER} Pages. I… I think I need pages. But why?",
    "{PLAYER} *You decide to explore your surroundings*",
],


"Room1.PagePickup.Before": [
    "{PLAYER} This… must be one of the pages.",
    "{PLAYER} *You pick it up carefully, feeling a strange pull.*"

],
"Room1.PagePickup.After": [
   "{PLAYER} Ah—!",
   "{PLAYER} All these words… are flowing into me.",
   "{PLAYER} I’m remembering something... fragments of knowledge.",
   "{PLAYER} These pages… they’re pieces of my memories."
],


"Room1.BookPickup": [
    "{PLAYER} A missing book… maybe it belongs somewhere.",
],


"Room1.MissingBook.Before": [
    "{PLAYER} There seems to be a book missing from the shelf...",
    "{PLAYER} Maybe I can find it somewhere in this room?"
    ],
"Room1.MissingBook.After1": [
    "{PLAYER} The book seems to fit perfectly in the gap.",
    "{PLAYER} *You slide the book into place.*"
  ],
"Room1.MissingBook.After2": [
    "{PLAYER} A hidden passage… someone wanted me to find this.",
    "{PLAYER} But why?"
   ],

"Room2.First.NPC1": [
   "{NPC} Ah… there you are. Awake at last.",
   "{NPC} Welcome, fledgling. You stand within the Library Between Realms.",
   "{PLAYER} <reset><obfuscated>W-what… is this place?</obfuscated>",
   "{PLAYER} Why can’t I speak?",
   "{NPC} Your voice, your understanding, your past… all sealed for your trial.",
   "{NPC} Take this page. It will steady your mind… enough to help you.",
   "{PLAYER} *You accept the page. A familiar warmth returns to your mind.*"
   ],
"Room2.First.NPC2": [
    "{NPC} The library will only open itself to those who earn its trust.",
    "{NPC} Explore the books here. They hold memories you once knew.",
    "{NPC} When you are ready, ascend to the next level.",
    "{NPC} There, you will gather the books I require.",
    "{PLAYER} I need answers… but for now, I’ll follow their lead."
   ],


"Room2.BarrierWords": [
    '{PLAYER} "Behind the <red>veil<gray> lies truth unlit, waiting for the worthy to lift it."',
    '{PLAYER} "A true <red>ward<gray> protects not through strength, but through devotion."',
    '{PLAYER} "A <red>barrier<gray> is the mind made manifest—resolve shaped into form."',
    '{PLAYER} "To <red>prevent<gray> is to guide fate gently away from ruin."',
    '{PLAYER} "To <red>seal<gray> is to hold fast the truth until its time has come."',
    '{PLAYER} "Where chaos breaks, <red>bind<gray> it; where order frays, bind again."',
    '{PLAYER} "<red>Halt<gray>, until the chosen one speaks the word unspoken."',
    '{PLAYER} "When the moment comes, utter the <red>release<gray>, and all bindings shall kneel to you."'
   ],


"Room2.BarrierClear": [
    "{PLAYER} The path to the second floor is clear...",
    "{PLAYER} I can feel something returning. I should head upstairs."
   ],


"Room2.GetAllBooks": [
    "{PLAYER} That should be every book they asked for. Time to return."
    ],


"Room2.Second.NPC1": [
    "{PLAYER} *You hand over the books*"
    ],
"Room2.Second.NPC2": [
    "{NPC} Excellent work. You have done well to retrieve these.",
    "{NPC} So… it seems what <red><bold>THEY</bold><reset> predicted was true.",
    "{NPC} The ones who walked these halls before you. The last to withstand the Library’s trials.",
    "{NPC} <red><bold>THEY</bold><reset> foresaw a successor… someone who would reclaim what <red><bold>THEY</bold><reset> surrendered.",
    "{PLAYER} <bold><red>THEY</bold><gray>? Who are <bold><red>THEY</bold><gray>…?",
    "{NPC} Your path climbs ever higher. Go to the top of the library. The truth waits there.",
    "{NPC} Ah—before you go. Another page. Without it, the ascent would deny you.",
    "{PLAYER} *You take the page, feeling your strength return.*"
   ],
"Room2.Ending1": [
    "{PLAYER} The book in this lectern is missing pages...",
    "{PLAYER} *The pages you have gathered begins to glow with a faint light*"
   ],
"Room2.Ending2": [
    "{PLAYER} These pages must belong to this book.",
    "{PLAYER} *You place the missing pages into the book*",
   ],
"Room2.Ending3": [
    "{UNKNOWN} The Library has tested you and you have prevailed.",
    "{UNKNOWN} Lost memories have been reclaimed. Knowledge once forgotten is now yours to wield.",
    "{UNKNOWN} From this day forward, the stories within these walls are entrusted to you.",
    "{UNKNOWN} Protect them, learn from them, and guide those who come after.",
    "{UNKNOWN} The library is alive, but its voice can only be heard by those worthy.", 
    "{UNKNOWN} You have earned that voice. Welcome."
   ],
}


def format_texts(text_list):
    """Format a list of strings into Text objects with placeholders replaced"""
    return [
        Text(text.format(PLAYER=PLAYER, NPC=NPC, PLAYER_TALK=PLAYER_TALK, UNKNOWN=UNKNOWN))
        for text in text_list
    ]


def create_list(variable, text_list):
    """Create a list and set it to the global variable"""
    return set_variable(
        "CreateList",
        f"$g list-{variable}",
        *format_texts(text_list),
    )


template = function(
    "05A DialogSetup",
    Item("note_block"),
    codeblocks=[create_list(key, text_list) for key, text_list in Dialogue.items()],
)

template.build_and_send()
