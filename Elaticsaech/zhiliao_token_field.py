from elasticsearch import Elasticsearch,exceptions
import datetime 
import xlsxwriter

def get_token_request_url():
    es = Elasticsearch([{"host":"10.253.2.125","port":9200}])
    date = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y.%m.%d")
    try:
        e = es.search( index="logstash-zhiliao-tomcat-log-%s" % date, fields='token,request_url',size=10000000)['hits']['hits']
        dkeys = [] 
        for i in e:
            if "fields" in i.keys():
                token = i['fields']['token']
                url = i['fields']['request_url']
                if "null" not in token:
                    d = dict(zip(url,token))    
                    dkeys.append(d)
        return dkeys
    except exceptions.NotFoundError,e:
        print e


def main():
    p = get_token_request_url()
    keys = []
    values = []
    for i in p:
        keys.append(i.keys()[0])
        values.append(i.values()[0])
    
    date = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    
    key_tuple = tuple(keys)
    value_tuple = tuple(values)
    workbook = xlsxwriter.Workbook('/Users/tianyongkang/Desktop/zhiliao_token_%s.xlsx' % date)
    worksheet = workbook.add_worksheet()
    worksheet.set_h_pagebreaks([20])
    worksheet.write_column('A1', key_tuple)
    worksheet.write_column('B1', value_tuple)
    workbook.close()
    
    
 
if __name__ == "__main__":
    main()

