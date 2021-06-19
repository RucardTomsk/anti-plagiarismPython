import shingles
import argparse
import decency
import final_app

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('arg', nargs=2)
 
    return parser

def main():
	parser = createParser()
	namespace = parser.parse_args()

	MAIN_FAIL = open("por.txt","r")
	mas = []
	for i in MAIN_FAIL:
		mas.append(i.strip())

	print(mas)

	lab1 = [mas[0].split(" "),mas[1].split(" "),mas[2].split(" ")]
	lab2 = [mas[3].split(" "),mas[4].split(" "),mas[5].split(" ")]
	lab3 = [mas[6].split(" "),mas[7].split(" "),mas[8].split(" ")]

	all_mas = [lab1,lab2,lab3]

	number_lab = int(namespace.arg[0])
	id_student = namespace.arg[1]
	fail_name = ""
	for i in all_mas[number_lab-1]:
		if i[0] == id_student:
			fail_name += i[2]
	data_time = ""
	for i in all_mas[number_lab-1]:
		if i[0] == id_student:
			data_time += i[3]
	k = ""
	for i in all_mas[number_lab-1]:
		if i[0] == id_student:
			k += i[4]
	#decency.get_decency(mas[0].split(" ")[3],mas[1].split(" ")[4])
	mas_d = []
	mas_i = []
	s_o = 0
	counter = 0

	for i in all_mas[number_lab-1]:
		if i[0] == id_student:
			continue
		else:
			shin = shingles.get_shingles(fail_name,i[2])
			if shin <= 0.6:
				mas_d.append(i[1])
				mas_i.append(i[2])
				s_o += shin
				counter += 1
	if counter != 0:
			s_o /= counter

	s_d = 0
	counter = 0

	for i in all_mas[number_lab-1]:
		if i[0] == id_student:
			continue
		else:
			d = decency.get_decency(data_time,i[3],k)
			s_d += d
			counter += 1
	if counter != 0:
			s_d /= counter

	print(final_app.finel(s_o,int(k),s_d,mas_d,mas_i))

if __name__ == '__main__':
	main()