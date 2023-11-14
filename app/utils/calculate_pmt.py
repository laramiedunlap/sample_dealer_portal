# This contains the math behind calculating Monthly Payments for RTO contracts. 
# However this is built on the server, it needs to be flexible and easy to update. 
# If this can be written in Python that would be great, because then I can build out more complexity as we incorporate more features into the underwriting model
# Or if it's just a route in the app, I could build the UW service as an API that could be called by the application... Actually that's probably a better long term solution. 

# Anyway here's the most basic math:

from typing import Union

def get_pmt(trailer_price:float,term:int)->Union[str,float]:
    if term not in [24,36,48]:
        return 'Term Length Not Currently Available'
    elif term == 24:
        return round(trailer_price/14,2)
    elif term == 36:
        return round(trailer_price/17,2)
    elif term == 48:
        return round(trailer_price/20.1,2)


def get_pmt_tbl():
    prices = [0,2_000,4_000,6_000,8_000,10_000,12_000]
    output_table = {}
    for term in [24,36,48]:
        output_table[str(term)] = []
        for price in prices:
            output_table[str(term)].append(get_pmt(price,term))
    return output_table, prices