from mathemeticians import simple_get
from bs4 import BeautifulSoup
from find_candidates import find_candidates, find_locations

def skeleton_scrape(url):
	step_two = simple_get(url)
	step_three = BeautifulSoup(step_two, 'html.parser')
	step_four = []
	for p in step_three.select('p'):
		step_four.append(p)
	step_five = find_candidates(step_four)
	step_six = find_locations(step_five)
	return step_six
