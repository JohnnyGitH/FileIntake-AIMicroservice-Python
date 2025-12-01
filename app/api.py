from fastapi import APIRouter
from app.services import summarize_document
from app.models import SummaryRequest, SummaryResponse

router = APIRouter()

@router.post("/summarize", response_model=SummaryResponse)
async def summarize(req: SummaryRequest):
    result = await summarize_document(req.text)
    return SummaryResponse(summary=result)