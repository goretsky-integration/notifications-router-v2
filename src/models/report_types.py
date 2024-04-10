from pydantic import BaseModel

__all__ = ('ReportType',)


class ReportType(BaseModel):
    id: int
    name: str
    verbose_name: str
