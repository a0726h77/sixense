#Leet Translator
#This will translate
#Normal english into
#l33t.
#Credit to: baavgai
#Cladus - 15/06/2012
version = 4
def toLeet(text):
	leet = (
                (('are', 'Are'), 'r'),
                (('ate', 'Ate'), '8'),
                (('that', 'That'), 'tht'),
		(('you', 'You'), 'j00'),
		(('o', 'O'), '0'),
		(('i', 'I'), '1'),
		(('e', 'E'), '3'),
		(('s', 'S'), '5'),
		(('a', 'A'), '4'),
		(('t', 'T'), '7'),
		)
	for symbols, replaceStr in leet:
		for symbol in symbols:
			text = text.replace(symbol, replaceStr)
	return text
def toEnglish(leet):
	eng = (
		('0','o'),
		('1','i'),
		('3','e'),
		('5','s'),
		('4', 'a'),
		('7', 't'),
                (' r ', 'are'),
                ('8', 'ate'),
                ('tht', 'that'),
		('joo', 'you'),
		)
	for symbols, replaceStr in eng:
		leet = leet.replace(symbols, replaceStr)
	return leet



