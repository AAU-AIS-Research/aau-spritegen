import dataclasses
from json import JSONEncoder
from typing import Any


class EnhancedJSONEncoder(JSONEncoder):
    def __camelize(self, o: dict[str, Any]) -> dict[str, Any]:
        def transform(k: str) -> str:
            pascal = k.replace("_", " ").title().replace(" ", "")
            return pascal[:1].lower() + pascal[1:]

        return {transform(k): v for k, v in o.items()}

    def default(self, o: object):
        if dataclasses.is_dataclass(o):
            obj_dict = dataclasses.asdict(o)  # type: ignore
            return self.__camelize(obj_dict)
        return super().default(o)
