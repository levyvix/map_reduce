import json
from urllib import request, parse
from itertools import chain
from pathos.multiprocessing import ProcessingPool as Pool
import networkx as nx


def link_to_title(link):
    return link["title"]


def clean_if_key(page, key):
    if key in page:
        return map(link_to_title, page[key])


def get_wiki_links(page_title):
    safe_title = parse.quote(page_title)
    url = (
        "https://en.wikipedia.org/w/api.php"
        f"?action=query&prop=links|linkshere&pllimit=500&lhlimit=500&titles={safe_title}&format=json&formatversion=2"
    )
    page = request.urlopen(url).read()
    j = json.loads(page)
    jpage = j["query"]["pages"][0]
    inbound = clean_if_key(jpage, "links")
    outbound = clean_if_key(jpage, "linkshere")
    return {"title": page_title, "in_links": list(inbound), "out_links": list(outbound)}


def flatten_network(page):
    return page["in_links"] + page["out_links"]


def page_to_edges(page):

    a = [(page["title"], p) for p in page["out_links"]]
    b = [(p, page["title"]) for p in page["in_links"]]
    return a + b


if __name__ == "__main__":
    root = get_wiki_links("Parallel_computing")
    initial_network = flatten_network(root)

    with Pool() as p:
        network = p.map(get_wiki_links, initial_network)
        edges = p.map(page_to_edges, network)
    edges = chain.from_iterable(edges)

    G = nx.DiGraph()
    for e in edges:
        G.add_edge(*e)
    nx.readwrite.gexf.write_gexf(G, "./MyGraph.gexf")
