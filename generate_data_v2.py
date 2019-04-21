import names
import random
import csv
import datetime
from faker import Faker
fake = Faker()
#global data
agent_id_set = list()
target_code_name_list = list()
spy_code_name_list = list()
unit_id_list = list()
home_spy_id_set = list()
foreign_spy_name_list = list()
other_name_list = list()
operator_code_list = list()
#const data
spy_organization = ['M.I.5', 'C.I.A.', 'K.G.B.', 'F.S.B.','M.S.S.', 'D.G.S.I.', 'N.I.S.', 'Reconnaissance General Bureau']
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
    type_list = ['rifle', 'pistol']
    make_list = ["ScottCLE added Smith & Wesson", "Heckler & Koch", "Sig Sauer", "Colt Defense", "Springfield Armory, Inc.", "Sturm, Ruger & Co., Inc."]
    serial_no_set = list()
    firearm_list = list()
    for _ in range(100):
        origin = fake.country() #random country
        caliber = random.choice([221, 224])   #choose either russian and NATO bullet diameters
        firearm_type = random.choice(type_list)   #choose rifle or pistol
        make = random.choice(make_list) #make
        #serial_no
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
    target_list = list()
    for _ in range(200):
        if len(target_code_name_list) == 0:
            target_code_name = names.get_full_name()
        else:
            target_code_name = names.get_full_name()
            while target_code_name in target_code_name_list:
                target_code_name = names.get_full_name()
        target_code_name_list.append(target_code_name)
        legal_name = names.get_full_name()
	    # TODO: affiliation NULL for now
        affiliation = None
        target_list.append((target_code_name, legal_name, affiliation))
    with open('target_list_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(target_list)

#Spy SPY
def generate_spy():
    spy_list = set()
    for _ in range(500):
        #spy_code_name
        if len(spy_code_name_list) == 0:
            spy_code_name = names.get_full_name()
        else:
            spy_code_name = names.get_full_name()
            while spy_code_name in spy_code_name_list:
                spy_code_name = names.get_full_name()
        spy_code_name_list.append(spy_code_name)
        #TODO: specialty NULL for now
        specialty = None
        target_code_name = random.choice(list(target_code_name_list))
        spy_list.add((spy_code_name, specialty, target_code_name))
    with open('spy_list_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(spy_list)

#Spy HOME_SPY
def generate_home_spy():
    home_spy_id_list = list()
    home_spy_list = list()
    for spy in range(300):
        #differnet from foreign spy
        spy_code_name = spy_code_name_list[spy + 200]
        current_location = fake.country()
        #unit_id
        unit_id = random.choice(unit_id_list)
        #home_spy_id = agent_id
        if len(home_spy_id_list) == 0:
            home_spy_id = random.choice(agent_id_set) #agent_id is a 5-digit number
        else:
            home_spy_id = random.choice(agent_id_set) #agent_id is a 5-digit number
            while home_spy_id in home_spy_id_list:
                home_spy_id = random.choice(agent_id_set) #agent_id is a 5-digit number
        home_spy_id_list.append(home_spy_id)
        home_spy_list.append(tuple((spy_code_name, current_location, unit_id, home_spy_id)))
    with open('home_spy_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(home_spy_list)

#Spy ALIAS
def generate_alias():
    alias_list = list()
    alias_code_name_list = list()
    for spy in range(500):
        spy_code_name = spy_code_name_list[spy]
        alias_code_name_list.append(spy_code_name)
        name = names.get_full_name()
        address = fake.address()
        while len(address) > 45:
            address = fake.address()
        occupation = fake.job()
        while len(address) > 45:
            occupation = fake.job()
        alias_list.append((spy_code_name, name, address, occupation))
    with open('alias_list_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(alias_list)

#Spy UNIT
def generate_unit():
    unit_list = list()
    for _ in range(200):
        #unit_id - primary
        if len(unit_id_list) == 0:
            unit_id = random.randint(100000000, 700000000)
        else:
            unit_id = random.randint(100000000, 700000000)
            while unit_id in unit_id_list:
                unit_id = random.randint(100000000, 700000000)
        unit_id_list.append(unit_id)
        budget = random.randint(1000, 500000)
        #get target code name
        target_code_name = random.choice(list(target_code_name_list))
        unit_list.append(tuple((unit_id, budget, target_code_name)))
    with open('unit_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(unit_list)

#Spy FOREIGN_SPY_ORGANIATION
def generate_foreign_spy_organization():
    locations = ['United Kingdom', 'U.S.A.', 'Soviet Union', 'Russia', 'Republic of China', 'France', 'South Korea', 'North Korea']
    relationships = ['FRIENDLY', 'NEUTRAL', 'HOSTILE']
    spy_organization_list = list()
    for org in range(len(spy_organization)):
        org_name = spy_organization[org]
        origin = locations[org]
        relationship = random.choice(relationships)
        spy_organization_list.append(tuple((org_name, origin, relationship)))
    with open('foreign_spy_organization.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(spy_organization_list)

#Spy GADGET
def generate_gadget():
    gadget_list = list()
    service_tag_list = list()
    for _ in range(500):
        #unique service tag
        if len(service_tag_list) == 0:
            service_tag = random.randint(10000, 99999)
        else:
            service_tag = random.randint(10000, 99999)
            while service_tag in service_tag_list:
                service_tag = random.randint(10000, 99999)
        service_tag_list.append(service_tag)
        cost = random.randint(1000, 500000)
        #TODO: description NULL for now
        description = None
        agent_id = random.choice(agent_id_set)
        gadget_list.append((service_tag, cost, description, agent_id))
    with open('gadget_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(gadget_list)

#Spy FOREIGN_SPY
#200 foreign spies
def generate_foreign_spy():
    foreign_spy_list = list()
    for spy in range(200):
        #spy_code_name is in the spy_code_name_list
        spy_code_name = spy_code_name_list[spy]#first 200 spies - foreign spies
        foreign_spy_name_list.append(spy_code_name)
        org_name = random.choice(spy_organization)#random org_name
        foreign_spy_list.append(tuple((spy_code_name, org_name)))
    with open('foreign_spy.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(foreign_spy_list)

#Spy FOREIGN_SPY_SIGHTING
def generate_foreign_spy_sighting():
    foreign_spy_sighting_list = list()
    spy_name_list = list()
    for _ in range(200):
        #spy_code_name
        if len(spy_name_list) == 0:
            spy_code_name = random.choice(foreign_spy_name_list)
        else:
            spy_code_name = random.choice(foreign_spy_name_list)
            while spy_code_name in spy_name_list:
                spy_code_name = random.choice(foreign_spy_name_list)
        date =  fake.date()
        address = fake.address()
        while len(address) > 45:
            address = fake.address()
        foreign_spy_sighting_list.append((spy_code_name, date, address))
    with open('foreign_spy_sighting_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(foreign_spy_sighting_list)

#Spy COMMON_LOCATION
def generate_common_location():
    target_name_list = list()
    common_locations = list()
    for _ in range(200):
        if len(target_name_list) == 0:
            target_code_name = random.choice(target_code_name_list)
        else:
            target_code_name = random.choice(target_code_name_list)
            while target_code_name in target_name_list:
                target_code_name = random.choice(target_code_name_list)
        target_name_list.append(target_code_name)
        address = fake.address()
        while len(address) > 45:
            address = fake.address()
        common_locations.append(tuple((target_code_name, address)))
    with open('common_location_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(common_locations)

#Spy Target Sighting
def generate_target_sighting():
    target_name_list = list()
    target_sighting_list = list()
    for _ in range(200):
        if len(target_name_list) == 0:
            target_code_name = random.choice(target_code_name_list)
        else:
            target_code_name = random.choice(target_code_name_list)
            while target_code_name in target_name_list:
                target_code_name = random.choice(target_code_name_list)
        target_name_list.append(target_code_name)
        date = fake.date()
        address = fake.address()
        while len(address) > 45:
            address = fake.address()
        target_sighting_list.append((target_code_name, date, address))
    with open('target_sighting_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(target_sighting_list)

#Spy Other
def generate_other():
    other_list = list()
    for _ in range(100):
        #other different from home_spy
        if len(other_name_list) == 0:
            other_code = random.choice(agent_id_set)
            while other_code in home_spy_id_set:
                other_code = random.choice(agent_id_set)
        else:
            other_code = random.choice(agent_id_set)
            while other_code in other_name_list or other_code in home_spy_id_set:
                other_code = random.choice(agent_id_set)
        other_name_list.append(other_code)
        job = fake.job()
        other_list.append((other_code, job))
    with open("other_file.csv", 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(other_list)

#Spy OPERATOR
def generate_operator():
    operator_list = list()
    for _ in range(100):
        if len(operator_code_list) == 0:
            operator_code = random.choice(agent_id_set)
            while operator_code in other_name_list:
                other_code = random.choice(other_name_list)
        else:
            operator_code = random.choice(agent_id_set)
            while operator_code in other_name_list or operator_code in operator_code_list:
                operator_code = random.choice(agent_id_set)
        operator_code_list.append(operator_code)
        unit_id = random.choice(unit_id_list)
        operator_list.append((operator_code, unit_id))
    #write files
    with open('operator_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(operator_list)

#Spy MEANS_OF_CONTACT
def generate_means_of_contact():
    means_of_contact_list = list()
    means_of_contact_code_list = list()
    for _ in range(100):
        #an unique operator id
        if len(means_of_contact_code_list) == 0:
            operator_id = random.choice(operator_code_list)
        else:
            opeartor_id = random.choice(operator_code_list)
            while operator_id in means_of_contact_code_list:
                operator_id = random.choice(operator_code_list)
        means_of_contact_code_list.append(operator_id)
        contact_line = random.randint(1000000000, 7000000000)#phone number
        satellite_link_address = fake.ipv6()
        delivery_point = fake.coordinate()
        means_of_contact_list.append((operator_id, contact_line, satellite_link_address, delivery_point))
    #write files
    with open('means_of_contact_file.csv', 'w+') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(means_of_contact_list)
