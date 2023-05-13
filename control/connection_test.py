def connection_in():
    json_string = """{
		"taskID" : 0,
		"pos_s_x" : 0,
		"pos_s_y" : 0,
		"pos_e_x" : 0,
		"pos_e_y" : 0
	}"""
    print('data in')
    return json_string

def connection_out(hello):
    print('data out')
    print(hello)
    return 0