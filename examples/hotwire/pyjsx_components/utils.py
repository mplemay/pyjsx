# pyjsx_components/utils.py
def dom_id(record: dict) -> str:
    """
    Generates a consistent DOM ID for a record.
    Assumes record is a dict with 'id' and 'type' keys.
    e.g., {"id": 123, "type": "item"} -> "item_123"
    """
    if "id" in record and "type" in record:
        return f"{record['type']}_{record['id']}"
    elif "type" in record: # For general IDs like "item-list"
        return record['type']
    raise ValueError("Record must have 'id' and 'type' or just 'type' for dom_id")

def dom_class(record: dict) -> str:
    """
    Generates a consistent DOM class for a record.
    Assumes record is a dict with 'type' key.
    e.g., {"type": "item"} -> "item"
    """
    if "type" in record:
        return record['type']
    raise ValueError("Record must have 'type' for dom_class")