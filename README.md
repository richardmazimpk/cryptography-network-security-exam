# cryptography-network-security-exam
# Student Records Encryption & Integrity Application

Security Compliance Notice
As mandated by security best practices:
The encryption key (`secret.key`) is generated dynamically at runtime and kept outside the repository architecture.
To prevent accidental data leaks or tracking keys via version control, add `secret.key` to your `.gitignore` configuration profile file.

1. Installation Instructions

a.  Prerequisites
Ensure you have a stable release version of **Python 3.11+** installed on your system. 

b. Dependencies Setup
The application relies on the industry-standard `cryptography` package to handle underlying secure primitives. Open your terminal within the application project folder environment directory and install it:

c. Windows (Standard Environment or IDE of your choce)
pip install cryptography

d. Alternative Explicit Environment Path (If system paths are unlinked)
%USERPROFILE%\AppData\Local\Programs\Python\Python311\python.exe -m pip install cryptography

 2. Execution Instructions

  a. Starting the Application
Launch the application interface using your terminal console prompt:

  b. General Command
      python encryp_student_records.py

  c. Explicit Windows PowerShell Command
      & "$env:USERPROFILE\AppData\Local\Programs\Python\Python311\python.exe" encryp_student_records.py


3. Operational Guide (Menu Options)

Once the application terminal workspace initializes, select a numeric choice option from the menu to perform specific data security workflows:

  Option 1: [Part a] Encrypt student record file
  * Generates a sample CSV student records database (`student_records.txt`) if a source file isn't already provided.
  * Dynamically provisions a fresh symmetric security token key (`secret.key`).
  * Encrypts the dataset file using AES-128 and outputs the cipher payload into `student_records.enc`.
  * Logs a baseline SHA-256 validation snapshot into `baseline_hash.txt`.

  Option 2: [Part b] Decrypt file and verify match
  * Loads the generated cryptographic validation token key from `secret.key`.
  * Reverses the mathematical cipher loop block to output a human-readable clean plaintext file (`student_records_decrypted.txt`).
  * Compares every single byte layer of the decrypted file against your original source records to confirm a perfect, uncorrupted match verification check.

  Option 3: [Part c] Perform SHA-256 integrity audit check
  * Generates a real-time SHA-256 verification string signature of the current source database file.
  * Evaluates it against your recorded `baseline_hash.txt` string to dynamically detect any unauthorized background modifications.

  Option 4: [Simulate] Unauthorized file tampering modification**
  * Appends a fake grading line item entry into your active student file database to simulate a malicious insider data manipulation attack. (Run **Option 3** directly       after this step to watch the integrity monitor flag a critical security warning alert).

  Option 5: Exit application
  * Safely closes the CLI environment workspace panel.
    
4.  Resilience & Fault Tolerance (Part d)
The application architecture wraps file transactions and user entries inside protective try-except blocks. If file dependencies are completely missing, or if an invalid menu item entry is selected, the application prints a clear warning alert and cycles back to the main option screen cleanly without crashing out.


Question 4
------------
a.  Project Structure & Reproducibility Guide (Question 4.a)

### Directory Map
Exam/
│
├── encryp_student_records.py   
├── apply_rules.sh            
├── filter_tests.md        
├── README.md                   
└── .gitignore                  

### How to Run the Program and Reproduce Tests

#### 1. Running the Core Application (Question 2)
To run the Python encryption, decryption, and SHA-256 baseline integrity monitor application, execute the script natively via your terminal environment:
"powershell"
& "$env:USERPROFILE\AppData\Local\Programs\Python\Python311\python.exe" encryp_student_records.py

* Use **Option 1** to initialize the baseline dataset file (`student_records.txt`), write out a tracking snapshot signature (`baseline_hash.txt`), and generate an encrypted storage payload (`student_records.enc`).
* Use **Option 2** to reverse the cipher blocks, confirm payload authenticity, and output a decrypted confirmation file (`student_records_decrypted.txt`).
* Use **Option 3** to verify matching state values against current modifications.
* Use **Option 4** to inject unauthorized text strings into the record database to test and reproduce the **SHA-256 Integrity Failure Warning Alert**.

#### 2. Reproducing Network Traffic Filtering Tests (Question 3)
To reproduce the simulated network routing and verify that traffic restrictions match the parameters configured in `apply_rules.sh`:
1. Start an interface-wide listener on port 443 in an administrative terminal instance:
   cmd#  %USERPROFILE%\AppData\Local\Programs\Python\Python311\python.exe -m http.server 443 --bind 0.0.0.0
   
2. Test the **Permitted Staff connection** pathway by running this tracking request from a secondary command terminal window:
   cmd# curl http://192.168.152.1:443 --connect-timeout 5
   
   *(Confirm that the terminal returns a clean directory HTTP index stream listing row to verify reproducibility)*.
3. Test the **Blocked Network boundaries** by executing standard calls across alternate interfaces:
   cmd# curl http://192.168.1.174:443 --connect-timeout 5
   *(Confirm that the terminal pauses, hits a hard barrier drop condition, and returns a dynamic timeout status string error)*.

