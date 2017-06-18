import pandas as pd

from file_util import FileUtil
from metrics_util import MetricsUtil

# read the list of files
file_list = FileUtil.get_files_from_directory("old_input")

file_data, service_data = MetricsUtil.get_metrics(file_list)

df_file = pd.DataFrame(file_data)
df_file = df_file.T

df_service = pd.DataFrame(service_data)
df_service = df_service.T


def get_sum(data_frame, key):
    print "\nSum: " + key
    return data_frame[key].sum()


def get_mean(data_frame, key):
    print "\nMean: " + key
    return data_frame[key].mean()


def get_distribution(data_frame, key):
    print "\nDist: " + key
    return data_frame[key].value_counts()


print "\n\n"
print df_file
print get_sum(df_file, "#services")
print get_mean(df_file, "#services")
print get_distribution(df_file, "#services")
print get_distribution(df_file, "version_number")
print get_sum(df_file, "#networks")
print get_mean(df_file, "#networks")
print get_distribution(df_file, "#networks")

exit()
print "\n\n"
print df_service
# print get_sum(df_service, "#services")
# print get_mean(df_service, "#services")
# print get_distribution(df_service, "version_number")



# print "\n\n"
# # print df_service
# df_service_sum = get_sum(df_service)
# df_service_mean = get_mean(df_service)
# print df_service_sum
# print df_service_mean
