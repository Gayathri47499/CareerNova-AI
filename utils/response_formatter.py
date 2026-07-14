from typing import Any


class ResponseFormatter:

    @staticmethod
    def format(model: Any):

        if model is None:
            return {"error": "Not Found"}

        if isinstance(model, list):
            return [item.model_dump() for item in model]

        return model.model_dump()