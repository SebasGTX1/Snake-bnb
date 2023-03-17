import mongoengine

def global_init():
    alias_core = 'core'
    db = 'snake_bnb'
    mongoengine.register_connection(alias=alias_core, name=db)