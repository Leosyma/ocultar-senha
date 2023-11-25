import keyring
import getpass


aplicacao_usuario = "USER_IRA"
aplicacao_senha = "BD_IRA"
aplicacao_dsn = "DSN"
usuario = "IRA"



keyring.set_password(aplicacao_usuario, usuario, getpass.getpass(f"Senha de {aplicacao_usuario}: "))
keyring.set_password(aplicacao_senha, usuario, getpass.getpass(f"Senha de {aplicacao_senha}: "))
keyring.set_password(aplicacao_dsn, usuario, getpass.getpass(f"Senha de {aplicacao_dsn}: "))



keyring.get_password(aplicacao_usuario, usuario)
keyring.get_password(aplicacao_senha, usuario)
keyring.get_password(aplicacao_dsn, usuario)
