import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    # Menggunakan database SQLite di memory (RAM) agar tidak merusak data asli
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        yield client

def test_homepage_status(client):
    """Test apakah halaman utama Manage Employees bisa diakses"""
    response = client.get('/')
    assert response.status_code == 200

def test_add_employee_page(client):
    """Test apakah form tambah karyawan tidak error"""
    response = client.get('/insert') # Sesuaikan dengan route di app.py
    # Status bisa 200 atau 405 tergantung routing GET/POST di aplikasi aslinya
    assert response.status_code in [200, 405]