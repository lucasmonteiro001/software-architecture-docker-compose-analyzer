import pandas as pd
import yaml

MAX = 1000000


class MetricsUtil(object):
    @staticmethod
    def get_metrics(file_list):

        errors = list()
        file_data = dict()
        service_data = dict()

        cont_file = 0
        cont_service = 0
        cont_max = 0

        # parses each file
        for file_path in file_list:

            try:
                # print cont_max
                # print "\t" + file_path

                if cont_max >= MAX:
                    break

                cont_max += 1

                with open(file_path, "r") as stream:
                    yaml_file = yaml.load(stream)

                # if there is any service
                if yaml_file.get("services"):
                    services = yaml_file.get("services")
                    version_number = yaml_file.get("version")

                    if version_number > 0:
                        version_number = int(float(version_number))

                    number_of_networks = len(yaml_file.get("networks") or [])
                else:
                    services = yaml_file
                    version_number = 0
                    number_of_networks = 0

                number_of_services = len(services)

                file_data["f: ({})".format(cont_file)] = pd.Series(
                    [number_of_services, version_number, number_of_networks],
                    ["#services", "version_number", "#networks"])

                # loop through services
                for s in services:

                    # remove data that was stored for unprocessed file
                    try:
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

                    except Exception:
                        # remove data that was stored for unprocessed file
                        try:
                            del service_data["s: ({})".format(cont_service)]
                        except Exception:
                            pass

                        raise "error"

                cont_file += 1

            except Exception:
                print "error: " + file_path
                errors.append(file_path)

                # remove data that was stored for unprocessed file
                try:
                    del file_data["f: ({})".format(cont_file)]

                except Exception:
                    pass

        # save error logs
        with open("errors.txt", "w") as f:
            for l in errors:
                f.write(l)
                f.write("\n")

        return file_data, service_data
