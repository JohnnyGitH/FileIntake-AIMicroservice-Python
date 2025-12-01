from pydantic import BaseModel

# Need models for the text to be sent
# and to return with a summary
class SummaryRequest(BaseModel):
    text: str

class SummaryResponse(BaseModel):
    summary: str