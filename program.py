import random, os

score=0
word_list = ['wares','soup','mount','extend','brown','expert','tired','humidity','backpack','crust','dent','market','knock',
'smite','windy','coin','throw','silence','bluff','downfall','climb','lying','weaver','snob','kickoff','match','quaker','foreman',
'excite','thinking','mend','allergen','pruning','coat','emerald','coherent','manic','multiple','square','funded','funnel',
'sailing','dream','mutation','strict','mystic','film','guide','strain','bishop','settle','plateau','emigrate','marching','optimal',
'medley','endanger','wick','condone','schema','rage','figure','plague','aloof','there','reusable','refinery','suffer','affirm',
'captive','flipping','prolong','main','coral','dinner','rabbit','chill','seed','born','shampoo','italian','giggle','roost','palm',
'globe','wise','grandson','running','sunlight','spending','crunch','tangle','forego','tailor','divinity','probe','bearded',
'premium','featured','serve','borrower','examine','legal','outlive','unnamed','unending','snow','whisper','bundle','bracket',
'deny','blurred','pentagon','reformed','polarity','jumping','gain','laundry','hobble','culture','whittle','docket','mayhem',
'build','peel','board','keen','glorious','singular','cavalry','present','cold','hook','salted','just','dumpling','glimmer',
'drowning','admiral','sketch','subject','upright','sunshine','slide','calamity','gurney','adult','adore','weld','masking','print',
'wishful','foyer','tofu','machete','diced','behemoth','rout','midwife','neglect','mass','game','stocking','folly','action',
'bubbling','scented','sprinter','bingo','egyptian','comedy','rung','outdated','radical','escalate','mutter','desert','memento',
'kayak','talon','portion','affirm','dashing','fare','battle','pupil','rite','smash','true','entrance','counting','peruse',
'dioxide','hermit','carving','backyard','homeless','medley','packet','tickle','coming','leave','swing','thicket','reserve',
'murder','costly','corduroy','bump','oncology','swatch','rundown','steal','teller','cable','oily','official','abyss','schism',
'failing','guru','trim','alfalfa','doubt','booming','bruised','playful','kicker','jockey','handmade','landfall','rhythm','keep',
'reassure','garland','sauna','idiom','fluent','lope','gland','amend','fashion','treaty','standing','current','sharpen','cinder',
'idealist','festive','frame','molten','sill','glisten','fearful','basement','minutia','coin','stick','featured','soot','static',
'crazed','upset','robotics','dwarf','shield','butler','stitch','stub','sabotage','parlor','prompt','heady','horn','bygone',
'rework','painful','composer','glance','acquit','eagle','solvent','backbone','smart','atlas','leap','danger','bruise','seminar',
'tinge','trip','narrow','while','jaguar','seminary','command','cassette','draw','anchovy','scream','blush','organic','applause',
'parallel','trolley','pathos','origin','hang','pungent','angular','stubble','painted','forward','saddle','muddy','orchid',
'prudence','disprove','yiddish','lobbying','neuron','tumor','haitian','swift','mantel','wardrobe','consist','storied','extreme',
'payback','control','dummy','influx','realtor','detach','flake','consign','adjunct','stylized','weep','prepare','pioneer','tail',
'platoon','exercise','dummy','clap','actor','spark','dope','phrase','welsh','wall','whine','fickle','wrong','stamina','dazed',
'cramp','filet','foresee','seller','award','mare','uncover','drowning','ease','buttery','luxury','bigotry','muddy','photon',
'snow','oppress','blessed','call','stain','amber','rental','nominee','township','adhesive','lengthy','swarm','court','baguette',
'leper','vital','push','digger','setback','accused','taker','genie','reverse','fake','widowed','renewed','goodness','featured',
'curse','shocked','shove','marked','interact','mane','hawk','kidnap','noble','proton','effort','patriot','showcase','parish',
'mosaic','coil','aide','breeder','concoct','pathway','hearing','bayou','regimen','drain','bereft','matte','bill','medal','prickly',
'sarcasm','stuffy','allege','monopoly','lighter','repair','worship','vent','hybrid','buffet','lively']

#menu function
def main():
	menu()

def menu():
	choice='y'
	while choice=='y' or choice=='yes':
		print("Welcome to Hangman Game")
		print("1.PLAY \n2.HIGHSCORES \n3.HELP \n4.QUIT")
		print()
		ch=int(input("Enter your choice:"))
		print()
		os.system('cls')
		if ch==1:
			print("Let's play!")
			play(score)

		elif ch==2:
			print("Opening details..")
			input()
			os.system('cls')
			read_score()

		elif ch==3:
			f=open("help.txt","r")
			print(f.read())
			f.close()

		elif ch==4:
			print("Quitting")
			break

		else:
			print("Invalid choice.")

		choice=input("Do you want to choose anything else?")
		choice=choice.lower()
		os.system('cls')


#play function
def play(score):
	i=1
	while i<=10:
		print("Welcome to Level",i)
		word=get_word()
		print("Guess the word:")
		print("_" * len(word))
		guesses=''
		turns=3
		while turns>0:
			fail=0
			guess=input("Guess a character:")
			guess=guess.upper()
			guesses+=guess
			for char in word:
				if char in guesses:
					print(char)

				else:
					print("_")
					fail+=1

			if fail==0:
				print("You completed Level",i)
				print("The word is:",word)
				score+=len(word)*10
				print("Total score is:",score)
				input()
				os.system('cls')
				break
			
			if guess not in word:
				turns-=1
				print(display_hangman(turns))
				print("Character guessed is wrong.")
				print("You have ",turns," more guesses.")

		else:
			print("You lost.")
			print("The word is:",word)
			print("Total score is:",score)
			break
		i+=1
	name=input("Enter name:")
	store_high_scores(score,name)
 
#For getting a random word from word_list
def get_word():
    word = random.choice(word_list)
    return word.upper()

#To store details of the user- name and score
def store_high_scores(score,name):
	f1=open("highscore.txt","a")
	line=name + ','+ str(score)
	f1.write(line)
	f1.write('\n')
	f1.close()

#to read the details from the file and printing them after sorting
def read_score():
	name_read=[]
	score_read=[]
	f2=open("highscore.txt","r")
	for line in f2:
		line=line.strip().split(',')
		name_read.append(line[0])
		score_read.append(int(line[1]))
	n=len(score_read)
	f2.close()

	for j in range(n):
		for k in range(n-j-1):
			if score_read[k]<score_read[k+1]:
				score_read[k],score_read[k+1]=score_read[k+1],score_read[k]
				name_read[k],name_read[k+1]=name_read[k+1],name_read[k]

#To overwrite the existing data in the file in sorted details
	print("NAME \t SCORE")
	f2=open("highscore.txt","w")
	for i in range(5):
		print(name_read[i],"\t",score_read[i])
		lines=name_read[i]+','+str(score_read[i])
		f2.write(lines)
		f2.write('\n')
	f2.close()

#to display the different stages of hangman
def display_hangman(turns):
	stages=[#Final stage - head, torso, both arms and legs
				"""
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
			#Head and body
				"""
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
			#Initial stage
				"""
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """
            ]

	return stages[turns]

#Calling main function
if __name__=="__main__":
	main()
