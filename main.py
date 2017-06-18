import pandas as pd

from file_util import FileUtil
from metrics_util import MetricsUtil

# read the list of files
file_list = FileUtil.get_files_from_directory("input")

file_data, service_data = MetricsUtil.get_metrics(file_list)

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
