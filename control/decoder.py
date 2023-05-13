from connection import connection_in, connection_out

def decoder_taskQueue():
    while True:
        New_data = connection_in()
        if(New_data == None):
            print('no new task in Queue')
        else:
            print('new task updated')
            print(New_data['pos_s_x'])
            print(New_data['pos_s_y'])
            print(New_data['pos_e_x'])
            print(New_data['pos_e_y'])