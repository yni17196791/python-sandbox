import json
import requests

"""
**set your access token**
1.sinup Google cloud pratform.(GCP)
1.install google cloud sdk and setup it,
2.get service-account key file from GCP (it's maybe json file)
3.type command "gcloud auth activate-service-account --key-file=XXXXXXXXXXXXX.json"
4.type command "gcloud auth print-access-token"
5.token show display .  copy it and set this file and run.
more detail:
https://cloud.google.com/translate/docs/premium
"""
token = 'ya29.c.El8mBdLlfDe4x8dCqjjzJFl1robng4DvRHNo0pv9uZzWwB_lu_1wF59ym1mM18bZtX4CO7Z_IEh0e7QUVz3SaGrGtCvoOFNPgQvLwa1PvPjP3QVdgqP6KkhyQoFU8iY4Wg' # set token here

#REST api / "premium translation" url not euqal "normal transration" url !
url = "https://translation.googleapis.com/language/translate/v2"
#oldurl = "https://www.googleapis.com/language/translate/v2"

# translate / en -> ja
source = "en"
target = "ja"

# new translation needed
model = "nmt"

# translate target chars / must be less than 2K characters.
# see : https://cloud.google.com/translate/docs/translating-text#translate-translate-text-python
# this is sample chars from : http://web-tan.forum.impressrd.jp/e/2016/11/17/24396
q = "GMP Production process and repeated experience is readily available to supply this peptide API including all CMC documentation necessary for registration. There is specific know-how available for microencapsulation of these peptides for slow release dosage forms. Gonadotropin-releasing hormone (GnRH), also known as Luteinizing-hormone-releasing hormone (LHRH) and luliberin, is a trophic peptide hormone responsible for the release of follicle-stimulating hormone (FSH) and luteinizing hormone (LH) from the anterior pituitary. This group of peptides (LHRH and analogues) are used in the treatment of breast and prostate cancer and precocious puberty, estrogen-dependent conditions (such as endometriosis or uterine fibroids)." # 長いので省略してます

payload = {
    'target':target,
    'source':source,
    'q':q,
    'model':model
}

headers = {
    'Content-Type':'application/json',
    'Authorization': 'Bearer ' + token,
}

response = requests.get(url,params=payload,headers=headers)

# JSON decode
jObj = json.loads(response.text)

print(jObj)
