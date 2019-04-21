import names
import random
import csv
import generate_data_v2 as gd
import insert_data as id

#generate_data
gd.generate_target()
gd.generate_common_location()
gd.generate_target_sighting()
gd.generate_unit()
gd.generate_foreign_spy_organization()
gd.generate_agent()
gd.generate_spy()
gd.generate_foreign_spy()
gd.generate_home_spy()
gd.generate_gadget()
gd.generate_alias()
gd.generate_firearm()
gd.generate_other()
gd.generate_operator()
gd.generate_alias()
gd.generate_foreign_spy_sighting()
gd.generate_means_of_contact()
print("Data generated")

#execute insert commands
id.insert_agent()
id.insert_firearm()
id.insert_target()
id.insert_unit()
id.insert_spy()
id.insert_home_spy()
id.insert_foreign_spy_organization()
id.insert_foreign_spy()
id.insert_foreign_spy_sighting()
id.insert_common_location()
id.insert_target_sighting()
id.insert_operator()
id.insert_alias()
id.insert_other()
id.insert_means_of_contact()
print("Data inserted")
