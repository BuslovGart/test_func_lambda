from pydantic import BaseModel


class InputDataSchema(BaseModel):
    param_1: str
    param_2: int


class OutputDataSchema(BaseModel):
    output_param_1: str
    output_param_2: int
    output_param_3: float | None = None


async def main_func(
    data: InputDataSchema,
) -> OutputDataSchema:
    """
    Convert text to doc
    """
    print(f"file__text_to_doc test data: {data}")
    return OutputDataSchema(output_param_1="123", output_param_2=123)


if __name__ == "__main__":
    import asyncio
    data = InputDataSchema(
        param_1="123",
        param_2=123,
    )
    result = asyncio.run(main_func(data))
    print(result)
