import names
import random
import csv

#data-items = 500
#Spy AGENT
def generate_agent():
    status_list = ['Retired', 'Deployed', 'Ready', 'MIA', 'KIA']
    agent_id_set = list()
    agent_list = list()
    for i in range(0, 500):
        agent_name = names.get_full_name()  #generate random name
        #agent_id is unique
        if len(agent_id_set) == 0:
            agent_id = random.randint(10000, 99999) #agent_id is a 5-digit number
        else:
            agent_id = random.randint(10000, 99999) #agent_id is a 5-digit number
            while agent_id in agent_id_set:
                agent_id = random.randint(10000, 99999) #agent_id is a 5-digit number
        agent_id_set.append(agent_id)
        agent_status = random.choice(status_list)   #randomly select a status
        agent_salary = random.randint(50000, 200000)   #random pay
        agent_emergency_contact = random.randint(0,1000000000) #random phone #
        #add to set of agents
        agent_list.append(tuple((agent_id, agent_name, agent_status, agent_salary, agent_emergency_contact)))

    #write file
    with open('agent_list_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerows(agent_list)
generate_agent()

#Spy FIREARM
def generate_firearm():
    #read country txt
    country = open("countries.txt", 'r')
    #country = csv.reader(country, delimiter = '\n')
    country = tuple(country.readlines())
    type_list = ['rifle', 'pistol']
    make_list = ["ScottCLE added Smith & Wesson", "Heckler & Koch", "Sig Sauer", "Colt Defense", "Springfield Armory, Inc.", "Sturm, Ruger & Co., Inc."]
    country = list(country)
    print(country)
    serial_no_set = list()
    firearm_list = list()
    for i in range(0, 500):
        origin = random.choice(country) #random country
        origin = origin.rstrip()
        caliber = random.choice([0.221, 0.224])   #choose either russian and NATO bullet diameters
        firearm_type = random.choice(type_list)   #choose rifle or pistol
        make = random.choice(make_list) #make
        if len(serial_no_set) == 0:
            serial_no = random.randint(200000000, 700000000)   #unique serial no
        else:
            serial_no = random.randint(200000000, 700000000)   #unique serial no
            while serial_no in serial_no_set:
                serial_no = random.randint(200000000, 700000000)   #unique serial no
        serial_no_set.append(serial_no)
        cost = random.randint(50, 500)  #cost
        agent_id = random.choice(agent_id_set) #agent id
        #add to list of firearms
        t = tuple((origin, caliber, firearm_type, make, serial_no, cost, agent_id))
        firearm_list.append(t)
    #write firearm list files
    with open('firearm_list_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(firearm_list)

target_list = set()
target_code_name_list = set()
for _ in range(500):
    target_code_name = names.get_full_name()
    target_code_name_list.add(target_code_name)
    legal_name = names.get_full_name()
    # TODO: affiliation NULL for now
    affiliation = None
    target_list.add((target_code_name, legal_name, affiliation))
with open('target_list_file.csv', 'w+') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(target_list)

spy_list = set()
for _ in range(500):
    spy_code_name = names.get_full_name()
    # TODO: specialty NULL for now
    specialty = None
    target_code_name = random.choice(list(target_code_name_list))
    # TODO: affiliation NULL for now
    affiliation = None
    spy_list.add((spy_code_name, specialty, target_code_name, affiliation))
with open('spy_list_file.csv', 'w+') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(spy_list)

