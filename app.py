# # app.py
# from flask import Flask, render_template, request
# from SPARQLWrapper import SPARQLWrapper, JSON

# app = Flask(__name__)

# # Set up the SPARQL endpoint
# sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# sparql.setReturnFormat(JSON)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     results = []
#     if request.method == 'POST':
#         search_query = request.form['search_query']
        
#         # Define your SPARQL query with the user's input
#         query = f"""
#         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#         PREFIX dbo: <http://dbpedia.org/ontology/>
#         PREFIX dct: <http://purl.org/dc/terms/>
#         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

#         SELECT DISTINCT ?subject ?label ?thumbnail ?abstract WHERE {{
#             ?subject rdf:type dbo:Person .
#             ?subject rdfs:label ?label .
#             OPTIONAL {{ ?subject dbo:thumbnail ?thumbnail . }}
#             OPTIONAL {{ ?subject dbo:abstract ?abstract . }}
#             FILTER (lang(?label) = "en" && lang(?abstract) = "en" && CONTAINS(LCASE(?label), LCASE("{search_query}")) )
#         }}
#         LIMIT 10
#         """

#         # Execute the query and convert results to JSON format
#         sparql.setQuery(query)
#         response = sparql.query().convert()
        
#         # Extracting bindings from the response
#         results = response.get("results", {}).get("bindings", [])

#     return render_template('index.html', results=results)

# if __name__ == '__main__':
#     app.run(debug=True)




















# #app.py
# from flask import Flask, render_template, request
# from SPARQLWrapper import SPARQLWrapper, JSON

# app = Flask(__name__)

# # Set up the SPARQL endpoint (DBpedia)
# sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# sparql.setReturnFormat(JSON)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     results = []
#     if request.method == 'POST':
#         search_query = request.form['search_query']
        
#         # Define your SPARQL query with the user's input
#         query = f"""
#         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#         PREFIX dbo: <http://dbpedia.org/ontology/>
#         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

#         SELECT DISTINCT ?subject ?label ?thumbnail ?abstract WHERE {{
#             ?subject rdf:type dbo:Person .
#             ?subject rdfs:label ?label .
#             OPTIONAL {{ ?subject dbo:thumbnail ?thumbnail . }}
#             OPTIONAL {{ ?subject dbo:abstract ?abstract . }}
#             FILTER (lang(?label) = "en" && lang(?abstract) = "en" && CONTAINS(LCASE(?label), LCASE("{search_query}")) )
#         }}
#         LIMIT 10
#         """

#         # Execute the query and convert results to JSON format
#         sparql.setQuery(query)
#         response = sparql.query().convert()
        
#         # Extracting bindings from the response
#         results = response.get("results", {}).get("bindings", [])

#     return render_template('index.html', results=results)

# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, request, redirect, url_for
# from SPARQLWrapper import SPARQLWrapper, JSON

# app = Flask(__name__)

# # Set up the SPARQL endpoint (DBpedia)
# sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# sparql.setReturnFormat(JSON)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     results = []
#     if request.method == 'POST':
#         search_query = request.form['search_query']
        
#         # Define your SPARQL query with the user's input
#         query = f"""
#         PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#         PREFIX dbo: <http://dbpedia.org/ontology/>
#         PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

#         SELECT DISTINCT ?subject ?label WHERE {{
#             ?subject rdfs:label ?label .
#             FILTER (lang(?label) = "en" && CONTAINS(LCASE(?label), LCASE("{search_query}")))
#         }}
#         LIMIT 10
#         """

#         # Execute the query and convert results to JSON format
#         sparql.setQuery(query)
#         response = sparql.query().convert()
        
#         # Extracting bindings from the response
#         results = response.get("results", {}).get("bindings", [])

#     return render_template('index.html', results=results)

# @app.route('/article/<title>')
# def article(title):
#     # Redirect to the corresponding Wikipedia page
#     return redirect(f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}")

# if __name__ == '__main__':
#     app.run(debug=True)



# app.py
from flask import Flask, render_template, request, redirect, url_for
from SPARQLWrapper import SPARQLWrapper, JSON

app = Flask(__name__)

# Set up the SPARQL endpoint (DBpedia)
sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql.setReturnFormat(JSON)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        search_query = request.form['search_query']
        
        # Define your SPARQL query with the user's input
        query = f"""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT DISTINCT ?subject ?label WHERE {{
            ?subject rdfs:label ?label .
            FILTER (lang(?label) = "en" && CONTAINS(LCASE(?label), LCASE("{search_query}")))
        }}
        LIMIT 10
        """

        # Execute the query and convert results to JSON format
        sparql.setQuery(query)
        response = sparql.query().convert()
        
        # Extracting bindings from the response
        results = response.get("results", {}).get("bindings", [])

    return render_template('index.html', results=results)

@app.route('/article/<title>')
def article(title):
    # Define a SPARQL query to get detailed information about the selected article
    query = f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?abstract ?thumbnail WHERE {{
        <http://dbpedia.org/resource/{title.replace(' ', '_')}> rdfs:label ?label .
        OPTIONAL {{ <http://dbpedia.org/resource/{title.replace(' ', '_')}> dbo:abstract ?abstract . }}
        OPTIONAL {{ <http://dbpedia.org/resource/{title.replace(' ', '_')}> dbo:thumbnail ?thumbnail . }}
        FILTER (lang(?label) = "en" && lang(?abstract) = "en")
    }}
    LIMIT 1
    """
    
    sparql.setQuery(query)
    response = sparql.query().convert()
    
    # Extracting details from the response
    details = response.get("results", {}).get("bindings", [])
    
    return render_template('article.html', title=title, details=details)

if __name__ == '__main__':
    app.run(debug=True)
