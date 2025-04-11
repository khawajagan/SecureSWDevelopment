from pydantic import BaseModel

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    age: int

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
