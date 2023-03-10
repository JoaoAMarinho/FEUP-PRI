# Define custom decorator to automatically calculate metric based on key
metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f)

@metric
def ap(results, relevant):
    """Average Precision"""
    precision_values = [
        len([
            doc
            for doc in results[:idx+1]
            if doc['tconst'] in relevant
        ]) / (idx + 1)
        for idx in range(0, len(results))
        if results[idx]['tconst'] in relevant
    ]
    return sum(precision_values)/len(precision_values)

@metric
def ap10(results, relevant, n=10):
    """Average Precision"""
    precision_values = [
        len([
            doc
            for doc in results[:idx+1]
            if doc['tconst'] in relevant
        ]) / (idx + 1)
        for idx in range(0, n)
        if results[idx]['tconst'] in relevant
    ]
    return sum(precision_values)/len(precision_values)

@metric
def map(results, _):
    """Mean Average Precision"""
    return sum(results)/len(results)

@metric
def p10(results, relevant, n=10):
    """Precision at 10"""
    return len([doc for doc in results[:n] if doc['tconst'] in relevant])/n

@metric
def p15(results, relevant, n=15):
    """Precision at 15"""
    return len([doc for doc in results[:n] if doc['tconst'] in relevant])/n

@metric
def ia(results, relevant, n=10):
    """Individual Assessment at 10"""
    return "".join(["R" if doc['tconst'] in relevant else "N" for doc in results[:n]])

def calculate_metric(key, results, relevant=None):
    return metrics[key](results, relevant)
