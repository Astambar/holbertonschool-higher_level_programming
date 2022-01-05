#!/usr/bin/python3
def common_elements(set_1, set_2):
	if set_1:
		if set_2:
			tab = []
			for i in set_1:
				for j in set_2:
					if i == j:
						tab.append(i)
			return tab
