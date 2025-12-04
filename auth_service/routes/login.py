from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from auth_service.models.usuario import Usuario
from auth_service.schemas.usuario import UsuarioBase, UsuarioResponse, UsuarioCreate
from database import get_db

router = APIRouter()

@router.post("/v1/login/usuario", response_model=dict)
def login_usuario(data: UsuarioBase, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.nombre == data.nombre, Usuario.clave == data.clave).first()
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    return {
        "message": "Inicio de sesión exitoso",
        "status": 200,
        "data": {
            "id_usuario": user.id_usuario,
            "nombre": user.nombre,
            "edad": user.edad
        }
    }

@router.post("/v1/register/usuario", response_model=dict)
def register_usuario(data: UsuarioCreate, db: Session = Depends(get_db)):
    # opcional: evitar usuarios duplicados por nombre
    existing = db.query(Usuario).filter(Usuario.nombre == data.nombre).first()
    if existing:
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    user = Usuario(nombre=data.nombre, clave=data.clave, edad=data.edad)
    db.add(user)
    db.commit()
    db.refresh(user)

    return {
        "message": "Usuario registrado correctamente",
        "status": 201
    }


@router.get("/v1/list/usuarios", response_model=dict)
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()

    if not usuarios:
        return {
            "message": "No se encontraron registros",
            "status": 200,
            "data": []
        }

    data = [
        {
            "id_usuario": u.id_usuario,
            "nombre": u.nombre,
            "edad": u.edad,
            "contraseña": u.clave
        }
        for u in usuarios
    ]

    return {
        "message": "Lista de usuarios obtenida correctamente",
        "status": 200,
        "data": data
    }
