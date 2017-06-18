import pandas as pd
import yaml
import six

class MetricsUtil(object):
    @staticmethod
    def get_metrics(file_list):

        file_data = dict()
        service_data = dict()

        cont_file = 0
        cont_service = 0

        # parses each file
        for file_path in file_list:
            with open(file_path, "r") as stream:
                yaml_file = yaml.load(stream)

            # if there is any service
            if yaml_file.get("services"):
                services = yaml_file.get("services")
                version_number = yaml_file.get("version")
            else:
                services = yaml_file
                version_number = None

            number_of_services = len(services)

            # TODO version
            # TODO networks

            file_data["f: ({})".format(cont_file)] = pd.Series([number_of_services, version_number],
                                                               ["#services", "versionNumber"])

            # loop through services
            for s in services:

                # if the file has no service key
                if yaml_file.get(s):
                    service = yaml_file.get(s)
                else:
                    service = services[s]

                ports = service.get("ports") or []
                number_of_ports = len(ports)

                depends_on = service.get("depends_on") or []
                number_of_depends_on = len(depends_on)

                volumes = service.get("volumes") or []
                number_of_volumes = len(volumes)

                service_data["s: ({})".format(cont_service)] = pd.Series(
                    [number_of_ports, number_of_depends_on, number_of_volumes],
                    ["#ports", "#depends_on", "#volumes"])

                cont_service += 1

            cont_file += 1

        return file_data, service_data
