#!/usr/bin/python3
from lists import Lists
class Lessons():
    """A container-class for methods that create random sentences,
        returns String."""
    def my_friends_call_me_hiro(self):
        """Random sentence generator of the sentence pattern:
            'My friends call me Hiro.'
            returns String."""
        possAdj =random.choice(Lists.possAdjList).title()
        subj = random.choice(Lists.personSubjectList)
        possProObj = random.choice(Lists.possProObjList)
        name = random.choice(Lists.nameList)
        # entering this loop when it should not be
        if possAdj == 'Our':
                subj = makePlural(subj)		
        if possAdj == 'Their':
                subj = makePlural(subj)
        sentence = possAdj + " " + subj + " " + wordCall(subj) + " " + possProObj + " " + name + "."
        return sentence

    def thisBookIsWritten(self):
        """Figure out this function."""

        #makePluralYesNo = random.choice(2)
        demonAdj = random.choice(Lists.demonAdjList).title()	
        commonNoun = random.choice(Lists.thisBookIsWrittenNounList)
        
        #if makePluralYesNo == 1:
                #commonNoun = makePlural(commonNoun)
        pastPart = 'place holder'
        if demonAdj == 'These':
                commonNoun = makePlural(commonNoun)
        if demonAdj== 'Those':
                commonNoun = makePlural(commonNoun)
        #if commonNoun[-1] =='s':
                #tempword = commonNoun[:-1]
                #pastPart = random.choice(Lists.pastPartPairDict[tempword])
        pastPart = random.choice(Lists.languageRelatedPastPart)
        POSSESSIVEADJECTIVE2 = random.choice(Lists.possAdjList)
        COMMONNOUN2 = random.choice(Lists.commonNounList)
        #need to make random choice of plurality call
        if demonAdj == 'This':
                beVerb = chooseBeVerbSing1()
        if demonAdj == 'That':
                beVerb = chooseBeVerbSing1()
        if demonAdj == 'These':
                beVerb = chooseBeVerbPlur()
        if demonAdj== 'Those':
                beVerb = chooseBeVerbPlur()
        mylist = random.choice(Lists.verbDict)	
        localpreplist = ['by','in']
        localprep = random.choice(localpreplist)
        
        # sentence structure
        sentence = demonAdj + " " + commonNoun + " " + beVerb + " " + pastPart + " " + localprep + " " + POSSESSIVEADJECTIVE2 + " " + COMMONNOUN2 + "."
        return sentence

    def thisTableWasMade(self):
        """Figure out this function."""

        demonAdj = random.choice(Lists.demonAdjList).title()	
        commonNoun = random.choice(Lists.thisTableWasMadeList.keys())
        pastPart = ''
        if demonAdj == 'These':
                commonNoun = makePlural(commonNoun)
        if demonAdj== 'Those':
                commonNoun = makePlural(commonNoun)
        if commonNoun[-1] =='s':
                tempword = commonNoun[:-1]
                pastPart = random.choice(Lists.thisTableWasMadeList[tempword])
        else:
                pastPart = random.choice(Lists.thisTableWasMadeList[commonNoun])
        POSSESSIVEADJECTIVE2 = random.choice(Lists.possAdjList)
        COMMONNOUN2 = random.choice(Lists.commonNounList)
        
        if demonAdj == 'This':
                beVerb = chooseBeVerbSing1()
        if demonAdj == 'That':
                beVerb = chooseBeVerbSing1()
        if demonAdj == 'These':
                beVerb = chooseBeVerbPlur()
        if demonAdj== 'Those':
                beVerb = chooseBeVerbPlur()
        mylist = random.choice(Lists.verbDict)	
        localpreplist = ['by','in']
        localprep = random.choice(localpreplist)
        
        # sentence structure
        sentence = demonAdj + " " + commonNoun + " " + beVerb + " " + pastPart + " " + localprep + " " + POSSESSIVEADJECTIVE2 + " " + COMMONNOUN2 + "."
        return sentence
