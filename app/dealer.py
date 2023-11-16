import streamlit as st
import pandas as pd
from utils import calculate_pmt
from typing import Tuple, List
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="SFM Dealer Portal", layout="wide")
col1, col2, col3 = st.columns(3)
col1.image('pics/_Logo_2.png',use_column_width=True)

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """

st.markdown(hide_default_format,unsafe_allow_html=True)

st.title('RTO Deal Builder')

tab1, tab2, tab3, tab4 = st.tabs(['1. Customer Information','2. Trailer Information','3. Contract Information', '4. Document Uploads'])

# Initialize a dictionary to store the inputs
@st.cache_data
def start_gathering():
    return {}

# Do a verify through out the form
def verify(user_data:dict)-> Tuple[bool,List[str]]:
    """
    
    Loop through and Check for missing data in the user's input data. 
    Could be augmented to call other functions or APIs down the road. 
    Not being used right now in the Demo App. See `tab1` code in dealer.py 
    to see a sample implementation.
    
    """

    invalid_fields = []
    for field, value in user_data.items():
        if value == '':
            invalid_fields.append(field)
    if len(invalid_fields)>0:
        return tuple([False,invalid_fields])
    else:
        return tuple([True, []])

# Just caches the input on the server --> returns a hashtable, dictionary, whatever. NBD.
input_data = start_gathering()

with tab1:
    st.write('Enter Customer Info')
    col1, col2, col3 = tab1.columns(3)
    with col1:
        input_data['last_name'] = st.text_input('Last Name',value='')
        input_data['first_name'] = st.text_input('First Name',value='')
        input_data['street_addr'] = st.text_input('Street Address',value='')
        input_data['city'] = st.text_input('City',value='')
        input_data['state'] = st.text_input('State',value='')
        input_data['zip'] = st.text_input('Zip',value='')
    with col2:
        input_data['dl_no'] = st.text_input('DL#',value='')
        input_data['ss_no'] = st.text_input('SS',value='')
    with col3:
        input_data['home_phone'] = st.text_input('Home Phone',value='')
        input_data['cell_phone'] = st.text_input('Cell Phone',value='')
        input_data['employer'] = st.text_input('Name of Employer',value='')
        input_data['employer_phone'] = st.text_input('Employer Phone',value='')

# Sample verification run
show_verification_button = False
if show_verification_button:
    with tab1:
        if tab1.button('Submit'):
            verification = verify(user_data=input_data)
            if verification[0]==True:
                tab1.write('Success')
            else:
                tab1.write('Invalid fields found:')
                for invalid_field in verification[1]:
                    tab1.write(f':red[{invalid_field}]')
    

with tab2:
    st.write('Enter Trailer Information')
    input_data['trailer_condition'] = st.radio('',['NEW', 'USED'])
    col4, col5, col6 = tab2.columns(3)
    with col4:
        input_data['serial'] = st.text_input('VIN')
        input_data['gps'] = st.text_input('GPS #')
    with col5:
        input_data['brand'] = st.text_input('Trailer Brand')
        input_data['trailer_type'] = st.text_input('Trailer Type')
        input_data['size_l'] = st.text_input('Trailer Length')
        input_data['size_w'] = st.text_input('Trailer Width')
    

with tab3:
    st.write('Enter Contract Information')
    input_data['term'] = st.radio('Select Term (months)',[24,36,48])
    sales_tax_upfront = st.checkbox('Sales Tax Paid Upfront?')
    col7, col8, col9 = tab3.columns(3)    
    with col7:
        input_data['trailer_cost'] = st.number_input('Enter Trailer Cost')
        input_data['sales_price'] = st.number_input('Enter Trailer Cash Price',step=1000)
        input_data['down_payment'] = st.number_input('Enter Renter Down Payment',help='The total amount of Funds the borrower will put toward the RTO contract today')
    with col8:
        input_data['epo'] = st.number_input('Early Payoff Percent',value=0.5,min_value=0.5)
        input_data['sales_taxx_r'] = st.number_input('Sales Tax Rate')


    if tab3.button('Get Payment'):
        st.write('Calculated Monthly Payment:')
        pmt = calculate_pmt.get_pmt(input_data['sales_price'], input_data['term'])
        user_term = input_data['term']
        st.write(f'{user_term} @ {pmt}')

        st.write('PMT TABLE')
        table, idx = calculate_pmt.get_pmt_tbl()
        x = pd.DataFrame.from_dict(table)
        x.index = idx
        x = x.iloc[1:]
        x.index.name = 'Trailer Price'
        st.write(x)
    
with tab4:
    tab4.file_uploader('Upload Applicant Docs')
    if tab4.button('Submit'):
        tab4.write('Thank you. The deal is currently being reviewed. A Sterling Financial Management Representative will be in touch shortly')