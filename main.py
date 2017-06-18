import os

import pandas as pd
import yaml

FILE_METRICS_MAP = {
    "#services": 0
}

SERVICE_METRICS_MAP = {
    "#ports": 0,
    "#depends_on": 1,
    "#volumnes": 2
}

file_data = dict()
service_data = dict()

# read the list of files
file_list = os.listdir("input")

cont_file = 0
cont_service = 0

# parses each file
for file_name in file_list:
    with open("input/" + file_name, "r") as stream:
        yaml_file = yaml.load(stream)

    # if there is any service
    if yaml_file.get("service"):
        print "existe servico"
    else:
        number_of_services = len(yaml_file)

        # TODO version
        # TODO networks

        file_data["f: ({})".format(cont_file)] = pd.Series([number_of_services], ["#services"])

        # loop through services
        for service_name in yaml_file:

            service = yaml_file.get(service_name)

            ports = service.get("ports") or []
            number_of_ports = len(ports)

            depends_on = service.get("depends_on") or []
            number_of_depends_on = len(depends_on)

            volumes = service.get("volumes") or []
            number_of_volumes = len(volumes)

            service_data["s: ({})".format(cont_service)] = pd.Series(
                [number_of_ports, number_of_depends_on, number_of_volumes], ["#ports", "#depends_on", "#volumes"])

            cont_service += 1

        cont_file += 1

df_file = pd.DataFrame(file_data)
df_service = pd.DataFrame(service_data)


def get_sum(data_frame):
    return data_frame.sum(axis=1)


def get_mean(data_frame):
    return data_frame.mean(axis=1)


print "\n\n"
# print df_file
df_file_sum = get_sum(df_file)
df_file_mean = get_mean(df_file)
print df_file_sum
print df_file_mean

print "\n\n"
# print df_service
df_service_sum = get_sum(df_service)
df_service_mean = get_mean(df_service)
print df_service_sum
print df_service_mean