from Services.weather import get_weather
from Services.crypto import get_crypto
from Services.air import get_pollution
from Functions.weathercity import get_weather_by_input
from Functions.bmicalculator import get_bmi
from Functions.recursive import get_factorial

import json
import markdown
import streamlit as st

st.set_page_config(page_title='Gift of Athena', page_icon='🎃', layout="wide", initial_sidebar_state="auto")

weather_data = get_weather()
crypto_data = get_crypto()
pollution_data = get_pollution()

# image_data = get_image_by_keyword('mouse')

# weather_by_city_data = get_weather_by_input(option)

# Weather city selection
selected_city = 'Berlin'

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

colFull, = st.columns(1)

col1, col2, col3 = st.columns(3)

with st.container():
    with colFull:
        st.header("Αθηνόδωρος Μπουδουράκης")
        st.subheader('Προχωρημένα Θέματα Τεχνολογίας Λογισμικού (CEI 521)')

with st.container():
    with col1:
        st.header("Τοπική θερμοκρασία")
        st.caption('Πρόγνωση για τις επόμενες 10 ημέρες')
        with st.expander("Πληροφορίες"):
            st.info(
                '- λήψη δεδομένων σε csv μορφή από "weather.visualcrossing.com" και επεξεργασία τους για προβολή δεδομένων σε πίνακα από data frame',
                icon="ℹ️")
            st.caption('Κώδικας')
            code = '''from csv import reader
import sys
from urllib import request
from urllib import error
import pandas as pd


def get_weather():
    try:
        result_bytes = request.urlopen(
            "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Limassol?unitGroup"
            "=metric&include=days&key=ACRB86QG8FL6QRU43EGJ26W8V&contentType=csv").read().decode("UTF-8")
        # print("ResultBytes", ResultBytes)
        array = result_bytes.splitlines()
        table_data = []
        for line in reader(array):
            table_data.append(line)

        df_columns = ["Περιοχή", "Ημερομηνία", "Θερμοκρασία (°C)", "Μικρότερη (°C)", "Μεγαλύτερη (°C)"]
        df_rows = []
        for lineIndex in range(1, len(table_data)):
            originalDate = table_data[lineIndex][1].split("-")
            refinedDate = "/".join(originalDate)
            df_rows.append([table_data[lineIndex][0],
                           refinedDate,
                           table_data[lineIndex][4] + " °C",
                           table_data[lineIndex][3],
                           table_data[lineIndex][2]])
        return pd.DataFrame(data=df_rows, columns=df_columns).style.hide_index()

    except error.HTTPError as e:
        error_info = e.read().decode()
        print("Error code: ", e.code, error_info)
        sys.exit()
    except error.URLError as e:
        error_info = e.read().decode()
        print("Error code: ", e.code, error_info)
        sys.exit()


dfResult = get_weather()
# print(dfResult)
'''
            st.code(code, language='python')
        st.dataframe(weather_data)

    with col2:
        st.header("Kρυπτονομίσματα")
        st.caption('Αξία και διακύμανση ψηφιακών νομισμάτων')
        with st.expander("Πληροφορίες"):
            st.info(
                '- λήψη δεδομένων σε μορφή json και εξαγωγή πληροφοριών σε dictionary από api.coinstats.app',
                icon="ℹ️")
            st.caption('Κώδικας')
            code = '''from csv import reader
import json
import sys
from urllib import request
from urllib import error
import pandas as pd


def get_crypto():
    try:
        result_bytes = request.urlopen(
            "https://api.coinstats.app/public/v1/coins?skip=0&limit=20&currency=EUR").read().decode('UTF-8')
        array = result_bytes.splitlines()
        dictionary = json.loads(array[0])

        coins_array = json.loads(array[0])
        pd_df = pd.DataFrame.from_dict(coins_array)
        coins_from_pd_df = pd_df['coins']
        expanded_coins = (coins_from_pd_df.explode().tolist())

        data_frame = pd.DataFrame.from_dict(dictionary)

        df_from_df = pd.DataFrame.from_records(coins_array)

        data_rows = []

        for ind in data_frame.index:
            data_rows.append(data_frame.loc[ind]['coins'])

        custom_columns = ['name', 'symbol', 'price', 'priceChange1h', 'priceChange1d', 'priceChange1w']

        refined_data_frame = pd.DataFrame(data=data_rows, columns=custom_columns)

        # renaming the DataFrame columns
        refined_data_frame.rename(columns={
            'name': 'Όνομα',
            'symbol': 'Σύμβολο',
            'price': 'Αξία ($)',
            'priceChange1h': 'Αυξομείωση 1 ώρα',
            'priceChange1d': 'Αυξομείωση 1 ημέρα',
            'priceChange1w': 'Αυξομείωση 1 εβδομάδα',
        },
            inplace=True)

        return refined_data_frame

    except error.HTTPError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()
    except error.URLError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()


dfResult = get_crypto()
        '''
            st.code(code, language='python')
        st.dataframe(crypto_data)

    with col3:
        st.header("Ποιότητα αέρα")
        st.caption(pollution_data[0])
        with st.expander("Πληροφορίες"):
            st.info(
                '- λήψη δεδομένων σε μορφή json από api.waqi.info. επεξεργασία και μετατροπή σε data frame με τα επιθυμητά πεδία ',
                icon="ℹ️")
            st.caption('Κώδικας')
            code = '''import json
import sys
from urllib import request
from urllib import error
import pandas as pd


def get_pollution():
    try:
        result_bytes = request.urlopen(
            "https://api.waqi.info/feed/here/?token=6991a7e7db2339c3304b0bbf7e057effbb1e98f8").read(

        ).decode(
            'UTF-8')
        dictionary = json.loads(result_bytes)

        cityData = dictionary['data']['city']
        greek_city_info = cityData['name'].split(',')[1]
        city_info = greek_city_info.split('  ')[0]
        pollution = dictionary['data']['iaqi']

        valuesArray = []

        table_columns = ['Ρύπος', 'Τιμή']
        table_rows = []

        for key in pollution:
            table_rows.append([key, pollution[key]['v']])
            valuesArray.append({key: pollution[key]['v']})
        return [city_info, pd.DataFrame(data=table_rows, columns=table_columns)]

    except error.HTTPError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()
    except error.URLError as e:
        error_info = e.read().decode()
        print('Error code: ', e.code, error_info)
        sys.exit()


dfResult = get_pollution()
        '''
            st.code(code, language='python')
        st.dataframe(pollution_data[1])

with st.container():
    with col1:
        st.header("Θερμοκρασία για επιλεγμένη περιοχή")
        with st.expander("Πληροφορίες"):
            st.info(
                '- WeatherProxy : λήψη επιλεγμένης περιοχής από μια λίστα με διαθέσιμες πόλεις και χρήση ως '
                'παράμετρος στη υπηρεσία "weather.visualcrossing.com". Χρησιμοποιήθηκε cloud function γραμμένη σε '
                'Javascript στο Azure Functions με λειτουργία σαν Mediator Service (wrapper/proxy)',
                icon="ℹ️")
            st.caption('Κώδικας')
            code = '''const axios = require('axios');

module.exports = async function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');
    const targetLocation = req.query.city || 'Limassol';
    const weatherDataResponse = await axios.get(`https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/${targetLocation}?unitGroup=metric&key=ACRB86QG8FL6QRU43EGJ26W8V&contentType=csv&include=days`);
    context.res = {
        // status: 200, /* Defaults to 200 */
        body: weatherDataResponse.data
    };
}
        '''
            st.code(code, language='python')
        option = st.selectbox(
            "επιλέξτε πόλη για να προβάλετε την πρόγνωση θερμοκραίας για τις επόμενες 10 μέρες",
            ("Limassol", "Nicosia", "Thessaloniki", "Athens", "Moscow"),
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )
        weather_by_city_data = get_weather_by_input(option)
        st.subheader(option)
        st.dataframe(weather_by_city_data)
    with col2:
        st.header("Υπολογισμός Δείκτη Μάζας Σώματος (BMI)")
        with st.expander("Πληροφορίες"):
            st.info(
                '- εκτέλεση μιας μεθόδου γραμμένη στο Azure functions με παραμέτρους ύψος κια βάρος για υπολογισμό '
                'του BMI ως '
                'BMI = weight/ height²',
                icon="ℹ️")
            st.caption('Κώδικας')
            code = '''module.exports = async function (context, req) {
    context.log('JavaScript HTTP trigger function processed a request.');

    const height = (req.query.height || (req.body && req.body.height));
    const weight = (req.query.weight || (req.body && req.body.weight));

    const BMI = weight / (height ** 2);

    let result = '';

    if (BMI < 18.5) {
        result = "Ο Δείκτης Μάζας Σώματος (BMI) βρίσκεται στο ελλιποβαρής εύρος";
    } else if ((BMI > 18.5) && (BMI < 24.9)) {
        result = "Ο Δείκτης Μάζας Σώματος (BMI) βρίσκεται στο κανονικό ή υγιές εύρος";
    } else if ((BMI > 25) && (BMI < 29.9)) {
        result = "Ο Δείκτης Μάζας Σώματος (BMI) βρίσκεται στο υπέρβαρες εύρος";
    } else {
        result = "Ο Δείκτης Μάζας Σώματος (BMI) βρίσκεται στο εύρος παχυσαρκίας";
    }
    context.res = {
        // status: 200, /* Defaults to 200 */
        body: result
    };
}
        '''
            st.code(code, language='python')
        height = st.text_input(
            "εισάξατε ύψος (σε μέτρα)",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )
        weight = st.text_input(
            "εισάξατε βάρος (σε κιλά)",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )
        if st.button('Ανάλυση'):
            bmi_result = get_bmi(height, weight)
            st.subheader(bmi_result or '')
    with col3:
        st.header("Παραγοντικό")
        with st.expander("Πληροφορίες"):
            st.info(
                '- εκτέλεση μιας μεθόδου γραμμένη στο Azure functions με παράμετρο ένα ακαίρεο όπου υπολογίζεται το '
                'παραγοντικό του καθώς και ο αριθμός αναδρομικών εκτελέσεων',
                icon="ℹ️")
            st.caption('Κώδικας')
            code = '''/**
 * Factorial function as a custom web service
 * - calculates the factorial of the provided number
 * and returns the result along with the number the recursive function was triggered
 *
 * !!!NOTE!!!: in factorials, the amount of recursion executed is meaningless mathematically as it is just the number provided
 * but is still provided in the results as an indication of the measuring feature of a recursive function, that could
 * indicate or estimate the cost of a recursive function applied for different uses such as machine learning model
 * training
 *
 * @param context
 * @param req
 * @returns {Promise<void>}
 */
module.exports = async function (context, req) {
    // context.log('JavaScript HTTP trigger function processed a request.');

    /**
     * Check if number parameter dose not exist or is 0 which is treated as false, but has result in factorials
     */
    if(req.query && req.query.number && (parseInt(req.query.number) === 0)) {
        // console.log('number is', parseInt(req.query.number));
        if(parseInt(req.query.number) === 0) {
            context.res = {
                // status: 200, /* Defaults to 200 */
                body: {
                    result: '1',
                    count: 'η συνάρτηση καλέστηκε 1 φορά'
                }
            };
            return;
        }
    }

    /** initialize number variable **/
    let numberInput = 0;

    /** check if parameter is passed as query param and parse it to integer **/
    if(req.query && req.query.number) {
        console.log('number is', parseInt(req.query.number));
        numberInput = parseInt(req.query.number);
    }

    /** check if parameter is passed as a body param and parse it to integer **/
    if(req.body && req.body.number && (typeof req.body.number === 'string')) {
        numberInput = parseInt(req.body.number);
    }

    /** check if there are no parameters provided */
    if((!req.query)&&(!req.body)) {
        context.res = {
            // status: 200, /* Defaults to 200 */
            body: {
                result: 'N/A',
                count: 'N/A'
            }
        };
        return;
    }

    /** check if any of the parameters contain the number value and proceed to the factorial calculation **/
    if (req.query?.number || (req.body && req.body.number)) {

        numberInput = (req.query.number || (req.body && req.body.number));

        if (!numberInput) {
            context.res = {
                // status: 200, /* Defaults to 200 */
                body: 'Could not get number param'
            };
        }

        let result;

        let recur_count = 0;

        /**
         * Recursive function that re-calls itself and appends the multiplied result recursively
         * @param current_number {number} - the current number received by the function trigger
         * @returns {number|*} - returns the multiplied current value by the result of the recursion iteration
         */
        const recursive_factorial_function = (current_number) => {
            recur_count += 1;
            if (current_number === 1) {
                return current_number
            } else {
                return current_number * recursive_factorial_function(current_number - 1)
            }
        };

        if (numberInput < 0) {
            // result = "Το παραγοντικό δεν υφίσταται για αρνητικούς αριθμούς";
            result = "N/A";
            recur_count = 'Το παραγοντικό δεν υφίσταται για αρνητικούς αριθμούς';
        } else if (numberInput === 0) {
            // result = 'το παραγοντικό του 0 είναι 1 και η συνάρτηση καλέστηκε ' + 1 + 'φορά';
            result = "1";
            recur_count = `η συνάρτηση καλέστηκε 1 φορά`;
        } else {
            const resulting_number = recursive_factorial_function(numberInput)
            // result = `το παραγοντικό του ${numberInput} είναι ${resulting_number} και η συνάρτηση καλέστηκε ${recur_count} φορές`
            result = JSON.stringify(resulting_number);
            recur_count = `η συνάρτηση καλέστηκε ${recur_count} φορές`;
        }

        context.res = {
            // status: 200, /* Defaults to 200 */
            body: {
                result: result,
                count: recur_count
            }
        };
    } else {
        context.res = {
            // status: 200, /* Defaults to 200 */
            body: {
                result: 'N/A',
                count: 'N/A'
            }
        };
    }
}

        '''
            st.code(code, language='python')

        with st.expander("Σημείωση!"):
            st.info('Η πληροφορία για τον αριθμό επαναλήψεων για τον υπολογισμό του παραγοντικού είναι μαθηματικά '
                    'περιττή καθώς ως δεδομένο θα ισούτε με τον δοθέντα αριθμό, αλλά συμπεριλήφθηκε για προβολή της '
                    'δυνατότητας παρακολούθησης των επαναλήψεων που θα μπορούσαν να φανούν χρήσιμα για τον '
                    'υπολογισμό/εκτίμιση εκτέλεσης παρόμοιας μεθόδου σε εφαρμογές μηχανικής μάθησης.', icon="ℹ️")
        number = st.text_input(
            "εισάξατε ακαίραιο αριθμό",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )
        if st.button('Υπολογισμός'):
            factorial_result = get_factorial(number)
            result = json.loads(factorial_result)
            st.subheader(result["result"] or '')
            st.subheader(result["count"] or '')

