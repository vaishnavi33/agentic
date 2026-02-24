from rag.vector_store import VectorStore
def load_policies(file_path: str):
    with open(file_path, "r") as f:
        policies = f.read().split("\n")
    return [p.strip() for p in policies if p.strip()]

if __name__ == "__main__":
    vs = VectorStore()
    docs = load_policies("data/sample_policies.txt")
    vs.add_documents(docs)

    print("Policies indexed successfully.")

    # Test search
    results = vs.search("Can I claim crypto losses as travel expense?")
    print("\nTop matches:")
    for r in results:
        print("-", r)
