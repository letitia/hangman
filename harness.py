import random
wordstring = 'contributeTcorrodeTdegradeTdetainTdiameterTsentinelTghettoTinitiateTbarterTresistanceTchildcareTnightclothesTfamilyTcovertTstreetTrumpleTlandingTinstructionalThatcheryTnavigationalTpopulateTwheedleTattentionTmisreadTwiggleTcleanersTsquintingTbelliedTunidentifiedTraspingTclenchedTfistTfinalTdecisionTdepartmentTjusticeTcomplicateTtakeoffTfascinateTrumpledTcharismaTjeeringTdistraughtTcrackleTparticipateTsiftingTunloadingTnurtureTcacheTgiggleTrecognizableTuneducatedTsupplementaryTobedientlyTunisonTteammateTpedalTstreakedTsympatheticallyTupturnedTconfuseTreleasingTtransgressionTrevolveTsquintTironicTanthemTnervousnessTfrighteningTclassmateTsickeningTgenderTadequatelyTchantingTdescriptiveTstumbleTbreathlesslyTreassuringTpalpableTtunicTnosedTindoorsTdaytimeTapologizeTapprehensiveTviewingTchurnTfrustrationTscrambleTsmoothedTreciteTstraightforwardTmiddayTtroublingTunspeakableTclassroomTsoundlyTsleekTdefiantTunloadingTperpetuateTfrontierTgripeTtemporaryTeffuseTcitrusTcomplainTdelicateTmenialTstrandTannounceTanticipateTbestowTflexibleTreplenishTwrathTinflateTvehicleTgingerlyTchartTanguishTplentyTsymbolTutterTspringTassertTplainTfatigueTgait'
terms = wordstring.split('T')
secretWord = random.choice(terms)


def wordProgress(guesses):
	result = ""
	for letter in secretWord:
		if letter in guesses:
			result += letter.upper() + ' '
		else:
			result += '__ '
	return result

def wordIsCompleted(guesses):
	if wordProgress(guesses).find('__') == -1:
		return True
	return False

def getLetter():
	guess = raw_input('Guess a letter: ')
	if (guess == "quit"):
		print "Goodbye!"
		exit
	if (len(guess) != 1):
		print "That is not a valid letter!"
		return False
	if (guess.isalpha()):
		return guess.lower()
	print "That is not a valid letter!"
	return False

def letterIsInWord(letter):
	return secretWord.find(letter) != -1

def revealSecretWord():
	print 'The secret word was "' + secretWord + '"'
