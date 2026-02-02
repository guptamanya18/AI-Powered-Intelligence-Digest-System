from pydantic import BaseModel, Field

class EvaluationResult(BaseModel):
    is_relevant: bool = Field(
        description="Whether the item is relevant GenAI news"
    )
    relevance_score: int = Field(
        ge=0, le=10,
        description="Relevance score from 0 to 10"
    )
    reason: str = Field(
        description="Short explanation for the decision"
    )
