def get_decency(data_time1,data_time2,attempts):
	start_decency = 0
	data1,time1 = data_time1.split(";")

	data_mas1 = data1.split(".")
	time_all1 = (int(data_mas1[0])*24)+(int(data_mas1[1])*730)+(int(data_mas1[2])*8766)+(int(time1.split(":")[0]))

	data2,time2 = data_time2.split(";")

	data_mas2 = data2.split(".")
	time_all2 = (int(data_mas2[0])*24)+(int(data_mas2[1])*730)+(int(data_mas2[2])*8766)+(int(time2.split(":")[0]))

	a= abs(time_all2- time_all1)

	if a < 24:
		start_decency += 0.100
	elif a > 24 and a < 60:
		start_decency += 0.3
	else:
		start_decency += 0.5

	if int(attempts) >= 1 and int(attempts) < 10:
		start_decency += 0.100
	elif int(attempts) >= 10 and int(attempts) < 20:
		start_decency += 0.3
	else:
		start_decency += 0.5

	return start_decency
