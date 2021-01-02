import csv
from jinja2 import Environment, FileSystemLoader


def import_csv(file):
    csv_file= open(file, 'r')
    csv_reader = csv.reader(csv_file)
    return csv_reader

def csvtodict(csv_reader):
    ap_list= list()
    next(csv_reader)
    for ap in csv_reader:
        ap_dict= {}
        ap_dict['Name']= ap[0]
        ap_dict['Mac']= ap[1]
        ap_dict['ip_address']= ap[4]
        ap_dict['secret']= '2401humanity'
        ap_list.append(ap_dict)
    return {'ap': ap_list}

def create_template_from_csv(jinja_file,csv_list_of_dict):
    env=Environment(loader=FileSystemLoader('.'))
    template=env.get_template(jinja_file)
    ps= template.render(data = csv_list_of_dict)
    return ps

if __name__=='__main__':
    file= import_csv('access_points.csv')
    aps= csvtodict(file)
    powershell_commands= create_template_from_csv('radius_cmd.j2',aps)
    with open('powershell_cmd.txt', 'w') as file:
        file.write(powershell_commands)
