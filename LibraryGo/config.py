# Configuration settings for LibraryGo
class Config:
    # Application Settings
    SECRET_KEY = 'librarygo_secret_key'
    DEBUG = True
    
    # Database Settings
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = ''
    DB_NAME = 'librarygo'
    
    # Session Settings
    SESSION_TYPE = 'filesystem'
    PERMANENT_SESSION_LIFETIME = 1800
    
    # Book Reservation Settings
    MAX_RESERVATIONS_PER_USER = 5
    RESERVATION_DURATION_DAYS = 14
    
    # Search Settings
    ITEMS_PER_PAGE = 10
    SEARCH_MIN_CHARS = 3