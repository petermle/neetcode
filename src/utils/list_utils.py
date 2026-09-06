# utility for normalizing lists for comparison of contents, rather than order
def normalize(groups):
    return sorted([sorted(group) for group in groups])
