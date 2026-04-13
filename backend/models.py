from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, UUID4


class VideoBase(BaseModel):
    title: str
    grade_level: str
    language: str = "SASL"
    is_published: bool = False


class VideoCreate(VideoBase):
    storage_url: str
    duration_sec: float


class VideoOut(VideoBase):
    id: UUID4
    storage_url: str
    duration_sec: float
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class SASLGlossChunkBase(BaseModel):
    start_sec: float
    end_sec: float
    saslgloss: Optional[str] = None
    english_text: str


class EngWordBase(BaseModel):
    eng_word: str
    start_sec: float
    end_sec: float
    saslgloss_id: UUID4


class LessonBase(BaseModel):
    title: str
    video_id: UUID4
    status: str  # "draft", "published"


class LessonOut(LessonBase):
    id: UUID4
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class AIGlobalSuggestion(BaseModel):
    id: UUID4
    video_id: UUID4
    start_sec: float
    end_sec: float
    ai_saslgloss: Optional[str] = None
    ai_english: str
    confidence: Optional[float] = None
    status: str  # "pending", "accepted", "rejected"
    created_at: datetime

    class Config:
        orm_mode = True


class LessonFullOut(BaseModel):
    lesson: LessonOut
    chunks: List[SASLGlossChunkBase]
    eng_words: List[EngWordBase]
    ai_suggestions: List[AIGlobalSuggestion]