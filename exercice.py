#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
def get_num_letters(text):
	return len([lettre for lettre in text if 64<ord(lettre)<91 or 96<ord(lettre)<123])

def get_word_length_histogram(text):
	text = text.strip().split(" ")
	histogram = []
	for mot in text:
		lenght = get_num_letters(mot)
		try:
			histogram[lenght] += 1
		except:
			histogram += [0 for x in range(lenght - len(histogram)+1)]
			histogram[lenght] += 1

	return histogram

def format_histogram(histogram):
	return "\n".join([f"{x} {'*'*histogram[x]}" for x in range(1,len(histogram))])

def format_horizontal_histogram(histogram: list) -> str:
	histogram.pop(0)
	lenght_hist, max_histogram = len(histogram), max(histogram)
	return "\n".join(["".join([chr(124 - 92*(histogram[x]<max_histogram-y)) for x in range(lenght_hist)]) for y in range(max_histogram)])+"\n"+"¯"*lenght_hist




if __name__ == "__main__":
	spam = "Stop right there criminal scum! shouted the guard confidently."
	eggs = get_word_length_histogram(spam)
	print(eggs, "\n")
	print(format_histogram(eggs), "\n")
	print(format_horizontal_histogram(eggs))
