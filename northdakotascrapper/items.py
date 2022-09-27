# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NorthdakotascrapperItem(scrapy.Item):
    # define the fields for your item here like:
    ID = scrapy.Field()
    TITLE = scrapy.Field()
    SUB_TITLE = scrapy.Field()
    FILING_DATE = scrapy.Field()
    RECORD_NUM = scrapy.Field()
    STATUS = scrapy.Field()
    STANDING = scrapy.Field()
    ALERT = scrapy.Field()
    CAN_REINSTATE = scrapy.Field()
    CAN_FILE_AR = scrapy.Field()
    CAN_ALWAYS_FILE_AR = scrapy.Field()
    CAN_FILE_REINSTATEMENT = scrapy.Field()

    REGISTERED_AGENT = scrapy.Field()
    COMMERCIAL_REGISTERED_AGENT = scrapy.Field()
    OWNERS = scrapy.Field()

    # Filing Type
    # Status
    # Standing - AR
    # Standing - RA
    # Standing - Other
    # Formed In
    # Term of Duration
    # Initial Filing Date
    # Principal Address
    # Mailing Address
    # AR Due Date
    # Registered Agent
    # Owner Name
    # Owner Address
    # Nature of Business
    # Expiration Date
    # Commercial Registered Agent
    # Owners
    # None
    # Delayed Effective Date
    # Filing Subtype

