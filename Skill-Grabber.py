#Uses the Runescape High Score JSON API
#Created by imSnayer
import re
import urllib2

def levelParse():
	global pageSource
	pageSource = pageSource.split("\n")
	skills = ["Attack", "Defense", "Strength", "Constitution", "Range", "Prayer", "Magic", "Cooking", "Woodcutting", "Fletching", "Fishing", "Firemaking", "Crafting", "Smithing", "Mining", "Herblore", "Agility", "Thieving", "Slayer", "Farming", "Runecrafting", "Hunting", "Construction", "Summoning", "Dungeoneering", "Divination"]
	dataNum = 1
	for skill in skills:
		skillName = pageSource[dataNum].split(",")
		print "%s is level %s" % (skill, skillName[1]) 
		"""
			Change skillName[0] for Rank
			Change skillName[1] for Level
			Change skillName[2] for Total XP
		"""
		dataNum += 1
	print "\n"
	main()
	
def getStats(name):
	failSafe = 0
	if " " in name: #Check if name has spaces
		name = name.replace (" ", "_") #Swap Spaces with underscores for URL use
		url = "http://hiscore.runescape.com/index_lite.ws?player=%s" % (name)
		failSafe = 1
	else:
		url = "http://hiscore.runescape.com/index_lite.ws?player=%s" % (name)
		failSafe = 1
	if failSafe == int(1):
		try:
			global pageSource
			webPage = urllib2.urlopen(url)
			pageSource = webPage.read()
			levelParse()
		except urllib2.HTTPError, error:
			contents = error.read()
			print "Sorry, there was an error finding that name."
			main()

def main():
	while True:
		name = raw_input("Enter a Member User name to grab the levels: ")
		print "\n"
		getStats(name)
		
if __name__ == "__main__":
  main()
