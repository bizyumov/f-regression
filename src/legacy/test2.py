import scholarly

author_name = '"Philippe Smets"'
# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author(author_name)
author = next(search_query).fill()
print('Info for %s: %s' % (author_name, author))

# Print the titles of the author's publications
print('List of publications: ')
print([pub.bib['title'] for pub in author.publications])

# Take a closer look at the first publication
print('Most cited publication: ')
pub = author.publications[0].fill()
print(pub)

# Which papers cited that publication?
print([citation.bib['title'] for citation in pub.get_citedby()])