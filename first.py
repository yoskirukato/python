from datetime import datetime

filename = 'input512.txt' 
with open(filename, 'r') as file:
    with open('timeSheet.txt', 'a') as f:
        lines = file.readlines()
        datas = []
        for line in lines:
            class_in_out, _, id, _, time, _, date = line.strip().split(" ")
            exist = False
            for data in datas:
                if data['id'] == id:
                    exists_date = False
                    for date_ in data['date']:
                        if date in date_:
                            date_[date][class_in_out] = time
                            exists_date = True
                            break
                    if not exists_date:
                        data['date'].append({date: {class_in_out: time}})
                    exist = True
                    break
            if not exist:
                data = {'id': id, 'date': [{date: {class_in_out: time}}]}
                datas.append(data)

        outputs = []
        for data in datas:
            output = {'id': data['id'], 'date': []}
            values = data['date']
            for value in values:
                for key in value:
                    start = value[key]['ClockIN']
                    stop = value[key]['ClockOUT']
                    date_start = datetime.strptime(start, '%H:%M:%S')
                    date_stop = datetime.strptime(stop, '%H:%M:%S')
                    delta = date_stop - date_start
                    output['date'].append({key: str(delta)})
            outputs.append(output)
        for output in outputs:
            print(output)
            f.write('{id: ' + output['id'])
            f.write(', date: ' + str(output['date']))
            f.write("}\n")
        f.close()
