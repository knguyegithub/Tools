import time
import random
import os

jokes = [
 {
   "ID": 1,
   "Joke": "What did the bartender say to the jumper cables? You better not try to start anything."
 },
 {
   "ID": 2,
   "Joke": "Don't you hate jokes about German sausage? They're the wurst!"
 },
 {
   "ID": 3,
   "Joke": "Two artists had an art contest... It ended in a draw"
 },
 {
   "ID": 4,
   "Joke": "Why did the chicken cross the playground? To get to the other slide."
 },
 {
   "ID": 5,
   "Joke": "What gun do you use to hunt a moose? A moosecut!"
 },
 {
   "ID": 6,
   "Joke": "If life gives you melons, you might have dyslexia."
 },
 {
   "ID": 7,
   "Joke": "Broken pencils... ...are pointless."
 },
 {
   "ID": 8,
   "Joke": "What did one snowman say to the other snowman? 'Do you smell carrots?'"
 },
 {
   "ID": 9,
   "Joke": "How many hipsters does it take to change a lightbulb? It's a really obscure number. You've probably never heard of it."
 },
 {
   "ID": 10,
   "Joke": "Where do sick boats go? The dock!"
 },
 {
   "ID": 11,
   "Joke": "I like my slaves like I like my coffee: Free."
 },
 {
   "ID": 12,
   "Joke": "My girlfriend told me she was leaving me because I keep pretending to be a Transformer... I said, No, wait! I can change!"
 },
 {
   "ID": 13,
   "Joke": "Old Chinese proverb: Man who not shower in 7 days makes one reek."
 },
 {
   "ID": 14,
   "Joke": "What did the owner of a brownie factory say when his factory caught fire? \"I'm getting the fudge outta here!\""
 },
 {
   "ID": 15,
   "Joke": "What form of radiation bakes you cookies? A gramma ray"
 },
 {
   "ID": 16,
   "Joke": "Bee jokes, courtesy of my niece (age 8). What did the bee use to dry off after swimming? A *bee*ch towel. What did the bee use to get out the tangles? A honeycomb."
 },
 {
   "ID": 17,
   "Joke": "What's the loudest economic system? CAPITALISM"
 },
 {
   "ID": 18,
   "Joke": "I went for a job interview today... The interviewer said to me, What would you say your greatest weakness is? I said, I think Id have to say my listening skills are my greatest strength."
 },
 {
   "ID": 19,
   "Joke": "Who was the knight that invented the round table? Sir Cumference. (via friend who got this from a street performance group in the England area of Epcot)"
 },
 {
   "ID": 20,
   "Joke": "What did the German air force eat for breakfast during WW2? Luftwaffles"
 },
 {
   "ID": 21,
   "Joke": "I the shell off a snail yesterday... you'd think it would move faster, but it was really kinda sluggish."
 },
 {
   "ID": 22,
   "Joke": "What did the number zero say to the number eight? \"Nice belt.\""
 },
 {
   "ID": 23,
   "Joke": "What's worse than a centipede with sore feet? A giraffe with a sore throat"
 },
 {
   "ID": 24,
   "Joke": "What's red and bad for your teeth? A brick."
 },
 {
   "ID": 25,
   "Joke": "Why did the Chicken cross the playground? To get to the other slide"
 },
 {
   "ID": 26,
   "Joke": "Did you hear about the French chef who committed suicide? He lost the huile d'olive"
 },
 {
   "ID": 27,
   "Joke": "Wanna hear a joke about unemployed people? Nevermind, they don't work."
 },
 {
   "ID": 28,
   "Joke": "Knock Knock Who's there Boo!! Boo who? Don't cry, it's only a joke"
 },
 {
   "ID": 29,
   "Joke": "How much did the skeleton charge for his excellent legal services? An arm and a leg."
 },
 {
   "ID": 30,
   "Joke": "Why do gorillas have such big nostrils? Cos they got big fingers."
 },
 {
   "ID": 31,
   "Joke": "What is the difference between a Siberian husky and an Alaskan husky? About 1500 miles."
 },
 {
   "ID": 32,
   "Joke": "What do vegan zombies eat? GRAAAIIINSSS!"
 },
 {
   "ID": 33,
   "Joke": "What's the difference between a Thai man and a Thai woman? Pls help."
 },
 {
   "ID": 34,
   "Joke": "What do you call a car that eats other cars? A carnivore."
 },
 {
   "ID": 35,
   "Joke": "Why did the golfer wear two pairs of pants In case he gets a hole in one"
 },
 {
   "ID": 36,
   "Joke": "An Olympic gymnast walked into a bar... She didnt get a medal..."
 },
 {
   "ID": 37,
   "Joke": "What does a mexican magician make for breakfast? Toast-tah-dahs!"
 },
 {
   "ID": 38,
   "Joke": "Why don't Bond villains feel cold in the winter? Because they dress in lairs."
 },
 {
   "ID": 39,
   "Joke": "What did the figurine say when the boot flew past her protective dome? \"That was a cloche call!\""
 },
 {
   "ID": 40,
   "Joke": "What was Carl Sagan's favorite drink? Cosmos."
 },
 {
   "ID": 41,
   "Joke": "What is the medical term for owning too many dogs? [A Roverdose](http://i.imgur.com/BtyF5ys.jpg)"
 },
 {
   "ID": 42,
   "Joke": "Knock knock... Who's there? I did up. I did up-who?"
 },
 {
   "ID": 43,
   "Joke": "I like my jokes they way I like my robots. Killer."
 },
 {
   "ID": 44,
   "Joke": "What type of school did Sherlock Holmes go to? Elementary :)"
 },
 {
   "ID": 45,
   "Joke": "My friend told an out of place joke about police searches. But I don't think it was warranted."
 },
 {
   "ID": 46,
   "Joke": "The Dalai Lama walks into a pizza store... and says, \"Can you make me one with everything?\""
 },
 {
   "ID": 47,
   "Joke": "Why did the vampire use mouthwash? Because he had bat breath"
 },
 {
   "ID": 48,
   "Joke": "What did the corn say when it was complemented? Aww, shucks!"
 },
 {
   "ID": 49,
   "Joke": "What did the green grape say to the purple grape? - \"Breathe, stupid!\""
 },
 {
   "ID": 50,
   "Joke": "Why did the Fall break off from all the other seasons? Because it wanted autumnomy"
 },
 {
   "ID": 51,
   "Joke": "If I ever fire someone who is a Taylor Swift fan I'll say \"I knew you were trouble when you clocked in.\""
 },
 {
   "ID": 52,
   "Joke": "What do you do if a cow is in the middle of the road you're driving on? steer clear"
 },
 {
   "ID": 53,
   "Joke": "What do you call a blind, legless buck? No eye-deer. EDIT: I totally messed this joke up. Please give me another chance with another joke?"
 },
 {
   "ID": 54,
   "Joke": "What do you get for the women who has everything? A divorce, then she'll only have half of everything."
 },
 {
   "ID": 55,
   "Joke": "There was a depressed sausage... he thought his life was THE WURST."
 },
 {
   "ID": 56,
   "Joke": "What's a dog's favorite mode of transportation? A waggin'"
 },
 {
   "ID": 57,
   "Joke": "Why did the sand dune blush? Because the sea weed"
 },
 {
   "ID": 58,
   "Joke": "What happened to the tyrannical peach? He got impeached!"
 },
 {
   "ID": 59,
   "Joke": "Why do elephants paint their toenails red? So they can hide in cherry trees. You ever seen an elephant in a cherry tree? *Then it's working*."
 },
 {
   "ID": 60,
   "Joke": "what did the mexican firecheif name his kids... Hose A and Hose B"
 },
 {
   "ID": 61,
   "Joke": "What did the German physicist use to drink his beer? Ein stein. - From Big Nate, as told by my kid."
 },
 {
   "ID": 62,
   "Joke": "What did earth say to the other planets? You guys have no life!"
 },
 {
   "ID": 63,
   "Joke": "One time we ran out of soap- -so we had to use hand sanitizer!!!"
 },
 {
   "ID": 64,
   "Joke": "Wanna hear a dirty joke? Two white stallions fell in the mud."
 },
 {
   "ID": 65,
   "Joke": "What did one frog say to the other frog? Time's fun when you're having flies."
 },
 {
   "ID": 66,
   "Joke": "Why did the boy take a pencil and paper to bed? He was told to draw the curtains before going to sleep."
 },
 {
   "ID": 67,
   "Joke": "Clean joke about sorority girls Why do sorority girls only travel in odd numbered groups? Because they *can't even*!"
 },
 {
   "ID": 68,
   "Joke": "What did the 8 say to the 0? Hey, fatty"
 },
 {
   "ID": 69,
   "Joke": "KNOCK KNOCK! WHO'S THERE! ***sombrero **** ^sombrero who,,,? *****SOMBRERO-VER THE RAINBOW****"
 },
 {
   "ID": 70,
   "Joke": "I'm reading a book about anti-gravity... ... It's impossible to put down"
 },
 {
   "ID": 71,
   "Joke": "What name is given to the most chickens ? pEGGy"
 },
 {
   "ID": 72,
   "Joke": "Why is Dr. Frankenstein never lonely? He's good at making friends."
 },
 {
   "ID": 73,
   "Joke": "What do you call a pig that does karate? *A pork chop.*"
 },
 {
   "ID": 74,
   "Joke": "What was the car doing in the dressing room? Changing attire."
 },
 {
   "ID": 75,
   "Joke": "What do you call a pile of dogs? A ruff terrain."
 },
 {
   "ID": 76,
   "Joke": "How do you prepare for a party in space? You Planet Thanks u/BostonCentrist"
 },
 {
   "ID": 77,
   "Joke": "What do you get when you cross an octopus with a cow? A stern rebuke from the Ethics Committee, and an immediate cessation of funding."
 },
 {
   "ID": 78,
   "Joke": "Why did the bicycle fall over? Because it was two-tired"
 },
 {
   "ID": 79,
   "Joke": "Two bookworms were having a dispute... ...across an open book until one bookworm moves closer to the other and says, \"well then, I'm glad we're on the same page.\""
 },
 {
   "ID": 80,
   "Joke": "Which kitchen appliance tells the best jokes? The beater - he cracks everybody up!"
 },
 {
   "ID": 81,
   "Joke": "Why did the jellyroll? He saw the apple turnover."
 },
 {
   "ID": 82,
   "Joke": "Why did the chicken? Q: Why did the chicken cross the road naked? A: Because chickens don't wear clothes."
 },
 {
   "ID": 83,
   "Joke": "What do you call Protestants who want to save a dime? Econoclasts."
 },
 {
   "ID": 84,
   "Joke": "What do dwarves use to cut their pizza? Little Caesars"
 },
 {
   "ID": 85,
   "Joke": "What did the fish say when it hit the wall? Dam."
 },
 {
   "ID": 86,
   "Joke": "What's that coffee drink with icecream? I used to know it, but... Affogato."
 },
 {
   "ID": 87,
   "Joke": "Where did Napoleon keep his armies? In his sleevies!"
 },
 {
   "ID": 88,
   "Joke": "makeup beauty Omg = oh my girl so cute next morning without makeup Omg = ohh My God omg/omg = life without wife"
 },
 {
   "ID": 89,
   "Joke": "Time flies like the wind. Fruit flies like... bananas!"
 },
 {
   "ID": 90,
   "Joke": "What did Vincent van Gogh call himself when he joined the Justice League? The Starry Knight"
 },
 {
   "ID": 91,
   "Joke": "Why did the boy take a ladder to school? He wanted to go to high school."
 },
 {
   "ID": 92,
   "Joke": "What's the best thing to put into a pie Your teeth."
 },
 {
   "ID": 93,
   "Joke": "What kind of house does a stoned loaf of bread live in? A high rise"
 },
 {
   "ID": 94,
   "Joke": "What do you get when you cross a firecracker and a duck? A firequacker."
 },
 {
   "ID": 95,
   "Joke": "What's a baker's biggest fear? Something going a-rye while they're raisin' bread."
 },
 {
   "ID": 96,
   "Joke": "What's the best way to get a hold of Vin Diesel? IM Groot. : D Source: https://www.youtube.com/watch?v=Lvlj1u9S258"
 },
 {
   "ID": 97,
   "Joke": "Why did everyone trust the marsupial? Everything he said was troo"
 },
 {
   "ID": 98,
   "Joke": "This dermatologist waits a month to diagnose a skin disorder... She's reluctant to make a rash decision."
 },
 {
   "ID": 99,
   "Joke": "Why are manhole covers round? Because manholes are round."
 },
 {
   "ID": 100,
   "Joke": "What did one casket say to the other? \"Is that you coffin?\""
 },
 {
   "ID": 101,
   "Joke": "How does a hamburger introduce his girlfriend? Meat patty! Thought of you guys!"
 },
 {
   "ID": 102,
   "Joke": "How does a mathematician get Tan? Sin/Cos"
 },
 {
   "ID": 103,
   "Joke": "What is a martian's favourite chocolate? A mars bar"
 },
 {
   "ID": 104,
   "Joke": "Where did Sally go after the explosion? Everywhere."
 },
 {
   "ID": 105,
   "Joke": "What did the cow say when it saw the farmer twice in one day? Deja Moo!"
 },
 {
   "ID": 106,
   "Joke": "Congratulation on the new baby, from your family... except from me because I don't really care."
 },
 {
   "ID": 107,
   "Joke": "What is agitated buy joyful? A washing machine"
 },
 {
   "ID": 108,
   "Joke": "What do you call a sleeping dinosaur? A dino-snore."
 },
 {
   "ID": 109,
   "Joke": "Breaking news! Energizer Bunny arrested... ...charged with battery."
 },
 {
   "ID": 110,
   "Joke": "It's an emergency! I need underwear jokes. My baby sister needs underwear jokes for some mysterious reason. I need your guys help!"
 },
 {
   "ID": 111,
   "Joke": "What did the butcher say when he handed his customer an empty pack of hotdogs on halloween? Happy halloweenie"
 },
 {
   "ID": 112,
   "Joke": "Can February March? No, but April May."
 },
 {
   "ID": 113,
   "Joke": "What's the internal temperature of a Taun-Taun? Lukewarm"
 },
 {
   "ID": 114,
   "Joke": "What's it called when a planet orbits its sun 8 times? An orbyte"
 },
 {
   "ID": 115,
   "Joke": "Why are there only two hundred and thirty nine beans in a bowl of bean soup? Because just one more and it would be two-farty"
 },
 {
   "ID": 116,
   "Joke": "What does a nosey pepper do? It gets jalapeno business."
 },
 {
   "ID": 117,
   "Joke": "Why don't blind people like to go skydiving? It scares their seeing-eye dog."
 },
 {
   "ID": 118,
   "Joke": "what does clark kent have for breakfast? alter-eggos"
 },
 {
   "ID": 119,
   "Joke": "I met Phil Spector's brother Crispin the other day. He's head of quality control at Lays."
 },
 {
   "ID": 120,
   "Joke": "Who is William Shatner's mythical nemesis? The Lepre-khaaaaannnnn!!!!!"
 },
 {
   "ID": 121,
   "Joke": "Two drums and a cymbal fall off a cliff... ba-dum tss"
 },
 {
   "ID": 122,
   "Joke": "Why does Mario hate Punchbug? Because he bruises like-a Peach!"
 },
 {
   "ID": 123,
   "Joke": "Where do pots go on vacation? JaPAN! From my 9 year old."
 },
 {
   "ID": 124,
   "Joke": "When German children play a game involving touching each other with bread... it's called gluten tag. I'll show myself out."
 },
 {
   "ID": 125,
   "Joke": "My laptop is so dumb. Every time it says \"Your password is incorrect\", I type in: \"incorrect\" and the silly thing still tells me the same thing."
 },
 {
   "ID": 126,
   "Joke": "Did you hear about the scarecrow who won the Nobel Prize? He was outstanding in his field. From: http://www.dadlaughs.com"
 },
 {
   "ID": 127,
   "Joke": "A man was caught stealing in a supermarket today... ...while balanced on the shoulders of a couple of vampires. He was charged with shoplifting on two counts."
 },
 {
   "ID": 128,
   "Joke": "why didn't the bicycle cross the road? because it was two-tired."
 },
 {
   "ID": 129,
   "Joke": "Every morning I run around the block 5 times... ...Then I slide the block back under the bed and go back to sleep"
 },
 {
   "ID": 130,
   "Joke": "Says she: \"Say something soft and sweet\" Says he: \"Marshmallow.\""
 },
 {
   "ID": 131,
   "Joke": "Why do cicadas stay up all night chirping irregularly, unable to sleep? Their cicadan rhythm is off"
 },
 {
   "ID": 132,
   "Joke": "What do you call a monk that operates a door unlocking service? A monkey. (p.s. I have a wonderful, terrible love for bad jokes)"
 },
 {
   "ID": 133,
   "Joke": "What do you call people who pretend to be Irish on St. Patrick's Day? Counterfitz"
 },
 {
   "ID": 134,
   "Joke": "What did the 0 say to the 8? Nice belt."
 },
 {
   "ID": 135,
   "Joke": "I love when I have dramatic realizations over my morning cereal... ... I call 'em \"breakfast epiphanies\""
 },
 {
   "ID": 136,
   "Joke": "Definitions Bigamist - An Italian fog. Myfunsalow - \"I am broke\" in Italian. Innuendo - Italian for suppository."
 },
 {
   "ID": 137,
   "Joke": "Have you heard what I think of windmills? Big Fan."
 },
 {
   "ID": 138,
   "Joke": "Max wondered why the ball was slowly growing larger... and then it hit him."
 },
 {
   "ID": 139,
   "Joke": "I saw a documentary on how they make jeans... It was riveting."
 },
 {
   "ID": 140,
   "Joke": "What goes \"Hahahahaha...*thud*\"? Someone laughing their head off"
 },
 {
   "ID": 141,
   "Joke": "Did you hear about the homemade poison ivy remedy? You can make it from scratch."
 },
 {
   "ID": 142,
   "Joke": "What did the apple say to the pear? [Man, go] away!"
 },
 {
   "ID": 143,
   "Joke": "When do elephants have eight feet? When there are two of them."
 },
 {
   "ID": 144,
   "Joke": "I bought a duckdoo yesterday! 'What's a duckdoo?' \"quack, quack\""
 },
 {
   "ID": 145,
   "Joke": "What do you call Batman skipping church? Christian Bail."
 },
 {
   "ID": 146,
   "Joke": "A man started to throw words beginning with 'th' at me I dodge this, then and there but I didn't see that coming - Tim Vine"
 },
 {
   "ID": 147,
   "Joke": "Why did the mobster buy a planner? So he could organize his crime"
 },
 {
   "ID": 148,
   "Joke": "James Bond went to get a haircut. The barber asked him if he wanted to dye his hair as well. Bond replied \"Dye another day.\""
 },
 {
   "ID": 149,
   "Joke": "I named my cat \"Curiosity\". He killed himself ... Nine times."
 },
 {
   "ID": 150,
   "Joke": "Why do they make Raisin Bran commercials? For raisin bran awareness."
 },
 {
   "ID": 151,
   "Joke": "What do you call a bald porcupine? Pointless!"
 },
 {
   "ID": 152,
   "Joke": "Where does the thumb meet its type? At the SPACE BAR! reddit is fun! I'm staring at the keyboard tryin' to think up a joke and voila'!"
 },
 {
   "ID": 153,
   "Joke": "What's Beethoven's favorite fruit? A ba-na-na-naaaaa"
 },
 {
   "ID": 154,
   "Joke": "I'm getting mighty fed up with these sheep-human hybrids! What is with ewe people!?"
 },
 {
   "ID": 155,
   "Joke": "What the plate say to the other plate? Dinners on me"
 },
 {
   "ID": 156,
   "Joke": "My finger became really swollen after I jammed it Friday. And thats how I found out Im allergic to jam."
 },
 {
   "ID": 157,
   "Joke": "Sports: So how's the shoestring game goin'? Right now, it's ***ALL TIED-UP!*** Oh my-oh-my! I couldn't find a cornylamejokes subreddit, so... ~Skip"
 },
 {
   "ID": 158,
   "Joke": "I wanted to put a pizza joke here ...but it was too saucy."
 },
 {
   "ID": 159,
   "Joke": "What do you call a cow that just gave birth? Decaffeinated"
 },
 {
   "ID": 160,
   "Joke": "Why did the bee go to the doctor? Because he had hives."
 },
 {
   "ID": 161,
   "Joke": "How many ears does Captain Picard have? A right ear. A left ear. And a final front ear."
 },
 {
   "ID": 162,
   "Joke": "What type of doctor prescribes Coke and 7-up for a living? A Poptometrist!"
 },
 {
   "ID": 163,
   "Joke": "What's grey? A melted penguin!"
 },
 {
   "ID": 164,
   "Joke": "Why was the healthy potato not allowed on the plane? He was on the \"No Fry\" list."
 },
 {
   "ID": 165,
   "Joke": "I saw an all frog production of Frozen yesterday... It was toad-aly cool!"
 },
 {
   "ID": 166,
   "Joke": "Just found this sub the other day and I've come to this realization... Currently, this subreddit seems to be in quite the pickle."
 },
 {
   "ID": 167,
   "Joke": "If you ever get cold, just stand in the corner of a room for a while. *They're normally around 90 degrees.*"
 },
 {
   "ID": 168,
   "Joke": "A farmer in (x-town) who rolled over a cart of horse manure... Is reported in \"stable condition.\""
 },
 {
   "ID": 169,
   "Joke": "What does a can of tuna say? Premium flaked tuna Best before dd/mm/yy"
 },
 {
   "ID": 170,
   "Joke": "How many magazines did the racquetball footwear company make before going out of business? Tennis shoes (Also: can anyone think of a more succinct buildup? It seems kinda unwieldy to me)"
 },
 {
   "ID": 171,
   "Joke": "Why was the actor detained by airport security? He said he was in town to shoot a pilot."
 },
 {
   "ID": 172,
   "Joke": "What did the llama say when asked to a picnic? Alpaca lunch!"
 },
 {
   "ID": 173,
   "Joke": "What do kids eat for breakfast? Yogoat!"
 },
 {
   "ID": 174,
   "Joke": "Did you hear about the casting for the new Batman movie? People have really Ben Affleckted by it."
 },
 {
   "ID": 175,
   "Joke": "What electronic device leaves behind a lot of broken glass? A PC, seeing how they typically run on Windows!"
 },
 {
   "ID": 176,
   "Joke": "Why did the orange move to veggieland? So he could live in peas and hominy."
 },
 {
   "ID": 177,
   "Joke": "A blind man walks into a bar. And a table. And a door. And a staircase. I don't think hes alright now."
 },
 {
   "ID": 178,
   "Joke": "What do you call beef that's been burned? A mis-steak."
 },
 {
   "ID": 179,
   "Joke": "How do cows get their gossip? They herd it through the bovine."
 },
 {
   "ID": 180,
   "Joke": "[ This one from the great /u/KingOfRibbles ] \"My sink was a bit dirty-\" \"-but all it needed was a little ...wiping!!!\""
 },
 {
   "ID": 181,
   "Joke": "Why doesn't the Sun go to college? Because he has a million of degrees."
 },
 {
   "ID": 182,
   "Joke": "What do you call a sheep with no legs? A cloud."
 },
 {
   "ID": 183,
   "Joke": "JKLMNOPQRST That's all that stands between U and I :)"
 },
 {
   "ID": 184,
   "Joke": "Original physics joke. I'm very proud. I was organizing my desk the other day and the Entropy Police gave me a ticket for disturbing the chaos."
 },
 {
   "ID": 185,
   "Joke": "There were two snowmen standing in a field, one says to the other... Can you smell Carrots?"
 },
 {
   "ID": 186,
   "Joke": "What kind of jackets do Audiophiles wear? FLAC jackets"
 },
 {
   "ID": 187,
   "Joke": "Shall I tell you the joke about the body snatchers? Best not, you might get carried away."
 },
 {
   "ID": 188,
   "Joke": "Gravity makes a terrible friend. It's always holding you down."
 },
 {
   "ID": 189,
   "Joke": "What do Catholics and guitar players have in common? Neither of them practice."
 },
 {
   "ID": 190,
   "Joke": "Do you know why the bike couldnt stand by itself? It was TWO TIRED!!!"
 },
 {
   "ID": 191,
   "Joke": "Just heard this on a PBS kids show... What did one wolf say to the other wolf? Howls it going?"
 },
 {
   "ID": 192,
   "Joke": "A man enters a store and asks for a color printer, the cashier asks \"What color?\""
 },
 {
   "ID": 193,
   "Joke": "An oldie but goldie! *How do you stop a charging bull?* ***Take away its credit card!*** wa-waa-waaaa! ~Skip"
 },
 {
   "ID": 194,
   "Joke": "Two antennas met on a roof . . . Two antennas met on a roof, they fell in love and got married, the ceremony was awful but the reception was brilliant."
 },
 {
   "ID": 195,
   "Joke": "Is it just me... ...or are circles pointless?"
 },
 {
   "ID": 196,
   "Joke": "Why do cows wear bells? Because their horns don't work."
 },
 {
   "ID": 197,
   "Joke": "What's brown and rhymes with Snoop? Dr. Dre"
 },
 {
   "ID": 198,
   "Joke": "What's the difference between a bird and a fly? A bird can fly, but a fly can't bird."
 },
 {
   "ID": 199,
   "Joke": "I've won the war! My pants fit! **Congratulations, have you lost weight?** _Even better... I've bought new pants!!!_"
 },
 {
   "ID": 200,
   "Joke": "Two drums and a cymbal fall off a cliff. Buh dum tss!"
 },
 {
   "ID": 201,
   "Joke": "What is Mozart doing right now? *Decomposing*"
 },
 {
   "ID": 202,
   "Joke": "Whatever you do, always give 100%... Unless of course, you're donating blood."
 },
 {
   "ID": 203,
   "Joke": "What did papa butter say to troublesome son butter? You had *butter* behave now, alright son? I sure know you don't want to get *whipped*!"
 },
 {
   "ID": 204,
   "Joke": "Why does the dog go to the gym? He wants to get ruff"
 },
 {
   "ID": 205,
   "Joke": "What kind of beer does a cow brew? Heifer-weizen."
 },
 {
   "ID": 206,
   "Joke": "How do you make a squid laugh? Ten tickles."
 },
 {
   "ID": 207,
   "Joke": "What cars do wolves drive? Auuuuuuuuuuuuudis!"
 },
 {
   "ID": 208,
   "Joke": "What do you call a cow that doesn't give milk? A Milk Dud."
 },
 {
   "ID": 209,
   "Joke": "What did the American call Karl Marx when a shrine was dedicated to him in Japan? A Kami."
 },
 {
   "ID": 210,
   "Joke": "Why are locomotive drivers so good at driving locomotives? Because they were trained."
 },
 {
   "ID": 211,
   "Joke": "What do you call a number that cant keep still? A roamin numeral."
 },
 {
   "ID": 212,
   "Joke": "Why did the redditor go to /r/zelda? To boost his link karma! (X-post from /r/Jokes)"
 },
 {
   "ID": 213,
   "Joke": "What did the Tin Man say when he got run over by a steamroller? Curses! Foil again!"
 },
 {
   "ID": 214,
   "Joke": "How can you tell that a straight pin is confused? Just look at it. It's headed in one direction and pointed in the other."
 },
 {
   "ID": 215,
   "Joke": "What is an astronaut's favorite meal? Launch"
 },
 {
   "ID": 216,
   "Joke": "What do you do to dead chemists? You barium."
 },
 {
   "ID": 217,
   "Joke": "Why did the tomato turned red? Because it saw the salad dressing"
 },
 {
   "ID": 218,
   "Joke": "Why are contortionists always angry? Their work usually has them pretty bent out of shape."
 },
 {
   "ID": 219,
   "Joke": "I never buy Velcro It's such a rip off."
 },
 {
   "ID": 220,
   "Joke": "How do you unlock a monastery door? With a monk key."
 },
 {
   "ID": 221,
   "Joke": "What is the ardent task of searching for a new wallpaper called? Running a Backgroud Check."
 },
 {
   "ID": 222,
   "Joke": "When does one play a corny game? You play it by ear."
 },
 {
   "ID": 223,
   "Joke": "The Great Yarn Race **Joe:** Did you hear about the great yarn race? **Jane:** No. Who won? **Joe:** Well, they had to weave their selves through the obstacles and in the end, it was a tie."
 },
 {
   "ID": 224,
   "Joke": "a red ship and a blue ship crashed on an island together the survivors were marooned."
 },
 {
   "ID": 225,
   "Joke": "Three tomatoes are walking down the street... A papa tomato, a mama tomato, and a baby tomato. The baby tomato starts falling behind so the papa tomato squishes him and says, Ketchup!"
 },
 {
   "ID": 226,
   "Joke": "What happens at night in Bangladesh? It gets Dhaka"
 },
 {
   "ID": 227,
   "Joke": "Why didn't the baby oyster share her little pearl? She was a little shellfish."
 },
 {
   "ID": 228,
   "Joke": "Why did Humpty Dumpty have a great fall? To make up for a lousy summer."
 },
 {
   "ID": 229,
   "Joke": "What kind of boats do smart people ride on? Scholar ships!"
 },
 {
   "ID": 230,
   "Joke": "How do you turn soup into gold? You add 24 carats!"
 },
 {
   "ID": 231,
   "Joke": "A photon checks into a hotel... The bellhop asks him if he has any luggage and the photon replies \"No. I'm travelling light.\""
 },
 {
   "ID": 232,
   "Joke": "I farted on an elevator, it was wrong on so many levels. From /r/PeterL"
 },
 {
   "ID": 233,
   "Joke": "What language do they speak in Holland? Hollandaise."
 },
 {
   "ID": 234,
   "Joke": "Last night, I had a dream that I was walking on a white sandy beach... At least that explains the footprints I found in the cat litter box this morning..."
 },
 {
   "ID": 235,
   "Joke": "Why should you always bring 2 pair of trousers when golfing? In case you get a hole in one."
 },
 {
   "ID": 236,
   "Joke": "Today I'm 45. But with the wind chill I feel like 32."
 },
 {
   "ID": 237,
   "Joke": "/r/pickle welcomes it's newest ally. It's always good to have clean jokes. I due urge the mods to add us to your sidebar, due to the fact that you are on ours."
 },
 {
   "ID": 238,
   "Joke": "Why are cats bad storytellers? Because they only have one *tale*"
 },
 {
   "ID": 239,
   "Joke": "Balloon's What's a balloon's favorite genre of music? Pop."
 },
 {
   "ID": 240,
   "Joke": "Why was the dolphin happy and the shark depressed? The sharks life lacked porpoise."
 },
 {
   "ID": 241,
   "Joke": "What Johnny Mercer song does December 21st remind you of? Autumn Leaves."
 },
 {
   "ID": 242,
   "Joke": "What's a comedian's favorite candy? Laffy Taffy."
 },
 {
   "ID": 243,
   "Joke": "There's a guy at the office today wearing full camo. At least I think so... I haven't seen him in a while."
 },
 {
   "ID": 244,
   "Joke": "Why do ghosts like to ride elevators? It lifts their spirits."
 },
 {
   "ID": 245,
   "Joke": "How do you call for a bath? With a Teletubbie."
 },
 {
   "ID": 246,
   "Joke": "Who was the chicken's favorite musician? BAAAACH BACH BACH BACH"
 },
 {
   "ID": 247,
   "Joke": "X-post from r/jokes: Mommy! I found a $10 bill today, but I threw it away, cus it was fake. \"Oh, how did you know it was fake?\" \"It had two zeroes instead of one.\""
 },
 {
   "ID": 248,
   "Joke": "How much does it cost a pirate to get his ear pierced? A buccaneer!"
 },
 {
   "ID": 249,
   "Joke": "What do you call the ghost of a chicken? A poultrygeist!"
 },
 {
   "ID": 250,
   "Joke": "What's invisible and smells like carrots? Bunny farts."
 },
 {
   "ID": 251,
   "Joke": "What did fish say when she hit the wall ? Dam(n) !!!"
 },
 {
   "ID": 252,
   "Joke": "Why are colds such bad robbers? Because they're so easy to catch!"
 },
 {
   "ID": 253,
   "Joke": "A man walks into an apple store and...... farts every one is really angry and there all shouting so he says it's not my fault you don't have windows"
 },
 {
   "ID": 254,
   "Joke": "Why are pirates so mean? I dont know, they just arrrrrrrrr!"
 },
 {
   "ID": 255,
   "Joke": "As I watched the dog chasing his tail, I thought, Dogs sure are easily amused!... ...then I realized I was watching the dog chasing his tail."
 },
 {
   "ID": 256,
   "Joke": "What happened to the ghost who couldn't scare? He had to join a support group since he couldn't handle his boos."
 },
 {
   "ID": 257,
   "Joke": "Did you hear about the butcher who backed into the meat grinder? He got a little behind in his work."
 },
 {
   "ID": 258,
   "Joke": "What do vegetarian zombies eat? Graaaaaaiiiins......"
 },
 {
   "ID": 259,
   "Joke": "Why did the lion spit out the clown? Because he tasted funny."
 },
 {
   "ID": 260,
   "Joke": "What was Marie Curie's fitness program on the airwaves called? Radio-Activity"
 },
 {
   "ID": 261,
   "Joke": "I went to the dermatologist about something on my neck- -and they said I just needed to scrub it!!!"
 },
 {
   "ID": 262,
   "Joke": "Why was the math book sad? It had a lot of problems"
 },
 {
   "ID": 263,
   "Joke": "What is the swamp-dwellers favorite form of extraterrestrial life? the Martians"
 },
 {
   "ID": 264,
   "Joke": "Why do good farmers only excel when they are actually farming? (X-post from /r/jokes) Because they are out standing in their field."
 },
 {
   "ID": 265,
   "Joke": "The cheesiest joke ever. \"I don't feel grate.\" -- Block of Cheese before it got shredded."
 },
 {
   "ID": 266,
   "Joke": "Every single morning I get hit by the same bike... It's a vicious cycle."
 },
 {
   "ID": 267,
   "Joke": "What do get when you cross 50 female pigs with 50 male deer? One hundred sows and bucks?"
 },
 {
   "ID": 268,
   "Joke": "You know youre getting old when Santa starts looking younger."
 },
 {
   "ID": 269,
   "Joke": "I hate when you're trying to be cheesy but everyone is laughtose intolerant."
 },
 {
   "ID": 270,
   "Joke": "What is irony? Irony is when something has the chemical symbol Fe."
 },
 {
   "ID": 271,
   "Joke": "What do you call a cow with no legs? Ground beef!"
 },
 {
   "ID": 272,
   "Joke": "was going to make a joke about science but I know for I wont get a reaction..."
 },
 {
   "ID": 273,
   "Joke": "The other day, I sent my girlfriend a huge pile of snow... I called her up and asked, ''Did you get my drift?''"
 },
 {
   "ID": 274,
   "Joke": "What do you call... What do you call an Italian romance novel model who's let himself go? Flabio."
 },
 {
   "ID": 275,
   "Joke": "How many tickles does it take to make an octopus laugh? Ten tickles."
 },
 {
   "ID": 276,
   "Joke": "How did the geologist develop a career as an expert in sinkholes? He fell into it."
 },
 {
   "ID": 277,
   "Joke": "A bear and a rabbit are pooping in the woods The bear asks the rabbit - \"do you have a problem with poop sticking to your fur?\" \"Nope\" So the bear wipes his butt with the rabbit."
 },
 {
   "ID": 278,
   "Joke": "Overheated some milk in a lab experiment today... ...and asked the teacher if it would affect the result. Her response? \"To a degree.\""
 },
 {
   "ID": 279,
   "Joke": "What's brown and sticky? A stick"
 },
 {
   "ID": 280,
   "Joke": "I was gonna make a joke on Reddit.. .. but I guess you've already Reddit somewhere."
 },
 {
   "ID": 281,
   "Joke": "Did you hear about the Antennas that got married? The wedding was lame, but the reception was great!"
 },
 {
   "ID": 282,
   "Joke": "What is the most religious unit in electrical engineering? Ohm."
 },
 {
   "ID": 283,
   "Joke": "I was walking in the desert and saw a redwood tree. I knew this must be a mirage, so I ran into it. To my dismay, the tree and I collided. I guess it must have been an obstacle illusion."
 },
 {
   "ID": 284,
   "Joke": "A Bagpiper, a Kangeroo, an Irish poet, and Mother Theresa walk into a bar . . . . . . . the barman, who was drying a glass, lifted his head and asked, \"Is this some kind of joke?\""
 },
 {
   "ID": 285,
   "Joke": "How many catholics does it take to change a lightbulb? CHANGE?!"
 },
 {
   "ID": 286,
   "Joke": "Why don't you want a turkey at your thanksgiving dinner? Because it'll gobble up everything."
 },
 {
   "ID": 287,
   "Joke": "What fruit do Romeo and Juliet eat? Cantelope"
 },
 {
   "ID": 288,
   "Joke": "Why was 9 afraid of 20? 28 29's"
 },
 {
   "ID": 289,
   "Joke": "What did one snowman say to the other? Do you smell carrots?"
 },
 {
   "ID": 290,
   "Joke": "What do you call a race run by baristas? A **decaf**alon"
 },
 {
   "ID": 291,
   "Joke": "What do you call a stegosaurus with carrots in its ears? Anything you want to - it can't here you!"
 },
 {
   "ID": 292,
   "Joke": "What bird can write underwater? A ball-point Penguin!"
 },
 {
   "ID": 293,
   "Joke": "What did the horse order at the bar? Chardaneiiiiiiggghhhhh"
 },
 {
   "ID": 294,
   "Joke": "What was Beethoven's favorite fruit? BA-NA-NA-NA!"
 },
 {
   "ID": 295,
   "Joke": "Why did the tissue get up and dance? It had a little boogy in it."
 },
 {
   "ID": 296,
   "Joke": "Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water."
 },
 {
   "ID": 297,
   "Joke": "What do sea monsters eat? Fish and ships."
 },
 {
   "ID": 298,
   "Joke": "What did Virginia get when she walked into the pet shop? (state joke) A New Hampshire"
 },
 {
   "ID": 299,
   "Joke": "The other day, I was looking through my socks, when I found one had a hole in it... \"darn it...\" I muttered."
 },
 {
   "ID": 300,
   "Joke": "What do you call the James Brown songs no one listens to? Defunct funk."
 },
 {
   "ID": 301,
   "Joke": "Did you see the guy at Walmart hiding from ugly people?"
 },
 {
   "ID": 302,
   "Joke": "You know what I hate about fashion designers? They are so clothes-minded."
 },
 {
   "ID": 303,
   "Joke": "What do you call a spider with no legs? A raisin"
 },
 {
   "ID": 304,
   "Joke": "A man walks into a bar... He says \"Ow\""
 },
 {
   "ID": 305,
   "Joke": "Which is the most silky planet? Satin!"
 },
 {
   "ID": 306,
   "Joke": "What does a train full of grain's whistle sound like? \"COUS, COUS!!!\""
 },
 {
   "ID": 307,
   "Joke": "What do you say to someone who is making a cardboard belt? \"That's a waist of paper!\""
 },
 {
   "ID": 308,
   "Joke": "Why didn't the skeleton go to the party? He had no *body* to go with"
 },
 {
   "ID": 309,
   "Joke": "What do you call a race ran by female horses? A mare-a-thon."
 },
 {
   "ID": 310,
   "Joke": "If April showers bring May flowers, what do May flowers bring? Pilgrims"
 },
 {
   "ID": 311,
   "Joke": "What do you call a Moroccan candy distributor? Fez dispenser."
 },
 {
   "ID": 312,
   "Joke": "Did you hear about the production delays at that company that makes scales using lengthy pipes? They had really long weights."
 },
 {
   "ID": 313,
   "Joke": "We don't allow faster-than-light neutrinos in here, says the bartender. A neutrino walks into a bar."
 },
 {
   "ID": 314,
   "Joke": "Almonds on the tree; Amonds off the tree cause to get them off the tree you hafta shake the \"L\" out of them!"
 },
 {
   "ID": 315,
   "Joke": "Did you hear the one about the constipated mathematician? He worked his problem out with a pencil."
 },
 {
   "ID": 316,
   "Joke": "How do crazy people go through the forest? They take the psycho-path."
 },
 {
   "ID": 317,
   "Joke": "What did the mama pig give her baby pig for its rash? ***OINKMENT!*** &gt; (This exchange that I found on /r/tumblr makes this joke even funnier to me: &gt; http://i.imgur.com/EzT0Bkd.jpg)"
 },
 {
   "ID": 318,
   "Joke": "What do you call a one-eyed dinosaur? Doyouthinkhesarus (Credit goes to whoever submitted that to the Coffee News)"
 },
 {
   "ID": 319,
   "Joke": "Why do bears hate shoes so much? They like to run around in their bear feet."
 },
 {
   "ID": 320,
   "Joke": "What do you call a cow with no legs? Ground beef."
 },
 {
   "ID": 321,
   "Joke": "How do you think the unthinkable? With an itheburg."
 },
 {
   "ID": 322,
   "Joke": "What do you call a bug that can't talk? A hoarse fly."
 },
 {
   "ID": 323,
   "Joke": "Always put sunglasses on your tree. Then, you'll get the proper shade."
 },
 {
   "ID": 324,
   "Joke": "Today I brought a computer back from the dead. I've decided that this makes me a techromancer."
 },
 {
   "ID": 325,
   "Joke": "What is tuba plus tuba? Fourba!"
 },
 {
   "ID": 326,
   "Joke": "Two dogs are going on a walk down the street They walk past a few parking meters and one dog says to the other, \"Hey, check it out! Pay toilets!\""
 },
 {
   "ID": 327,
   "Joke": "Why couldn't Elsa hold on to a balloon? She would always let it go."
 },
 {
   "ID": 328,
   "Joke": "How can you tell if a hamburger was grilled in space? It's a little meteor."
 },
 {
   "ID": 329,
   "Joke": "What did the amazed Kazakhstani say? That's Astana-shing"
 },
 {
   "ID": 330,
   "Joke": "Why don't blind people skydive? Because it scares their dogs too much!"
 },
 {
   "ID": 331,
   "Joke": "When is a door not a door? When it's a jar"
 },
 {
   "ID": 332,
   "Joke": "What's Medusa's favorite kind of cheese? Gorgonzola."
 },
 {
   "ID": 333,
   "Joke": "Why Does Snoop Dogg need an umbrella? For drizzle, my nizzle. :D"
 },
 {
   "ID": 334,
   "Joke": "My dental hygienist retired after working 55 years... All she got was a lousy plaque..."
 },
 {
   "ID": 335,
   "Joke": "I've just made a meeting site for retired chemists It's called Carbon Dating"
 },
 {
   "ID": 336,
   "Joke": "What do you call a parade of rabbits hopping backwards? A receding hare-line."
 },
 {
   "ID": 337,
   "Joke": "Two wrongs don't make a right... but three lefts make a right. And two Wrights make a plane 6 lefts make a plane."
 },
 {
   "ID": 338,
   "Joke": "Why did the library book go to the doctor? It needed to be checked out; it had a bloated appendix."
 },
 {
   "ID": 339,
   "Joke": "A frog decided to trace his genealogy one day... He discovered he was a tad Polish."
 },
 {
   "ID": 340,
   "Joke": "Two artists had an art contest... It ended in a draw"
 },
 {
   "ID": 341,
   "Joke": "What did the fish say before he hit the wall? Oh, Dam."
 },
 {
   "ID": 342,
   "Joke": "What's the smartest dinosaur? Thesaurus Rex! omg, I crack myself up! ~Skip"
 },
 {
   "ID": 343,
   "Joke": "I like camping but... it's so in tents"
 },
 {
   "ID": 344,
   "Joke": "If the house is in the kitchen, and Diana's in the kitchen, what's in Diana? A state (Indiana)"
 },
 {
   "ID": 345,
   "Joke": "A sentence and a phrase is arguing, what did the sentence say? I know where you're coming from this phrase, but I can't see your point."
 },
 {
   "ID": 346,
   "Joke": "What's brown and sounds like a bell? Dung."
 },
 {
   "ID": 347,
   "Joke": "What's a balloon's favorite genre of music? Pop."
 },
 {
   "ID": 348,
   "Joke": "Did you hear about what happened with the elk? It was really amoosing."
 },
 {
   "ID": 349,
   "Joke": "I got hit hard in the head with a can of 7up today... I'm alright though, it was a soft drink."
 },
 {
   "ID": 350,
   "Joke": "What's so great about living in Switzerland? Well, the flag is a big plus."
 },
 {
   "ID": 351,
   "Joke": "Why did the girl quit her job at the donut factory? She was fed up with the hole business."
 },
 {
   "ID": 352,
   "Joke": "What colour T-shirt would win a race? Red, because it runs the most."
 },
 {
   "ID": 353,
   "Joke": "Why was the Egyptian kid confused? Because his daddy was a mummy"
 },
 {
   "ID": 354,
   "Joke": "After watching a strongman competition... it amazed me to see how much the human body can lift without pooing itself."
 },
 {
   "ID": 355,
   "Joke": "What did the O say to the 8? Nice belt."
 },
 {
   "ID": 356,
   "Joke": "Why was the burrito embarrassed? It saw the salad dressing."
 },
 {
   "ID": 357,
   "Joke": "How many tickles does it take to make an octopus laugh? Ten tickles"
 },
 {
   "ID": 358,
   "Joke": "What do you call a bunch of Asian bears roaring? Panda-monium."
 },
 {
   "ID": 359,
   "Joke": "What does a rock do all day? Nothing. (this joke was made by daughter when she was 5)"
 },
 {
   "ID": 360,
   "Joke": "The joke of 2016 Trump"
 },
 {
   "ID": 361,
   "Joke": "How does Han Solo like to get around Endor? Ewoks"
 },
 {
   "ID": 362,
   "Joke": "I don't have the faintest idea why I passed out Just a short pun"
 },
 {
   "ID": 363,
   "Joke": "What do you call a vegetarian? A hopeless romaine-tic"
 },
 {
   "ID": 364,
   "Joke": "I want to die peacefully in my sleep, like my grandfather... Unlike the passengers in his car who were screaming and yelling! http://www.thedailyenglishshow.com/friday-joke/98-how-to-die/"
 },
 {
   "ID": 365,
   "Joke": "What do you call a chicken crossed with a cow? Cock-a-doodle-moo!"
 },
 {
   "ID": 366,
   "Joke": "Kind of a kid joke What kind of cereal do zombies like? Kellog's All Brain"
 },
 {
   "ID": 367,
   "Joke": "What did the farmer say when he lost his tractor? Where's my tractor?"
 },
 {
   "ID": 368,
   "Joke": "What do you call a blind deer? No-eye deer. What do you call a blind deer with no legs? *Still* no-eye deer."
 },
 {
   "ID": 369,
   "Joke": "Why are proteins so cranky? Because they're made of a mean ol' acids."
 },
 {
   "ID": 370,
   "Joke": "What do you call a pachyderm that doesn't matter? Irrelephant."
 },
 {
   "ID": 371,
   "Joke": "What are caterpillars afraid of? DOGerpillars!"
 },
 {
   "ID": 372,
   "Joke": "Why should you never invite a boxer to a party? He always throws the punch."
 },
 {
   "ID": 373,
   "Joke": "How much does it cost for a pirate to get his ear pierced? A buccaneer."
 },
 {
   "ID": 374,
   "Joke": "I was addicted to the hokey pokey but I turned myself around."
 },
 {
   "ID": 375,
   "Joke": "Why didn't the bicycle cross the road? ...he was two-tired..."
 },
 {
   "ID": 376,
   "Joke": "Why did the Russians use peanuts for torture in the Cold War? Because in Soviet Russia, Nut Cracks You!"
 },
 {
   "ID": 377,
   "Joke": "How do trees get online? They just log in..."
 },
 {
   "ID": 378,
   "Joke": "Apparently vegetables can hear when they're being eaten. So I always drown mine in salad dressing first. Because it's the Romaine thing to do."
 },
 {
   "ID": 379,
   "Joke": "Why were Wrigley, Doublemint, and Orbit watching CNN? To find out the latest on gum control legislation."
 },
 {
   "ID": 380,
   "Joke": "I wanna make a joke about sodium. But Na."
 },
 {
   "ID": 381,
   "Joke": "Why couldn't the melons be together? Everyone knows melons cantaloupe."
 },
 {
   "ID": 382,
   "Joke": "Why couldn't the alligator satisfy his lover? He had a reptile dysfunction."
 },
 {
   "ID": 383,
   "Joke": "What's a blind person's favorite fast food joint? Taco Braille"
 },
 {
   "ID": 384,
   "Joke": "The preacher today used Star Wars as a sermon illustration. I felt it was a little forced."
 },
 {
   "ID": 385,
   "Joke": "What did the grape say when it got stepped on? Nothing, it just gave a little wine"
 },
 {
   "ID": 386,
   "Joke": "Why are giraffes' necks so long? Because their heads are so far away from their bodies."
 },
 {
   "ID": 387,
   "Joke": "what's orange and sounds like a parrot? a carrot."
 },
 {
   "ID": 388,
   "Joke": "Why was the panda crying? He had a bambooboo. Aonther one from my 9 year old."
 },
 {
   "ID": 389,
   "Joke": "Why does Thor have insomnia? He's up all night to get Loki."
 },
 {
   "ID": 390,
   "Joke": "Did you hear the one about the three eggs? Too Bad."
 },
 {
   "ID": 391,
   "Joke": "/r/askreddit thread \"What's the best clean joke you know\" with thousands of replies http://www.reddit.com/r/AskReddit/comments/zrotp/whats_the_best_clean_joke_you_know/"
 },
 {
   "ID": 392,
   "Joke": "Chemistry Student I'm a science teacher and once I asked one of my lazy students if he knew the chemical symbol for sodium. He replied, 'Na, I don't'. Lucky sod, he's only ever right periodically."
 },
 {
   "ID": 393,
   "Joke": "What do you call a smart pig? Swinestein."
 },
 {
   "ID": 394,
   "Joke": "So, I have this new knock knock joke You start... (when you get it)"
 },
 {
   "ID": 395,
   "Joke": "Captain Ahab's crew were highly efficient sailors In fact, they were running like a whale oiled machine."
 },
 {
   "ID": 396,
   "Joke": "What kind of fish would be good to tune a piano? Oh, you guessed it right ... the tuna fish!"
 },
 {
   "ID": 397,
   "Joke": "Bulls from all over India sent a petition to SC asking it to classify them as 'Jallikatu Bulls'."
 },
 {
   "ID": 398,
   "Joke": "Did you hear about NASA finding bones on the moon? Yeah,the cow didn't make it."
 },
 {
   "ID": 399,
   "Joke": "Some people have trouble sleeping... ...but I can do it with my eyes closed..."
 },
 {
   "ID": 400,
   "Joke": "I think I want a job cleaning mirrors... ...it's just something I can see myself doing."
 },
 {
   "ID": 401,
   "Joke": "What did the eye say to the other eye? Something smells between us."
 },
 {
   "ID": 402,
   "Joke": "Did you hear about the kidnapping in Delaware? Don't worry, he eventually woke up."
 },
 {
   "ID": 403,
   "Joke": "What animal is best at hitting a baseball? A bat!"
 },
 {
   "ID": 404,
   "Joke": "Why did the octopus beat the shark in a fight? Because the octopus was well armed."
 },
 {
   "ID": 405,
   "Joke": "I'll always remember what my uncle said before he passed on up... \"Flying houses? Talking dogs? That movie looks dumb.\""
 },
 {
   "ID": 406,
   "Joke": "Whats Red and Smells Like Blue Paint? Red Paint"
 },
 {
   "ID": 407,
   "Joke": "Why did Little Miss Muffet have GPS on her Tuffet? To keep her from losing her whey."
 },
 {
   "ID": 408,
   "Joke": "What do you call an obese psychic that works at a bank? A four chin teller"
 },
 {
   "ID": 409,
   "Joke": "A man walked into a doctor's office . . . He said to the doctor: \"I've hurt my arm in several places.\" The doctor said: \"Well don't go there any more.\""
 },
 {
   "ID": 410,
   "Joke": "Why did the chicken lay an egg? (Quoted from daughter at age 3) To get food for her babies!"
 },
 {
   "ID": 411,
   "Joke": "Why do Gastroenterologists have such a passion for their job? Because they find the components of one's stomach very intestine."
 },
 {
   "ID": 412,
   "Joke": "Science joke The bartender says \"we don't serve your kind here\" He orders a drink A Tachyon walks into a bar Who wants to hear a Tachyon joke?"
 },
 {
   "ID": 413,
   "Joke": "How much does it cost a pirate to pierce his ears? A buccaneer!"
 },
 {
   "ID": 414,
   "Joke": "There's a TV channel where you can buy all the Pope's speeches It's called \"Papal View\"."
 },
 {
   "ID": 415,
   "Joke": "So today is Earth day on what grounds are we celebrating?"
 },
 {
   "ID": 416,
   "Joke": "What did one slice of bread say to the other at the end of a game of chess? \"It's stale, mate.\""
 },
 {
   "ID": 417,
   "Joke": "I heard it's a good night to see the Perseid meteor shower . . . . . . but I haven't heard how it got dirty."
 },
 {
   "ID": 418,
   "Joke": "Why shouldn't you have coffee while on the clock? Because that would be \"grounds\" for termination!"
 },
 {
   "ID": 419,
   "Joke": "What is green, has four legs and if it fell out of a tree and landed on you it would kill you? A pool table!"
 },
 {
   "ID": 420,
   "Joke": "What do you call a Frenchman in sandals? Philippe Philoppe."
 },
 {
   "ID": 421,
   "Joke": "What do you call a truthful piece of paper? Fax."
 },
 {
   "ID": 422,
   "Joke": "What type of melon would Romeo and Juliet have been? Cantaloupe."
 },
 {
   "ID": 423,
   "Joke": "What kind of turns do letters take? U-turns! *From my 9 year old son yesterday. Fixed typo."
 },
 {
   "ID": 424,
   "Joke": "What did one computer CPU say to the other after getting hit? Ow! That megahertz!"
 },
 {
   "ID": 425,
   "Joke": "Knock knock. Who's there? A cow. A cow who? Not a cow \"who\"! A cow moos. An owl says \"who\"."
 },
 {
   "ID": 426,
   "Joke": "Did you take a shower today? Why, is one missing?"
 },
 {
   "ID": 427,
   "Joke": "What did the Hungarian say to the annoying kid? \"You're nothing budapest!\""
 },
 {
   "ID": 428,
   "Joke": "I was thinking of ways to become transgender... So I figured I'd fly to Paris. Because then I'd be abroad."
 },
 {
   "ID": 429,
   "Joke": "How does the Mummy plan to destroy Superman? He's gonna lure him in to the crypt tonight."
 },
 {
   "ID": 430,
   "Joke": "What do you call a cow with one leg? Steak."
 },
 {
   "ID": 431,
   "Joke": "What concert tickets should cost $0.45? 50 cent feat. Nickelback :P"
 },
 {
   "ID": 432,
   "Joke": "A woman files for divorce from her husband... citing that he makes too many Star Wars puns. When asked if this is true the husband says, \"Divorce is strong with this one.\""
 },
 {
   "ID": 433,
   "Joke": "Why can't you run in a camp ground? You can only 'ran'; it's past tents."
 },
 {
   "ID": 434,
   "Joke": "What kind of soda do dogs drink? Barq's Root Beer."
 },
 {
   "ID": 435,
   "Joke": "I saw a middle aged man staring at a picture of his very first steps. With tears in his eyes, he told me he regrets ever replacing the steps with an elevator."
 },
 {
   "ID": 436,
   "Joke": "[OC] Why couldn't the dragon breathe fire? He had a cold"
 },
 {
   "ID": 437,
   "Joke": "What do fish smoke? Seaweed!"
 },
 {
   "ID": 438,
   "Joke": "Why is it a bad idea to get in a relationship with a statue? Because it's not going anywhere."
 },
 {
   "ID": 439,
   "Joke": "Where do you go to weigh a pie? Somewhere over the rainbow weigh a pie. (sounds like way up high)"
 },
 {
   "ID": 440,
   "Joke": "I forgot where I threw my boomerang. Oh wait.. It's coming back to me now."
 },
 {
   "ID": 441,
   "Joke": "What did the Estonian student say in language class? I'll never Finnish. *dodges tomato*"
 },
 {
   "ID": 442,
   "Joke": "What do you call the delivery boy at an Indian restaurant? Curry-er."
 },
 {
   "ID": 443,
   "Joke": "I had to clean out my spice rack and found everything was too old and had to be thrown out. What a waste of thyme."
 },
 {
   "ID": 444,
   "Joke": "Why were the breakfast potatoes running around hitting each other? HashTag!"
 },
 {
   "ID": 445,
   "Joke": "What's the difference between Bird flu and swine flu? For one you get tweetment and the other you get oinkment..."
 },
 {
   "ID": 446,
   "Joke": "Where do dogs go when they lose their tails? To a retail store."
 },
 {
   "ID": 447,
   "Joke": "I have the opposite of a photographic memory i have a potatographic memory."
 },
 {
   "ID": 448,
   "Joke": "Why did the vegetable band break up? They couldn't keep a beet."
 },
 {
   "ID": 449,
   "Joke": "Why did the Spy cross the road? 'Cause he wasn't really on your side."
 },
 {
   "ID": 450,
   "Joke": "What's orange and sounds like a parrot? A carrot"
 },
 {
   "ID": 451,
   "Joke": "I invented a time machine... ...next week."
 },
 {
   "ID": 452,
   "Joke": "Who was the only novelist with both direction and magnitude? Vector Hugo."
 },
 {
   "ID": 453,
   "Joke": "My plumber finally quit on me... He couldn't take any more of my crap. Sorry that this isn't a CLEAN joke. Heh"
 },
 {
   "ID": 454,
   "Joke": "I went to the store and asked for a one handed sailor... he said sorry, \"I'm a wholesaler.\""
 },
 {
   "ID": 455,
   "Joke": "what do you call an effeminate dwarf? A metro-gnome...."
 },
 {
   "ID": 456,
   "Joke": "I told my girlfriend she drew her eyebrows on too high she looked surprised."
 },
 {
   "ID": 457,
   "Joke": "What do you call a Jihadist that loves turkey? A Tryptophanatic."
 },
 {
   "ID": 458,
   "Joke": "What did the Tin Man say when he got run over by a steamroller? Curses! Foil again!"
 },
 {
   "ID": 459,
   "Joke": "Why there should be a February 30th So dentists can have a day to celebrate"
 },
 {
   "ID": 460,
   "Joke": "What do you call a big pile of kittens? A meowtain."
 },
 {
   "ID": 461,
   "Joke": "What do you call an arcade in eastern europe? czech-e-cheese"
 },
 {
   "ID": 462,
   "Joke": "My relationship is like Monopoly. She gives me too many Chances."
 },
 {
   "ID": 463,
   "Joke": "How do you call a deer with no eyes? No idea."
 },
 {
   "ID": 464,
   "Joke": "Why did the bicycle fall over? Because it was two tired."
 },
 {
   "ID": 465,
   "Joke": "What happened when the man couldn't afford the mortgage on his haunted house? ...it was repossessed!"
 },
 {
   "ID": 466,
   "Joke": "My uncle wanted to give all his sheep a sex change... But it entailed too many ramifications!"
 },
 {
   "ID": 467,
   "Joke": "How many dancers does it take to change a lightbulb? 5,6,7,8"
 },
 {
   "ID": 468,
   "Joke": "What was wrong with the wooden car? It wooden go."
 },
 {
   "ID": 469,
   "Joke": "What do caves have? Echosystems. From my 9 year-old."
 },
 {
   "ID": 470,
   "Joke": "One fifth of people... ...are just too tense!"
 },
 {
   "ID": 471,
   "Joke": "What do you call a fish with no eye? fsh"
 },
 {
   "ID": 472,
   "Joke": "Where do rabbits like to eat breakfast? IHOP!"
 },
 {
   "ID": 473,
   "Joke": "What did the wall ask the picture? (All together now!) ***\"How's it hangin'?\"*** ~Skip"
 },
 {
   "ID": 474,
   "Joke": "Me have great grammar... Me learnt everything I know from Sesame Street!"
 },
 {
   "ID": 475,
   "Joke": "If I don't eat all of my food, it goes to waste. If I do eat all of my food, it goes to *waist*."
 },
 {
   "ID": 476,
   "Joke": "What did the green light say to the red light? I love you, but I'm sick of yellow light always breaking us up."
 },
 {
   "ID": 477,
   "Joke": "What do you call the Hamburglar's accomplice? hamburglar helpler"
 },
 {
   "ID": 478,
   "Joke": "Did you hear about the fight in the candy store? Two suckers got licked"
 },
 {
   "ID": 479,
   "Joke": "Did I tell you I'm joining a gym in Gainesborough? Because I'm all about those gains bro"
 },
 {
   "ID": 480,
   "Joke": "I have a lot of jokes about the unemployed... ...but none of them work."
 },
 {
   "ID": 481,
   "Joke": "What is the last thing to go through a fly's mind when it hits a windshield? Its butt."
 },
 {
   "ID": 482,
   "Joke": "Which fairground ride is made of iron? The ferrous wheel"
 },
 {
   "ID": 483,
   "Joke": "What do you call a bulimic tree? Sycamore."
 },
 {
   "ID": 484,
   "Joke": "Why was the lobster upset? Because he found out his friends thought he was a little crabby!"
 },
 {
   "ID": 485,
   "Joke": "Did you hear about the ointment... Did you hear about the ointment that couldn't stop talking about politics? When confronted, he said he was just trying to be topical."
 },
 {
   "ID": 486,
   "Joke": "What's the first rule of bug ownership? Watch your step!"
 },
 {
   "ID": 487,
   "Joke": "Three drums and a cymbal rolled down a hill ba dum dum ching"
 },
 {
   "ID": 488,
   "Joke": "What is invisible and smells like carrots? Bunny Farts."
 },
 {
   "ID": 489,
   "Joke": "What did the number zero say to the number eight? Nice Belt"
 },
 {
   "ID": 490,
   "Joke": "When I grow old, I am sure I will look back at my life and say \"aaaah! my neck hurts\""
 },
 {
   "ID": 491,
   "Joke": "The pollen count  that's a difficult job! [Credit to Milton Jones]"
 },
 {
   "ID": 492,
   "Joke": "Why did the cowgirl name her pony ink? Because it kept running out of the pen!! My favorite joke when young :)."
 },
 {
   "ID": 493,
   "Joke": "Did you know yesterday was National Middle Child Day? Don't worry, no one else remembered either."
 },
 {
   "ID": 494,
   "Joke": "Have you heard about the 2 Spanish firemen? Jose and hose B"
 },
 {
   "ID": 495,
   "Joke": "There are two types of people in this world 1. Those who can extrapolate from incomplete data"
 },
 {
   "ID": 496,
   "Joke": "What did the flat iron say to the follicle? Now let me get this straight . . ."
 },
 {
   "ID": 497,
   "Joke": "6:30 is the best time on a clock... ...hands down."
 },
 {
   "ID": 498,
   "Joke": "I love graphs! I used to be obsessed with them... I've calmed down now though, you've gotta draw the line somewhere"
 },
 {
   "ID": 499,
   "Joke": "What kind of car did the German cowboy purchase? Audi *tips hat*"
 },
 {
   "ID": 500,
   "Joke": "Garbage men have Hefty contracts."
 },
 {
   "ID": 501,
   "Joke": "Dolphins don't do anything by accident.. Always on porpoise."
 },
 {
   "ID": 502,
   "Joke": "What do you call a fish with no eyes? A fsh"
 },
 {
   "ID": 503,
   "Joke": "What goes oh oh oh? Santa walking backwards."
 },
 {
   "ID": 504,
   "Joke": "Why does a milking stool have only three legs? Because the cow has the udder!"
 },
 {
   "ID": 505,
   "Joke": "A skeleton walks into a bar orders a beer and a mop."
 },
 {
   "ID": 506,
   "Joke": "First original joke! Why did the rapper visit the urologist? Because his flows were so sick."
 },
 {
   "ID": 507,
   "Joke": "What's gray and all around? Everything. I'm a dog."
 },
 {
   "ID": 508,
   "Joke": "~tips fedora at mosquito~ Mlaria"
 },
 {
   "ID": 509,
   "Joke": "Need help While scratching my ear with key few hours ago, audio on my brand new TV went off. Does anyone know good TV Service. Sh... I think my Laptop sound died too."
 },
 {
   "ID": 510,
   "Joke": "Who's the world's greatest underwater spy? Pond. James Pond."
 },
 {
   "ID": 511,
   "Joke": "Why was the belt locked up? Because it held a pair of pants."
 },
 {
   "ID": 512,
   "Joke": "How many apples grow on a tree? All of them."
 },
 {
   "ID": 513,
   "Joke": "Alrighty Kids always remember: you are what you eat So eat loads of sweets and pass on those vegetables"
 },
 {
   "ID": 514,
   "Joke": "How did the desk lamp store manager feel when thieves stole all his lightbulbs? He was delighted."
 },
 {
   "ID": 515,
   "Joke": "Did you hear about Scrooge's drinking problem? He had a dickens of a time with spirits."
 },
 {
   "ID": 516,
   "Joke": "Cogito Ergo Spud. I think, therefore I yam."
 },
 {
   "ID": 517,
   "Joke": "What's the best part about twenty two year old wheels of cheese? There are twenty of them."
 },
 {
   "ID": 518,
   "Joke": "My brother said he's incontinent. Yeah, he said he's wet his pants in nearly every nation in the world."
 },
 {
   "ID": 519,
   "Joke": "What do you call an elephant with a poor memory? A bold and innovative departure from the hackneyed stereotypes that all too often dominate the joke-telling industry."
 },
 {
   "ID": 520,
   "Joke": "What do you call a nose without a body? Nobody knows..."
 },
 {
   "ID": 521,
   "Joke": "How do you know ancient Egyptians loved books so much? Because they built their stuff with reads!"
 },
 {
   "ID": 522,
   "Joke": "Old game show bloopers...I miss this kind of humor today Found this video randomly http://www.youtube.com/watch?v=xv3gK2bmkAk&amp;feature=related"
 },
 {
   "ID": 523,
   "Joke": "Where do weirdos ride their bicycles? Psycho-paths. (as told by one of my coworkers)"
 },
 {
   "ID": 524,
   "Joke": "Why do sailors give their wives a bouqet of ropes instead of flowers?? It's a bouqet of forget-me-knots."
 },
 {
   "ID": 525,
   "Joke": "What's the difference between a hippo and a zippo? One is really heavy, and the other is a little lighter."
 },
 {
   "ID": 526,
   "Joke": "Where did the cat go when it lost it's tail? To the retail store!"
 },
 {
   "ID": 527,
   "Joke": "What do you call an Italian romance novel model who's let himself go? Flabio"
 },
 {
   "ID": 528,
   "Joke": "What do you call a lion in the circus. A Carny-vore"
 },
 {
   "ID": 529,
   "Joke": "Actually, there are but two types of people Those who can extrapolate from limited data ..."
 },
 {
   "ID": 530,
   "Joke": "Why'd the chicken cross the Mobius strip? To get to the same side."
 },
 {
   "ID": 531,
   "Joke": "X-post from r/jokes: \"Hey! The dog you sold me yesterday just fell over and died today!\" \"Huh, strange. He's never done that before.\""
 },
 {
   "ID": 532,
   "Joke": "What is the longest word in the English language? SMILES because there is a mile between the first and last letters!"
 },
 {
   "ID": 533,
   "Joke": "I had a joke about time travel but you guys didn't like it."
 },
 {
   "ID": 534,
   "Joke": "How does the farmer count up his cows? ...with a cowculator."
 },
 {
   "ID": 535,
   "Joke": "I would make a sparrow joke... But they don't fly very well."
 },
 {
   "ID": 536,
   "Joke": "Why did the golfer need to buy a new pair of socks? Because he got a hole in one!"
 },
 {
   "ID": 537,
   "Joke": "Why don't you want to hang out with a dude from Chicago? Because 'Illinois you!"
 },
 {
   "ID": 538,
   "Joke": "What did the fish say when it hit the wall? Dam"
 },
 {
   "ID": 539,
   "Joke": "What does Colonel Mustard's Mexican maid call him? *(Phonetically-ish)* Mis'ser Dijon."
 },
 {
   "ID": 540,
   "Joke": "Did you hear about the man who was accidentally buried alive? It was a grave mistake. Woohoo! I'm making these up!!"
 },
 {
   "ID": 541,
   "Joke": "What do you call a happy penguin? A pengrin!"
 },
 {
   "ID": 542,
   "Joke": "What did the green grape say to the purple grape? \"Breathe you idiot! Breathe!\""
 },
 {
   "ID": 543,
   "Joke": "Did you hear about the two monocles at the party? They made spectacles out of themselves."
 },
 {
   "ID": 544,
   "Joke": "What do you get when you drop a piano in a coal mine? A flat minor. Night... Don't forget to tip your waitress"
 },
 {
   "ID": 545,
   "Joke": "Wanna hear a dirty joke? A white horse fell in the mud."
 },
 {
   "ID": 546,
   "Joke": "A skeleton walks into a bar The bartender says, what will you have? Skeleton says, a beer... and a mop"
 },
 {
   "ID": 547,
   "Joke": "My daughter hit me with this one while preparing for dinner Why did the table love playing volleyball? Because it was always getting set! I think she gets it from her mother."
 },
 {
   "ID": 548,
   "Joke": "How did the aquarium win the battle? Giant Fish Tanks."
 },
 {
   "ID": 549,
   "Joke": "What do you call an alligator in a vest? An investigator"
 },
 {
   "ID": 550,
   "Joke": "What does a duck call a tractor? A quacktor"
 },
 {
   "ID": 551,
   "Joke": "What did daddy fish do when mommy fish got herself lost? ...He flounder"
 },
 {
   "ID": 552,
   "Joke": "There are three types of people in this world. Those who can count and those who can't."
 },
 {
   "ID": 553,
   "Joke": "Why did the chicken kill itself? To get to the other side."
 },
 {
   "ID": 554,
   "Joke": "Why can't you hear a pterodactyl use the restroom? Because the *p* is silent"
 },
 {
   "ID": 555,
   "Joke": "I thought about starting a business selling halos... ...but the cost of overheads was too high."
 },
 {
   "ID": 556,
   "Joke": "Where did the team get there uniforms? New Jersey"
 },
 {
   "ID": 557,
   "Joke": "Programmers tend to byte their food"
 },
 {
   "ID": 558,
   "Joke": "What do you call a group of security guards in front of a Samsung store? Guardians of the Galaxy."
 },
 {
   "ID": 559,
   "Joke": "I heard the best time travel joke tomorrow."
 },
 {
   "ID": 560,
   "Joke": "What do you call a woman on a cruise ship in Mexico using the diving board at the pool? A broad abroad on a board aboard."
 },
 {
   "ID": 561,
   "Joke": "What did the topic sentence say to the evidence? Why aren't you supporting me?"
 },
 {
   "ID": 562,
   "Joke": "What do you get when you mix Michael Jordan with Donald Trump? A Dunkin' Donut."
 },
 {
   "ID": 563,
   "Joke": "Two horses are standing in a field. \"I'm so hungry I could eat a horse\" Says the first. \"Moo!\" says the second"
 },
 {
   "ID": 564,
   "Joke": "What do you call a pile of kittens? A meowtin"
 },
 {
   "ID": 565,
   "Joke": "What happens to a frog's car when it breaks down? It gets toad away."
 },
 {
   "ID": 566,
   "Joke": "Two peanuts were walking down the street.... And one of them was assaulted"
 },
 {
   "ID": 567,
   "Joke": "If you walk into the bathroom an American and walk out an American, what are you in the bathroom? European."
 },
 {
   "ID": 568,
   "Joke": "An ion walked up to Lost and Found and reported that he had lost an electron. The clerk asked:are you sure? The ion replied :Yes, I am positive.VCN"
 },
 {
   "ID": 569,
   "Joke": "What do you say to your sister when she's crying? Are you having a crisis?"
 },
 {
   "ID": 570,
   "Joke": "What do you call a cross between a gorilla and a monkey? A cross."
 },
 {
   "ID": 571,
   "Joke": "What do you call it when Google Glass connects to the internet? Eye-fi."
 },
 {
   "ID": 572,
   "Joke": "Why did the Kurd bury his music collection? His tribesman said \"ISIL is approaching, and they're coming for Yazidis.\""
 },
 {
   "ID": 573,
   "Joke": "This mallard waddled into a bar... Should've ducked."
 },
 {
   "ID": 574,
   "Joke": "We now have TWO Wawa's by the interstate. The one on the east side of I4 is not so bad. But the other one, whoa. It's the Wawa West over there."
 },
 {
   "ID": 575,
   "Joke": "What' the difference between roast beef and pea soup? Anyone can roast beef, but not everyone can pea soup. (As told by my 8yo, who made me laugh with a joke for the first time. Proud dad moment.)"
 },
 {
   "ID": 576,
   "Joke": "the only one of its kind on this sub Want to hear a dirty joke? horse fell in the mud!"
 },
 {
   "ID": 577,
   "Joke": "What do you call it when Batman skips church? Christian Bale."
 },
 {
   "ID": 578,
   "Joke": "What do you call a social media platform designed for religious people who also have speech impediments? Faithbook"
 },
 {
   "ID": 579,
   "Joke": "I'm so sad because my friend is moving to Shanghai. More like Shang-bye."
 },
 {
   "ID": 580,
   "Joke": "What do you call a alligator in a vest? Investigator."
 },
 {
   "ID": 581,
   "Joke": "How to create a clean joke Step 1. Find a dirty joke Step 2. Clean it"
 },
 {
   "ID": 582,
   "Joke": "A skelleton goes to the bar and says \"Can I have a pint and a mop...\""
 },
 {
   "ID": 583,
   "Joke": "Did you hear about the fortune teller that... Had bad breath, calluses all over his body and couldn't win a fight? He was a Super Callused Fragile Mystic Hexed with halitosis."
 },
 {
   "ID": 584,
   "Joke": "Why was the scarecrow promoted? Because he was outstanding in his field!"
 },
 {
   "ID": 585,
   "Joke": "My friend gave me a balloon and told me not to pop it.. but I blew it!"
 },
 {
   "ID": 586,
   "Joke": "My old roommate's bathroom was so dirty- -I had to clean the soap before using it. (Seriously.)"
 },
 {
   "ID": 587,
   "Joke": "Why did the paper follow the pencil? Because it LED THE WAY! I'm on a roll here! this is fun! ~Skip"
 },
 {
   "ID": 588,
   "Joke": "Why does a chicken coupe only have two doors? If it had four it'd be a chicken sedan!"
 },
 {
   "ID": 589,
   "Joke": "What do you call a cow with only two legs? Lean Beef!"
 },
 {
   "ID": 590,
   "Joke": "Why was the school grey? Because it was a Greyed School. I woke up with this joke in my head this morning. I think my brain is trying to kill me with horrible puns."
 },
 {
   "ID": 591,
   "Joke": "Want to hear a clean Joke? Johnny took a bath with bubbles. Want to hear a dirty one? Bubbles is a man"
 },
 {
   "ID": 592,
   "Joke": "Why do sharks swim in salt water? Because pepper would make them sneeze!"
 },
 {
   "ID": 593,
   "Joke": "A Siri joke!: Two iPhones walk into a bar... ...Carrying a set of iPod shuffles. The bartender says: &gt; Let those iPods sing, man! He was an iSurfer on iPad mini."
 },
 {
   "ID": 594,
   "Joke": "I used to work at an orange juice factory... I ended up getting fired because I couldn't concentrate."
 },
 {
   "ID": 595,
   "Joke": "Just wrote a book on reverse psychology... Don't read it!"
 },
 {
   "ID": 596,
   "Joke": "Why did the melon get married in a church? Because he was in love with a cantaloupe."
 },
 {
   "ID": 597,
   "Joke": "Why do fish live in salt water? Because *pepper* makes them sneeze!"
 },
 {
   "ID": 598,
   "Joke": "Why was the apricot late to the party? He got stuck in a jam."
 },
 {
   "ID": 599,
   "Joke": "Passwords 123456 abcdef Password"
 },
 {
   "ID": 600,
   "Joke": "I knew I was old when I opened internet explorer."
 },
 {
   "ID": 601,
   "Joke": "What does a storm cloud have on beneath its clothes? Thunderwear!"
 },
 {
   "ID": 602,
   "Joke": "Where does the little king keep his little armies? Up his little sleevies."
 },
 {
   "ID": 603,
   "Joke": "\"What kind of house does cheese like to live in?\" \"A cottage\""
 },
 {
   "ID": 604,
   "Joke": "Why did the bullet stay home? Because it got fired!"
 },
 {
   "ID": 605,
   "Joke": "What do vegan zombies eat? GRAAAAINS"
 },
 {
   "ID": 606,
   "Joke": "What do you call an economics lecturer? Prof. it"
 },
 {
   "ID": 607,
   "Joke": "/r/cleanjokes hits 10K subscribers **/r/cleanjokes metrics:** Total Subscribers: 10,000 Subreddit Rank: 2,246 Milestones &amp; Subreddit Growth: http://redditmetrics.com/r/cleanjokes"
 },
 {
   "ID": 608,
   "Joke": "Why did the rope get put in timeout? Because he was very knotty."
 },
 {
   "ID": 609,
   "Joke": "What do mathematicians get if they stare at the roots of negative numbers for too long? Square eyes"
 },
 {
   "ID": 610,
   "Joke": "I'm going to stand outside... So if anyone asks, I am outstanding."
 },
 {
   "ID": 611,
   "Joke": "What is Forrest Gump's favorite pasta? Penne"
 },
 {
   "ID": 612,
   "Joke": "Where did the universe attend college? At the university."
 },
 {
   "ID": 613,
   "Joke": "How do you find Will Smith in the winter? You search for Fresh Prints."
 },
 {
   "ID": 614,
   "Joke": "Why did the squirrel cross the road on the telephone wire? To be on the safe side!"
 },
 {
   "ID": 615,
   "Joke": "What is Paula Deen's favorite insect? The Butterfly"
 },
 {
   "ID": 616,
   "Joke": "What do you call an antelope that wants a big wedding? Cantelope"
 },
 {
   "ID": 617,
   "Joke": "Why did no one ever consider Tony Stark (the Iron Man) a protagonist? Because he was always cited as the Anthony hero."
 },
 {
   "ID": 618,
   "Joke": "What's the difference between a firstborn prince and a baseball? A baseball is thrown to the air."
 },
 {
   "ID": 619,
   "Joke": "What do you call an Autobot who works in an overpriced makeup store at the mall ? Ulta Magnus!"
 },
 {
   "ID": 620,
   "Joke": "I can't stand Russian Dolls... They're always so full of themselves!"
 },
 {
   "ID": 621,
   "Joke": "What do you call a cow with no legs? Ground beef."
 },
 {
   "ID": 622,
   "Joke": "A teacher asked her students to use the word \"beans\" in a sentence... \"My father grows beans,\" said one girl. \"My mother cooks beans,\" said a boy. A third student spoke up, \"We are all human beans.\""
 },
 {
   "ID": 623,
   "Joke": "What did the mailman say when his Mail truck caught fire? That he needed to address the situation"
 },
 {
   "ID": 624,
   "Joke": "Math problem: I had 10 chocolate bars and ate 9. What do I have now? \"Oh, I do not know, DIABETES MAYBE!\""
 },
 {
   "ID": 625,
   "Joke": "Why don't cannibals like clowns? they taste funny!"
 },
 {
   "ID": 626,
   "Joke": "What's the difference between pea soup and roast beef? Anyone can roast beef..."
 },
 {
   "ID": 627,
   "Joke": "Did you know that protons have mass? &gt;Yes Well I didn't even know they were Catholic!"
 },
 {
   "ID": 628,
   "Joke": "How do you find Will Smith in the snow? Look for the fresh prints."
 },
 {
   "ID": 629,
   "Joke": "*THUD* \"What was that?\" \"My pants fell down.\" \"...Why so loud?\" \"I'm wearing them.\""
 },
 {
   "ID": 630,
   "Joke": "What do you call an Italian guy with a rubber toe? Roberto"
 },
 {
   "ID": 631,
   "Joke": "What does a ghost cow say? *wave arms around* MoooooOOOOOOoooooooo"
 },
 {
   "ID": 632,
   "Joke": "How much does wonton soup weigh? One ton, but I don't know anyone that'd wantonly order it."
 },
 {
   "ID": 633,
   "Joke": "Saitama tried to change his Facebook password to Goku but Facebook said it was too weak..."
 },
 {
   "ID": 634,
   "Joke": "Why did the fly fly? Because the spider spied her."
 },
 {
   "ID": 635,
   "Joke": "What do you call a boomerang that doesn't come back? pt 2 A boomer-WRONG!"
 },
 {
   "ID": 636,
   "Joke": "What do you call a Mexican with crazy intentions? A locomotive!"
 },
 {
   "ID": 637,
   "Joke": "How many nihilists does it take to screw in a lightbulb? #"
 },
 {
   "ID": 638,
   "Joke": "Where do snowmen dance? At the snowball!"
 },
 {
   "ID": 639,
   "Joke": "Why is a shooting star better than a hamburger? It's meteor."
 },
 {
   "ID": 640,
   "Joke": "Why did the vegetables hop into the boiling pot of water? They were part of a stewicide pact."
 },
 {
   "ID": 641,
   "Joke": "I find hanging around in coffee shops A great way to espresso yourself"
 },
 {
   "ID": 642,
   "Joke": "First post and an original How much does a Chinese elephant weigh? .................. Wonton"
 },
 {
   "ID": 643,
   "Joke": "Heard the one about the corduroy pillowcase? It's making headlines."
 },
 {
   "ID": 644,
   "Joke": "What do you get when you drop a piano down a mineshaft? A flat miner."
 },
 {
   "ID": 645,
   "Joke": "Why did the spider land on the keyboard? She wanted a new website."
 },
 {
   "ID": 646,
   "Joke": "Why did the woman buy new wine glasses? Because the ones she was using made everything blurry."
 },
 {
   "ID": 647,
   "Joke": "What did one dry erase marker say to the other? I'm bored! (As in board) Another one from my 9 year-old."
 },
 {
   "ID": 648,
   "Joke": "What did the tailpipe say to the muffler? I'm exhausted. What did the muffler say back? ^mmmmbfmbm"
 },
 {
   "ID": 649,
   "Joke": "What do you cal a bear with extreme mood swings? A bi-polar bear."
 },
 {
   "ID": 650,
   "Joke": "Why did the snail drink beer? To come out of its shell!"
 },
 {
   "ID": 651,
   "Joke": "If I bought a balloon for $0.99 ... How much should I sell it for when I adjust for inflation?"
 },
 {
   "ID": 652,
   "Joke": "I went out with anorexic twins last night... 2 birds, 1 stone"
 },
 {
   "ID": 653,
   "Joke": "Why should you never invest in bakeries? Because they have a high turnover rate."
 },
 {
   "ID": 654,
   "Joke": "a disability, a curse word and a radical interpretation of scripture walk into a bar nothing happened welcome to /r/cleanjokes"
 },
 {
   "ID": 655,
   "Joke": "What do you call a bear with no teeth? *A gummy bear.*"
 },
 {
   "ID": 656,
   "Joke": "Barely amusing Japanese joke Why are snakes so difficult to pick up in Japan? Because in Japan, snakes are hebi."
 },
 {
   "ID": 657,
   "Joke": "A priest, a minister, and a rabbit walk into a bar... ...and the bartender says, \"What is this, a joke?\""
 },
 {
   "ID": 658,
   "Joke": "No matter what anyone said, I was never going to take the stand. It's 1000 pages, for Pete's sake!"
 },
 {
   "ID": 659,
   "Joke": "Why couldn't the skeleton cross the street? Because he didn't have the guts!"
 },
 {
   "ID": 660,
   "Joke": "Why don't crabs give to charities? They are shellfish."
 },
 {
   "ID": 661,
   "Joke": "Why did the mortgage broker go out of business? ...because he lost interest."
 },
 {
   "ID": 662,
   "Joke": "My buddy the hacker took the quiz \"What Beatles song best describes your life.\" The answer he got: \"My Way\"."
 },
 {
   "ID": 663,
   "Joke": "I hear that in Star Wars VIII they're going to introduce Han's perpetually depressed younger brother. His name is Y Solo."
 },
 {
   "ID": 664,
   "Joke": "Did you hear about the skeleton who didn't go to prom? He had no body to go with."
 },
 {
   "ID": 665,
   "Joke": "What do you call a group of people standing in the arctic circle? A Finnish line."
 },
 {
   "ID": 666,
   "Joke": "Whats brown and rhymes with \"snoop\"? Dr. Dre"
 },
 {
   "ID": 667,
   "Joke": "I came into this subreddit expecting jokes about soap. I am mildly disappointed."
 },
 {
   "ID": 668,
   "Joke": "What game do you play with a wombat? Wom."
 },
 {
   "ID": 669,
   "Joke": "Wash the alligator clips with rubbing alcohol during flu season Protect yourself from catching a terminal illness."
 },
 {
   "ID": 670,
   "Joke": "What age were pigs discovered in? The Saus Age."
 },
 {
   "ID": 671,
   "Joke": "You've got to really be careful when ingesting shoes... cause they're usually laced"
 },
 {
   "ID": 672,
   "Joke": "Did you hear about the guy who invented a knife that can cut four loaves of bread at once? He's calling it the \"Four Loaf Cleaver.\""
 },
 {
   "ID": 673,
   "Joke": "Armadillo The world needs more armed dillos."
 },
 {
   "ID": 674,
   "Joke": "This is an X and Z conversation... Y are you in the middle?"
 },
 {
   "ID": 675,
   "Joke": "What did the fish say when it swam into the wall? Dam."
 },
 {
   "ID": 676,
   "Joke": "Heart attack When is the worst possible time to have a heart attack? When you are playing Charades."
 },
 {
   "ID": 677,
   "Joke": "The hole in the boat So two guys steal a boat and get drunk. Kane of them goes \"Hey, there is a hole in this boat\". The other says \"don't worry it's not ours\"."
 },
 {
   "ID": 678,
   "Joke": "What is a tuna's favorite city? Albacoreque."
 },
 {
   "ID": 679,
   "Joke": "What kind of pants does Super Mario wear? [Denim, denim, denim.](http://www.youtube.com/watch?v=c0SuIMUoShI)"
 },
 {
   "ID": 680,
   "Joke": "Why did the cop wake up his son? To stop a kid napping."
 },
 {
   "ID": 681,
   "Joke": "I hate people who talk about me behind my back... They discussed me."
 },
 {
   "ID": 682,
   "Joke": "What did the Buddhist say to the hotdog vendor? Make me one with everything."
 },
 {
   "ID": 683,
   "Joke": "I came up with a joke about my old cell phone Nevermind, it tends to get terrible reception"
 },
 {
   "ID": 684,
   "Joke": "What did music tell the pancakes? B flat."
 },
 {
   "ID": 685,
   "Joke": "What's Anakin Skywalker's favorite animal? Well, it was cats, originally, but then he was turned to the dog side."
 },
 {
   "ID": 686,
   "Joke": "Have you seen the movie - Constipated? No? Why? Cause it hasn't come out yet!"
 },
 {
   "ID": 687,
   "Joke": "Why did the people not like the restaurant on the moon? There was no atmosphere"
 },
 {
   "ID": 688,
   "Joke": "Why did the grocery delivery guy get fired? He drove people bananas!"
 },
 {
   "ID": 689,
   "Joke": "What does a thesaurus eat for breakfast? A synonym roll."
 },
 {
   "ID": 690,
   "Joke": "What does Captain Kirk wear to the fitness center? Jim shorts."
 },
 {
   "ID": 691,
   "Joke": "Did you hear about the lawyer for U2? He was Pro-Bono"
 },
 {
   "ID": 692,
   "Joke": "What do you call an old fruit-picker in Wisconsin? Cherry-atric"
 },
 {
   "ID": 693,
   "Joke": "I heard she accidentally spilled her chocolate milkshake on her white poodle- -knick knack paddy whack give the dog a... bath!!!"
 },
 {
   "ID": 694,
   "Joke": "An idea for a board game... BONOPOLY - Similar to Monopoly, but where the streets have no name."
 },
 {
   "ID": 695,
   "Joke": "Mary had a little lamb. She's not a vegan anymore."
 },
 {
   "ID": 696,
   "Joke": "What did 0 say to 8? Nice belt!"
 },
 {
   "ID": 697,
   "Joke": "Santa keeps his suits in the clauset."
 },
 {
   "ID": 698,
   "Joke": "Why couldn't the woman date a German man? Because she was Klaustrophobic!"
 },
 {
   "ID": 699,
   "Joke": "Knock! Knock! Knock! Knock! Whos there? Control Freak. Con Okay, now you say, Control Freak who?"
 },
 {
   "ID": 700,
   "Joke": "How did the townspeople react when the mayor presented them with a cost efficient, vegan protein source? They chia'd."
 },
 {
   "ID": 701,
   "Joke": "Did you hear that H.P. Lovecraft wrote a cookbook? It's called the Necronomnomnomicon."
 },
 {
   "ID": 702,
   "Joke": "Why should you leery of stairs? Because they are always up to something."
 },
 {
   "ID": 703,
   "Joke": "I'm calculating how much it would cost to install lights for a little league baseball field A ballpark estimate would be perfect"
 },
 {
   "ID": 704,
   "Joke": "What is the horror movie Quija rated? Quija-13"
 },
 {
   "ID": 705,
   "Joke": "So, a guy gave his friend 10 puns, hoping that one of them would make him laugh. Sadly, no pun in ten did."
 },
 {
   "ID": 706,
   "Joke": "What was the allergic 2\"X4\"'s terrifying hallucination? He sawdust."
 },
 {
   "ID": 707,
   "Joke": "What's orange and sounds like a Parrot? A Carrot"
 },
 {
   "ID": 708,
   "Joke": "What's brown and sticky? A stick."
 },
 {
   "ID": 709,
   "Joke": "What do you call a chef who's stingy with herbs? PARSLEYMONIOUS"
 },
 {
   "ID": 710,
   "Joke": "Which US state is the friendliest towards the Japanese? Ohio"
 },
 {
   "ID": 711,
   "Joke": "A classic: what do you call somebody with no body and no nose? Nobody knows."
 },
 {
   "ID": 712,
   "Joke": "what do you call a fake noodle? An impasta! :D"
 },
 {
   "ID": 713,
   "Joke": "What do Engineers use as birth control? Their Personality."
 },
 {
   "ID": 714,
   "Joke": "How much does a pirate earing cost? A buccaneer"
 },
 {
   "ID": 715,
   "Joke": "What do you call an alligator with a vest? An Investigator!"
 },
 {
   "ID": 716,
   "Joke": "Seven days without a joke makes one weak."
 },
 {
   "ID": 717,
   "Joke": "I'm a social person. I'm friends with 25 letters of the alphabet. I don't know why."
 },
 {
   "ID": 718,
   "Joke": "My grandpa started walking five miles a day when he was 60... Now hes 97 years old and we have no idea where he is..."
 },
 {
   "ID": 719,
   "Joke": "Where do toilets live? Porcel Lane."
 },
 {
   "ID": 720,
   "Joke": "Why did the Country Bear Jamboree bear blush? Because he was a bear a-singing. ..... I am at Disney with the kids this week..."
 },
 {
   "ID": 721,
   "Joke": "What's a martini's favorite garnish? Olive 'em!"
 },
 {
   "ID": 722,
   "Joke": "Why did the chess master order a Russian bride? He needed a Chech mate!"
 },
 {
   "ID": 723,
   "Joke": "What's the difference between a bag of chips and a duck with the flu? One's a quick snack and the other's a sick quack!"
 },
 {
   "ID": 724,
   "Joke": "Why didn't the cargo ship want to leave the bay? Because it was a freight!"
 },
 {
   "ID": 725,
   "Joke": "What do you call someone who really loves breakfast? A cereal killer."
 },
 {
   "ID": 726,
   "Joke": "What did Captain Ahab say when he harpooned a whale's tail fin on the first try? \"Well that was a fluke.\""
 },
 {
   "ID": 727,
   "Joke": "What do you call someone that steals shoes? A sneaker."
 },
 {
   "ID": 728,
   "Joke": "What song can never be played on #throwback Thursday? Friday by Rebecca Black"
 },
 {
   "ID": 729,
   "Joke": "What did the neutrino say to the planet? Just passing through"
 },
 {
   "ID": 730,
   "Joke": "What do you do with epileptic lettuce? You make a seizure salad!"
 },
 {
   "ID": 731,
   "Joke": "Did you hear they're republishing that Simple Mathematics study guide? It's the revised edition. (Revise Addition)"
 },
 {
   "ID": 732,
   "Joke": "Do you have a hole in your sock? \"No ...\" *(looks at sock)* . . How'd you get your foot in it?"
 },
 {
   "ID": 733,
   "Joke": "What does a baker wear on his feet? Loafers."
 },
 {
   "ID": 734,
   "Joke": "What cars do cows drive? Cattleacs"
 },
 {
   "ID": 735,
   "Joke": "I was at Redbox, but I didn't know what to watch. I consulted my groceries, and my pizza said, \"Keep Frozen.\""
 },
 {
   "ID": 736,
   "Joke": "What do you get when you cross a pig and a spider? Bacon and scrambled leggs."
 },
 {
   "ID": 737,
   "Joke": "Why didn't the fisherman go to Florida to fish for long jawed fish with rows of razor like teeth? He didn't have a Gar"
 },
 {
   "ID": 738,
   "Joke": "Why don't robots have any brothers anymore? Because they have trans-sisters."
 },
 {
   "ID": 739,
   "Joke": "Whats blue and smells like red paint? Blue paint"
 },
 {
   "ID": 740,
   "Joke": "Darth Vader told me he knows what i'm getting for Christmas He said he felt my presents..."
 },
 {
   "ID": 741,
   "Joke": "Why did the hippie drown? He was too *far out*!"
 },
 {
   "ID": 742,
   "Joke": "What's the difference between a Jew and a pizza? The pizza can have ham and cheese together."
 },
 {
   "ID": 743,
   "Joke": "Define \"Will\" Isn't it obvious? It's a dead giveaway!"
 },
 {
   "ID": 744,
   "Joke": "There's a wreath hanging on my door with hundred dollar bills attached. I call it an Aretha Franklin. c:"
 },
 {
   "ID": 745,
   "Joke": "How many roads must a man walk? 42."
 },
 {
   "ID": 746,
   "Joke": "What is a spectre's favorite theme park attraction? The Roller Ghoster"
 },
 {
   "ID": 747,
   "Joke": "What does a nosey pepper do? Gets jalapeno business!"
 },
 {
   "ID": 748,
   "Joke": "Did you know that in high school, Robert E. Lee was voted \"most likely to secede?\""
 },
 {
   "ID": 749,
   "Joke": "Did you hear the Offspring song about how to store mummies? \"You gotta keep 'em desiccated\""
 },
 {
   "ID": 750,
   "Joke": "This is 2 girls with 1 cup. [A.K.A. Friends At (a) Cafe Bar](http://www.gettyimages.com/detail/photo/friends-at-cafe-bar-high-res-stock-photography/156534295)"
 },
 {
   "ID": 751,
   "Joke": "Why were the treefrog's stories always so attention grabbing? Because he was absolutely ribbeting!"
 },
 {
   "ID": 752,
   "Joke": "What do you call a slice of bread from another country? An immigraint."
 },
 {
   "ID": 753,
   "Joke": "You know what they say about men that have big feet? #They wear big shoes! *Come on guys, this is /r/cleanjokes! Get your minds out of the gutter!*"
 },
 {
   "ID": 754,
   "Joke": "Q: What do you call a deer with no eyes? A: No eye deer (No idea) Q: What do you call a quadriplegic deer with no eyes? A: Still, no eye deer. (Still no idea)"
 },
 {
   "ID": 755,
   "Joke": "How many golfers does it take to change a light bulb? FOUR!"
 },
 {
   "ID": 756,
   "Joke": "What did the famous musician say the moment he was born? *I'LL BE BACH*"
 },
 {
   "ID": 757,
   "Joke": "What did the pebble say to the rock? I wish I was a little boulder!"
 },
 {
   "ID": 758,
   "Joke": "What goes up and down but does not move? Stairs"
 },
 {
   "ID": 759,
   "Joke": "In what town lives the mathematician who can only multiply by two? Dublin."
 },
 {
   "ID": 760,
   "Joke": "What did the buffalo say to his son when he left for college? Bison"
 },
 {
   "ID": 761,
   "Joke": "Why do Jamaican chickens make fun of all the other chickens? Because they're jerks."
 },
 {
   "ID": 762,
   "Joke": "Did y'all hear the one about the professional jump-roper? Never mind. *Skip it*."
 },
 {
   "ID": 763,
   "Joke": "The victim's body was found in the kitchen surrounded by eight empty boxes of cornflakes. Police suspect it was the work of a serial killer."
 },
 {
   "ID": 764,
   "Joke": "\"Stay strong!\" I said to my wi-fi signal."
 },
 {
   "ID": 765,
   "Joke": "Pick up line for a Shakespeare lover. How now brown chicken brown cow?"
 },
 {
   "ID": 766,
   "Joke": "Why did the snail draw an \"S\" on the side of his car? So that when he drove by people could say, \"Look at that escargot!\""
 },
 {
   "ID": 767,
   "Joke": "When do you know you are getting a good deal on a boat? When there's a sail on it."
 },
 {
   "ID": 768,
   "Joke": "What happens if socialism comes to the Sahara? Old Soviet-era joke told in Russia: What happens if socialism comes to the Sahara? Nothing at first, but then the sand shortages will start."
 },
 {
   "ID": 769,
   "Joke": "How do sailors finish a corny joke on a boat? Ba dum ship."
 },
 {
   "ID": 770,
   "Joke": "What's the best part of a baker's body? Their buns."
 },
 {
   "ID": 771,
   "Joke": "What do you call coffee made from coal? Tarbucks."
 },
 {
   "ID": 772,
   "Joke": "What did the three holes in the ground say? Well, well, well My grandpa's favorite joke. Took me five years to get it."
 },
 {
   "ID": 773,
   "Joke": "When you ask a girl, Wanna go to the gym with me? https://www.youtube.com/watch?v=rQegAi6d-MM"
 },
 {
   "ID": 774,
   "Joke": "I once ate a watch. It was time consuming, I didn't go back for seconds."
 },
 {
   "ID": 775,
   "Joke": "Why do zombies always kill at comedy clubs? Because their jokes are told post-humorously!"
 },
 {
   "ID": 776,
   "Joke": "What do you get when you cross a crocodile with a cartridge? A snapshot."
 },
 {
   "ID": 777,
   "Joke": "Where do you learn to make ice cream? Sundae School"
 },
 {
   "ID": 778,
   "Joke": "What is a rocket's favorite meal? Launch! Another one from my 9 year old."
 },
 {
   "ID": 779,
   "Joke": "What do lawyers wear to court? Lawsuits."
 },
 {
   "ID": 780,
   "Joke": "What do they call a monastery key that opens all doors? Monk key"
 },
 {
   "ID": 781,
   "Joke": "I fell in the mud. And took a shower right after!"
 },
 {
   "ID": 782,
   "Joke": "Fart tutor wanted, must have references"
 },
 {
   "ID": 783,
   "Joke": "I do my best when my manager puts a gun to my head."
 },
 {
   "ID": 784,
   "Joke": "What do you call someone who majors in geology and astronomy A rockstar"
 },
 {
   "ID": 785,
   "Joke": "I rang up a local builder and said, \"I want a skip outside my house.\" He said, \"I'm not stopping you.\" **Tim Vine**"
 },
 {
   "ID": 786,
   "Joke": "What kind of bird can write? A penguin."
 },
 {
   "ID": 787,
   "Joke": "What did the bunny say to the frog? [My name is Rabbit, not ribbit!!](https://www.youtube.com/watch?v=CYkDxsaHlkg)"
 },
 {
   "ID": 788,
   "Joke": "What do you get when you cross an elephant and a rhino? 'ell if I know wot to call it!"
 },
 {
   "ID": 789,
   "Joke": "Why did the chef invest in chicken and cow bones? He wanted to buy stock options."
 },
 {
   "ID": 790,
   "Joke": "What side of a leopard has the most spots? The outside"
 },
 {
   "ID": 791,
   "Joke": "How was the Roman Empire cut in two? With a pair of Caesars."
 },
 {
   "ID": 792,
   "Joke": "What's faster hot or cold? Hot! Because anyone can catch a cold! buh duh tsst"
 },
 {
   "ID": 793,
   "Joke": "What did one octopus say to the other octopus? Will you hold my hand hand hand hand hand hand hand hand?"
 },
 {
   "ID": 794,
   "Joke": "Why do fish always sing off key? Because you can't tune a fish. Say it outloud if you don't get it. I made this one up in first grade IIRC."
 },
 {
   "ID": 795,
   "Joke": "[PICKLE] Our first chance to help our new ally! http://www.reddit.com/r/pickle/comments/1a2xg8/next_attack_for_our_entire_army_march_12th_at_520/"
 },
 {
   "ID": 796,
   "Joke": "What type of cheese lives under your bed? Muenster."
 },
 {
   "ID": 797,
   "Joke": "What did the 0 say to the 8? ... Hey, nice belt.."
 },
 {
   "ID": 798,
   "Joke": "How does a duck pay for lipstick? She puts it on her bill"
 },
 {
   "ID": 799,
   "Joke": "So I work in a Steak House and all the people there are really lazy So I must say after working there: That it's rare to see a job well done"
 },
 {
   "ID": 800,
   "Joke": "What is H.P. Lovecraft's cook book called? The Necronomnomnomicon."
 },
 {
   "ID": 801,
   "Joke": "Why did the rabbit go to rehab? He was hopped up on easter eggs."
 },
 {
   "ID": 802,
   "Joke": "Knock Knock... 1.Knock knock. Whos there? Yoda lady. Yoda lady who? Good job yodeling! 2.Knock knock. Whos there? Well, not your parents, because your parents never knock!"
 },
 {
   "ID": 803,
   "Joke": "What do you call cheese that isn't yours? Nacho cheese!"
 },
 {
   "ID": 804,
   "Joke": "Reinventing Yourself http://dryinginside.blogspot.com/2012/10/reinventing-yourself-doesnt-always-work.html"
 },
 {
   "ID": 805,
   "Joke": "What do you call a Macho Man Randy Savage that does not belong to you? &gt;Nacho Man Randy Savage!!!!! this is my original content!!!!"
 },
 {
   "ID": 806,
   "Joke": "What does the horse call the pigs on his farm? Neigh-boars."
 },
 {
   "ID": 807,
   "Joke": "What's brown and sticky? A stick"
 },
 {
   "ID": 808,
   "Joke": "What is the world famous Chef Gordan's favorite football team? The Ramsays"
 },
 {
   "ID": 809,
   "Joke": "My shower had a bit of mildew- -but all it took was a little... scrubbing!!!"
 },
 {
   "ID": 810,
   "Joke": "Choose a major you love and you won't have to work for a day in your life Because that major probably has no jobs (not an original)"
 },
 {
   "ID": 811,
   "Joke": "When is booger not a booger? When it('s not)."
 },
 {
   "ID": 812,
   "Joke": "What's the longest word in the dictionary? \"Smiles\" because there is a mile between each S!"
 },
 {
   "ID": 813,
   "Joke": "At the end of the Age of Dinosaurs what happened to the good ones? They got veloci-raptured."
 },
 {
   "ID": 814,
   "Joke": "Which Pokemon got a cold? Pik-a-choo."
 },
 {
   "ID": 815,
   "Joke": "What do you call someone who's studied Old Norse literature and become an expert. Well edda-cated."
 },
 {
   "ID": 816,
   "Joke": "What instrument does God play? He plays the cello. As it says in scripture: \"Our God is a cellist God.\""
 },
 {
   "ID": 817,
   "Joke": "What do you call a fly with no wings? A walk."
 },
 {
   "ID": 818,
   "Joke": "Want to hear a joke about a crappy restaurant? Nevermind, I'm afraid it may be in poor taste."
 },
 {
   "ID": 819,
   "Joke": "Knock knock Who's there? Abby. Abby who. A bee has stolen my wallet. (I will show my self out)"
 },
 {
   "ID": 820,
   "Joke": "Which celebrity is great at creating probate documents? Will Smith"
 },
 {
   "ID": 821,
   "Joke": "Why couldn't Joe be friends with a double-amputee? Because he's lack-toes intolerant."
 },
 {
   "ID": 822,
   "Joke": "What do you say when you find two banana peels together? Answer: A pair of slipper"
 },
 {
   "ID": 823,
   "Joke": "Why cant college students take exams at the zoo? Too many cheetahs"
 },
 {
   "ID": 824,
   "Joke": "I saw this man and woman wrapped in a barcode... I asked, Are you two an item?"
 },
 {
   "ID": 825,
   "Joke": "A photon walks into a hotel. The bellhop asks if he needs help with his bags. The photon says, \"no, I'm travelling light. \""
 },
 {
   "ID": 826,
   "Joke": "If you're not buying kraft mac and cheese you might be buying an impasta."
 },
 {
   "ID": 827,
   "Joke": "How do you make a kleenex dance? You put a little Boogie in it!"
 },
 {
   "ID": 828,
   "Joke": "TV playback craziness [Through the eyes of Adrienne Hedger](https://www.facebook.com/HedgerHumor/photos/pb.630201143662377.-2207520000.1443863939./1179935295355623/?type=3&amp;theater). :)"
 },
 {
   "ID": 829,
   "Joke": "What do you call a very religious person who sleep walks? A Roman Catholic."
 },
 {
   "ID": 830,
   "Joke": "I don't have a Facebook or Twitter account... ...so I just go around announcing out loud what I'm doing at random times. I've got 3 followers so far, but I think 2 are cops."
 },
 {
   "ID": 831,
   "Joke": "Soap addiction I used to be addicted to soap. But I'm clean now!!"
 },
 {
   "ID": 832,
   "Joke": "Why is 6 afraid of 7? Because 7, 8, 9."
 },
 {
   "ID": 833,
   "Joke": "What Did Delaware? A brand New Jersey!"
 },
 {
   "ID": 834,
   "Joke": "Why don't you see penguins in Britain? Because they're afraid of Wales"
 },
 {
   "ID": 835,
   "Joke": "New Internet acronym: RALSHMICOMN Rolling Around Laughing So Hard Milk Is Coming Out My Nose"
 },
 {
   "ID": 836,
   "Joke": "How do you kill a circus? You stab it in the juggler."
 },
 {
   "ID": 837,
   "Joke": "More retailers should adopt the \"Leave A Penny / Take A Penny\" system. It is literally, common cents."
 },
 {
   "ID": 838,
   "Joke": "How much do pirates pay for earrings? about a buck an ear."
 },
 {
   "ID": 839,
   "Joke": "Why did the boy throw a clock out the window? He wanted to see time fly."
 },
 {
   "ID": 840,
   "Joke": "Which word is the longest in the English language? Smiles - because there is a mile between the first and last letters"
 },
 {
   "ID": 841,
   "Joke": "What do you call a person who farts in private? A private tutor"
 },
 {
   "ID": 842,
   "Joke": "Why did the raisin take the prune to the new year's ball? Because he couldn't find a date!"
 },
 {
   "ID": 843,
   "Joke": "Why did the chicken soup cross the road? Because it was down hill!"
 },
 {
   "ID": 844,
   "Joke": "What did one math book say to the other math book? We've got a lot of problems."
 },
 {
   "ID": 845,
   "Joke": "Two competing podiatrists opened offices next door to each other... They were arch enemies. Edit: Spelling"
 },
 {
   "ID": 846,
   "Joke": "What do you call fake German currency? Question marks"
 },
 {
   "ID": 847,
   "Joke": "What do you call a fat psychic? A four chin teller."
 },
 {
   "ID": 848,
   "Joke": "How does Harry Houdini tell people to steal stuff? Straight jack it."
 },
 {
   "ID": 849,
   "Joke": "Why can't you hear a pterodactyl urinate? Because of the silent P."
 },
 {
   "ID": 850,
   "Joke": "What do you call an Egyptian bone-setter? Cairo-practor."
 },
 {
   "ID": 851,
   "Joke": "My first job... My first job out of college was a \"diesel fitter\" at a pantyhose factory... As they came off the line, I would hold them up and say, \"Yep, deez'll fit her!\""
 },
 {
   "ID": 852,
   "Joke": "What did the closed can say to the half opened can? YOU'RE BEING UNCANNY!"
 },
 {
   "ID": 853,
   "Joke": "Whats the problem with tainted money? It taint yours and it taint mine :D (Puns for the win? :D)"
 },
 {
   "ID": 854,
   "Joke": "What do you call it when someone resuscitates a person who chokes on alcohol? La chaim-lich maneuver."
 },
 {
   "ID": 855,
   "Joke": "How many minimalists does it take to screw in a light bulb? 1"
 },
 {
   "ID": 856,
   "Joke": "What do you call a loaf baked in a zoo? Bread in captivity."
 },
 {
   "ID": 857,
   "Joke": "Where does a river keep it's money? At the bank."
 },
 {
   "ID": 858,
   "Joke": "What side of a turkey has the most feathers? The outside."
 },
 {
   "ID": 859,
   "Joke": "My teacher's nickname in school is Flush. He always has the same suit."
 },
 {
   "ID": 860,
   "Joke": "What kind of dish does LeBron like? anything with curry in it."
 },
 {
   "ID": 861,
   "Joke": "There are 10 types of people in the world. Those who understand binary code and those who do not."
 },
 {
   "ID": 862,
   "Joke": "What do lawyers wear to court? Law suits!"
 },
 {
   "ID": 863,
   "Joke": "Why are the nordic countries the best countries to live in? Their flags are big plusses."
 },
 {
   "ID": 864,
   "Joke": "When Captain Picard's sewing machine broke he brought it to the repairman and said... \"make it sew.\""
 },
 {
   "ID": 865,
   "Joke": "My brother... Likes driving black and white F1 race cars. They call him the F1 racist."
 },
 {
   "ID": 866,
   "Joke": "What is green, fuzzy, and will kill you if it falls out of a tree? A pool table. [Thanks, Wagon Train camper!]"
 },
 {
   "ID": 867,
   "Joke": "How do you make a tissue dance? You put a boogie in it! (Not sure of the spelling, heard it from someone)."
 },
 {
   "ID": 868,
   "Joke": "Who makes the sweetest video games? Masahiro Saccharide"
 },
 {
   "ID": 869,
   "Joke": "Someone dropped their Scrabble in the middle of the road... ...that's the word on the street anyway."
 },
 {
   "ID": 870,
   "Joke": "Harry Potter can't tell the difference between his cooking pot and his best friend. [X Post from r/Fantasy] They're both cauldron."
 },
 {
   "ID": 871,
   "Joke": "My dog chewed up my laptop... I guess he wanted a byte to eat! ^imagine ^this ^in ^zoidberg's ^voice"
 },
 {
   "ID": 872,
   "Joke": "Why did the chicken cross the playground? To get to the other slide"
 },
 {
   "ID": 873,
   "Joke": "Why don't cats play poker in the jungle... ...theres too many cheet-ahs"
 },
 {
   "ID": 874,
   "Joke": "What did Ernie say to Bert when he asked for ice-cream? Sure, Bert!"
 },
 {
   "ID": 875,
   "Joke": "Ask your doctor if left is right for you."
 },
 {
   "ID": 876,
   "Joke": "Why was the tank top more gangster than the tube top? The tube top was strapless."
 },
 {
   "ID": 877,
   "Joke": "This boy said he was going to hit me with the neck of a guitar.... I said, Is that a fret?"
 },
 {
   "ID": 878,
   "Joke": "Apple just released a brand new programming language, *Swift*. Job recruiters everywhere immediately started posting ads for Swift programmers with 5 years of experience."
 },
 {
   "ID": 879,
   "Joke": "Which way will it fall? If a rooster lays an egg on a pointed roof, which way will it land? Roosters don't lay eggs"
 },
 {
   "ID": 880,
   "Joke": "What do you call a cow with a twitch? Beef jerky"
 },
 {
   "ID": 881,
   "Joke": "I'm naming my TV remote Waldo... ...for obvious reasons."
 },
 {
   "ID": 882,
   "Joke": "A platypus went into a hotel owned by a duck.. ..A platypus went into a hotel owned by a duck. Platypus ate food. Duck billed platypus"
 },
 {
   "ID": 883,
   "Joke": "Have you heard about the Black Magic book for orphans? It's called the necro**mom**icon"
 },
 {
   "ID": 884,
   "Joke": "What do you call a black and white bird that can't win, nor fly. A peng-lose."
 },
 {
   "ID": 885,
   "Joke": "How do you catch a unique rabbit? *unique* up on it!"
 },
 {
   "ID": 886,
   "Joke": "what keeps the lions from leaving the savannah the ele-fence"
 },
 {
   "ID": 887,
   "Joke": "Will you tell you the story of the huge sad wall? I shouldn't, you'll never get over it."
 },
 {
   "ID": 888,
   "Joke": "Where do you buy Pikmin from? The Oli-Mart"
 },
 {
   "ID": 889,
   "Joke": "Where do literal dogs live? On the roof."
 },
 {
   "ID": 890,
   "Joke": "I just bought a Bonnie Tyler sat-nav. It keeps telling me to turn around, and every now and then it falls apart."
 },
 {
   "ID": 891,
   "Joke": "Why was the Headless Horseman depressed? He could never seem to get ahead in life."
 },
 {
   "ID": 892,
   "Joke": "everybody gets their 15 minutes of fame - so here's my first original joke! why is it impossible to surprise a snowman? .. he has ice in the back of his head"
 },
 {
   "ID": 893,
   "Joke": "What's the difference between me and a calendar? A calendar has dates. #foreveralone"
 },
 {
   "ID": 894,
   "Joke": "What time does Sean Connery arrive at Wimbledon? Tennish"
 },
 {
   "ID": 895,
   "Joke": "Knock-knock... \"Knock-knock\" \"Who's there?\" \"Control Freak - now you say 'Control Freak who?'\" :)"
 },
 {
   "ID": 896,
   "Joke": "What did the picture say to the Judge? I WAS FRAMED! I just now made that up. I feel good about this one! ~Skip"
 },
 {
   "ID": 897,
   "Joke": "Have you heard the one about the agnostic with dyslexia and insomnia? He tossed and turned all night wondering if there was a dog"
 },
 {
   "ID": 898,
   "Joke": "Why did Woodrow Wilson take a long time to turn around? Because he could only make 14 point turns."
 },
 {
   "ID": 899,
   "Joke": "totally original joke/first post: What do you get when you play a Frank Sinatra record at twice the speed? \"Shrank Sinatra\""
 },
 {
   "ID": 900,
   "Joke": "How did Hitler tie his shoelaces? In cute little knotsies!"
 },
 {
   "ID": 901,
   "Joke": "My first joke here and an original! Did you hear about the two lawyers who set up shop under the old oak tree? I heard it was a pretty shady business."
 },
 {
   "ID": 902,
   "Joke": "What do you call a discounted Zuckerberg? Marked down!"
 },
 {
   "ID": 903,
   "Joke": "What did the floor say to the desk? I can see your drawers!"
 },
 {
   "ID": 904,
   "Joke": "There were two flies sitting on a toilet seat... one got pissed off."
 },
 {
   "ID": 905,
   "Joke": "What's a difference between a teacher and a train? The teacher tells you to spit you gum out. The train says, \"Chew, chew, chew!\""
 },
 {
   "ID": 906,
   "Joke": "Why don't blind people like skydiving? It scares the crap out of the dog."
 },
 {
   "ID": 907,
   "Joke": "The scientists a scientist went to a remote island with a dog in order to teach his speaking. Three years later, the scientist returns, and is asked about his experiment; he replied \"woof, woof, woof\""
 },
 {
   "ID": 908,
   "Joke": "What do you call a con-artist who minored in psychology? Sigmund Fraud"
 },
 {
   "ID": 909,
   "Joke": "What's a pigs favorite muscle? The hamstring."
 },
 {
   "ID": 910,
   "Joke": "What do fish think about air? It's UN-B-REATHABLE!"
 },
 {
   "ID": 911,
   "Joke": "What did the hammer say to the drill? You're too boring."
 },
 {
   "ID": 912,
   "Joke": "What did Sean Connery say when his books fell on his head? I blame my shelf"
 },
 {
   "ID": 913,
   "Joke": "Why did tomato blush? because it saw the salad dressing"
 },
 {
   "ID": 914,
   "Joke": "My biggest problem with passive smoking is having to follow the smoker around."
 },
 {
   "ID": 915,
   "Joke": "What did the traffic light say to the car? Don't look at me I'm changing."
 },
 {
   "ID": 916,
   "Joke": "What is green, sings and can be found in the fridge? Elvis Parsley"
 },
 {
   "ID": 917,
   "Joke": "What is Jackie Chan's favorite drink? Wata"
 },
 {
   "ID": 918,
   "Joke": "What did the Pelican say to the fish when he was running late for work? I'll catch you later!"
 },
 {
   "ID": 919,
   "Joke": "What do you call a camel in Alaska? Lost."
 },
 {
   "ID": 920,
   "Joke": "All these people getting emails from the Prince of Nigeria, I got one from an Egyptian Pharaoh... But it turned out to just be a pyramid scheme."
 },
 {
   "ID": 921,
   "Joke": "I love self deprecating humour. Shame I'm no good at it."
 },
 {
   "ID": 922,
   "Joke": "Here's a funny joke I heard about pizza oh nevermind. It's too cheesy."
 },
 {
   "ID": 923,
   "Joke": "What Time Do You Go To The Dentist? Tooth - Hurty! XD"
 },
 {
   "ID": 924,
   "Joke": "Knock knock. Who's there? Doorbell technician."
 },
 {
   "ID": 925,
   "Joke": "If Mr. Bean lost one of his legs he'd be cannellini!"
 },
 {
   "ID": 926,
   "Joke": "When is the month when the most trees fall? Sep-timber"
 },
 {
   "ID": 927,
   "Joke": "What do you call a cow with three legs? Tri-tip."
 },
 {
   "ID": 928,
   "Joke": "How was Rome split in half? With a pair of *Caesars*"
 },
 {
   "ID": 929,
   "Joke": "What do you call Washington State after a long rain storm? Washed a Ton State. I woke up with that joke in my head this morning. My brain is weird. Had to share it with someone."
 },
 {
   "ID": 930,
   "Joke": "What did the one wall say to the other wall? \"Meet you at the corner\""
 },
 {
   "ID": 931,
   "Joke": "What do beef hearts smell like? Honey."
 },
 {
   "ID": 932,
   "Joke": "How many Romans does it take to screw in a light bulb? V."
 },
 {
   "ID": 933,
   "Joke": "Why do birds fly south for the winter? because its too far to walk!"
 },
 {
   "ID": 934,
   "Joke": "What is a traveler's favorite font? Times New Roamin'!"
 },
 {
   "ID": 935,
   "Joke": "What do you call a nosey pepper? Jalapeno Business"
 },
 {
   "ID": 936,
   "Joke": "Science Jokes Thread on AskReddit! For your amusement: http://en.reddit.com/r/AskReddit/comments/1auxsf/what_are_some_funny_scientific_jokes_that_you_know/"
 },
 {
   "ID": 937,
   "Joke": "Why was Cinderella thrown off the basketball team? *She ran away from the ball.*"
 },
 {
   "ID": 938,
   "Joke": "Why did the air freshener company go out of business? Because they lacked common scents..."
 },
 {
   "ID": 939,
   "Joke": "With a name like Freddy Mercury... shouldn't he have done heavy metal?"
 },
 {
   "ID": 940,
   "Joke": "What do you call someone who serves smelly drinks? a Fartender"
 },
 {
   "ID": 941,
   "Joke": "What do you call a group of Geometry classes? A geomeforest."
 },
 {
   "ID": 942,
   "Joke": "What's red and is bad for your teeth? A brick"
 },
 {
   "ID": 943,
   "Joke": "How much did the pirate charge for corn? He sold them for a buccaneer."
 },
 {
   "ID": 944,
   "Joke": "A penguin walks into a bar... He goes up to the barman and says, \"Have you seen my father in here today?\" The barman says, \"I don't know, what does he look like?\""
 },
 {
   "ID": 945,
   "Joke": "I'm very keen I could tell he was bald at the drop of a hat."
 },
 {
   "ID": 946,
   "Joke": "So I was feeling down the other day... My friend wanted to cheer me up, so he told me 10 jokes to make me feel better. Unfortunately, no pun in ten did."
 },
 {
   "ID": 947,
   "Joke": "What do the French call artificial feet for cats? Faux Paws"
 },
 {
   "ID": 948,
   "Joke": "I just invented a new word! It's called \"plagiarism\"."
 },
 {
   "ID": 949,
   "Joke": "What did the host serve his guests for The Simpsons marathon night? Disco Stew!"
 },
 {
   "ID": 950,
   "Joke": "Why did the mechanic go to art school? Because he wanted to learn how to make a van go!"
 },
 {
   "ID": 951,
   "Joke": "What do you call a fish with no eyes? ....a fssshhh..."
 },
 {
   "ID": 952,
   "Joke": "What kind of dog can do magic tricks? A labracadabrador."
 },
 {
   "ID": 953,
   "Joke": "WHAT is Bruce Lee's favorite drink? WAH TAHH!!!!"
 },
 {
   "ID": 954,
   "Joke": "What other body parts did Voldemort not have apart from his nose? His legs and arms.. because he was disarmed and defeated."
 },
 {
   "ID": 955,
   "Joke": "A police officer bought a robot this robot was fueled by sodium and alkaline, but could only hold enough for 24 hours at a time. so every morning he had to charge it with a salt and battery."
 },
 {
   "ID": 956,
   "Joke": "What kind of bee will not take credit for his contributions? A Humblebee."
 },
 {
   "ID": 957,
   "Joke": "What does a Vulcan lawnmower need to function? A spock plug."
 },
 {
   "ID": 958,
   "Joke": "Why did the chicken cross the road? To show the opossum it could be done."
 },
 {
   "ID": 959,
   "Joke": "I would never exaggerate... ...in a million years."
 },
 {
   "ID": 960,
   "Joke": "They told me I had type \"A\" blood... turns out it was a typo."
 },
 {
   "ID": 961,
   "Joke": "Why did the chicken cross the road? To get to the other side."
 },
 {
   "ID": 962,
   "Joke": "Why do ducks have flat feet? To stomp out forest fires. Why do elephants have flat feet? To stomp out flaming ducks."
 },
 {
   "ID": 963,
   "Joke": "What do you call a midget psychic that broke out of prison? A small medium at large!"
 },
 {
   "ID": 964,
   "Joke": "The hairdresser's oath First, harm no 'do..."
 },
 {
   "ID": 965,
   "Joke": "What kind of pants does Super Mario wear? Denim Denim Denim"
 },
 {
   "ID": 966,
   "Joke": "A man once thought he'd discovered a new primary color but it proved to be merely a pigment of his imagination."
 },
 {
   "ID": 967,
   "Joke": "You'd think that people who kept their head warm would tend to be healthier... but as it turns out, people who wear turbans are actually more likely to be Sikh"
 },
 {
   "ID": 968,
   "Joke": "What do you call a man with his big toe above his shin? Tony"
 },
 {
   "ID": 969,
   "Joke": "what do you call a vampire that sucks mucus instead of blood? nose-feratu!"
 },
 {
   "ID": 970,
   "Joke": "What do you call someone who wears leather, likes bondage and likes getting inked? Moleskine"
 },
 {
   "ID": 971,
   "Joke": "What's the difference between a piano, a tuna and a jar of glue? You: You can tuna piano but you can't piano a tuna! Person getting told joke: What about the glue? You: I knew you'd get stuck there!"
 },
 {
   "ID": 972,
   "Joke": "Why arent koalas actual bears? They dont meet the koalafications."
 },
 {
   "ID": 973,
   "Joke": "What was Dr Frankenstein's second job? He was a body-builder"
 },
 {
   "ID": 974,
   "Joke": "What do you call somebody with no body and no nose? Nobody knows."
 },
 {
   "ID": 975,
   "Joke": "This summer I'm going to go to the beach and bury metal objects that say, 'Get a life' on them. Demetri Martin"
 },
 {
   "ID": 976,
   "Joke": "I had a conversation with a Mobius strip... It was one-sided."
 },
 {
   "ID": 977,
   "Joke": "Coco The Clown took his car back to the garage this week. The door wouldn't fall off."
 },
 {
   "ID": 978,
   "Joke": "What do you call a pachyderm that sings jazz? Elephants Gerald"
 },
 {
   "ID": 979,
   "Joke": "How much do drum shaped sofas cost? 5 dollars per-cushion."
 },
 {
   "ID": 980,
   "Joke": "What do you call a cow jumping over a barbed wire fence? Utter destruction! !!!!"
 },
 {
   "ID": 981,
   "Joke": "Did someone say \"purple\"? Sorry, it must have been a pigment of my imagination!"
 },
 {
   "ID": 982,
   "Joke": "What did the blue denims say to the black denims? I guess we have different genes! *knee slap* ... I'll see myself to the door"
 },
 {
   "ID": 983,
   "Joke": "I just found out I'm colorblind It came out of the yellow."
 },
 {
   "ID": 984,
   "Joke": "Ever heard about that movie called Constipation? It never came out."
 },
 {
   "ID": 985,
   "Joke": "How does a plant walk? It uses a plant stand."
 },
 {
   "ID": 986,
   "Joke": "Did you hear about the two silk worms that got in a fight? It ended in a tie."
 },
 {
   "ID": 987,
   "Joke": "What do you call a midget psychic who just escaped from prison? A small medium at large"
 },
 {
   "ID": 988,
   "Joke": "Why does Mr. Pencil hate Mr. Pen so much? Because he is an erascist."
 },
 {
   "ID": 989,
   "Joke": "I made a model aircraft. I wanted it to be an unpainted smooth finish wooden aircraft. So I made a plain planed plane plane."
 },
 {
   "ID": 990,
   "Joke": "What happened to the Denver Broncos in the Super Bowl? They had a MetLife crisis. (that's the name of the stadium)"
 },
 {
   "ID": 991,
   "Joke": "How do you pay for things in the Czech Republic? Cash or Czech Edit: a word"
 },
 {
   "ID": 992,
   "Joke": "What begins with E, ends with E, and has one letter? envelope"
 },
 {
   "ID": 993,
   "Joke": "Why did Beethoven get rid of his chickens? All they said was, Bach, Bach, Bach ..."
 },
 {
   "ID": 994,
   "Joke": "Why did the packaged green onion get into trouble? Because it was a wrapped scallion."
 },
 {
   "ID": 995,
   "Joke": "What time do you go to the dentist? 2:30"
 },
 {
   "ID": 996,
   "Joke": "Did you hear about the kidnapping recently? The goatherd woke him up."
 },
 {
   "ID": 997,
   "Joke": "What do you call two guys above a window? Curt 'n Rod"
 },
 {
   "ID": 998,
   "Joke": "Why did the lettuce get arrested? ...for disturbing the peas!"
 },
 {
   "ID": 999,
   "Joke": "What happened to the tyrannical fruit? He was impeached!"
 },
 {
   "ID": 1000,
   "Joke": "Did you hear about the corduroy pillow? You didn't hear? It made headlines!"
 },
 {
   "ID": 1001,
   "Joke": "Today, the doctor told me that the bottom of my heart has stopped functioning. My girlfriend will be disappointed; that's the part I loved her from."
 },
 {
   "ID": 1002,
   "Joke": "How do you make gold soup? You use 14 carrots."
 },
 {
   "ID": 1003,
   "Joke": "What's my New Year resolution? Well, I just got a Hi-Def TV, so it's 1920 X 1080i."
 },
 {
   "ID": 1004,
   "Joke": "How does a cactus do his math homework? He uses a cacti-lator!"
 },
 {
   "ID": 1005,
   "Joke": "What's an oven's favorite comedy routine? Deadpan."
 },
 {
   "ID": 1006,
   "Joke": "Two balloons are floating across the desert One balloon says to the other, Look out for the cactussssssssssssssssssss!"
 },
 {
   "ID": 1007,
   "Joke": "linuxmint 13 or 15 question why does 13 have lts and not newer versions?"
 },
 {
   "ID": 1008,
   "Joke": "why was Pavlov's hair so soft? classical conditioning."
 },
 {
   "ID": 1009,
   "Joke": "What did the slab of meat say when it was covered in salt and left out to dry? \"I'm cured!\""
 },
 {
   "ID": 1010,
   "Joke": "What do you call an animal that goes through your trash and tells great stories? A raccoonteur."
 },
 {
   "ID": 1011,
   "Joke": "I'm making a band! I started a band called 999 Megabytes...we havent gotten a gig yet."
 },
 {
   "ID": 1012,
   "Joke": "What do you call thrusting a hairy rod in and out of your mouth really fast then afterwards spitting out a white liquid? Brushing your teeth"
 },
 {
   "ID": 1013,
   "Joke": "Why doesn't the sun need to go to University? He's too bright."
 },
 {
   "ID": 1014,
   "Joke": "Why did the turtle cross the road? To get to the nearest Shell Station!"
 },
 {
   "ID": 1015,
   "Joke": "Do you know why one side of the the V formation of geese in flight is longer than the other side? Because It has more geese in it!"
 },
 {
   "ID": 1016,
   "Joke": "What's a pirates favorite letter? You think it's the \"R\" but it's really the \"C\". Happy talk like a pirate day!"
 },
 {
   "ID": 1017,
   "Joke": "Did you hear about the Native American who went to a party and drank 37 cups of tea? They found him dead the next morning in his tea pee."
 },
 {
   "ID": 1018,
   "Joke": "What did the elephant say to the horn-less rhino? \"Rhino horn?\""
 },
 {
   "ID": 1019,
   "Joke": "What do you call a cow with no legs? Ground beef!"
 },
 {
   "ID": 1020,
   "Joke": "How do porcupines play leapfrog? Very carefully"
 },
 {
   "ID": 1021,
   "Joke": "Where does the General keep his armies? In his sleevies."
 },
 {
   "ID": 1022,
   "Joke": "How many Super Saiyans does it take to change a lightbulb? Just 1 but it will take 3 episodes."
 },
 {
   "ID": 1023,
   "Joke": "What do you call 99 bunnies walking forward and they take one step backwards? A receding hare line."
 },
 {
   "ID": 1024,
   "Joke": "What kind of jeans do ghosts wear? Boo Jeans"
 },
 {
   "ID": 1025,
   "Joke": "What should you do before criticizing Pac-Man? WAKA WAKA WAKA mile in his shoes"
 },
 {
   "ID": 1026,
   "Joke": "What do you call a father who was kidnapped in Iraq? A Baghdad."
 },
 {
   "ID": 1027,
   "Joke": "What has six eyes but cannot see? Three men in a house with dirty dishes in the sink, laundry that needs to be folded and kids that need a bath"
 },
 {
   "ID": 1028,
   "Joke": "What do Egyptians do when their mass transit breaks down? Get Anubis."
 },
 {
   "ID": 1029,
   "Joke": "What's the difference between unlawful and illegal? Unlawful is against the law and illegal is a sick bird."
 },
 {
   "ID": 1030,
   "Joke": "How long did it take for the police to catch the man running in his underwear? It was a brief chase..."
 },
 {
   "ID": 1031,
   "Joke": "What do call a horse that lives near you? A neighbor (naybor for pessimist horses)"
 },
 {
   "ID": 1032,
   "Joke": "A termite walks into a pub And asks \"where's the bar tender?\""
 },
 {
   "ID": 1033,
   "Joke": "What kind of birds stick together? Vel-crows"
 },
 {
   "ID": 1034,
   "Joke": "What happens when you get some vinegar in your ear? You suffer from pickled hearing!"
 },
 {
   "ID": 1035,
   "Joke": "A sad can goes to get recycled. He was soda-pressed."
 },
 {
   "ID": 1036,
   "Joke": "What does Drew Carey have in his driveway? Cleveland Rocks!"
 },
 {
   "ID": 1037,
   "Joke": "Why don't you want your nose to be 12 inches long? because then it would be a foot!"
 },
 {
   "ID": 1038,
   "Joke": "Branson My wife and I went to Branson, Missouri. I think our hotel caters to senior citizens because it had a free incontinental breakfast."
 },
 {
   "ID": 1039,
   "Joke": "A long joke jooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooke"
 },
 {
   "ID": 1040,
   "Joke": "What did one ocean say to the other ocean? Nothing, they just waved."
 },
 {
   "ID": 1041,
   "Joke": "Whats blue and smells like red paint? Blue paint"
 },
 {
   "ID": 1042,
   "Joke": "ABCDEFGHIJKMNOPQRSTUVWXYZ Noel."
 },
 {
   "ID": 1043,
   "Joke": "Kids, I don't know if our ceiling is the best ceiling... ...but it's definitely up there."
 },
 {
   "ID": 1044,
   "Joke": "Why was the hula hoop a great boxer? It could go round for round."
 },
 {
   "ID": 1045,
   "Joke": "how do you make 7 even? remove the \"s\""
 },
 {
   "ID": 1046,
   "Joke": "What gets longer the more you cut it at both ends? A ditch."
 },
 {
   "ID": 1047,
   "Joke": "Where does dubious pasta come from? The spaghetto. I can't take all the credit, however: I heard the word from [this](http://www.reddit.com/r/funny/comments/xdp4k/the_gaydar/c5lnkep) guy"
 },
 {
   "ID": 1048,
   "Joke": "What did the 0 say to the 8? Nice belt!"
 },
 {
   "ID": 1049,
   "Joke": "Why was the chicken kicked out of class? For using *fowl* language."
 },
 {
   "ID": 1050,
   "Joke": "At least I now know why the lions leave the plains before the end of summer. Because the Pride goeth before the Fall."
 },
 {
   "ID": 1051,
   "Joke": "What do you call an economist at an amusement park who is just sitting around? A lazy fair goer!"
 },
 {
   "ID": 1052,
   "Joke": "How did the prostitute get promoted? She slept her way to the top!"
 },
 {
   "ID": 1053,
   "Joke": "What did the space between two tiles say? I AM GROUT"
 },
 {
   "ID": 1054,
   "Joke": "What do you say to the Montana barista when they overfill your chamomile? Beautiful"
 },
 {
   "ID": 1055,
   "Joke": "What's green and fuzzy and can kill you if it falls from a tree? A pool table."
 },
 {
   "ID": 1056,
   "Joke": "How do you make a tissue dance? You put a little boogie in it. :)"
 },
 {
   "ID": 1057,
   "Joke": "Wanna hear a construction joke? I'm working on it."
 },
 {
   "ID": 1058,
   "Joke": "What do gamers plant in their garden? Skill trees! **Dances wildly with top hat and cane**"
 },
 {
   "ID": 1059,
   "Joke": "What's an idealist vegetarian's favorite meal? Peas and hominy"
 },
 {
   "ID": 1060,
   "Joke": "Who's bad at baseball but fun at parties? A pitcher filled with margaritas!"
 },
 {
   "ID": 1061,
   "Joke": "What do you get when you mix two chains and a cow? Truuuuuuuuuuu-moooooooooooooooooo!!!"
 },
 {
   "ID": 1062,
   "Joke": "Why do elephants hide behind trees? To trip ants."
 },
 {
   "ID": 1063,
   "Joke": "I can make a movie with my hand. All it takes is a FLICK of the wrist!"
 },
 {
   "ID": 1064,
   "Joke": "I am not pro gay. I am not even amateur gay. But, I support their rights."
 },
 {
   "ID": 1065,
   "Joke": "why didn't the american leek want to talk to the japanese leek? because it was negi"
 },
 {
   "ID": 1066,
   "Joke": "I hate girls with double standards unless they're pretty"
 },
 {
   "ID": 1067,
   "Joke": "What did the lazy surgeon say to his patient? Suture self!"
 },
 {
   "ID": 1068,
   "Joke": "I have found that there are three kinds of people; Those who can count and those who can't."
 },
 {
   "ID": 1069,
   "Joke": "I made half a cup of tea the other day... It was so nice I had two."
 },
 {
   "ID": 1070,
   "Joke": "Why did peanut butter flop at the talent show? He didn't have the right jam."
 },
 {
   "ID": 1071,
   "Joke": "How many tickles does it take to make a squid laugh? Tentacles."
 },
 {
   "ID": 1072,
   "Joke": "Where do Cows go for parties? The Moovies"
 },
 {
   "ID": 1073,
   "Joke": "How many Saiyans does it take to change a lightbulb? Just one, but it takes 5 episodes."
 },
 {
   "ID": 1074,
   "Joke": "Did you hear about the schizophrenic accounts manager? He couldn't help but hear invoices inside his head."
 },
 {
   "ID": 1075,
   "Joke": "[My Joke] Why do galaxies put on boring shows while separated? Because their performance is lack-cluster."
 },
 {
   "ID": 1076,
   "Joke": "Knock Knock..."
 },
 {
   "ID": 1077,
   "Joke": "There is a special species of bird that is really good at holding stuff together... They're called velcrows."
 },
 {
   "ID": 1078,
   "Joke": "Why are jokes about rotten eggs banned? Because they're infeggtious"
 },
 {
   "ID": 1079,
   "Joke": "What side dish do frogs like to enjoy with their hamburgers? French Flies!"
 },
 {
   "ID": 1080,
   "Joke": "What do cows do for fun? They go to the mooooo-vies."
 },
 {
   "ID": 1081,
   "Joke": "Why did the puppy get away with committing murder? ...He had paws-able deniability."
 },
 {
   "ID": 1082,
   "Joke": "There once was a jealous zombie... But he ate his heart out."
 },
 {
   "ID": 1083,
   "Joke": "What do you call a ubiquitous spud? A common-tater!"
 },
 {
   "ID": 1084,
   "Joke": "Why was Cinderella banned from playing sports? Because she always ran away from the ball &lt;p&gt; My favorite joke since I was little"
 },
 {
   "ID": 1085,
   "Joke": "Want to hear a joke about pizza? Never mind, it's probably too cheesy."
 },
 {
   "ID": 1086,
   "Joke": "What has a bottom at the top? Your legs."
 },
 {
   "ID": 1087,
   "Joke": "What type of grain uses profanity? Vulgar Wheat"
 },
 {
   "ID": 1088,
   "Joke": "What do you call a penguin with a smoking problem? It's a puffin!"
 },
 {
   "ID": 1089,
   "Joke": "What did they call the Pillsbury Doughboy after he hurt his leg? Limp Biscuit"
 },
 {
   "ID": 1090,
   "Joke": "Better be named after what? If you had to choose, would you prefer having a disease named after you, or be named after your mother in law?"
 },
 {
   "ID": 1091,
   "Joke": "I know a woman who owns a taser... Let me tell you, she's stunning!"
 },
 {
   "ID": 1092,
   "Joke": "Did you hear about the neutron who was arrested? He was held without charge."
 },
 {
   "ID": 1093,
   "Joke": "Have you ever heard the one about the dust bunny and the mud pie? Well then sorry, I only tell clean jokes."
 },
 {
   "ID": 1094,
   "Joke": "Why was the tomato blushing? Because it saw the salad dressing."
 },
 {
   "ID": 1095,
   "Joke": "My buddy said he'd give his right arm to be ambidextrous I can only admire such dedication."
 },
 {
   "ID": 1096,
   "Joke": "Why did the skeleton not attend prom? He had no body to go with."
 },
 {
   "ID": 1097,
   "Joke": "Why was the owl afraid of Raidoactivity Because it was made of Hootonium"
 },
 {
   "ID": 1098,
   "Joke": "How many US Congressmen does it take to change a lightbulb? Oh, please. Like they've ever changed anything that needed it."
 },
 {
   "ID": 1099,
   "Joke": "What do you call soup that you've found a hair in? Rabbit Soup :D"
 },
 {
   "ID": 1100,
   "Joke": "What do you call a woman with one leg? Eileen"
 },
 {
   "ID": 1101,
   "Joke": "Two birds are sitting on a perch. One bird says to the other, \"Do you smell fish?\""
 },
 {
   "ID": 1102,
   "Joke": "A man wanted to name his son a very long name... ...so he named him Miles"
 },
 {
   "ID": 1103,
   "Joke": "What killed the guy ordering at an Italian restaurant? He'd had trouble deciding to go with the appetizers or entrees, but eventually he went antipasto way."
 },
 {
   "ID": 1104,
   "Joke": "I'm tired of people calling America the dumbest country in the world Quite frankly, I think Europe is!"
 },
 {
   "ID": 1105,
   "Joke": "What did Arnold Schwarzenegger say upon being asked to star in a Broadway production about the world's greatest composers? I'll be Bach. Sorry."
 },
 {
   "ID": 1106,
   "Joke": "What did the owner of the Indian restaurant say when he burned all of his bread? \"Don't worry, it's a naan issue.\""
 },
 {
   "ID": 1107,
   "Joke": "Who was the most important Knight of the Round Table? Sir Cumference."
 },
 {
   "ID": 1108,
   "Joke": "Why did Beethoven kill off his chickens? They kept saying, \"Bach, Bach, Bach.\""
 },
 {
   "ID": 1109,
   "Joke": "Why did the bigamist cross the road? To get to the other bride."
 },
 {
   "ID": 1110,
   "Joke": "Why did the fox cross the road? It was chassing after the chicken!"
 },
 {
   "ID": 1111,
   "Joke": "Why did the man throw his watch out the window? He wanted to see time fly!"
 },
 {
   "ID": 1112,
   "Joke": "Why is ok to leave the lid off a basket of socialist crabs? Because whenever one of them climbs to the top, the others drag it back down."
 },
 {
   "ID": 1113,
   "Joke": "Why did the banker leave his job? he lost interest"
 },
 {
   "ID": 1114,
   "Joke": "What do you call a cashew in space? An astronut."
 },
 {
   "ID": 1115,
   "Joke": "Why are some chillies nosy? They're jalapeno business"
 },
 {
   "ID": 1116,
   "Joke": "What did the digital clock say to the grandfather clock? \"Look grandpa, no hands!\""
 },
 {
   "ID": 1117,
   "Joke": "What do you call it when you dip poultry and beef in chocolate?  Brown-chichen-Brown-cow"
 },
 {
   "ID": 1118,
   "Joke": "What happens when your cousin eats all the Pumpkin pie on Thanksgiving? Plump kin!"
 },
 {
   "ID": 1119,
   "Joke": "Why does the Pope only eat munchkins? Cause they're the holy part of the donut!"
 },
 {
   "ID": 1120,
   "Joke": "Knock, Knock... Who's there? The K.G.B. The K.G.B. wh... **SLAP**! WE are K.G.B., WE will ask questions!!"
 },
 {
   "ID": 1121,
   "Joke": "What is Mozart doing right now? Decomposing"
 },
 {
   "ID": 1122,
   "Joke": "What is a vampire's favorite fruit? a Neck-tarine --From a great co-worker"
 },
 {
   "ID": 1123,
   "Joke": "\"So Sherlock...\" asked Watson, \"I forget, what was your highest degree of education?\" \"Elementary, my dear Watson.\""
 },
 {
   "ID": 1124,
   "Joke": "What did Descartes say while shopping online? I think therefore I Amazon"
 },
 {
   "ID": 1125,
   "Joke": "What does r/The_Donald call its rule list? The MAGA Carta"
 },
 {
   "ID": 1126,
   "Joke": "A cow fell off a truck in Russia Apparently he hadn't been Put in properly."
 },
 {
   "ID": 1127,
   "Joke": "What do you call a flower in Florida? Orlando Bloom."
 },
 {
   "ID": 1128,
   "Joke": "What do you call an Egyptian doctor who works on peoples backs? A Cairopractor!"
 },
 {
   "ID": 1129,
   "Joke": "Why did the dog go into the water? Because he didn't want to be a hot dog."
 },
 {
   "ID": 1130,
   "Joke": "Why'd the hipster burn his mouth on his coffee? Because he drank it before it was cool."
 },
 {
   "ID": 1131,
   "Joke": "Why couldn't the lifeguard save the hippie from drowning? He was *too far out, maaan*."
 },
 {
   "ID": 1132,
   "Joke": "If you have bladder problems. Urine trouble."
 },
 {
   "ID": 1133,
   "Joke": "Where did the general keep his armies? In his sleevies!"
 },
 {
   "ID": 1134,
   "Joke": "What did Cholera say to Malaria? Are you gonna Jaundice on Saturday?"
 },
 {
   "ID": 1135,
   "Joke": "Q)What will you call a person who sleeps next to a close relative? A) NapKin"
 },
 {
   "ID": 1136,
   "Joke": "Scary Halloween Joke **Person 1:** Knock knock! **Person 2:** Who's there? **Person 1:** A GHOST!!!"
 },
 {
   "ID": 1137,
   "Joke": "Who invented fractions? Henry the 1/8"
 },
 {
   "ID": 1138,
   "Joke": "What's cold and scary?! I-scream!"
 },
 {
   "ID": 1139,
   "Joke": "Why was the rooster happy after his trip to Vegas? He got clucky."
 },
 {
   "ID": 1140,
   "Joke": "What did the judge ask when he went to the dentist? Do you swear to pull the tooth, the whole tooth and nothing but the tooth?"
 },
 {
   "ID": 1141,
   "Joke": "Why are horses never overweight? They're on a stable diet."
 },
 {
   "ID": 1142,
   "Joke": "Why does not a forth-grader ever take the bus home? Because he knew his parents will make him return it."
 },
 {
   "ID": 1143,
   "Joke": "Why was Farmer Bob so good at his job? Because he was outstanding in his field"
 },
 {
   "ID": 1144,
   "Joke": "What do you call a fish who works for the government? An Official."
 },
 {
   "ID": 1145,
   "Joke": "Why didn't the Duke of Windsor let his French servant help him tie his tie? He never does it with a four-in (foreign)-hand."
 },
 {
   "ID": 1146,
   "Joke": "Why did the bald man draw rabbits all over his head? From a distance they look like hares!"
 },
 {
   "ID": 1147,
   "Joke": "I went to a shredded cheese convention the other day... it was grate"
 },
 {
   "ID": 1148,
   "Joke": "What is ISIL's favourite dessert? Terrormisu"
 },
 {
   "ID": 1149,
   "Joke": "Wanna hear two short jokes and a long joke? Joke joke jooooke!"
 },
 {
   "ID": 1150,
   "Joke": "What happened to the runny nose... it tripped and fell. Now it's all boogered up."
 },
 {
   "ID": 1151,
   "Joke": "Four years ago, I asked out the girl of my dreams. Today, I asked her to marry me. She said no both times. (not an original)"
 },
 {
   "ID": 1152,
   "Joke": "What do you call a cavator that isnt a cavator anymore? an EXcavator"
 },
 {
   "ID": 1153,
   "Joke": "Why did the strawberry cry? Because his mother was in a jam."
 },
 {
   "ID": 1154,
   "Joke": "People dont like having to bend over to get their drinks... We really need to raise the bar."
 },
 {
   "ID": 1155,
   "Joke": "I fear for the calendar... ...its days are numbered."
 },
 {
   "ID": 1156,
   "Joke": "why are there fences around graveyards? people are just dying to get in there these days."
 },
 {
   "ID": 1157,
   "Joke": "One Eskimo said to the other, \"Where is your mother from?\" The second Eskimo says \"Alaska.\""
 },
 {
   "ID": 1158,
   "Joke": "Why can't a Pirate make it through their ABC's? They always get lost at C."
 },
 {
   "ID": 1159,
   "Joke": "Jesus wrote a play about a tornado. It was an Act of God."
 },
 {
   "ID": 1160,
   "Joke": "What did the blonde do when she discovered that most accidents happen within a mile from home? She moved."
 },
 {
   "ID": 1161,
   "Joke": "Why did the girltree fall in love with the boy tree? He was sappy"
 },
 {
   "ID": 1162,
   "Joke": "I went to a seafood disco last week... ...and pulled a mussel."
 },
 {
   "ID": 1163,
   "Joke": "Why did the pie go to the dentist? It needed a filling."
 },
 {
   "ID": 1164,
   "Joke": "(True story) So my friend saw me browsing this subreddit and he said... \"Is this a subreddit for really bad jokes?\""
 },
 {
   "ID": 1165,
   "Joke": "Superman and Eyore had a baby. The baby's name? Supereyore"
 },
 {
   "ID": 1166,
   "Joke": "What cheese do you use to get a bear out of a tree? Camembert!"
 },
 {
   "ID": 1167,
   "Joke": "Did you know that it's traditional to serve Eggs Benedict on a hubcap? There's no plate like chrome for the Hollandaise."
 },
 {
   "ID": 1168,
   "Joke": "What do you call a deep-sea diving dog? Scuba - Doo!"
 },
 {
   "ID": 1169,
   "Joke": "Where did the fish go when it needed an operation? To the sturgeon"
 },
 {
   "ID": 1170,
   "Joke": "My English teacher got really angry about the format of my essay. It wasn't justified."
 },
 {
   "ID": 1171,
   "Joke": "Starcraft: Why did the marine vote for the dragoon? He was Protoss"
 },
 {
   "ID": 1172,
   "Joke": "All these people getting emails from the Prince of Nigeria, I got one from an Egyptian Pharaoh... But it turned out to just be a pyramid scheme."
 },
 {
   "ID": 1173,
   "Joke": "What do you get if you cross an elephant with a fish? Swimming trunks"
 },
 {
   "ID": 1174,
   "Joke": "Where is Engagement, Ohio? Between Dayton and Marion."
 },
 {
   "ID": 1175,
   "Joke": "Why is Ireland the richest country in the world? Because it's capital is always Dublin."
 },
 {
   "ID": 1176,
   "Joke": "Can you tell me what you call a person from Corsica? Course a can."
 },
 {
   "ID": 1177,
   "Joke": "How did the metal get the wrong idea? He was misled."
 },
 {
   "ID": 1178,
   "Joke": "So today is Star Wars day May the fourth be with you!"
 },
 {
   "ID": 1179,
   "Joke": "what happens if you drink 3.14 liters of water? you will Pi ss"
 },
 {
   "ID": 1180,
   "Joke": "A WWII Joke! What did the German Shepherd say at his Nuremberg trial? \"I was just following odors.\""
 },
 {
   "ID": 1181,
   "Joke": "What do cows like to put on their hot dogs? moostard"
 },
 {
   "ID": 1182,
   "Joke": "Why did the cow go to the psychologist? She had a fodder complex."
 },
 {
   "ID": 1183,
   "Joke": "Why did the knife quit? It couldn't CUT IT! woohoo! I made this one up while sitting at a buffet table. Enjoy! ~Skip"
 },
 {
   "ID": 1184,
   "Joke": "What's George Washington's least favorite flower? Li[e]-lacs!"
 },
 {
   "ID": 1185,
   "Joke": "Why should you avoid people dressed as celery? They could be stalking you!"
 },
 {
   "ID": 1186,
   "Joke": "Wanna hear a joke about Nitric Oxide ? NO"
 },
 {
   "ID": 1187,
   "Joke": "What's the strongest letter in the alphabet? ***P*** Even Superman can't hold it."
 },
 {
   "ID": 1188,
   "Joke": "What do you call it when your wife brings you rice porridge in prison? Congee-gal visit"
 },
 {
   "ID": 1189,
   "Joke": "Why did the dinosaur cross the road? Because the chicken didn't exist."
 },
 {
   "ID": 1190,
   "Joke": "Why does a rapper need an umbrella? Fo' drizzle."
 },
 {
   "ID": 1191,
   "Joke": "What did Tennessee? What Arkansas."
 },
 {
   "ID": 1192,
   "Joke": "My son decided to help me clean the car today. After ten minutes of watching him, I told him to use some elbow grease. Two hours later, the idiot came back and told me that he couldn't find it."
 },
 {
   "ID": 1193,
   "Joke": "What do you call a group of Combi's? A Combi nation!"
 },
 {
   "ID": 1194,
   "Joke": "How do you get down from an elephant? You don't, you get down from a duck"
 },
 {
   "ID": 1195,
   "Joke": "You can pick your friends, and you can pick your nose... But you can't pick your friend's nose"
 },
 {
   "ID": 1196,
   "Joke": "Which whiskey should you buy if you want to dance all night? Wild Twerky!"
 },
 {
   "ID": 1197,
   "Joke": "Why couldn't the hunter cook breakfast? The game warden found out he poached his eggs!"
 },
 {
   "ID": 1198,
   "Joke": "I went to an ATM... I was at an ATM this morning and this older lady asked me to help check her balance, so I pushed her over."
 },
 {
   "ID": 1199,
   "Joke": "How much does a truck full of bones weigh? A skeleTon"
 },
 {
   "ID": 1200,
   "Joke": "Why don't cats play poker in the jungle? Too many cheetahs!"
 },
 {
   "ID": 1201,
   "Joke": "A skeleton walks into a bar... Asks for a beer and a mop."
 },
 {
   "ID": 1202,
   "Joke": "What do you call an atheist bone? A blasfemur."
 },
 {
   "ID": 1203,
   "Joke": "How do you catch a one-of-a-kind rabbit? Unique up on it. How do you catch a very calm rabbit? The tame way."
 },
 {
   "ID": 1204,
   "Joke": "Will Smith's website isn't responding. What do you do? Refresh Prince of Bel Air."
 },
 {
   "ID": 1205,
   "Joke": "What the the electrician say to his buddy? Watts up?!"
 },
 {
   "ID": 1206,
   "Joke": "How many South Americans does it take to change a lightbulb? A Brazilian.... I'll get my coat..."
 },
 {
   "ID": 1207,
   "Joke": "How do you catch a bra? You set a booby trap."
 },
 {
   "ID": 1208,
   "Joke": "April showers bring May flowers, but what do May flowers bring? Pilgrims."
 },
 {
   "ID": 1209,
   "Joke": "Which cheese is the loneliest? Prov-alone!"
 },
 {
   "ID": 1210,
   "Joke": "Did you hear the joke about the fast car? I would tell you but I think you're too slow to get it."
 },
 {
   "ID": 1211,
   "Joke": "Why did the twinkie go to the dentist? He lost his filling!"
 },
 {
   "ID": 1212,
   "Joke": "How does a fish always know how much they weigh? Because they have their own scales!"
 },
 {
   "ID": 1213,
   "Joke": "What does music have to do with safety? If you don't C sharp, you'll B flat."
 },
 {
   "ID": 1214,
   "Joke": "Why is there very little honey in Belgium? Because there is only one B in Belgium"
 },
 {
   "ID": 1215,
   "Joke": "How many goals did Germany score? gerMANY"
 },
 {
   "ID": 1216,
   "Joke": "Why did the elephant turn around in the airport and go home? He forgot to pack his trunk."
 },
 {
   "ID": 1217,
   "Joke": "Two fish are in a tank... Two fish are in a tank... First one says: I'll drive! Second one says: \"I'll man the guns!\""
 },
 {
   "ID": 1218,
   "Joke": "How many hipsters does it take to change a light bulb? it's a pretty obscure number.... i'm sure you haven't heard of it."
 },
 {
   "ID": 1219,
   "Joke": "What celebrity never payed with a cheque or credit? Johnny Cash."
 },
 {
   "ID": 1220,
   "Joke": "What is a pair of sheep's favorite instrument? Two-Baaas."
 },
 {
   "ID": 1221,
   "Joke": "You know why ancient Greek children were always getting lost from their parents? 'Cause they kept Roman around!"
 },
 {
   "ID": 1222,
   "Joke": "Have you heard about that hot Thai lounge singer? Yeah. They call him *Frank Sriracha.*"
 },
 {
   "ID": 1223,
   "Joke": "...walks into a bar... A golfer, a priest and a lawyer walk into a bar. The bartender looks up and asks, \"What is this? Some kind of joke?\""
 },
 {
   "ID": 1224,
   "Joke": "Other uses for chloroform 1) A great conversational piece when talking to the cops about using it 2) Make the day go by faster 3) And finally, as a reagent."
 },
 {
   "ID": 1225,
   "Joke": "Cars Why do lazy people only drive automatics? Because they're shiftless."
 },
 {
   "ID": 1226,
   "Joke": "Why is Yoda afraid of seven? Because six seven eight."
 },
 {
   "ID": 1227,
   "Joke": "Why couldn't the pirate learn the alphabet? Because he was always lost at C."
 },
 {
   "ID": 1228,
   "Joke": "College My son took Rock Climbing in college but he had to drop the class. He couldn't find any \"Cliff Notes.\""
 },
 {
   "ID": 1229,
   "Joke": "What is the cheapest part of a boat? The part with the sail in it."
 },
 {
   "ID": 1230,
   "Joke": "Why was the egg kicked out of the comedy club? Because he was telling bad yolks!"
 },
 {
   "ID": 1231,
   "Joke": "You know what's the problem with Mexican and black jokes? If you've heard Juan, you've heard Jamaal."
 },
 {
   "ID": 1232,
   "Joke": "The signature dish of a restaurant called the Twisted Rooster: Mobius Chicken Strips."
 },
 {
   "ID": 1233,
   "Joke": "What did one math book say to the other? Don't bother me; I've got my own *problems!*"
 },
 {
   "ID": 1234,
   "Joke": "Why are giraffes slow to apologize? It takes them a long time to swallow their pride"
 },
 {
   "ID": 1235,
   "Joke": "Velcro What a rip off. Joke by Tim Vine."
 },
 {
   "ID": 1236,
   "Joke": "Why don't melons ever run away and get married? Because they cantaloupe!"
 },
 {
   "ID": 1237,
   "Joke": "Like most people my age... I'm 27."
 },
 {
   "ID": 1238,
   "Joke": "Two fish in a tank Fish 1:Uh, Greg? Fish 2:What Fish 1:How do we drive this thing"
 },
 {
   "ID": 1239,
   "Joke": "Did you hear about the Italian chef that died? He pasta way."
 },
 {
   "ID": 1240,
   "Joke": "Why did the bacteria cross the microscope? To get to the other slide"
 },
 {
   "ID": 1241,
   "Joke": "I read a story about a kid that ate 4 cans of alphabet soup in one sitting... It said that he later had a massive vowel movement. Maybe a dirty joke."
 },
 {
   "ID": 1242,
   "Joke": "Tasted the best Borscht ever! It'll be hard to beet."
 },
 {
   "ID": 1243,
   "Joke": "The Fine Bros. 'React' announcement was like a television with no antenna. Poor reception."
 },
 {
   "ID": 1244,
   "Joke": "What do call a horse that lives near you? A naybor"
 },
 {
   "ID": 1245,
   "Joke": "What kind of bees make milk? Boobies."
 },
 {
   "ID": 1246,
   "Joke": "What does Mario use to get his hot dogs off the grill? He uses his Donkey Tongs."
 },
 {
   "ID": 1247,
   "Joke": "\"We don't serve time travelers here\" A time traveler walks into a bar."
 },
 {
   "ID": 1248,
   "Joke": "How do you kill bread? Bake it for a little while, and it will be toast."
 },
 {
   "ID": 1249,
   "Joke": "What do you call an imaginary color? A pigment of your imagination."
 },
 {
   "ID": 1250,
   "Joke": "Did you hear about the mathematician who hated negative numbers? He'll stop at nothing to avoid them!"
 },
 {
   "ID": 1251,
   "Joke": "What do you call security guards working outside Samsung shops? Guardians of the Galaxy"
 },
 {
   "ID": 1252,
   "Joke": "What do you call cheese that is by itself? Provolone"
 },
 {
   "ID": 1253,
   "Joke": "I just got a job helping a one arm typist do capital letters... Its shift work."
 },
 {
   "ID": 1254,
   "Joke": "Why does a Bicycle have a kickstand? Because it's two tired."
 },
 {
   "ID": 1255,
   "Joke": "Which side of a horse has the most hair? The OUTSIDE! oh-my-goodness, that's hilarious! ~Skip"
 },
 {
   "ID": 1256,
   "Joke": "I went in to a pet shop and said, Can I buy a goldfish? The guy said, Do you want an aquarium? I said, I dont care what star sign it is."
 },
 {
   "ID": 1257,
   "Joke": "Noah wasn't much for civilized society . . . You could say he was an-arc-ist."
 },
 {
   "ID": 1258,
   "Joke": "Two silk worms had a race. They ended up in a tie."
 },
 {
   "ID": 1259,
   "Joke": "What do you call a sheep covered in chocolate? A candy baa"
 },
 {
   "ID": 1260,
   "Joke": "What do you do if you see a spaceman? You park in it, man."
 },
 {
   "ID": 1261,
   "Joke": "Why did Trump insist on Hillary Clinton as Secretary of state? He doesn't believe women should get above secretary"
 },
 {
   "ID": 1262,
   "Joke": "I was wondering why the frisbee was getting bigger. And then it hit me."
 },
 {
   "ID": 1263,
   "Joke": "What did the Buffalo say when his child left for college? Bison"
 },
 {
   "ID": 1264,
   "Joke": "How do you keep an idiot in suspense? I'll tell you later."
 },
 {
   "ID": 1265,
   "Joke": "Batman doesn't have nightmares Nightmares have batman"
 },
 {
   "ID": 1266,
   "Joke": "Charles Dickens walks into a bar... and orders a martini. The bartender asks \"olive 'er twist?\""
 },
 {
   "ID": 1267,
   "Joke": "Nickelback walks into a bar.... So Nickelback walks into a bar, and there is no punchline, because ruining music isn't funny."
 },
 {
   "ID": 1268,
   "Joke": "So a polar bear walks into a bar... and says, \"I'll have a gin.....and tonic\" The bartender says, \"What's with the big pause?\" And the polar bear says, \"Oh, I've always had them.\""
 },
 {
   "ID": 1269,
   "Joke": "Mom asked if I wanted to race toy cars with my neighbor Chucky. I responded, \"Nah, that's child's play.\""
 },
 {
   "ID": 1270,
   "Joke": "What do you find in a cloud's shorts? Thunderpants!"
 },
 {
   "ID": 1271,
   "Joke": "Why did the SSD burn a flag? Because it was a Patriot Blaze"
 },
 {
   "ID": 1272,
   "Joke": "Difference between a dead squirrel and a dead drummer in the road? http://imgur.com/PKibj The squirrel might have been on his way to a gig."
 },
 {
   "ID": 1273,
   "Joke": "By shear coincidence... ...all these sheep look the same..."
 },
 {
   "ID": 1274,
   "Joke": "Finally decided on my thesis paper. It's a LOTR themed essay in defense of Sauron Titled \"Getting away with Mordor\""
 },
 {
   "ID": 1275,
   "Joke": "What do you call a bee from the wrong side of town? A bumblegee"
 },
 {
   "ID": 1276,
   "Joke": "Why did Mrs. Grape leave Mr. Grape? She was tired of raisin kids."
 },
 {
   "ID": 1277,
   "Joke": "What does batman take in his whiskey? Just ice."
 },
 {
   "ID": 1278,
   "Joke": "What do you call a boomerang that doesn't come back? A Stick"
 },
 {
   "ID": 1279,
   "Joke": "A guy walks into a bar Ouch"
 },
 {
   "ID": 1280,
   "Joke": "Why did the scale decide that the scam artists were heavier than the novels? Because the cons outweighed the prose."
 },
 {
   "ID": 1281,
   "Joke": "Im trying to get into classical music... ...but I cant find any original recordings. All the music is performed by cover bands."
 },
 {
   "ID": 1282,
   "Joke": "What did aged mother cheddar say to her son the day of school photos? Looking sharp."
 },
 {
   "ID": 1283,
   "Joke": "Why does a chicken coop have two doors? Because if it had four it would be a chicken sedan!"
 },
 {
   "ID": 1284,
   "Joke": "Note for Santa Dear Santa, Please give me a big fat bank account and a slim body. Please don't mix those two up like you did last year. Thanks."
 },
 {
   "ID": 1285,
   "Joke": "Why was Pavlov's hair so soft? He conditioned it."
 },
 {
   "ID": 1286,
   "Joke": "What's an atheist's favorite Christmas movie? Coincidence on 34th Street"
 },
 {
   "ID": 1287,
   "Joke": "What do you call someone who makes a lot of money through deforestation of the Amazon? A Brazillionaire!"
 },
 {
   "ID": 1288,
   "Joke": "Whats Marios favorite type of jeans? denim denim denim!"
 },
 {
   "ID": 1289,
   "Joke": "What did the 0 say to the 8? Let's make a snowman!"
 },
 {
   "ID": 1290,
   "Joke": "Have a very Joseph Christmas! We shouldn't discriminate by sex, you know."
 },
 {
   "ID": 1291,
   "Joke": "Never try to kill a termite with a napkin. It'll only get bigger."
 },
 {
   "ID": 1292,
   "Joke": "What did one nose say when the other nose said \"I love you\"? \"Back achoo!\""
 },
 {
   "ID": 1293,
   "Joke": "Hope you guys like clean humor videos https://www.youtube.com/watch?v=kNt-aTq0hxM"
 },
 {
   "ID": 1294,
   "Joke": "Why don't blind people like to skydive? Because it scares the dog."
 },
 {
   "ID": 1295,
   "Joke": "Two guys walk into a bar... the third one ducks."
 },
 {
   "ID": 1296,
   "Joke": "What did the french butter say when it got stocked in the cooler? Beurre... I came up with this today while grocery shopping. I'm ridiculously pleased with myself."
 },
 {
   "ID": 1297,
   "Joke": "Why did the dog sleep on the chandelier? Because he was a light sleeper."
 },
 {
   "ID": 1298,
   "Joke": "What happens when a spoon and fork get into a fight? civilwar"
 },
 {
   "ID": 1299,
   "Joke": "My grandma refused to be an organ donor. She was buried with all of her musical instruments."
 },
 {
   "ID": 1300,
   "Joke": "How do you count cows? With a cowculator."
 },
 {
   "ID": 1301,
   "Joke": "I dig, she dig, we dig, he dig, they dig, you dig ... Maybe not a funny joke but at least it is deep."
 },
 {
   "ID": 1302,
   "Joke": "What do you call a burial chamber full of Moose? Moosoleum."
 },
 {
   "ID": 1303,
   "Joke": "Mints I was eating mint chocolates and I felt sick after eight."
 },
 {
   "ID": 1304,
   "Joke": "A Polar Bear walks into a cafe He says, \"I'll have a burger and.... a coke.\" The waitress says, \"Okay. But, why the long pause?\" The bear says, \"I don't know. I was born with them.\""
 },
 {
   "ID": 1305,
   "Joke": "What did the hot dogs name their child? Frank"
 },
 {
   "ID": 1306,
   "Joke": "I may be middle-class, but I'm hard. *Al dente*, you might say. **Jimmy Carr**"
 },
 {
   "ID": 1307,
   "Joke": "What do you say when you see three whales? Whale whale whale, what do we have here?"
 },
 {
   "ID": 1308,
   "Joke": "What did Cinderella say while waiting for her photos? Someday my prints will come"
 },
 {
   "ID": 1309,
   "Joke": "What did the fish say when it hit the concrete wall? Dam"
 },
 {
   "ID": 1310,
   "Joke": "My Bucket List * ~~Five gallon bucket~~ * ~~Mop bucket~~ * Bucket hat"
 },
 {
   "ID": 1311,
   "Joke": "What do you call an old soldier who has been sprinkled in salt and pepper? A seasoned veteran."
 },
 {
   "ID": 1312,
   "Joke": "The fast food restaurant for babies. \"Welcome to Gerber King, may I take your order?\""
 },
 {
   "ID": 1313,
   "Joke": "What did one frog say to the other? Time's fun when you're having flies."
 },
 {
   "ID": 1314,
   "Joke": "What do you get when you cross the Atlantic with the Titanic? Halfway."
 },
 {
   "ID": 1315,
   "Joke": "Want to hear a dirty joke? This boy trips and falls into some mud."
 },
 {
   "ID": 1316,
   "Joke": "No matter how much you push the envelope... ...it's still stationery."
 },
 {
   "ID": 1317,
   "Joke": "My buddy went to a foreign country to get his sex change operation. Now he's a dude who's abroad."
 },
 {
   "ID": 1318,
   "Joke": "A vampire stopped coming to my nightly poker games. All I said was that he made too many mistakes..."
 },
 {
   "ID": 1319,
   "Joke": "What's the most beautiful thing in Advanced Physics? A passing grade. :)"
 },
 {
   "ID": 1320,
   "Joke": "I bought a vacuum cleaner six months ago... ...and so far, all it's been doing is gathering dust."
 },
 {
   "ID": 1321,
   "Joke": "Where do you drown a hipster? The Mainstream."
 },
 {
   "ID": 1322,
   "Joke": "What did the mama cow say to the baby cow? (x-post from /r/3amjokes) [It's pasture bedtime!](http://www.reddit.com/r/3amjokes/comments/1y8d67/what_did_the_mama_cow_say_to_the_baby_cow/)"
 },
 {
   "ID": 1323,
   "Joke": "Why did the man with one hand cross the road? To get to the second hand shop!"
 },
 {
   "ID": 1324,
   "Joke": "An invisible man marries an invisible woman... The kids were nothing to look at either."
 },
 {
   "ID": 1325,
   "Joke": "What did the creepy scientist say to his new creepy wife? Let's grow MOLD together!"
 },
 {
   "ID": 1326,
   "Joke": "Never trust an atom They make up everything"
 },
 {
   "ID": 1327,
   "Joke": "When you cook duck you should always add a little bit of goose It makes a game out of every bite."
 },
 {
   "ID": 1328,
   "Joke": "A pair of mittens says to a hat, \"I'll stay here, you go on a head\""
 },
 {
   "ID": 1329,
   "Joke": "What is black, bitter and dont work worth a damn? Decaf coffee"
 },
 {
   "ID": 1330,
   "Joke": "Knock, Knock... Who's there? Peas. Peas who? *Peas pass the butter*"
 },
 {
   "ID": 1331,
   "Joke": "My \"go to\" zoo joke I tell this to my wife and kids every time we go to a zoo... Q. What do you get when you cross an elephant with a rhino? A. Elephino"
 },
 {
   "ID": 1332,
   "Joke": "Why did the chicken cross the road half-way? She wanted to lay it on the line."
 },
 {
   "ID": 1333,
   "Joke": "I knew this guy who was so dumb... he saw a road sign that said, \"Disney Land Left\", so he turned around and went home."
 },
 {
   "ID": 1334,
   "Joke": "I'm not really sure I'm understanding this financial crisis in Greece... It's all Greek to me."
 },
 {
   "ID": 1335,
   "Joke": "What happened when porky pig fell asleep at his construction job? The foreman fired him, saying, 'We can't have bored boars boring boards.'"
 },
 {
   "ID": 1336,
   "Joke": "Did you hear about that spicy knight? Sir Acha."
 },
 {
   "ID": 1337,
   "Joke": "What did the Buddhist say to the hot dog vendor? Make me one with everything."
 },
 {
   "ID": 1338,
   "Joke": "What do you call a cow with no legs? Ground beef."
 },
 {
   "ID": 1339,
   "Joke": "There once was a girl from Nantucket... Who carried her ice in a bucket. She walked down a hill. She had a great spill. And when she got up, she said, \"I'm going to watch my step next time!\""
 },
 {
   "ID": 1340,
   "Joke": "Why are bears so hairy ? They don't have salons in the jungle !"
 },
 {
   "ID": 1341,
   "Joke": "How many tickles does it take to make an octopus laugh? ten-tickles"
 },
 {
   "ID": 1342,
   "Joke": "Which is faster, hot or cold? Hot is faster. Anyone can catch a cold."
 },
 {
   "ID": 1343,
   "Joke": "Do you think George Clooney has an iTunes playlist called Clooney Tunes?"
 },
 {
   "ID": 1344,
   "Joke": "I was going to go to a clairvoyants meeting the other day but.... it was cancelled due to unforeseen events."
 },
 {
   "ID": 1345,
   "Joke": "Joke request Tell me your best joke that includes \"July\" \"fourth\" and \"fire\" Let's see what you've got, Reddit!"
 },
 {
   "ID": 1346,
   "Joke": "What is black, white, and red all over? A Communist Propaganda film from the 1930s."
 },
 {
   "ID": 1347,
   "Joke": "[OC c/o my 9 y.o.] What holds up a bowl's pants? Suspoonders!"
 },
 {
   "ID": 1348,
   "Joke": "I don't like going to funerals early in the day. I'm not much of a mourning person."
 },
 {
   "ID": 1349,
   "Joke": "What happens when breed a shark and snowman? You get a frostbite!"
 },
 {
   "ID": 1350,
   "Joke": "Which letter of the alphabet is the laziest? letter G (lethargy)"
 },
 {
   "ID": 1351,
   "Joke": "whats brown and sticky? a stick!"
 },
 {
   "ID": 1352,
   "Joke": "Which day do chickens fear most? Fryday."
 },
 {
   "ID": 1353,
   "Joke": "What did the knob say to the door? I LOCK you a lot! yep, its corny, indeed, but... I'm tryin'! ~Skip"
 },
 {
   "ID": 1354,
   "Joke": "Shout out to... ...baseball players who have three strikes."
 },
 {
   "ID": 1355,
   "Joke": "why do they call them light bulbs? they don't weigh very much"
 },
 {
   "ID": 1356,
   "Joke": "What's a reporter's favorite food? Ice cream because they always want a scoop!"
 },
 {
   "ID": 1357,
   "Joke": "Why did the scarecrow win the Nobel prize? He was outstanding in his field."
 },
 {
   "ID": 1358,
   "Joke": "Is your refrigerator running? Well, you better get glasses, and stop doing drugs"
 },
 {
   "ID": 1359,
   "Joke": "A stamp collector walks into a bar... He walks up to the hostess and says, \"You're more beautiful than any stamp in my collection\" She replied, \"Philately will get you nowhere.\""
 },
 {
   "ID": 1360,
   "Joke": "I personally don't believe in bros before hoes or hoes before hoes.. There needs to be a balance. A homie-hoe-stasis"
 },
 {
   "ID": 1361,
   "Joke": "How do you fix a broken pumpkin? With a pumpkin patch!"
 },
 {
   "ID": 1362,
   "Joke": "My dad's not an alcoholic... ...He just collects empty bottles, sounds so much better, doesn't it? ~ Stewart Francis"
 },
 {
   "ID": 1363,
   "Joke": "I believe a lot of conflict in the Wild West could have been avoided completely... ...if cowboy architects had just made their towns big enough for everyone."
 },
 {
   "ID": 1364,
   "Joke": "Q) What do you call a group of 8 rabbits? A) Rabbyte!"
 },
 {
   "ID": 1365,
   "Joke": "What is a bacteria's OTHER favorite dish? The PETRI dish!"
 },
 {
   "ID": 1366,
   "Joke": "What do you call a productive Asian? China get something done."
 },
 {
   "ID": 1367,
   "Joke": "Why do ghosts carry tissues? Because they have BOOOOgers."
 },
 {
   "ID": 1368,
   "Joke": "Two pretzels.. Two pretzels went walking down the street, one was \"assaulted\""
 },
 {
   "ID": 1369,
   "Joke": "What is the Sun's favorite candy? Starburst! Another one from my 9 year old. I don't know where he gets it."
 },
 {
   "ID": 1370,
   "Joke": "I just met someone who was a steam-roller operator. He was such a flatterer."
 },
 {
   "ID": 1371,
   "Joke": "Why did the chicken cross the road? To get away from Gordon ramsey"
 },
 {
   "ID": 1372,
   "Joke": "What did the turkey say to the turkey hunter? \"Quack, quack, quack.\""
 },
 {
   "ID": 1373,
   "Joke": "What is the difference between a man and a cat? One eats a lot, is lazy and doesnt care who brings the food. The other is a pet."
 },
 {
   "ID": 1374,
   "Joke": "How do you confuse a fish? You put it in a bowl and tell it go to a corner!"
 },
 {
   "ID": 1375,
   "Joke": "Have you guys ever heard of the crazy Mexican Train Killer? He had...... Loco Motives"
 },
 {
   "ID": 1376,
   "Joke": "Do you know why there's no casinos in Africa? Because there's too many CHEETAHS!"
 },
 {
   "ID": 1377,
   "Joke": "what did the zero say to the eight? nice belt"
 },
 {
   "ID": 1378,
   "Joke": "They laughed when I said I wanted to be a comedian. Well, no ones laughing now."
 },
 {
   "ID": 1379,
   "Joke": "I just heard because of the government shutdown government archeologists are working with a skeleton crew."
 },
 {
   "ID": 1380,
   "Joke": "Why do abcdefghijklmopqrstuvwxy &amp; z hate hanging out with the letter n? Because n always has to be the center of attention."
 },
 {
   "ID": 1381,
   "Joke": "Why couldn't Bach pay for his dinner? Because he was Baroque."
 },
 {
   "ID": 1382,
   "Joke": "What is the difference... What is the difference between unlawful and illegal? One is against the law and the other is a sick bird."
 },
 {
   "ID": 1383,
   "Joke": "What did one ocean say to the other? Nothing, they just waved."
 },
 {
   "ID": 1384,
   "Joke": "What's made of brass and sounds like Tom Jones? Trombones!"
 },
 {
   "ID": 1385,
   "Joke": "Why did the Wise Man get 25 to life? Myrrhder"
 },
 {
   "ID": 1386,
   "Joke": "What do you call a dinosaur FBI agent? A pteredacted."
 },
 {
   "ID": 1387,
   "Joke": "What did the fish say when it ran into the wall? Dam"
 },
 {
   "ID": 1388,
   "Joke": "16 sodium atoms walk into a bar followed by Batman."
 },
 {
   "ID": 1389,
   "Joke": "What's the difference between a poorly dressed man on a tricycle and a well dessed man on a bicycle? Attire...!!"
 },
 {
   "ID": 1390,
   "Joke": "What did the pilot say when his plane wasn't flying? \"Aw man, that's a drag.\""
 },
 {
   "ID": 1391,
   "Joke": "I asked my soap who it voted for, it said... I'd lather not say! note: This one came to me in the shower just now, gotta go back in now. Oh, the irony! I think. ~Skip"
 },
 {
   "ID": 1392,
   "Joke": "Why did the coffee file a police report? Because it was mugged."
 },
 {
   "ID": 1393,
   "Joke": "How does the man in the moon cut his hair? Eclipse it."
 },
 {
   "ID": 1394,
   "Joke": "How did the burglar get into the house? Intruder window"
 },
 {
   "ID": 1395,
   "Joke": "Two chimps are in the bath One says \"ooh oooh eek eek\" The other one says \"well put some cold water in then!\""
 },
 {
   "ID": 1396,
   "Joke": "What do ducks do at Christmas time? They duckerate cookies."
 },
 {
   "ID": 1397,
   "Joke": "What do you call a dead fly? a flew"
 },
 {
   "ID": 1398,
   "Joke": "Knock knock. Who's there? Interrupting cow. Interrup........ MOOOOOOOOOOOOOOOO!!!! [Works best IRL](/spoiler)"
 },
 {
   "ID": 1399,
   "Joke": "What di you call a snowman in may? A puddle!"
 },
 {
   "ID": 1400,
   "Joke": "What do you call a white supremacist who doesn't eat meat? A vegitaryan"
 },
 {
   "ID": 1401,
   "Joke": "How is a rabbit similar to a plum? they are both purple, except for the rabbit."
 },
 {
   "ID": 1402,
   "Joke": "Why are there no midget accountants? They always come up short."
 },
 {
   "ID": 1403,
   "Joke": "What do you call a noisy Chinese dog? How-Ling (my dad wanted me to post this)"
 },
 {
   "ID": 1404,
   "Joke": "Why can't you hear a pterodactyl in the bathroom ... because the \"p\" is silent"
 },
 {
   "ID": 1405,
   "Joke": "How did the Pillsbury Dough Boy Die? A Yeast Infection"
 },
 {
   "ID": 1406,
   "Joke": "What do you call a native american cook a sioux chef"
 },
 {
   "ID": 1407,
   "Joke": "I said bring your coffee maker whenever you want Them: great headphones on planes is heavier than flying over TEAs"
 },
 {
   "ID": 1408,
   "Joke": "A poem for Valentine's day Roses are red Poppies are red The grass is red Oh no my yard is on fire"
 },
 {
   "ID": 1409,
   "Joke": "What did the dad buffalo say when his offspring left for college? Bison"
 },
 {
   "ID": 1410,
   "Joke": "How do you get Pikachu on the bus? Poke 'em on!"
 },
 {
   "ID": 1411,
   "Joke": "Whats brown and sticky? a stick"
 },
 {
   "ID": 1412,
   "Joke": "What do you call a fish that operates on brains? A brain sturgeon."
 },
 {
   "ID": 1413,
   "Joke": "The reason angels can fly... ...is that they take themselves lightly. **G. K. Chesterton**"
 },
 {
   "ID": 1414,
   "Joke": "I'm in the terminator musical. I'll be Bach."
 },
 {
   "ID": 1415,
   "Joke": "I try not to spend too much time online... ...but Wi-Fight it?"
 },
 {
   "ID": 1416,
   "Joke": "What does December have that other months dont have? The letter D."
 },
 {
   "ID": 1417,
   "Joke": "What's the best way to capitalize on an opportunity? ON AN OPPORTUNITY"
 },
 {
   "ID": 1418,
   "Joke": "What's green, fuzzy, and if it falls out of a tree it'll kill you? A pool table."
 },
 {
   "ID": 1419,
   "Joke": "A termite walks into a bar... And asks the nearest person \"Hey, is the bar tender here?\""
 },
 {
   "ID": 1420,
   "Joke": "I tired playing soccer But I couldn't get a kick out of it."
 },
 {
   "ID": 1421,
   "Joke": "What did the priest say when watering his garden? Let us spray."
 },
 {
   "ID": 1422,
   "Joke": "How did the musician catch his fish? He castanet"
 },
 {
   "ID": 1423,
   "Joke": "What do you call a plastic sheep? Lambinated!"
 },
 {
   "ID": 1424,
   "Joke": "I need this plant to grow. Well, water you waiting for?"
 },
 {
   "ID": 1425,
   "Joke": "Book, you look so much thinner! I know! I had my appendix removed!"
 },
 {
   "ID": 1426,
   "Joke": "Have you been injured in a car accident? call 555-bottom-feeders. We will do anything for money."
 },
 {
   "ID": 1427,
   "Joke": "Did you hear about the stallion and the mare? They had a stable relationship."
 },
 {
   "ID": 1428,
   "Joke": "What are two doctors with colds An ironic Paradox."
 },
 {
   "ID": 1429,
   "Joke": "What do you get when you cross Kansas with a vulture? Carrion my wayward son"
 },
 {
   "ID": 1430,
   "Joke": "How do you know it's time to go to bed? Hitler is raping you!"
 },
 {
   "ID": 1431,
   "Joke": "What do you call a Romanian grocery clerk? Scanthesku"
 },
 {
   "ID": 1432,
   "Joke": "What do you call a fear of horned bovines? Aurochnophobia."
 },
 {
   "ID": 1433,
   "Joke": "What haircut did the Texan barber recommend when asked? He couldn't think of anything, and said \"I'll mullet over\""
 },
 {
   "ID": 1434,
   "Joke": "[OC] How does Gandhi measure passive resistance? In oooooohms."
 },
 {
   "ID": 1435,
   "Joke": "Why is Kim Jong Un like todays music? They both ain't got the same Seoul."
 },
 {
   "ID": 1436,
   "Joke": "I knew this guy who would ask men at church, \"is your tie made out of bird cloth?\" &lt;blank stare&gt; \"It's cheep, cheep, cheep.\""
 },
 {
   "ID": 1437,
   "Joke": "What happened when the carrot died? There was a huge turnip at the funeral."
 },
 {
   "ID": 1438,
   "Joke": "Why can't you hear a pterodactyl go to the bathroom? Because the P is silent"
 },
 {
   "ID": 1439,
   "Joke": "Why do librarians like the wind? It says, \"Shhh!\" all day!"
 },
 {
   "ID": 1440,
   "Joke": "One potato asks another: -\"Are you sure we are related?\" -\"Yes I yam!\""
 },
 {
   "ID": 1441,
   "Joke": "I like my slaves like I like my coffee Free."
 },
 {
   "ID": 1442,
   "Joke": "Who is the only superhuman Frozone can't deal with? Thor."
 },
 {
   "ID": 1443,
   "Joke": "Why don't bears wear boots? Cos they like to walk around in their bear feet."
 },
 {
   "ID": 1444,
   "Joke": "There's 10 kind of people in the world. Those who know binary and those who don't."
 },
 {
   "ID": 1445,
   "Joke": "What do you call the object Attila the Hun uses to brush his leg hair? A Hun knee comb."
 },
 {
   "ID": 1446,
   "Joke": "Words can't possibly describe how beautiful you are... But numbers can 4/10"
 },
 {
   "ID": 1447,
   "Joke": "What are twins favorite fruits? Pears"
 },
 {
   "ID": 1448,
   "Joke": "Did you hear about the guy who fell into an upholstery machine? Now he's fully recovered."
 },
 {
   "ID": 1449,
   "Joke": "Why did the chicken cross the road? To get to the moron's house. *knock knock* ^^Whose ^^there? *the chicken...*"
 },
 {
   "ID": 1450,
   "Joke": "Why did the wave fail the driving test? It kept crashing on the beach."
 },
 {
   "ID": 1451,
   "Joke": "What did one earthquake say to the other? Hey, it's not my fault."
 },
 {
   "ID": 1452,
   "Joke": "I bought some shoes from a drug dealer, I don't know what he laced them with but I have been tripping all day. --My amazing girlfriend told me this one"
 },
 {
   "ID": 1453,
   "Joke": "Request: Jokes for the sick? I have a good friend who was just hospitalized, hopefully nothing too serious. I'd love to send him a few short, clean jokes to cheer him up. Thanks!"
 },
 {
   "ID": 1454,
   "Joke": "Why would no one listen to the percussion section? Because they couldn't drum up enough support."
 },
 {
   "ID": 1455,
   "Joke": "What kind of bee can never be understood? A mumble-bee."
 },
 {
   "ID": 1456,
   "Joke": "What's the difference between Botox and Borax? Two letters."
 },
 {
   "ID": 1457,
   "Joke": "A broom only likes one brand of comedy. Dustpan."
 },
 {
   "ID": 1458,
   "Joke": "If you bury someone in the wrong place then you have made a grave mistake."
 },
 {
   "ID": 1459,
   "Joke": "A man walks into a fancy dress party carrying a woman on his back... The host asks the man why this is so. \"Oh, I'm a tortoise and this is Michelle\" says the man."
 },
 {
   "ID": 1460,
   "Joke": "There's only one problem with reading articles about space based technology It all goes waaaay over my head."
 },
 {
   "ID": 1461,
   "Joke": "Pac-Man What should you do before you criticize Pac-Man? WAKA WAKA WAKA mile in his shoes."
 },
 {
   "ID": 1462,
   "Joke": "What does a bag of rice and an onion do when they get into a fast car? They pilaf. I'll show my way out"
 },
 {
   "ID": 1463,
   "Joke": "Want to hear a joke about pizza? Never mind it is too cheesy."
 },
 {
   "ID": 1464,
   "Joke": "What did the Triangle say to the Circle? \"Your life is pointless.\""
 },
 {
   "ID": 1465,
   "Joke": "HELP! We need your best joke you have! We will choose the best joke and make a video of it, just for you!"
 },
 {
   "ID": 1466,
   "Joke": "I heard a great joke about a boomerang earlier. I'm sure it will come back to me eventually."
 },
 {
   "ID": 1467,
   "Joke": "What did the pony say when he had a sore throat? Pardon me, I'm just a little hoarse."
 },
 {
   "ID": 1468,
   "Joke": "I'm good friends with 25 letters of the alphabet... I don't know why."
 },
 {
   "ID": 1469,
   "Joke": "What's pink and fluffy? Pink fluff. Whats blue and fluffy? Pink fluff holding its breath"
 },
 {
   "ID": 1470,
   "Joke": "What's Sam Smith's favorite type of nut?  [It's an alllllllllmond](https://www.youtube.com/watch?v=fB63ztKnGvo&amp;feature=youtu.be&amp;t=37s)"
 },
 {
   "ID": 1471,
   "Joke": "What did the koala bear say to the barber? You ca-lip this?"
 },
 {
   "ID": 1472,
   "Joke": "What city loves to eat sandwiches? Koldcutta"
 },
 {
   "ID": 1473,
   "Joke": "Why aren't sumos chummy with racecar drivers? They move in different circles."
 },
 {
   "ID": 1474,
   "Joke": "What do you call shaving a crazy sheep? Shear madness."
 },
 {
   "ID": 1475,
   "Joke": "Why don't tennis players get married? Because to them love means nothing."
 },
 {
   "ID": 1476,
   "Joke": "What do you call a fake noodle? An Impasta"
 },
 {
   "ID": 1477,
   "Joke": "I thought I had a brain tumor but then I realized it was all in my head."
 },
 {
   "ID": 1478,
   "Joke": "Did you know that 1 in every doll, in every doll, in every doll, in every doll are Russian?"
 },
 {
   "ID": 1479,
   "Joke": "Today's my cake day! And I'm going to eat it too!"
 },
 {
   "ID": 1480,
   "Joke": "How do you kill a vampire from the South? With a chicken fried stake"
 },
 {
   "ID": 1481,
   "Joke": "You can pick your friends, and you can pick your nose... But you can't pick your friend's nose"
 },
 {
   "ID": 1482,
   "Joke": "Two atoms walk into a bar... One says, \"Oh no, I've lost an electron.\" The other asks, \"Are you sure?\" \"Yeah, I'm positive!\""
 },
 {
   "ID": 1483,
   "Joke": "What is robot jazz called? Beep Boop Bop!"
 },
 {
   "ID": 1484,
   "Joke": "My Girlfriend told me she didn't want anything for Birthday I didn't give her anything :O #ThugLife"
 },
 {
   "ID": 1485,
   "Joke": "What have you got if your pet kangaroo gets into molasses and Indian curry? An Indian goo roo"
 },
 {
   "ID": 1486,
   "Joke": "I would think you'd have to be open minded... ...to be a brain surgeon."
 },
 {
   "ID": 1487,
   "Joke": "I fell off a forty foot ladder today.... lucky I was on the bottom rung."
 },
 {
   "ID": 1488,
   "Joke": "Where did Napoleon Bonaparte keep his armies? In his sleevies."
 },
 {
   "ID": 1489,
   "Joke": "what did socrates learn from the T-rex? i dino"
 },
 {
   "ID": 1490,
   "Joke": "Why do ducks have webbed feet? To stomp out fires. Why do elephants have flat feet? To stomp out the burning ducks."
 },
 {
   "ID": 1491,
   "Joke": "What do cows like on their hotdogs? MOOstard."
 },
 {
   "ID": 1492,
   "Joke": "Broom advocates for cleaner work environment."
 },
 {
   "ID": 1493,
   "Joke": "I was watching a TV program on various Religious orders and how the use stringed instruments. I was appalled by the amount of sects and violins!"
 },
 {
   "ID": 1494,
   "Joke": "If you give a mouse a cookie.. If you give a mouse a cookie.. Why are you giving a mouse any food? That's unsanitary."
 },
 {
   "ID": 1495,
   "Joke": "What happens if you pass gas in church? You have to sit in your own pew."
 },
 {
   "ID": 1496,
   "Joke": "Whats the best thing to put into a pie? Your teeth!"
 },
 {
   "ID": 1497,
   "Joke": "I have to find a new personal trainer. He didn't do squat(s)."
 },
 {
   "ID": 1498,
   "Joke": "Wanna hear a dirty joke? A white horse fell in a mud puddle."
 },
 {
   "ID": 1499,
   "Joke": "A funny bird is the pelican His beak can hold more than his belly can He can hold in his beak Enough for a week And I don't know how the heck he can!"
 },
 {
   "ID": 1500,
   "Joke": "Where do dinosaurs get their pickles from? Vlasic Park"
 },
 {
   "ID": 1501,
   "Joke": "What's the difference between a fish and a guitar? You can't tuna fish!"
 },
 {
   "ID": 1502,
   "Joke": "What do you call two crows? Attempted murder."
 },
 {
   "ID": 1503,
   "Joke": "What do you call a t-shirt with stalks of wheat on it? A crop top!"
 },
 {
   "ID": 1504,
   "Joke": "What do you call a cow with 2 legs? Lean beef."
 },
 {
   "ID": 1505,
   "Joke": "What is the scientific name for a crippled tyrannosaurus rex ? Tywalkasoreus Rex"
 },
 {
   "ID": 1506,
   "Joke": "What type pf culture is most peaceful and never gets angry? Nomads!"
 },
 {
   "ID": 1507,
   "Joke": "I tried to change my password to 14days... The computer said it was two week."
 },
 {
   "ID": 1508,
   "Joke": "2 fish in a tank, one says to the other Do you know how to drive this thing?"
 },
 {
   "ID": 1509,
   "Joke": "Knock knock - Who's there? - Impatient cow. - Impatient co- - He already left."
 },
 {
   "ID": 1510,
   "Joke": "Why were the Libyans eating money? They were having dinar."
 },
 {
   "ID": 1511,
   "Joke": "Why can't you hear it when a pteranodon goes to the bathroom? Because they're all dead."
 },
 {
   "ID": 1512,
   "Joke": "why was the rabbit promoted to brewmaster? All his beers had a lot of hops"
 },
 {
   "ID": 1513,
   "Joke": "What is Captain Ahab's favorite reggae band? Bob Marley and The Whalers!"
 },
 {
   "ID": 1514,
   "Joke": "Where did the mistletoe go to become rich and famous? Hollywood."
 },
 {
   "ID": 1515,
   "Joke": "bad scary film I was watching a really poorly done scary movie last night, it was horrorble."
 },
 {
   "ID": 1516,
   "Joke": "What did batman say to robin before robin got in the car? get in the car"
 },
 {
   "ID": 1517,
   "Joke": "Why did the strawberry go out with the pineapple? Because he couldn't get a date!"
 },
 {
   "ID": 1518,
   "Joke": "Why did the buddhist refuse novocaine when he went to get a tooth pulled? He wanted to transcend dental medication."
 },
 {
   "ID": 1519,
   "Joke": "What happens when you don't serve drinks at a party? There's no punch line."
 },
 {
   "ID": 1520,
   "Joke": "I just read this article about short term memory I don't remember what it was about"
 },
 {
   "ID": 1521,
   "Joke": "Did you hear about the farmer that fell into the field machine and lost half his body? He's all right now! :-)"
 },
 {
   "ID": 1522,
   "Joke": "Accidental Seafood I tried dolphin once...but not on porpoise."
 },
 {
   "ID": 1523,
   "Joke": "Did you hear about the wedding between the two antenna? The service was terrible, but the reception was great."
 },
 {
   "ID": 1524,
   "Joke": "What state do most people live in? Denial. Myself included."
 },
 {
   "ID": 1525,
   "Joke": "whats brown and rhymes with snoop? Dr Dre"
 },
 {
   "ID": 1526,
   "Joke": "Why do space rocks taste better than earth rocks? Because they are a little meteor"
 },
 {
   "ID": 1527,
   "Joke": "What does a hawk call a high ledge A *falcony!*"
 },
 {
   "ID": 1528,
   "Joke": "What did the German policeman say to his nipples? You are under a vest!"
 },
 {
   "ID": 1529,
   "Joke": "Someone talked to me today about having two X chromosomes. Typical woman."
 },
 {
   "ID": 1530,
   "Joke": "If you're American, when are you not American? When European. Or when you're Russian. Any more? :)"
 },
 {
   "ID": 1531,
   "Joke": "A mathematician was constipated, how did he solve his problem? He worked it out with a pencil and paper."
 },
 {
   "ID": 1532,
   "Joke": "What do you call a barbarian you can't see? an Invisigoth."
 },
 {
   "ID": 1533,
   "Joke": "Where did the seaweed... Where did the seaweed find a job? In the \"Kelp Wanted\" section of the want-ads."
 },
 {
   "ID": 1534,
   "Joke": "How many tickles does it take to make an octopus laugh? Ten tickles"
 },
 {
   "ID": 1535,
   "Joke": "Who is the roundest knight at King Arthur's table? Sir Cumference."
 },
 {
   "ID": 1536,
   "Joke": "I know a guy who collects candy canes... ...they are all in mint condition."
 },
 {
   "ID": 1537,
   "Joke": "I'm reading a book about anti-gravity. I can't put it down."
 },
 {
   "ID": 1538,
   "Joke": "Why do the French like eating snails? Because they can't stand fast food!"
 },
 {
   "ID": 1539,
   "Joke": "What does a Jedi say after a tragic loss of life? \"May my thoughts be with them\"."
 },
 {
   "ID": 1540,
   "Joke": "What do you call an alien in a swamp? A MARSHian"
 },
 {
   "ID": 1541,
   "Joke": "Will Smith joke How do you find Will Smith in the snow? You look for fresh prince..."
 },
 {
   "ID": 1542,
   "Joke": "One time, a cow saved my life It was bovine intervention."
 },
 {
   "ID": 1543,
   "Joke": "Why should you always knock before opening the refrigerator? Because there might be an Italian dressing."
 },
 {
   "ID": 1544,
   "Joke": "What did the rubber band factory worker say when he was fired? Oh snap!"
 },
 {
   "ID": 1545,
   "Joke": "Why did the rap battle champion get the most spacious and accessible seat on the bus? Because of his dis-ability."
 },
 {
   "ID": 1546,
   "Joke": "What lies at the bottom of the ocean and twitches? A nervous wreck."
 },
 {
   "ID": 1547,
   "Joke": "We always bought our cars used, this one was as black as the night- -that is, until we washed it!!!"
 },
 {
   "ID": 1548,
   "Joke": "I feed my cat lemons. He's a real sour puss."
 },
 {
   "ID": 1549,
   "Joke": "I thought the dryer shrank my clothes.. turns out it was the refrigerator"
 },
 {
   "ID": 1550,
   "Joke": "I was driving today... And saw a sign that said, \"Steamed Crabs\". I began to wonder: \"What made them so mad?\""
 },
 {
   "ID": 1551,
   "Joke": "My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away."
 },
 {
   "ID": 1552,
   "Joke": "What do you call someone who points out the obvious? Someone who points out the obvious."
 },
 {
   "ID": 1553,
   "Joke": "What do you call a Mexican with a rubber toe? Rubber-Toe! (Roberto)"
 },
 {
   "ID": 1554,
   "Joke": "What do you call the ultimate fish doctor? The Sturgeon General"
 },
 {
   "ID": 1555,
   "Joke": "How did the firefly feel when he flew into the fan? He was de-lighted"
 },
 {
   "ID": 1556,
   "Joke": "Why couldn't the pony sing? He was a little horse."
 },
 {
   "ID": 1557,
   "Joke": "What did the horse say when he fell over? \"Help! I've fallen and I can't giddy up.\""
 },
 {
   "ID": 1558,
   "Joke": "What happens when you steamroll Batman and Robin? They become flatman and ribbon."
 },
 {
   "ID": 1559,
   "Joke": "Why did the melon try so hard to get her father's approval? Because she cant-aloupe"
 },
 {
   "ID": 1560,
   "Joke": "My girl asks why I love chocolate so much. Well, I have several Reisens..."
 },
 {
   "ID": 1561,
   "Joke": "I finally finished baby proofing the house. Let's see those babies get in here now."
 },
 {
   "ID": 1562,
   "Joke": "My friend says she's doing good but she means well"
 },
 {
   "ID": 1563,
   "Joke": "Why does Snoop Dogg use an umbrella? For Drizzle"
 },
 {
   "ID": 1564,
   "Joke": "What do vegan zombies eat? Graaaaains!"
 },
 {
   "ID": 1565,
   "Joke": "Schooner or later, sailors... ...engage in rudder nonsense."
 },
 {
   "ID": 1566,
   "Joke": "What's a pirate's favorite letter? The C."
 },
 {
   "ID": 1567,
   "Joke": "What happened to the butched after he backed into the meat grinder? he got a little \"behind\" in his work"
 },
 {
   "ID": 1568,
   "Joke": "I still remember what my grandpa said before he kicked the bucket... \"How far do you think I can kick this bucket?!\""
 },
 {
   "ID": 1569,
   "Joke": "Knock knock -Who's there? Ash -Ash who? Bless you.. P.S. kids love it"
 },
 {
   "ID": 1570,
   "Joke": "What do you call a singing laptop? A Dell"
 },
 {
   "ID": 1571,
   "Joke": "If all of Ireland sank, what part of it wouldn't? County Cork"
 },
 {
   "ID": 1572,
   "Joke": "Knock knock! **Who's there?** *Tank* **Tank who?** *You're welcome*"
 },
 {
   "ID": 1573,
   "Joke": "This Post just says it all! It all."
 },
 {
   "ID": 1574,
   "Joke": "What kind of music does a printer make? A paper jam."
 },
 {
   "ID": 1575,
   "Joke": "My friend's bakery burned down last night. Now his business is toast."
 },
 {
   "ID": 1576,
   "Joke": "Why did the superhero make a lot of shredded cheese? It was for the grater good."
 },
 {
   "ID": 1577,
   "Joke": "What mysterious hair product does Lucifer use to keep himself looking good? Arcane-gel!"
 },
 {
   "ID": 1578,
   "Joke": "Overheard: Augustus Caesar on New Year's Day: \"I keep writing 'B.C.' on all my checks.\""
 },
 {
   "ID": 1579,
   "Joke": "What did the mom say to her son when he said he didn't want any of her flippin' pancakes? Fine. They will just be burnt on one side."
 },
 {
   "ID": 1580,
   "Joke": "What has more letters than the alphabet? The post office."
 },
 {
   "ID": 1581,
   "Joke": "You can tune a guitar... but you can't tuna fish!"
 },
 {
   "ID": 1582,
   "Joke": "What has two arms and 14 legs? Guy who collects legs."
 },
 {
   "ID": 1583,
   "Joke": "How does a penguin build its house? Igloos it together!"
 },
 {
   "ID": 1584,
   "Joke": "Why didn't Silento knock before coming inside? Because you already know who it's isss! My little sister told me this joke."
 },
 {
   "ID": 1585,
   "Joke": "[My Joke] Where do noodles get their nails done? At the spa-getti."
 },
 {
   "ID": 1586,
   "Joke": "What do you call a dog in a diving bell? A sub-woofer"
 },
 {
   "ID": 1587,
   "Joke": "What do you get when you sit on a potato? A potato wedge! (I made this up when I was 9)"
 },
 {
   "ID": 1588,
   "Joke": "Do you guys/gals like horse jokes? Yeah or neeiiigghh?"
 },
 {
   "ID": 1589,
   "Joke": "What did one duck say to the other? Quack!"
 },
 {
   "ID": 1590,
   "Joke": "How did the pilot like his hotdog? Plane."
 },
 {
   "ID": 1591,
   "Joke": "A horse walks into a bar, orders a beer. The bartender says, \"Why the long face?\" And the horse answers, \"They've started a round of layoffs at the plant.\""
 },
 {
   "ID": 1592,
   "Joke": "Why did the Buddhist monk refuse Novocain? Because he wanted to transcend dental medication."
 },
 {
   "ID": 1593,
   "Joke": "Wise man once say... He who runs in front of car will get tired, He who runs behind car will get exhausted."
 },
 {
   "ID": 1594,
   "Joke": "My buddy says he is the world's worst at self-deprecating humor. he worried once he was too modest. Then realized he was wrong."
 },
 {
   "ID": 1595,
   "Joke": "What do you call a dog with no legs? It doesn't matter what you call it, it won't come."
 },
 {
   "ID": 1596,
   "Joke": "I support farming and math... I'm pro-tractor."
 },
 {
   "ID": 1597,
   "Joke": "How do you make a computer your best friend? You buy it a nice bunch of software and get it loaded!"
 },
 {
   "ID": 1598,
   "Joke": "What do you call a dog with no legs? Don't bother, he's not coming."
 },
 {
   "ID": 1599,
   "Joke": "Every journey has a beginning. -ahem- Just a small town girl Living in a lonely world..."
 },
 {
   "ID": 1600,
   "Joke": "What's the difference between a cat and a complex sentence? A cat has claws at the end of its paws. A complex sentence has a pause at the end of its clause."
 },
 {
   "ID": 1601,
   "Joke": "Never play poker with a pieces of paper. They're bound to fold."
 },
 {
   "ID": 1602,
   "Joke": "Why do Hutus hate Dustin Hoffman? He impersonated a Tootsie."
 },
 {
   "ID": 1603,
   "Joke": "A Thanksgiving Joke What did the turkey say about the television program from the 1950s? There's a little bit too much grayvy."
 },
 {
   "ID": 1604,
   "Joke": "What's invisible and smells like carrots? Rabbit farts"
 },
 {
   "ID": 1605,
   "Joke": "What did one wall say to the other wall? I`ll meet you at the corner."
 },
 {
   "ID": 1606,
   "Joke": "What's the most beautiful thing in mathematics? A cute angle"
 },
 {
   "ID": 1607,
   "Joke": "A dog with only 3 legs walks into a saloon in the Old West He slides up to the bar and announces: ''I'm looking for the man who shot my paw.\""
 },
 {
   "ID": 1608,
   "Joke": "I used to be addicted... to the hokey pokey but I turned myself around (x-post from /r/jokes)"
 },
 {
   "ID": 1609,
   "Joke": "The three unwritten rules of /r/cleanjokes are: 1. 2. 3."
 },
 {
   "ID": 1610,
   "Joke": "Why did Beethoven get rid of his chickens? All they said was, Bach, Bach, Bach\""
 },
 {
   "ID": 1611,
   "Joke": "Why does a chicken coup have 2 doors? Because if it had 4 doors, it would be a chicken Sedan."
 },
 {
   "ID": 1612,
   "Joke": "Someone sly sheared sleeping sheep. Talk about shear terror."
 },
 {
   "ID": 1613,
   "Joke": "Did ya hear about the magic tractor? It turned into a field"
 },
 {
   "ID": 1614,
   "Joke": "Why do Java developers wear glasses? Because they don't C#"
 },
 {
   "ID": 1615,
   "Joke": "Just went to an emotional wedding Even the cake was in tiers."
 },
 {
   "ID": 1616,
   "Joke": "Why does Snoop Dog carry and umbrella? Fo-Drizzle"
 },
 {
   "ID": 1617,
   "Joke": "How do you know you put the right joke in the right thread? Don't worry, someone will tell you."
 },
 {
   "ID": 1618,
   "Joke": "What do you call a camel with 3 humps? Humphrey. (I was told this joke by an actual dad, it was his response to one of my jokes)"
 },
 {
   "ID": 1619,
   "Joke": "Two fish in a tank. [x-post from r/Jokes] One asks: How do you drive this thing?"
 },
 {
   "ID": 1620,
   "Joke": "\"Stay strong!\" I said to my wi-fi signal."
 },
 {
   "ID": 1621,
   "Joke": "Why was the tomato blushing? Because it saw the salad dressing!"
 },
 {
   "ID": 1622,
   "Joke": "What is heavy forward but not backward? **ton**"
 }
]

cls = lambda: os.system('cls')

def tell_a_joke():
    selected = random.choice(jokes)
    joke = selected["Joke"]
    entry = joke.split("?")
    if len(entry) > 1:
        question = entry[0]
        answer = entry[1]
        cls()
        print(question + "?")
        time.sleep(8)
        cls()
        print(answer)
        time.sleep(6)
    else:
        cls()
        print(entry[0])
        time.sleep(6)

def main():
    option = input("Hey, wanna hear a joke (yes or no)? ")
    if option == "yes":
        tell_a_joke()
        cls()
        main()
    elif option == "no":
        cls()
        print("Okay, have a nice day!")
        exit()
    else:
        cls()
        ("I'm sorry, was it yes or no?")
        main()



if __name__ == "__main__":
    main()