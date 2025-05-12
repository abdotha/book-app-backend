from fastapi import HTTPException,Depends,APIRouter,status

from typing import List  # Add this import
from sqlalchemy.orm import Session
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import os
from dotenv import load_dotenv
from typing import Annotated

from app.database import libraryDatabase, get_db
from app.schemas import borrowBookSchema, libraryBookSchema 
from app.utils import verify_credentials

router= APIRouter(prefix="/library",tags=["Library"])

@router.get("")
async def get_books(db: Session = Depends(get_db)):
    books = db.query(libraryDatabase).all()
    return books




@router.put("/borrow")
async def borrow_book(request:borrowBookSchema , db: Session = Depends(get_db)):
    book = db.query(libraryDatabase).filter(libraryDatabase.bookid == request.bookid).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if not book.available:
        raise HTTPException(status_code=400, detail="Book is not available for borrowing")
    
    book.available = False
    book.email = request.email
    db.commit()
    db.refresh(book)
    return {"message": "Book borrowed successfully"}

@router.put("/return")
async def return_book(request:borrowBookSchema , db: Session = Depends(get_db)):
    book = db.query(libraryDatabase).filter(libraryDatabase.bookid == request.bookid).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if book.available:
        raise HTTPException(status_code=400, detail="Book is already available")
    
    book.available = True
    book.email = None
    db.commit()
    db.refresh(book)
    return {"message": "Book returned successfully"}

@router.get('/userbooks')
async def get_user_books(email: str, db: Session = Depends(get_db)):
    books = db.query(libraryDatabase).filter(libraryDatabase.email == email).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found for this user")
    return books




@router.post("/add",status_code=status.HTTP_201_CREATED)
async def add_book(request : libraryBookSchema,db: Session = Depends(get_db),username: str = Depends(verify_credentials)):
    book = libraryDatabase(**request.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book



@router.delete('/delete',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(bookid: int, db: Session = Depends(get_db),username: str = Depends(verify_credentials)):
    book = db.query(libraryDatabase).filter(libraryDatabase.bookid == bookid).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}

