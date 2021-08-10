import time
import requests
import csv
import datetime


corrected_records = []


def convert_extension_case(url):
    """
    Some records could not resolved because of case sensitivity, where jpg should be JPG or vice versa.
    The function converts uppercase extension to lowercase extension and vice versa.
    :param url: url link to the multimedia file, should ends with file extension.
    :return: url with lower case extension converted to uppercase or vice versa.
    """
    # split at last "." gives ['https://zenodo.org/record/4942307/files/St24_BVV_A1', 'JPG']
    split_url = url.rsplit('.', 1)
    slug = split_url[0]
    extension = split_url[1]
    uppercase_extension = extension.upper()
    lowercase_extension = extension.lower()
    if split_url[1] == uppercase_extension:
        new_url = '{}.{}'.format(slug, lowercase_extension)
    else:
        new_url = '{}.{}'.format(slug, uppercase_extension)
    return new_url


def fix_url(file_path):
    """
    A function to fix url using `convert_extension_case` function above. Will write the records into new file under
    data/processed/ directory.
    :param file_path: Path to multimedia file
    :return:
    """
    today = datetime.datetime.now().date()
    with open(file_path) as f:
        tsv_file = csv.reader(f, delimiter="\t")
        for line in tsv_file:
            time.sleep(0.1)
            url = '{}'.format(line[3])
            r = requests.get(url)
            print(url, r.status_code)
            if r.status_code == 200:
                corrected_records.append(line)
            else:
                new_url = convert_extension_case(url)
                corrected_records.append([line[0], line[1], line[2], new_url, line[4], line[5], line[6], line[7], line[8]])
    fixed_url_file = './data/processed/{}_ANTAR-XXVII-multimedia.tsv'.format(today)
    with open(fixed_url_file, "w+") as outfile:
        tsv_writer = csv.writer(outfile, delimiter="\t")
        for line in corrected_records:
            tsv_writer.writerow(line)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fix_url("data/interim/2021-06-23_ANTAR-XXVII.xlsx-multimedia.tsv")
