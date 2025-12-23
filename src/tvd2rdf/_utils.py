import yaml
from pathlib import Path
from rdflib import URIRef
from urllib.parse import quote

default_base = "http://example.org/"

def load_config():
    config_file_path = Path(__file__).parent / "config.yaml"
    with open(config_file_path,"r") as f:
        try:
            c = yaml.safe_load(f)
            return c
        except yaml.YAMLError as e:
            print(e)


def toLowerCamelCase(s):
    """Converts a string to lowerCamelCase."""
    # convert to a list
    l = s.strip().replace("_", " ").replace("-", " ").split(" ")
    # convert inital letter of first word to lc but leave anything that is already in CamelCase
    word1 = l[0]
    if word1 == word1.upper():
        r = word1.lower()  # don't camel case words that are all UC, e.g. URL
    else:
        r = word1[0].lower() + word1[1:]
    # convert inital letters of the rest to UC but leave anything that is alread in CamelCase
    for word in l[1:]:
        t = word[0].capitalize() + word[1:].lower()
        r = r + t
    return r

def convert_namespace(prefix:str, uri:str):
    ns = dict()
    if (type(prefix) == str) and (type(uri) == str):
        if (len(prefix) == 0) or prefix == ":":
            prefix = "default"
        elif (prefix[-1]) == ":":
            prefix = prefix[:-1]
        else:
            pass
        ns[prefix] = uri
    else:
        msg = "Both prefix and URI must be strings."
        raise TypeError(msg)
    return ns

def str2URIRef(namespaces, s):
    """Return a URIRef from a string that may be a URI or a curie."""
    if type(namespaces) is dict:
        pass
    else:
        msg = "Namespaces should be a dictionary."
        raise TypeError(msg)
    if type(s) is str and len(s) > 0:
        pass
    else:
        msg = "Value to convert should be a non-empty string."
        raise TypeError(msg)
    if "base" in namespaces.keys():
        base = namespaces["base"]
    else:
        base = default_base
    if ":" in s:
        [pre, name] = s.split(":", 1)
        if pre.lower() in ["http", "https"]:  # TODO: make this configurable
            return URIRef(s)
        elif pre in namespaces.keys():
            return URIRef(namespaces[pre] + name)
        else:
            # TODO logging/exception warning that prefix not known
            msg = "Prefix " + pre + " not in namespace list."
            raise ValueError(msg)
    else:
        # there's no prefix, convert to URI using base & URI safe str
        if (s[0] == "#") and (base[-1] == "#"):
            s = s[1:]
        return URIRef(base + quote(s))