ORDER_FILTER = [
    'status', "client__phone", "delivery__phone",
                        "client__id", "delivery__id", 'estimated_date'
]

ORDER_SEARCH = [ "client__phone", "delivery__phone",]