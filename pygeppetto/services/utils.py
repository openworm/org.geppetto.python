from pygeppetto.model import AQueryResult

# Use to distinguish QueryResult by ID in a set
def modified_hash(self):
    return hash(self.values[self._id_pos])
def modified_eq(self, other):
    return self.values[self._id_pos] == other.values[self._id_pos]

# Restore default set identification
def regular_hash(self):
    return super(AQueryResult, self).__hash__()
def regular_eq(self, other):
    return super(AQueryResult, self).__eq__(other)


def set_custom_query_result_hash(id_index):
    setattr(AQueryResult, '_id_pos', id_index)
    setattr(AQueryResult, '__eq__', modified_eq)
    setattr(AQueryResult, '__hash__', modified_hash)

def unset_custom_query_result_hash():
    setattr(AQueryResult, '_id_pos', None)
    setattr(AQueryResult, '__eq__', regular_eq)
    setattr(AQueryResult, '__hash__', regular_hash)