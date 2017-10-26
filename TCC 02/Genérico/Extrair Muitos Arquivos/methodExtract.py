# -*- coding: UTF-8 -*-

def yourMethodExtractExample(string, ini):
	text = ""
	i = ini;

	while i < len(string):
		if (string[i] != " "):
			text += string[i]
		if (string[i] == " "):
			break
		i += 1

	return text