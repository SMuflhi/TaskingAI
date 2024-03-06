# -*- coding: utf-8 -*-

# collection_create_request.py

"""
This script is automatically generated for TaskingAI Community server
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Dict

__all__ = ["CollectionCreateRequest"]


class CollectionCreateRequest(BaseModel):
    name: str = Field("", min_length=0, max_length=127)
    description: str = Field("", min_length=0, max_length=512)
    capacity: int = Field(..., ge=0)
    embedding_model_id: str = Field(..., min_length=8, max_length=8)
    metadata: Dict = Field({}, min_length=0, max_length=16)
