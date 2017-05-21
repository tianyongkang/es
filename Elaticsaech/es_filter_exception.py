#-*- coding:UTF-8 -*-

import es_config_file
import es_get_data 


def excute_es_alert():
    index = es_config_file.Es_index().es_get_index()
    print index
    for i in index:
        es_get_data.Es_Alert_filter(i).es_get_filter()

#excute_es_alert()

excute_es_alert()