
# 🔐 Password Hiding

## Project Overview

This project demonstrates a secure method for handling and storing sensitive user credentials using Python. The script utilizes the `keyring` and `getpass` libraries to safely input and retrieve passwords for multiple application contexts, preventing exposure of plain-text credentials in the codebase or logs.

---

## 📂 Features

- **Secure Password Input**: Prompts the user to enter passwords using `getpass`, ensuring that passwords are not displayed during input.
- **Credential Storage**: Uses the `keyring` library to securely store credentials in the system's native credential manager.
- **Password Retrieval**: Enables retrieval of saved credentials securely when needed by the application.
- **Multi-Application Setup**: Configured to store and retrieve credentials for different contexts such as `USER_IRA`, `BD_IRA`, and `DSN`.

---

## 🛠 Technologies Used

- **Python 3**
- **keyring** – For secure password storage.
- **getpass** – For hidden password input.

---

## 💻 How to Use

1. Clone or download the repository.
2. Run the script using Python:
   ```bash
   python Ocultar_senha_20231124.py
   ```
3. Input the passwords when prompted. The script will store them securely.
4. Passwords can then be retrieved from the keyring in other scripts using:
   ```python
   keyring.get_password("APPLICATION_NAME", "USERNAME")
   ```

---

## ✅ Use Cases

- Applications that require secure password management.
- Avoid hardcoding credentials into scripts.
- Managing multiple credentials in enterprise or development environments.

---

## 🔒 Disclaimer

This script assumes the use of a supported keyring backend (e.g., Windows Credential Locker, macOS Keychain, or SecretService on Linux). Ensure your environment supports the `keyring` library for proper functionality.

