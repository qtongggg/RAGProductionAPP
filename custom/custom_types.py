from pydantic import BaseModel, EmailStr, Field
from typing import Any, List, Optional

class MatchResult(BaseModel):
    fit_score: float
    matching_skills: List[str]
    missing_skills: List[str]
    reason: str



class SummaryJobInfo(BaseModel):
    brief_summary: str
    hr_insights: str

class JobSearchInfo(BaseModel):
    job_id: str
    title: str
    company: str
    job_description: str
    location: str
    employment_type: str
    link: str

class JobSearchRequest(BaseModel):
    keyword: str
    location: str = "Malaysia"
    per_page: int = 5
    page: int = 1


class AgentResult(BaseModel):
    status: str
    data: dict[str, Any]
    error: Optional[str] = None
    meta: dict[str, Any] = {}

class MatchJobInfo(BaseModel):
    title: str
    company: str
    location: str
    job_description: str
    job_id: str
    link: str
    matching_skills: List[str]
    missing_skills: List[str]
    reason: str
    fit_score: float = Field(ge=0, le=1)