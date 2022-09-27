import json
import scrapy
import xmltodict

from northdakotascrapper.items import NorthdakotascrapperItem


class GetallSpider(scrapy.Spider):
    name = 'getall'
    allowed_domains = ['firststop.sos.nd.gov']
    start_urls = ['http://firststop.sos.nd.gov/']
    totalScrapped = 0

    def start_requests(self):
        url = "https://firststop.sos.nd.gov/api/Records/businesssearch"
        _body = {'SEARCH_VALUE': "X", 'STARTS_WITH_YN': 'true', "ACTIVE_ONLY_YN" : True}
        yield scrapy.Request( url, method='POST', 
                          body=json.dumps(_body), 
                          callback=self.parse,
                          headers={'Content-Type':'application/json'} )

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        l_rows = jsonresponse["rows"]
        for _key,_row in l_rows.items():
            business = NorthdakotascrapperItem()
            business["ID"] = _row["ID"]

            try:
                business["TITLE"] = self.clearString(_row["TITLE"][0])
                business["SUB_TITLE"] = self.clearString(_row["TITLE"][1])
            except:
                business["TITLE"] = ""
                business["SUB_TITLE"] = ""

            business["FILING_DATE"] = _row["FILING_DATE"]
            business["RECORD_NUM"] = _row["RECORD_NUM"]
            business["STATUS"] = _row["STATUS"]
            business["STANDING"] = _row["STANDING"]
            business["ALERT"] = _row["ALERT"]
            business["CAN_REINSTATE"] = _row["CAN_REINSTATE"]
            business["CAN_FILE_AR"] = _row["CAN_FILE_AR"]
            business["CAN_ALWAYS_FILE_AR"] = _row["CAN_ALWAYS_FILE_AR"]
            business["CAN_FILE_REINSTATEMENT"] = _row["CAN_FILE_REINSTATEMENT"]

            url = f"https://firststop.sos.nd.gov/api/FilingDetail/business/{_key}/false"
            yield scrapy.Request(url, callback=self.parse_details, cb_kwargs=dict(business=business))
    
    def parse_details(self, response, business):
        data = xmltodict.parse(response.text)
        #l_detail_list = data.get("DRAWER").get("DRAWER_DETAIL_LIST")
        for _list in data.get("DRAWER").get("DRAWER_DETAIL_LIST").get("DRAWER_DETAIL"):
            if _list.get("LABEL") == "Registered Agent":
                business["REGISTERED_AGENT"] = self.clearString((_list.get("VALUE")))
            elif _list.get("LABEL") == "Commercial Registered Agent":
                business["COMMERCIAL_REGISTERED_AGENT"] = self.clearString((_list.get("VALUE")))
            elif _list.get("LABEL") == "Owners":
                business["OWNERS"] = self.clearString((_list.get("VALUE")))
        self.totalScrapped = self.totalScrapped + 1
        print('\r' + f"Business Scraped: {self.totalScrapped}", end='', flush=True)
        yield business
    
    def clearString(self, _string):
        return _string.replace('\n', ' ').replace('\r', '')