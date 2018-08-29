#!/usr/bin/python3

# make variations on "I like cats" for the English Program Website


from Clean_Code_Lists import Lists
lists = Lists()
total_variations = []
sentence_pattern = ("pronoun", "verb", "noun")


pronouns = []
for word in lists.singular_pronouns:
    pronouns.append(word)
for word in lists.plural_pronouns:
    pronouns.append(word)
pronoun_choices = len(pronouns)


def i_like_cats():
    """Random sentence generator of the sentence pattern 'I like cats.',
        returns String."""
    pronoun = random.choice(Lists.pronouns)
    verb = 'like'
    noun = random.choice(Lists.commonNounList) #make this specific to grade 1 common noun
    if ((pronoun in Lists.pluralPronouns) or (pronoun == 'I')):
            pass
    #elif pronoun == 'I':
            #pass
    else:
            verb += 's'
    if pronoun != 'name and name':
            pronoun = pronoun.title()
    elif pronoun == 'name and name':
            name1 = random.choice(Lists.nameList)
            name2 = random.choice(Lists.nameList)
            pronoun = name1.title() + ' and ' + name2.title()
    if pronoun == 'name':
            pronoun = random.choice(Lists.nameList)
    if noun in ListMod.countableNouns:
            noun = makePlural(noun)
    sentence = [pronoun, verb, noun]
    iLike = ' '.join(sentence)
    iLike += "."
    return iLike
    

verbs = ['assist', 'attract', 'believe', 'borrow', 'bring', 'build', 'burn', 'buy', 'call', 'carry', 'catch', 'celebrate', 'change', 'choose', 'collect', 'cook', 'count', 'cover', 'cut', 'design', 'eat', 'enjoy', 'feel', 'fight', 'find', 'follow', 'get', 'give', 'grow', 'have', 'help', 'hold', 'keep', 'know', 'like', 'love', 'make', 'meet', 'receive', 'see', 'send', 'show', 'study', 'take', 'teach', 'thank', 'understand', 'visit', 'walk', 'want', 'wash', 'watch', 'win', 'hear', 'hit', 'hurt', 'influence', 'invite', 'lend', 'need', 'package', 'push', 'raise', 'recycle', 'reduce', 'remember', 'reuse', 'ride', 'save', 'scare', 'sell', 'serve', 'shake', 'sort', 'kill', 'melt', 'miss', 'notice', 'plant', 'produce','respect', 'share', 'shock', 'smell', 'spend', 'support', 'surround', 'swallow', 'throw', 'touch', 'trap', 'trust']
verb_choices = len(verbs)



##for word in lists.verbs:
##    print(word)
##    my_choice = input("y_n")
##    if my_choice == "y":
##        verbs.append(word)
##
##print(verbs)


noun_choices = len(lists.nouns)
print(lists.nouns[:100])

print("pronoun_choices =", pronoun_choices)
print("verb_choices =", verb_choices)
print("noun_choices =", noun_choices)
##
print("total possible =", pronoun_choices * verb_choices * noun_choices)




