try:
    from flask import app,Flask
    from flask_restful import Resource, Api, reqparse
    import elasticsearch
    from elasticsearch import Elasticsearch
    import datetime
    import concurrent.futures
    import requests
    import json
except Exception as e:
    print("Modules Missing {}".format(e))


app = Flask(__name__)
api = Api(app)

#------------------------------------------------------------------------------------------------------------

NODE_NAME = 'autocomplete'
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#------------------------------------------------------------------------------------------------------------


"""
{
"wildcard": {
    "title": {
        "value": "{}*".format(self.query)
    }
}
}

"""


# mapping using  search_as_you_type
# interestingly it is using skip-gram techniques. so, we can add additional filter as well in future.
# 
"""

curl --request PUT 'http://localhost:9200/autocomplete' \
--header 'Content-Type: application/json' \
-d '{
   "mappings": {
       "properties": {
           "title": {
               "type": "search_as_you_type"
           },
           "genre": {
               "type": "search_as_you_type"
           }
       }
   }
}'
 

"""


class Controller(Resource):
    def __init__(self):
        self.query = parser.parse_args().get("query", None)
        self.baseQuery= {
            "size": 10,
            "query": {
                "multi_match": {
                    "query": "{}".format(self.query),
                    "type": "bool_prefix",
                    "fields": [
                        "title",
                        "title._2gram",
                        "title._3gram"
                    ]
                }
            }
        }
        # self.baseQuery ={
        #     "_source": [],
        #     # "size": 0,
        #     # "min_score": 0.5,
        #     "query": {
        #         "bool": {
        #             "must": [
        #                 {
        #                     "match_phrase_prefix": {
        #                         "title": {
        #                             "query": "{}".format(self.query)
        #                         }
        #                     }
        #                 }
        #             ],
        #             "filter": [],
        #             "should": [],
        #             "must_not": []
        #         }
        #     },
        #     "aggs": {
        #         "auto_complete": {
        #             "terms": {
        #                 "field": "title.keyword",
        #                 "order": {
        #                     "_count": "desc"
        #                 },
        #                 "size": 25
        #             }
        #         }
        #     }
        # }

    def get(self):

        # print("print to get something!")
        # autocomp;ete retunr size suggesion
        default_size = 10
        res = es.search(index=NODE_NAME, size = default_size,  body=self.baseQuery)

        return res


parser = reqparse.RequestParser()
parser.add_argument("query", type=str, required=True, help="query parameter is Required ")

api.add_resource(Controller, '/autocomplete')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
