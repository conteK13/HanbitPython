def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])       #경로 압축기법(Path Compression)
    return parent[x]