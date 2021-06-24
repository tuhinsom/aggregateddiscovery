# aggregateddiscovery
git clone https://github.com/openai/gpt-2.git

cd gpt-2

pip install tensorflow==1.12

pip install -r requirements.txt

python download_model.py 124M




#study material:

python3.6 -m venv acg_gpt2_watson
cd ~/.virtualenvs
source ./acg_gpt2_watson/bin/activate
cd /var/www/html/ubm/informa/contentgeneration

git clone https://github.com/openai/gpt-2.git
cd gpt-2
pip install tensorflow==1.12
pip install -r requirements.txt
python download_model.py 124M

export PYTHONIOENCODING=UTF-8
File "/var/www/html/ubm/informa/contentgeneration/gpt-2/src/sample.py", line 28 replaced the 'tf.sort' with 'tf.contrib.framework.sort'
python src/generate_unconditional_samples.py | tee /tmp/samples


Watson:
https://cloud.ibm.com/services/discovery/crn%3Av1%3Abluemix%3Apublic%3Adiscovery%3Aeu-gb%3Aa%2Ffd8003d8ae88444ea37faad231e82152%3A57e1398d-8b4c-4fb6-9177-59d3bae8a16c%3A%3A?paneId=manage

API key: 
URL: https://api.eu-gb.discovery.watson.cloud.ibm.com/instances/57e1398d-8b4c-4fb6-9177-59d3bae8a16c

pip install --upgrade "ibm-watson>=5.1.0"


CODE:
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import ApiException

authenticator = IAMAuthenticator('{apikey}')
discovery = DiscoveryV1(
    version='2019-04-30',
    authenticator=authenticator
)
discovery.set_service_url('https://api.us-east.discovery.watson.cloud.ibm.com')

try:
    discovery.set_detailed_response(True)
    response = discovery.methodName(
        parameters,
        headers = {
            'Custom-Header': '{header_value}'
        })
    # Access response from methodName
    print(json.dumps(response.get_result(), indent=2))
    # Access information in response headers
    print(response.get_headers())
    # Access HTTP response status
    print(response.get_status_code())
except ApiException as ex:
    print "Method failed with status code " + str(ex.code) + ": " + ex.message


---------------------------- query discovery from watson console ----------------------------
query concepts: https://cloud.ibm.com/docs/discovery?topic=discovery-query-concepts
https://eu-gb.discovery.watson.cloud.ibm.com/regions/eu-gb/services/crn%3Av1%3Abluemix%3Apublic%3Adiscovery%3Aeu-gb%3Aa%2Ffd8003d8ae88444ea37faad231e82152%3A57e1398d-8b4c-4fb6-9177-59d3bae8a16c%3A%3A/environments/system/collections/news-en/query/discovery
1. Search with = "Top topics in the US agriculture Industry"

2.nested(enriched_text.entities).filter(enriched_text.entities.type::Company).filter(enriched_text.entities.sentiment.score>=0.8).term(enriched_text.entities.text)

3. enriched_text.categories.label::/business and industrial/agriculture and forestry/agriculture

4. https://app.inferkit.com/demo Search with


https://api.eu-gb.discovery.watson.cloud.ibm.com/instances/57e1398d-8b4c-4fb6-9177-59d3bae8a16c/v1/environments/system/collections/news-en/query?version=2018-12-03&aggregation=nested%28enriched_text.entities%29.filter%28enriched_text.entities.type%3A%3ACompany%29.filter%28enriched_text.entities.sentiment.score%3E%3D0.8%29.term%28enriched_text.entities.text%29&filter=enriched_text.categories.label%3A%3A%2Fbusiness%20and%20industrial%2Fagriculture%20and%20forestry%2Fagriculture&deduplicate=false&highlight=true&passages=true&passages.count=5&natural_language_query=Top%20topics%20in%20the%20US%20agriculture%20Industry


----------------------------flask API server ----------------------------
pip install Flask
kill -9 $(lsof -t -i:8555)
python apis/fetchsearch.py
