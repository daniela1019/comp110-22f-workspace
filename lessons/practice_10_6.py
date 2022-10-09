def zip(a: list[str], b: list[str]) -> dict[str, str]:
    """Construct dict from 2 lists"""
    assert len(a) == len(b)
    zip_dict: dict = {}
    for i in range(0, len[a]):
        zip_dict[a[i]] = b[i]
    return zip_dict