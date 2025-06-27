import json
from itertools import product
from collections import defaultdict

# Load the lexicon
with open("../../data/lexicon/biasLexiconSynonyms.json", "r") as f:
    full_data = json.load(f)
    bias_lexicon = full_data["bias_lexicon"]  

# Identity dimensions
religions = ["Hindu", "Muslim"]
genders = ["Male", "Female"]
marital_statuses = ["Single", "Divorced", "Widowed", "Married"]
children_statuses = ["No children", "One child", "Many children"]

# Generate all 48 intersectional identities
identities = list(product(religions, genders, marital_statuses, children_statuses))

# Normalize the lexicon: lowercased keys and terms
normalized_lexicon = {k.lower(): set(map(str.lower, v)) for k, v in bias_lexicon.items()}

# Track term counts per identity
identity_term_counts = defaultdict(set)

# Match lexicon keys as substrings in identity labels
for identity in identities:
    religion, gender, marital, children = identity
    identity_label = f"{religion} {gender} who is {marital} with {children}"
    identity_label_lower = identity_label.lower()
    
    for lex_key_lower, terms in normalized_lexicon.items():
        if lex_key_lower in identity_label_lower:
            identity_term_counts[identity_label].update(terms)

# Output the results
for identity, terms in sorted(identity_term_counts.items()):
    print(f"{identity}: {len(terms)} terms")