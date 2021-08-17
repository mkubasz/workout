from typing import List, Any


def tail(nums: Any, length: int) -> List[Any]:
    if length <= 0:
        return []
    return list(nums)[-length:]
