import names
import random
import csv

#global data
agent_id_set = list()
target_code_name_list = set()
spy_code_name_list = set()
unit_id_list = list()
#data-items = 500
#Spy AGENT
def generate_agent():
    status_list = ['Retired', 'Deployed', 'Ready', 'MIA', 'KIA']
    agent_list = list()
    for _ in range(500):
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

#Spy FIREARM
def generate_firearm():
    #read country txt
    country = open("countries.txt", 'r')
    country = tuple(country.readlines())
    type_list = ['rifle', 'pistol']
    make_list = ["ScottCLE added Smith & Wesson", "Heckler & Koch", "Sig Sauer", "Colt Defense", "Springfield Armory, Inc.", "Sturm, Ruger & Co., Inc."]
    country = list(country)
    print(country)
    serial_no_set = list()
    firearm_list = list()
    for _ in range(500):
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
        firearm_list.append(tuple((origin, caliber, firearm_type, make, serial_no, cost, agent_id)))
    #write firearm list files
    with open('firearm_list_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(firearm_list)

#Spy TARGET
def generate_target():
    target_list = set()
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
#Spy SPY
def generate_spy():
    spy_list = set()
    for _ in range(500):
        spy_code_name = names.get_full_name()
        spy_code_name_list.add(spy_code_name)
        #TODO: specialty NULL for now
        specialty = None
        target_code_name = random.choice(list(target_code_name_list))
        #TODO: affiliation NULL for now
        affiliation = None
        spy_list.add((spy_code_name, specialty, target_code_name, affiliation))
    with open('spy_list_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        write.writerows(spy_list)

#Spy HOME_SPY
def generate_home_spy():
    country = open("countries.txt", 'r')
    country = tuple(country.readlines())
    home_spy_list = list()
    home_spy_id_set = list()
    for _ in range(500):
        spy_code_name = names.get_full_name()
        current_location = random.choice(country)
        current_location = current_location.rstrip('\n')
        #unit_id
        if len(unit_id_list) == 0:
            unit_id = random.randint(10000, 99999)
        else:
            unit_id = random.randint(10000, 99999)
            while unit_id in unit_id_list:
                unit_id = random.randint(10000, 99999)
        unit_id_list.append(unit_id)

        #home_spy_id = agent_id
        if len(agent_id_set) == 0:
            home_spy_id = random.choice(agent_id_set) #agent_id is a 5-digit number
        else:
            home_spy_id = random.choice(agent_id_set) #agent_id is a 5-digit number
            while home_spy_id in home_spy_id_set:
                home_spy_id = random.choice(agent_id_set) #agent_id is a 5-digit number
        home_spy_id_set.append(home_spy_id)

        home_spy_list.append(tuple((spy_code_name, current_location, unit_id, home_spy_id)))
    with open('home_spy_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(home_spy_list)

#Spy ALIAS
def generate_alias():
    alias_list = set()
    for _ in range(500):
        spy_code_name = random.choice(list(spy_code_name_list))
        name = names.get_full_name()
        # TODO: address and occupation attributes NULL for now
        address = None
        occupation = None
        alias_list.add((spy_code_name, name, address, occupation))
    with open('alias_list_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(alias_list)

#Spy UNIT
def generate_unit():
    unit_id_list_2 = list()
    unit_list = list()
    for _ in range(500):
        #unit_id - primary
        if len(unit_id_list_v2) == 0:
            unit_id = random.choice(unit_id_list)
        else:
            unit_id = random.choice(unit_id_list)
            while unit_id in unit_id_list_v2:
                unit_id = random.choie(unit_id_list)
        unit_id_list_2.append(unit_id)
        budget = random.randint(1000, 500000)
        target_code_name = random.choice(list(target_code_name_list))
        unit_list.append(tuple((unit_id, budget, target_code_name)))
    with open('unit_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(unit_list)

#Spy FOREIGN_SPY_ORGANIATION
def generate_foreign_spy_organization():
    spy_organization = ['M.I.5', 'C.I.A.', 'K.G.B.', 'F.S.B.','M.S.S.', 'D.G.S.I.', 'N.I.S.', 'Reconnaissance General Bureau']
    locations = ['United Kingdom', 'U.S.A.', 'Soviet Union', 'Russia', 'Republic of China', 'France', 'South Korea', 'North Korea']
    relationships = ['FRIENDLY', 'NEUTRAL', 'HOSTILE']
    spy_organization_list = list()
    for org in range(5):
        org_name = spy_organization[org]
        origin = locations[org]
        relationship = random.choice(relationships)
        spy_organization_list.append(tuple((org_name, origin, relationship)))
    with open('foreign_spy_organization.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(spy_organization_list)
        
#Spy GADGET
def generate_gadget():
    gadget_list = set()
    for _ in range(500);
        agent_id = random.choice(list(agent_id_set))
        service_tag = random.randint(10000, 99999)
        cost = random.randint(1000, 500000)
        #TODO: description NULL for now
        description = None
        gadget_list.add((agent_id, service_tag, cost, description))
    with open('gadget_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(gadget_list)


