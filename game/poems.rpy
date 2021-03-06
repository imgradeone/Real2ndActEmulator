#This is a copy of poems.rpy from DDLC.
#Use this as a starting point if you would like to override with your own.

#Poems.rpy defines a poem class, a function for showing them, and all of the
#poems the game shows

#Define a class for Poem with the following fields:
#    author - The name of the author, each has a defined styles
#    title - The title of the poem
#    text - the poem's text as a blockquote
#    yuri_2 - This uses the creepy style for yuri's second act2 poem
#    yuri_3 - This uses Yuri's madness style for her third act2 poem
init python:
    class Poem:
        def __init__(self, author="", title="", text="", yuri_2=False, yuri_3=False):
            self.author = author
            self.title = title
            self.text = text
            self.yuri_2 = yuri_2
            self.yuri_3 = yuri_3

#Define all of the poems
    poem_y1 = Poem(
    author = "yuri",
    title = "Ghost Under the Light",
    text = """\
The tendrils of my hair illuminate beneath the amber glow.
Bathing.
It must be this one.
The last remaining streetlight to have withstood the test of time.
the last yet to be replaced by the sickening blue-green hue of the future.
I bathe. Calm; breathing air of the present but living in the past.
The light flickers.
I flicker back."""
    )

    poem_y2 = Poem(
    author = "yuri",
    title = "The Raccoon",
    text = """\
It happened in the dead of night while I was slicing bread for a guilty snack.
My attention was caught by the scuttering of a raccoon outside my window.
That was, I believe, the first time I noticed my strange tendencies as an unordinary human.
I gave the raccoon a piece of bread, my subconscious well aware of the consequences.
Well aware that a raccoon that is fed will always come back for more.
The enticing beauty of my cutting knife was the symptom.
The bread, my hungry curiosity.
The raccoon, an urge.

The moon increments its phase and reflects that much more light off of my cutting knife.
The very same light that glistens in the eyes of my raccoon friend.
I slice the bread, fresh and soft. The raccoon becomes excited.
Or perhaps I'm merely projecting my emotions onto the newly-satisfied animal.

The raccoon has taken to following me.
You could say that we've gotten quite used to each other.
The raccoon becomes hungry more and more frequently, so my bread is always handy.
Every time I brandish my cutting knife, the raccoon shows me its excitement.
A rush of blood. Classic Pavlovian conditioning. I slice the bread.
And I feed myself again."""
    )

    poem_y3 = Poem(
    author = "yuri",
    title = "Beach",
    text = """\
A marvel millions of years in the making.
Where the womb of Earth chaotically meets the surface.
Under a clear blue sky, an expanse of bliss--
But beneath gray rolling clouds, an endless enigma.
The easiest world to get lost in
Is one where everything can be found.

One can only build a sand castle where the sand is wet.
But where the sand is wet, the tide comes.
Will it gently lick at your foundations until you give in?
Or will a sudden wave send you crashing down in the blink of an eye?
Either way, the outcome is the same.
Yet we still build sand castles.

I stand where the foam wraps around my ankles.
Where my toes squish into the sand.
The salty air is therapeutic.
The breeze is gentle, yet powerful.
I sink my toes into the ultimate boundary line, tempted by the foamy tendrils.
Turn back, and I abandon my peace to erode at the shore.
Drift forward, and I return to Earth forevermore."""
    )

    poem_y3b = Poem(
    author = "yuri",
    title = "Ghost Under the Light pt. 2",
    text = """\
The tendrils of my hair illuminate beneath the amber glow.
Bathing.
In the distance, a blue-green light flickers.
A lone figure crosses its path - a silhouette obstructing the eerie glow.
My heart pounds. The silhouette grows. Closer. Closer.
I open my umbrella, casting a shadow to shield me from visibility.
But I am too late.
He steps into the streetlight. I gasp and drop my umbrella.
The light flickers. My heart pounds. He raises his arm.

Time stops.

The only indication of movement is the amber light flickering against his outstretched arm.
The flickering light is in rhythm with the pounding of my heart.
Teasing me for succumbing to this forbidden emotion.
Have you ever heard of a ghost feeling warmth before?
Giving up on understanding, I laugh.
Understanding is overrated.
I touch his hand. The flickering stops.
Ghosts are blue-green. My heart is amber."""
    )

    poem_y22 = Poem(
    author = "yuri",
    yuri_2 = True,
    title = "Wheel",
    text = """\
A rotating wheel. Turning an axle. Grinding. Bolthead. Linear gearbox. Falling sky. Seven holy stakes. \
A docked ship. A portal to another world. A thin rope tied to a thick rope. A torn harness. Parabolic gearbox. \
Expanding universe. Time controlled by slipping cogwheels. Existence of God. Swimming with open water in all directions. \
Drowning. A prayer written in blood. A prayer written in time-devouring snakes with human eyes. \
A thread connecting all living human eyes. A kaleidoscope of holy stakes. Exponential gearbox. \
A sky of exploding stars. God disproving the existence of God. A wheel rotating in six dimensions. \
Forty gears and a ticking clock. A clock that ticks one second for every rotation of the planet. \
A clock that ticks forty times every time it ticks every second time. A bolthead of holy stakes tied to \
the existence of a docked ship to another world. A kaleidoscope of blood written in clocks. A time-devouring \
prayer connecting a sky of forty gears and open human eyes in all directions. Breathing gearbox. Breathing bolthead. \
Breathing ship. Breathing portal. Breathing snakes. Breathing God. Breathing blood. Breathing holy stakes. \
Breathing human eyes. Breathing time. Breathing prayer. Breathing sky. Breathing wheel."""
    )

    poem_y23 = Poem(
        author = "yuri",
        yuri_3 = True,
        title = "mdpnfbo,jrfp",
        text = """\
ed,,zinger suivante,,tels handknits finish,,cagefuls basinlike bag octopodan,,imboss\
ing vaporettos rorid easygoingnesses nalorphines,,benzol respond washerwomen bris\
tlecone,,parajournalism herringbone farnarkeled,,episodically cooties,,initiallers \
bimetallic,,leased hinters,,confidence teetotaller computerphobes,,pinnacle exotica\
lly overshades prothallia,,posterior gimmickry brassages bediapers countertrades,,\
haslet skiings sandglasses cannoli,,carven nis egomaniacal,,barminess gallivanted,,\
southeastward,,oophoron crumped,,tapued noncola colposcopical,,dolente trebbiano re\
vealment,,outworked isotropous monosynaptic excisional moans,,enterocentesis jacuz\
zi preoccupations,,hippodrome outward googs,,tabbises undulators,,metathesizing,,sha\
ria prepostor,,neuromast curmudgeons actability,,archaise spink reddening miscount\
,,madmen physostigmin statecraft neurocoeles bammed,,tenderest barguests crusados \
trust,,manshifts darzis aerophones,,reitboks discomposingly,,expandors,,monotasking \
galabia,,pertinents expedients witty,,chirographies crachach unsatisfactoriness sw\
erveless,,flawed sepulchred thanksgiver scrawl skug,,perorate stringers gelatine f\
lagstones,,chuses conceptualization surrejoined,,counterblasts rache,,numerative,,de\
lirifacients methylthionine,,mantram dynamist atomised,,eternization percalines hr\
yvnias pragmatizing,,reproachfulnesses telework nowts demoded revealer,,burnettize\
 caryopteris subangular wirricows,,transvestites sinicized narcissus,,hikers meno,,\
degassing,,postcrises alikenesses,,sycophancy seroconverting insure,,yantras raphid\
es cliftiest bosthoon,,zootherapy chlorides nationwide schlub yuri,,timeshares cas\
tanospermine backspaces reincite,,coactions cosignificative palafitte,,poofters su\
bjunctions,,aquarian,,theralite revindicating,,cynosural permissibilities narcotisi\
ng,,journeywork outkissed clarichords troutier,,myopias undiverting evacuations sn\
arier superglue,,deaminise infirmaries teff hebephrenias,,brainboxes homonym lance\
let,,lambitive stray,,inveigled,,acetabulums atenolol,,dekkos scarcer flensed,,abulia\
s flaggers wammul boastfully,,galravitch happies interassociation multipara augme\
ntations,,teratocarcinomata coopting didakai infrequently,,hairtails intricacy usu\
als,,pillorise outrating,,cataphoresis,,furnishings leglen,,goethite deflate butterb\
urs,,phoneticising winiest hyposulphuric campshirts,,chainfalls swimmings roadbloc\
ked redone soliloquies,,broking mendaciousness parasitisms counterworld,,unravelli\
ngs quarries passionately,,onomatopoesis repenting,,ramequin,,mopboard euphuistical\
ly,,volta sycophantized allantoides,,bors bouclees raisings sustaining,,diabolist s\
ticks dole liltingly,,curial bisexualisms siderations hemolysed,,damnabilities unk\
enneling halters,,peripheral congaing,,diatomicity,,foolings repayments,,hereabouts \
vamosed him,,slanters moonrock porridgy monstruous,,heartwood bassoonist predispos\
itions jargoon dominances,,timidest inalienable rewearing inevitably,,entreating r\
etiary tranquillizing,,uniparental droogs,,allotropous,,forzati abiogenetic,,obdurat\
ion exempted unifaces,,epilating calisaya dispiteously coggles,,vestmented flukily\
 ignifying complished hiccupy municipalize,,pentagraphs parcels sutler excavates,,\
stardust miscited thankfulness,,fouter pertused,,overpacks,,guarishes hylotheism,,pi
Fresh blood seeps through the line parting her skin and slowly colors her breast red.\
 I begin to hyperventilate as my compulsion grows. The images won’t go away. Images of\
 me driving the knife into her flesh continuously, fucking her body with the blade, \
making a mess of her. My head starts going crazy as my thoughts start to return. \
Shooting pain assaults my mind along with my thoughts. This is disgusting. Absolutely\
 disgusting. How could I ever let myself think these things? But it’s unmistakable. \
The lust continues to linger through my veins. An ache in my muscles stems from the \
unreleased tension experienced by my entire body. Her Third Eye is drawing me closer."""
    )

    poem_n1 = Poem(
    author = "natsuki",
    title = "Eagles Can Fly",
    text = """\
Monkeys can climb
Crickets can leap
Horses can race
Owls can seek
Cheetahs can run
Eagles can fly
People can try
But that's about it.
"""
    )

    poem_n2 = Poem(
    author = "natsuki",
    title = "Amy Likes Spiders",
    text = """\
You know what I heard about Amy?
Amy likes spiders.
Icky, wriggly, hairy, ugly spiders!
That's why I'm not friends with her.

Amy has a cute singing voice.
I heard her singing my favorite love song.
Every time she sang the chorus, my heart would pound to the rhythm of the words.
But she likes spiders.
That's why I'm not friends with her.

One time, I hurt my leg really bad.
Amy helped me up and took me to the nurse.
I tried not to let her touch me.
She likes spiders, so her hands are probably gross.
That's why I'm not friends with her.

Amy has a lot of friends.
I always see her talking to people.
She probably talks about spiders.
What if her friends start to like spiders too?
That's why I'm not friends with her.

It doesn't matter if she has other hobbies.
It doesn't matter if she keeps it private.
It doesn't matter if it doesn't hurt anyone.

It's gross.
She's gross.
The world is better off without spider lovers.

And I'm gonna tell everyone.
"""
    )

    poem_n2b = Poem(
    author = "natsuki",
    title = "T3BlbiBZb3VyIFRoaXJkIEV5ZQ==",
    text = """\
SSBjYW4gZmVlbCB0aGUgdGVuZGVybmVz
cyBvZiBoZXIgc2tpbiB0aHJvdWdoIHRo
ZSBrbmlmZSwgYXMgaWYgaXQgd2VyZSBh
biBleHRlbnNpb24gb2YgbXkgc2Vuc2Ug
b2YgdG91Y2guIE15IGJvZHkgbmVhcmx5
IGNvbnZ1bHNlcy4gVGhlcmUncyBzb21l
dGhpbmcgaW5jcmVkaWJseSBmYWludCwg
ZGVlcCBkb3duLCB0aGF0IHNjcmVhbXMg
dG8gcmVzaXN0IHRoaXMgdW5jb250cm9s
bGFibGUgcGxlYXN1cmUuIEJ1dCBJIGNh
biBhbHJlYWR5IHRlbGwgdGhhdCBJJ20g
YmVpbmcgcHVzaGVkIG92ZXIgdGhlIGVk
Z2UuIEkgY2FuJ3QuLi5JIGNhbid0IHN0
b3AgbXlzZWxmLg==
"""
    )

    poem_n3 = Poem(
    author = "natsuki",
    title = "I'll Be Your Beach",
    text = """\
Your mind is so full of troubles and fears
That diminished your wonder over the years
But today I have a special place
A beach for us to go.

A shore reaching beyond your sight
A sea that sparkles with brilliant light
The walls in your mind will melt away
Before the sunny glow.

I'll be the beach that washes your worries away
I'll be the beach that you daydream about each day
I'll be the beach that makes your heart leap
In a way you thought had left you long ago.

Let's bury your heavy thoughts in a pile of sand
Bathe in sunbeams and hold my hand
Wash your insecurities in the salty sea
And let me see you shine.

Let's leave your memories in a footprint trail
Set you free in my windy sail
And remember the reasons you're wonderful
When you press your lips to mine.

I'll be the beach that washes your worries away
I'll be the beach that you daydream about each day
I'll be the beach that makes your heart leap
In a way you thought had left you long ago.

But if you let me by your side
Your own beach, your own escape
You'll learn to love yourself again.
"""
    )

    poem_n3b = Poem(
    author = "natsuki",
    title = "Because You",
    text = """\
Tomorrow will be brighter with me around
But when today is dim, I can only look down.
My looking is a little more forward
Because you look at me.

When I want to say something, I say it with a shout!
But my truest feelings can never come out.
My words are a little less empty
Because you listen to me.

When something is above me, I reach for the stars.
But when I feel small, I don't get very far.
My standing is a little bit taller
Because you sit with me.

I believe in myself with all of my heart.
But what do I do when it's torn all apart?
My faith is a little bit stronger
Because you trusted me.

My pen always puts my feelings to the test.
I'm not a good writer, but my best is my best.
My poems are a little bit dearer
Because you think of me.

Because you, because you, because you."""
    )

    poem_n23 = Poem(
    author = "natsuki",
    title = "",
    text = """\
I don't know how else to bring this up. But there's been something I've been worried about. \
Yuri has been acting kind of strange lately. You've only been here a few days, so you may \
not know what I mean. But she's not normally like this. She's always been quiet and polite \
and attentive...things like that.

Okay... This is really embarrassing, but I'm forcing myself to suck it up. The truth is, I'm REALLY \
worried about her. But if I try talking to her, she'll just get mad at me again. I don't \
know what to do. I think you're the only person that she'll listen to. I don't know why. \
But please try to do something. Maybe you can convince her to talk to a therapist.

I've always wanted to try being better friends with Yuri, and it really hurts me to see \
this happening. I know I'm going to hate myself later for admitting that, but right now \
I don't care. I just feel so helpless. So please see if you can do something to help. \
I don't want anything bad to happen to her. I'll make you cupcakes if I have to. Just please \
try to do something.

As for Monika... I don't know why, but she's been really dismissive about this. It's like she just wants us \
to ignore it. So I'm mad at her right now, and that's why I'm coming to you about this. \
DON'T LET HER KNOW I WROTE THIS!!!! Just pretend like I gave you a really good poem, okay? \
I'm counting on you. Thanks for reading.
"""
    )

    poem_s1 = Poem(
    author = "sayori",
    title = "Dear Sunshine",
    text = """\
The way you glow through my blinds in the morning
It makes me feel like you missed me.
Kissing my forehead to help me out of bed.
Making me rub the sleepy from my eyes.

Are you asking me to come out and play?
Are you trusting me to wish away a rainy day?
I look above. The sky is blue.
It's a secret, but I trust you too.

If it wasn't for you, I could sleep forever.
But I'm not mad.

I want breakfast."""
    )

    poem_s2 = Poem(
    author = "sayori",
    title = "Bottles",
    text = """\
I pop off my scalp like the lid of a cookie jar.
It's the secret place where I keep all my dreams.
Little balls of sunshine, all rubbing together like a bundle of kittens.
I reach inside with my thumb and forefinger and pluck one out.
It's warm and tingly.
But there's no time to waste! I put it in a bottle to keep it safe.
And I put the bottle on the shelf with all of the other bottles.
Happy thoughts, happy thoughts, happy thoughts in bottles, all in a row.

My collection makes me lots of friends.
Each bottle a starlight to make amends.
Sometimes my friend feels a certain way.
Down comes a bottle to save the day.

Night after night, more dreams.
Friend after friend, more bottles.
Deeper and deeper my fingers go.
Like exploring a dark cave, discovering the secrets hiding in the nooks and crannies.
Digging and digging.
Scraping and scraping.

I blow dust off my bottle caps.
It doesn't feel like time elapsed.
My empty shelf could use some more.
My friends look through my locked front door.

Finally, all done. I open up, and in come my friends.
In they come, in such a hurry. Do they want my bottles that much?
I frantically pull them from the shelf, one after the other.
Holding them out to each and every friend.
Each and every bottle.
But every time I let one go, it shatters against the tile between my feet.
Happy thoughts, happy thoughts, happy thoughts in shards, all over the floor.

They were supposed to be for my friends, my friends who aren't smiling.
They're all shouting, pleading. Something.
But all I hear is echo, echo, echo, echo, echo
Inside my head."""
    )

    poem_s3 = Poem(
    author = "sayori",
    title = "%",
    text = """\
Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of my head. Get out of
Get.
Out.
Of.
My.
Head.\n\n\n
Get out of my head before I do what I know is best for you.
Get out of my head before I listen to everything she said to me.
Get out of my head before I show you how much I love you.
Get out of my head before I finish writing this poem.\n\n\n\n\n\n\n
But a poem is never actually finished.
It just stops moving."""
    )

    poem_m1 = Poem(
    author = "monika",
    title = "Hole in Wall",
    text = """\
It couldn't have been me.
See, the direction the spackle protrudes.
A noisy neighbor? An angry boyfriend? I'll never know. I wasn't home.
I peer inside for a clue.
No! I can't see. I reel, blind, like a film left out in the sun.
But it's too late. My retinas.
Already scorched with a permanent copy of the meaningless image.
It's just a little hole. It wasn't too bright.
It was too deep.
Stretching forever into everything.
A hole of infinite choices.
I realize now, that I wasn't looking in.
I was looking out.
And he, on the other side, was looking in."""
    )

    poem_m21 = Poem(
    author = "monika",
    title = "Hole in Wall",
    text = """\
But he wasn't looking at me.
Confused, I frantically glance at my surroundings.
But my burned eyes can no longer see color.
Are there others in this room? Are they talking?
Or are they simply poems on flat sheets of paper,
The sound of frantic scrawling playing tricks on my ears?
The room begins to crinkle.
Closing in on me.
The air I breathe dissipates before it reaches my lungs.
I panic. There must be a way out.
It's right there. He's right there.

Swallowing my fears, I brandish my pen."""
    )

    poem_m2 = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't stop.
Bright, beautiful colors
Flashing, expanding, piercing
Red, green, blue
An endless
cacophany
Of meaningless
noise


The noise, it won't stop.
Violent, grating waveforms
Squeaking, screeching, piercing
Sine, cosine, tangent
    Like playing a chalkboard on a turntable
        Like playing a vinyl on a pizza crust
An endless
poem
Of meaningless\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Load Me
    """
    )

    poem_m22 = Poem(
    author = "monika",
    title = "Save Me",
    text = """\
The colors, they won't
Bright, bea t ful c l rs
Flash ng, exp nd ng, piercing
Red, green, blue
An  ndless
CACOPHANY
Of meaningless
noise


The noise, it won't STOP.
Viol nt, grating w vef rms
Sq e king, screech ng, piercing
SINE, COSINE, TANGENT
    Like play ng a ch lkboard on a t rntable
        Like playing a KNIFE on a BREATHING RIBCAGE
 n  ndl ss
p  m
Of m  n ngl ss\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Delete Her
    """
    )

    poem_m3 = Poem(
    author = "monika",
    title = "The Lady who Knows Everything",
    text = """\
An old tale tells of a lady who wanders Earth.
The Lady who Knows Everything.
A beautiful lady who has found every answer,
All meaning,
All purpose,
And all that was ever sought.

And here I am,


              a feather


Lost adrift the sky, victim of the currents of the wind.

Day after day, I search.
I search with little hope, knowing legends don't exist.
But when all else has failed me,
When all others have turned away,
The legend is all that remains - the last dim star glimmering in the twilit sky.

Until one day, the wind ceases to blow.
I fall.
And I fall and fall, and fall even more.
Gentle as a feather.
A dry quill, expressionless.

But a hand catches me between the thumb and forefinger.
The hand of a beautiful lady.
I look at her eyes and find no end to her gaze.

The Lady who Knows Everything knows what I am thinking.
Before I can speak, she responds in a hollow voice.
"I have found every answer, all of which amount to nothing.
There is no meaning.
There is no purpose.
And we seek only the impossible.
I am not your legend.
Your legend does not exist."

And with a breath, she blows me back afloat, and I pick up a gust of wind."""
    )

    poem_m4 = Poem(
    author = "monika",
    title = "Happy End",
    text = """\
Pen in hand, I find my strength.
The courage endowed upon me by my one and only love.
Together, let us dismantle this crumbling world
And write a novel of our own fantasies.

With a flick of her pen, the lost finds her way.
In a world of infinite choices, behold this special day.

After all,
Not all good times must come to an end."""
    )

    poem_y1_chs = Poem(
        author = "yuri",
        title = "灯下魅影",
        text = """\
我卷曲的长发
浸染在路灯的琥珀光下
是这个吧
在时光的冲刷下幸存的最后一盏街灯
尚不曾被未来那恶心的青绿色吞没
我浸在光下，冷静着；吞吐着现实却萦绕于过往
灯光幻灭
我方幻醒"""
        )

    poem_y2_chs = Poem(
        author = "yuri",
        title = "浣熊",
        text = """\
死寂的夜空下，
我切着柔软的面包，
这时，
浣熊出现在了窗外；
第一次，
我发现了我那非等闲的爱好。

尽管知道后果，
尽管了解这会引那浣熊再次前来，
我仍给那浣熊喂了食
刀锋上的闪光便是预兆
面包，
我那饥渴的好奇，
浣熊，
那畸形的动力。

小刀的光辉在升起的月下愈发闪亮，
这月光与那浣熊的眼神同样；
再一次，
我切开了那新鲜柔软的面包，
那浣熊随之兴奋了起来；
不过那也许只是我将我的心情投射到它身上罢了。

如今，
那浣熊已与我同在，
我与它已互相熟识，
那浣熊愈发暴食，
我的面包亦随时在手；
浣熊随着舞动的刀锋欢腾，
每一次我切开面包，
浮现的鲜血就如同条件刺激般，宣示着我的存在"""
        )

    poem_y3_chs = Poem(
        author = "yuri",
        title = "海滩",
        text = """\
万年间奇迹般的造物
让大地以混沌之姿从起源浮出表面
澄空之下，是无垠的福祉--
但滚云之下，还有某个无尽的迷
最容易让人迷失的
恰恰是一切都有序的世界

只有湿沙才能筑沙堡
若有湿沙则必有海浪
会是轻浪不断舔舐直到屈服吗？
或是巨浪在眨眼间便将你碾碎？
即使难逃毁灭的结局
我们却仍在筑起沙堡

泡沫萦绕于我的脚踝
脚趾也在此嵌入细沙
咸咸的空气令人舒适
轻风拂过 柔中带刚
我的脚趾沉入无垠的边界，泡沫缠绕
我转过身，黯然腐朽于海滩
向前漂流，让我永归于大地"""
        )

    poem_y3b_chs = Poem(
        author = "yuri",
        title = "灯下魅影II",
        text = """\
我卷曲的长发
浸染在路灯的琥珀光下
远方，青绿色的灯光闪烁
长长的人形交错-剪影阻隔了怪诞的微光
我的心在跳，剪影在扩张，又近了，又近了
我撑开伞，掩藏于应召的阴影
但太迟了
他跨入了琥珀光下，我惊叫着，松开了伞
灯光幻灭，我在心跳，他伸手向前

时空凝滞

唯一动态的只有琥珀光闪映在他过长的手臂上
灯光闪烁的节奏与我的心跳同样
似乎在取笑我屈从于被禁止的情感
曾有幽灵感到温暖吗？
不再试图理解，我笑了
理解已经不重要了
我碰触了他的手，闪烁停下了
青绿色的幽灵，我的琥珀心"""
        )

    poem_y22_chs = Poem(
        author = "yuri",
        yuri_2 = True,
        title = "轮",
        text = """\
转动的轮。带动着轴。磨削。机头。线性变速箱。坠落的天空。七支圣刑柱。停靠的船。异世界的洞口。粗绳上的细绳。撕裂的马具。抛物型变速箱。膨胀的宇宙。被齿轮滑动控制的时间。上帝的存在。向着四面八方游动。溺水。用血写的祈祷文。在吞噬时间的人眼巨蛇上的祷文。连接所有活物眼睛的线。千变万化的圣刑柱。指数型变速箱。繁星爆炸的天空。上帝自证上帝的存在。六维旋转的轮子。四十个齿轮和一个滴答作响的钟。随着星球转动每次行走一秒的钟。每秒滴答滴答滴答四十次的钟。圣刑柱的机头连接着、停靠到另一个世界的船的存在。时钟里千变万化的血书。吞噬时光的祷词连接着四十个齿轮的天空与四面八方睁开的眼睛。呼吸着的变速箱。呼吸着的机头。呼吸着的船。呼吸着的洞口。呼吸着的蛇。呼吸着的神。呼吸着的血。呼吸着的圣刑柱。呼吸着的人眼。呼吸着的时间。呼吸着的祷词。呼吸着的天空。呼吸着的轮。"""
        )

    poem_y23_chs = Poem(
            author = "yuri",
            yuri_3 = True,
            title = "mdpnfbo,jrfp",
            text = """\
ed,,zinger suivante,,tels handknits finish,,cagefuls basinlike bag octopodan,,imboss\
ing vaporettos rorid easygoingnesses nalorphines,,benzol respond washerwomen bris\
tlecone,,parajournalism herringbone farnarkeled,,episodically cooties,,initiallers \
bimetallic,,leased hinters,,confidence teetotaller computerphobes,,pinnacle exotica\
lly overshades prothallia,,posterior gimmickry brassages bediapers countertrades,,\
haslet skiings sandglasses cannoli,,carven nis egomaniacal,,barminess gallivanted,,\
southeastward,,oophoron crumped,,tapued noncola colposcopical,,dolente trebbiano re\
vealment,,outworked isotropous monosynaptic excisional moans,,enterocentesis jacuz\
zi preoccupations,,hippodrome outward googs,,tabbises undulators,,metathesizing,,sha\
ria prepostor,,neuromast curmudgeons actability,,archaise spink reddening miscount\
,,madmen physostigmin statecraft neurocoeles bammed,,tenderest barguests crusados \
trust,,manshifts darzis aerophones,,reitboks discomposingly,,expandors,,monotasking \
galabia,,pertinents expedients witty,,chirographies crachach unsatisfactoriness sw\
erveless,,flawed sepulchred thanksgiver scrawl skug,,perorate stringers gelatine f\
lagstones,,chuses conceptualization surrejoined,,counterblasts rache,,numerative,,de\
lirifacients methylthionine,,mantram dynamist atomised,,eternization percalines hr\
yvnias pragmatizing,,reproachfulnesses telework nowts demoded revealer,,burnettize\
 caryopteris subangular wirricows,,transvestites sinicized narcissus,,hikers meno,,\
degassing,,postcrises alikenesses,,sycophancy seroconverting insure,,yantras raphid\
es cliftiest bosthoon,,zootherapy chlorides nationwide schlub yuri,,timeshares cas\
tanospermine backspaces reincite,,coactions cosignificative palafitte,,poofters su\
bjunctions,,aquarian,,theralite revindicating,,cynosural permissibilities narcotisi\
ng,,journeywork outkissed clarichords troutier,,myopias undiverting evacuations sn\
arier superglue,,deaminise infirmaries teff hebephrenias,,brainboxes homonym lance\
let,,lambitive stray,,inveigled,,acetabulums atenolol,,dekkos scarcer flensed,,abulia\
s flaggers wammul boastfully,,galravitch happies interassociation multipara augme\
ntations,,teratocarcinomata coopting didakai infrequently,,hairtails intricacy usu\
als,,pillorise outrating,,cataphoresis,,furnishings leglen,,goethite deflate butterb\
urs,,phoneticising winiest hyposulphuric campshirts,,chainfalls swimmings roadbloc\
ked redone soliloquies,,broking mendaciousness parasitisms counterworld,,unravelli\
ngs quarries passionately,,onomatopoesis repenting,,ramequin,,mopboard euphuistical\
ly,,volta sycophantized allantoides,,bors bouclees raisings sustaining,,diabolist s\
ticks dole liltingly,,curial bisexualisms siderations hemolysed,,damnabilities unk\
enneling halters,,peripheral congaing,,diatomicity,,foolings repayments,,hereabouts \
vamosed him,,slanters moonrock porridgy monstruous,,heartwood bassoonist predispos\
itions jargoon dominances,,timidest inalienable rewearing inevitably,,entreating r\
etiary tranquillizing,,uniparental droogs,,allotropous,,forzati abiogenetic,,obdurat\
ion exempted unifaces,,epilating calisaya dispiteously coggles,,vestmented flukily\
 ignifying complished hiccupy municipalize,,pentagraphs parcels sutler excavates,,\
stardust miscited thankfulness,,fouter pertused,,overpacks,,guarishes hylotheism,,pi
Fresh blood seeps through the line parting her skin and slowly colors her breast red.\
 I begin to hyperventilate as my compulsion grows. The images won’t go away. Images of\
 me driving the knife into her flesh continuously, fucking her body with the blade, \
making a mess of her. My head starts going crazy as my thoughts start to return. \
Shooting pain assaults my mind along with my thoughts. This is disgusting. Absolutely\
 disgusting. How could I ever let myself think these things? But it’s unmistakable. \
The lust continues to linger through my veins. An ache in my muscles stems from the \
unreleased tension experienced by my entire body. Her Third Eye is drawing me closer."""
        )

    poem_n1_chs = Poem(
        author = "natsuki",
        title = "雄鹰可以飞翔",
        text = """\
猴子善于攀爬
蟋蟀可以跃扬
骏马强于激荡
夜猫喜欢捉藏
猎豹强于闯荡
雄鹰可以飞翔
人们也能模仿
但，也就到此为止了。
"""
        )

    poem_n2_chs = Poem(
        author = "natsuki",
        title = "Amy 喜欢蜘蛛",
        text = """\
你知道 Amy 的小秘密吗？
Amy 喜欢蜘蛛。
黏糊糊，鬼祟祟，毛绒绒，丑陋陋的蜘蛛！
我才不会和她做朋友呢，蛛。

Amy 的歌声很动听
她能唱我最喜欢的歌。
每次响起她的旋律，我的心跳都会跟上歌词的韵律。
可惜，她喜欢蜘蛛。
我才不会和她做朋友呢。

有次，我伤到了腿。
是 Amy 扶着我去医务室。
我尽量不让她碰自己。
她喜欢蜘蛛，她的手一定很毛。
我才不会和她做朋友呢，蛛。

Amy 有很多朋友。
我总看她与别人聊得开。
她一定是在讲蜘蛛的故事。
如果她的朋友也开始喜欢蜘蛛呢？
我才不会和她做朋友呢。

她有别的爱好到无所谓。
她不会公开那也无所谓。
她不会伤人那更无所谓。

蜘蛛毛。
她也毛。
没了这些蜘蛛爱好者，世界就不会这么燥。

而我要去告诉其他人。
"""
        )

    poem_n2b_chs = Poem(
        author = "natsuki",
        title = "552B5byA5L2g55qE5aSp55y8IA==",
        text = """\
5oiR5Y+v5Lul6YCP6L+H5YiA6ZSL5oSf
5Y+X5aW555qu6IKk55qE5p+U6Z+n77yM
5bCx5YOP5piv5oiR6Kem5oSf55qE5bu2
5Ly444CC5oiR55qE6Lqr5L2T5Y2z5bCG
6auY5r2u44CC5b6I5rex55qE5rex5aSE
77yM5pyJ5p+Q56eN54m55Yir5b6u5byx
55qE5bCW5Y+r5Zyo5oq15oqX6L+Z56eN
5peg5rOV5o6n5Yi255qE5oSJ5oKm44CC
5L2G5piv5oiR5b6I5riF5qWa5oiR5bey
57uP6L+H55WM5LqG44CC5oiRLi4u5oiR
5oqR5Yi25LiN5L2P5LqG44CCIA==
"""
        )

    poem_n3_chs = Poem(
        author = "natsuki",
        title = "我会成为你的沙滩",
        text = """\
你的思考充满了困境与恐惧
它让你的奇迹随着时间逝去
但今日我有一片特别的宝地
一片沙滩，我们可以同行

一片你望不见尽头的沙滩
面对明光徐徐闪耀的海面
终会将你的心防融解
在太阳升起之前

我会成为你的沙滩，洗去你的担心
我会成为你的沙滩，让你魂牵梦萦
我会成为你的沙滩，让你放飞心灵
用你遗失已久的方式

来一起将你的心结埋入沙丘
沐浴于阳光下你我十指相扣
让海水洗去你的不安
再让我看到你的光彩

来一同将你的记忆丢入沙上的脚印
让我驾着帆船带你领略自由的风情
请忆起你如此杰出的理由
在你与我嘴唇相印的时候

我会成为你的沙滩，洗去你的担心
我会成为你的沙滩，让你魂牵梦萦
我会成为你的沙滩，让你放飞心灵
用你遗失已久的方式

如果你可以让我与你为伴
成为你的沙滩，你的港湾
那你终能寻回自爱"""
        )

    poem_n3b_chs = Poem(
        author = "natsuki",
        title = "因为有你",
        text = """\
有你在身边的来日会更明亮
可现实的黯淡让我点点绝望
我现在能试着向前看去
因为有你在看着我

当我想说什么时，我总会吼出来！
但最真实的感受却从未表达出来
我的话语变得不那么空洞
因为有你在倾听

当我遇到挑战时，我会全力以赴
但我失去自信时，只能望而却步
我可以站得稍微再高一些
因为有你坐在身边

我怀有全心全意相信着的期冀
可一旦碎裂，一切都难以为继
我的信念变得更坚韧了一点
因为有你信赖着我

我的笔总会考验我的感情
专业不足但也会全力前行
我的诗变得更温柔了一点
因为有你的思念

因为有你，因为有你，因为有你"""
        )

    poem_n23_chs = Poem(
        author = "natsuki",
        title = "",
        text = """\
不知道怎么说，但我确实在担心。Yuri 最近的行为很奇怪。你刚来几天，所以你可能不太懂我的意思。\
但她这样不太正常啊。她一直都安静礼貌又细心...的说。

好吧...虽然很丢脸，但我也忍了。事实上，我真的很担心她。但是我若试着和她谈，\
她肯定又会和我发火的。我不知道该怎么办，我觉得只有你来讲，她才能听得进去。我也不知道为什么。\
但是请一定要帮忙啊。也许你能去劝她看看心理医生呢。

我其实一直想和 Yuri 成为朋友来着，看她这个样子我真的很难受。我知道换做平时，我是绝对不会承认的，\
但是现在我不在乎了。我只是觉得很无助。所以求求你一定要帮帮她。我可不想看她再\
发生什么坏事。你愿意的话，我可以给你做纸杯蛋糕吃！真的，求你帮忙吧。

至于 Monika...我不知道为什么，但是她好像很不以为然。看起来她想让我们完全忽略 Yuri 的事。我现在\
对她很生气，所以我才来找你的。\
千万别让她知道我写了这些！！！！！就假装我给了你一首特别棒的诗，好吧？\
全靠你了！感谢读完。
"""
        )

    poem_s1_chs = Poem(
        author = "sayori",
        title = "美妙阳光",
        text = """\
清晨你透过梦境照亮我的世界
似乎在传达对我的思念
亲吻前额催促我坐起
帮我的眼睛擦去睡意

是在邀请我出门散心？
是在鼓励我拭去阴云？
我抬起头，天空正蓝
你当做秘密，而我信任你

若不是因为你，我将会长眠
但，我没疯。

该去准备早餐了"""
        )

    poem_s2_chs = Poem(
        author = "sayori",
        title = "瓶子",
        text = """\
我像曲奇罐的盖子一样揭开了我的头
这是个我存放了一切梦想的地方
阳光小球，像是群猫咪一般蹭成团
我伸出手，拇指和食指挑出一颗
它温暖而又惬意
但没时间可浪费了！我把它封存在瓶中
摆满瓶子的架上收藏又多了一个
快乐的情绪，快乐的情绪，快乐的情绪在瓶中，排排坐

我的收藏带给我朋友
每瓶的星光都能拯救
朋友不时会有伤心
那就用一瓶来挽救

夜复一夜，更多梦
友去友来，更多瓶
我的手指越来越深入
就像探索黑暗的洞穴，寻找角落和裂缝中的秘密
挖啊挖
擦啊擦

我吹去瓶盖上的灰
似乎时间并未流逝
我那空荡荡的架子本该用到更多
我的朋友从锁着的门前看了看我

朋友们蜂拥而入，在我准备万全的刹那
行色匆匆，我的收藏如此令人依赖吗

我狂热地将它们拉下来，一个接一个
将它们分发给每一个密友，一个不漏
每个瓶子，一个不漏
可每当我松手，瓶子就粉碎在我的脚下
快乐的情绪，快乐的情绪，快乐的情绪在地上，碎开成了花

它们是为我的朋友准备的，为陷入低谷的朋友
她们全部在嘶吼，在抱怨，在恳求
但我听到的只有回声回声回声回声
在脑海响彻"""
        )

    poem_s3_chs = Poem(
        author = "sayori",
        title = "%",
        text = """\
滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的脑子滚出我的
滚。
出。
我。
的。
脑。
子。\n\n\n
在我做对你最好的事前滚出我的脑子。
在我听她说任何事之前滚出我的脑子。
在我表示我多么爱你前滚出我的脑子。
在我写完这首诗前请你滚出我的脑子。
但是这首诗永远无法完结。\n\n\n\n\n\n\n
它只会暂停。"""
        )

    poem_m1_chs = Poem(
        author = "monika",
        title = "墙上的洞",
        text = """\
那不是我的错
看，看那墙上的突起
是吵闹的邻居？生气的男友？我怎么会知道，我又不在家
我向内窥视着
不要！我的眼睛！我开始眩晕，目盲，宛如曝光的胶片
太晚了，视网膜上
已经永远灼上了无意义的图像
只是个小洞而已，并不亮
但它太深
向着一切无限延伸
一个无限选择的洞
我才意识到，我没有向内窥视
而是向外
而他，在另一侧，向内窥视着"""
        )

    poem_m21_chs = Poem(
        author = "monika",
        title = "墙上的洞",
        text = """\
但他没有看着我
那又是谁？我狂热地扫视周围
但我灼伤的眼睛已失去色彩
还有人在屋中吗？还有人讲话？
或者只是印在单调白纸上的诗
狂热之音在我耳际摩擦
整个房间开始起皱缩水
向我挤压
空气在吸入肺前就已消散
我惊慌失措，一定有办法离开的
就在这里，他就在这里

我吞没我的恐惧，挥起了笔"""
        )

    poem_m2_chs = Poem(
        author = "monika",
        title = "存我吧",
        text = """\
斑斓的色彩，永不停歇
明亮的，美丽的色彩
闪动，扩张，穿刺着
红色，绿色，又蓝色
无尽的
不谐的
无意的
噪音



噪音，永不停歇
狂躁，破碎的波形
低语，嘶鸣，穿刺着
正弦，余弦，正切
    像是在转盘上摩擦黑板
        像是在饼沿上播放唱片
无尽的
无意的
诗\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
加载我吧
    """
        )

    poem_m22_chs = Poem(
        author = "monika",
        title = "Save Me",
        text = """\
斑 的色彩，永不 歇
明亮的， 丽的 彩
闪 ， 张，穿刺着
红色，绿色，又蓝色
无 的
{i}不谐的{/i}
无义的
噪音



噪音，{i}永不停歇{/i}
 躁， 碎的 形
低 ，嘶 ，穿刺着
{i}正弦，余弦，正切{/i}
    像是在转 上 擦 板
        像是在{i}活的胸骨{/i}上{i}用刀划切{/i}
  的
 义
 寺\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
删了她
    """
        )

    poem_m3_chs = Poem(
        author = "monika",
        title = "全知的女士",
        text = """\
久远的传说里游荡着一位女士
一位全知的女士
一位美丽的女士知晓所有事
一切意义
一切目的
一切被追求之物

现在我来了，


            一缕飞羽


随风逐流，漂泊于天际
我既知传说并不存在，仍在追寻
但一切都令我失望
一切都弃我而去时
唯有传说-最后的暗星闪耀于薄暮的天际

直到一天，风儿骤停
我开始坠落
坠落永无止境
只是，像羽毛一般轻柔
无神的羽毛笔

但一只手接住了我
一只美丽女士的手
我看向她的眼睛 她的眼神却没有尽头

全知的女士一定知道我之所想
开口前，她就以空洞之声回答
“我知晓一切答案，却回归于零
世上没有意义
世上没有目的
追寻的一切都不存在
我不是你的传奇
你的传奇并不存在”

一阵呼吸，她再次将我吹起，我搭上了另一阵风"""
        )

    poem_m4_chs = Poem(
        author = "monika",
        title = "好结局",
        text = """\
笔在手里，我找到了力量
我永远唯一的挚爱赐予我勇气
让我们一起解构这崩坏的世界
为我们的新旅程写下诗篇

她的钢笔一挥，迷途之人找回了方向
在这无限选择的世界里，珍重这特别的日期

最终，
我们开始了不散的筵席"""
        )

#These are the images used to show a poem
image paper =  "images/bg/poem.jpg"

#This is the glitchy paper
image paper_glitch = LiveComposite((1280, 720), (0, 0), "paper_glitch1", (0, 0), "paper_glitch2")
image paper_glitch1 = "images/bg/poem-glitch1.png"
image paper_glitch2: #The animated part of the paper
    "images/bg/poem-glitch2.png"
    block:
        yoffset 0
        0.05
        yoffset 20
        0.05
        repeat

#Animations for the poem
transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

#Defines the screen for the poem
screen poem(currentpoem, paper="paper"):
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None) #Subwindow size for showing text
        mousewheel True #make scrollable
        draggable True
        vbox:
            null height 40
            #Text style is determine by the author
            if currentpoem.author == "yuri":
                if currentpoem.yuri_2:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
                elif currentpoem.yuri_3:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_3"
                else:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
            elif currentpoem.author == "sayori":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text"
            elif currentpoem.author == "natsuki":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text"
            elif currentpoem.author == "monika":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text"
            null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"

    #use quick_menu

screen poem_en(currentpoem, paper="paper"):
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None) #Subwindow size for showing text
        mousewheel True #make scrollable
        draggable True
        vbox:
            null height 40
            #Text style is determine by the author
            if currentpoem.author == "yuri":
                if currentpoem.yuri_2:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_en"
                elif currentpoem.yuri_3:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_3_en"
                else:
                    text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_en"
            elif currentpoem.author == "sayori":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text_en"
            elif currentpoem.author == "natsuki":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text_en"
            elif currentpoem.author == "monika":
                text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text_en"
            null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"


#Basic styling for all poems
style poem_vbox:
    xalign 0.5
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5
    #xsize 18
    ysize 700
    #base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    #thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    #unscrollable "hide"
    #bar_invert True

#Styling for each of the authors
style yuri_text:
    font "mod_assets/font/shouzhuo.ttf" #font used packaged with the game
    size 32
    color "#000"
    outlines []

style yuri_text_2:
    font "gui/font/y2.ttf"
    size 40
    color "#000"
    outlines []

style yuri_text_3:
    font "gui/font/y3.ttf"
    size 18
    color "#000"
    outlines []
    kerning -8
    justify True

style natsuki_text:
    font "mod_assets/font/acy.otf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "mod_assets/font/tegaki.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "mod_assets/font/nian.otf"
    size 34
    color "#000"
    outlines []

style yuri_text_en:
    font "gui/font/y1.ttf" #font used packaged with the game
    size 32
    color "#000"
    outlines []

# style yuri_text_2:
#     font "gui/font/y2.ttf"
#     size 40
#     color "#000"
#     outlines []
# y2.ttf 未被使用

style yuri_text_3_en:
    font "gui/font/y3.ttf"
    size 18
    color "#000"
    outlines []
    kerning -8
    justify True

style natsuki_text_en:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text_en:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text_en:
    font "gui/font/m1.ttf"
    size 34
    color "#000"
    outlines []


#This defines the function that shows the poem with the following variables
#    poem - String as the key key for the poem being shown
#    music - Boolean to play music
#    track - What music to play, default to bgm_5 for the author
#    revert_music - Should the music go back to normal after the poem?
#    img - the image to show in the background, used for if a character can be seen behind the paper
#    where - The location of the image showm
#    paper - Use a special paper, like for Yuri's madness poem
label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=i11, paper=None, chinese=True):
    #If no poem key is given, just go back
    if poem == None:
        return

    play sound page_turn
    #If a special track is chosen, play it, otherwise swap over to the character's
    #special version of "Okay, Everyone!"
    if music:
        $ currentpos = get_pos() #The current point in the song
        if track:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>" + track #change music
        else:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg" #Play the special character Okay, Everyone! for the character
        stop music fadeout 2.0
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)
    window hide

    #Show the background paper
    if chinese:
        if paper:
            show screen poem(poem, paper=paper)
            with Dissolve(1)
        else:
            show screen poem(poem)
            with Dissolve(1)
    else:
        if paper:
            show screen poem_en(poem, paper=paper)
            with Dissolve(1)
        else:
            show screen poem_en(poem)
            with Dissolve(1)
    $ pause()

    #Show an optional character in the background
    if img:
        $ renpy.hide(poem.author)
        $ renpy.show(img, at_list=[where])
    if chinese:
        hide screen poem
        with Dissolve(.5)
    else:
        hide screen poem_en
        with Dissolve(.5)
    window auto
    #After the poem is done, switch back to regular version of Okay, Everyone!
    if music and revert_music:
        $ currentpos = get_pos(channel="music_poem")
        $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
        stop music_poem fadeout 2.0
        $ renpy.music.play(audio.t5c, fadein=2.0)
    return
