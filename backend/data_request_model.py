from pydantic import BaseModel, validator, root_validator
from typing import Optional


class MlRequest(BaseModel):
    IDH1: int
    TP53: int
    ATRX: int
    PTEN: int
    EGFR: int
    CIC: int
    MUC16: int
    PIK3CA: int
    NF1: int
    PIK3R1: int
    FUBP1: int
    RB1: int
    NOTCH1: int
    BCOR: int
    CSMD3: int
    SMARCA4: int
    GRIN2A: int
    IDH2: int
    FAT4: int
    PDGFRA: int