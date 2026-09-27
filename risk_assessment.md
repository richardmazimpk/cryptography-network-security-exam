a. Identify three assets, three vulnerabilities, and their possible consequences.
Assets: Student records on the central server
        Files transferred between campuses
        Central server and network infrastructure
vulnerabilities: Guest network has access to the records server
                File transfers are unencrypted
                Weak staff passwords and outdated soft
Possible Consequences: Unauthorized access, disclosure or alteration of confidential student information
                        Data can be intercepted, stolen, or modified during transmission
                        Attackers may compromise accounts or exploit software vulnerabilities, causing data theft or service disruption

b. Rankthethree risks by likelihood and impact, giving reasons
Risk : 1. Unauthorized access to the records server
        2. External attack on the central server
        3. Interception of campus file transfers
        
Likelihood: 1. Medium
             2. high
            3. medium
Impact: 1. High
        2. High
        3. Medium
        
Reason: 1. Likelihood is Medium because the polytechnic has a direct vulnerability: 
        the guest network has a completely open network path to the records server. 
        Any student or visitor can probe it. However, it isn't "High" because the actor still needs to crack or bypass the server’s authentication screen. 
        Impact is High because student records contain personally identifiable information (PII) and financial records. 
        A breach triggers severe legal penalties (e.g., FERPA compliance issues) and massive reputational damage.
        2. Likelihood is Medium because the IT team has explicitly observed repeated attempts from an unfamiliar external address, meaning they are actively targeted. 
        Combined with unpatched, outdated software, a vulnerability is present. It isn't "High" because standard perimeter firewalls usually drop generic external
        scans before they penetrate software layers.Impact is High because this is the central server. If a hacker breaches it via an unpatched exploit, 
        they gain administrative control, allowing them to steal all institutional data or deploy catastrophic ransomware.
        3. Likelihood is Low because even though the files are unencrypted, intercepting data in transit between two physically separate campuses is technically difficult.
            An attacker cannot easily tap into external telecom lines or fiber optics across a city unless they have already compromised the ISP or deep internal network routing switches.
            Impact is Medium because intercepting traffic only exposes the specific documents being actively sent at that exact second (like a class list). 
            It does not give the attacker administrative entry or control over the master student database itself.
            
c. Recommend one suitable control for each risk.

1. Control for Risk 1: Unauthorized access to the records server
	Recommended Control: Network Segmentation & Access Control Lists (ACLs)
	How it works: You must physically or logically separate the public network from the private network.
  Configure the institute's core switches and internal firewalls to place the guest Wi-Fi on a completely isolated VLAN (Virtual Local Area Network).
  Apply strict ACLs so that any network traffic originating from the guest network is blocked from reaching the student records server.
  Only authorized IP addresses from the staff or administrator network should be allowed to connect.
2. Control for Risk 2: External attack on the central server
	Recommended Control: Automated Patch Management & Multi-Factor Authentication (MFA)
	How it works: To stop external attackers from exploiting outdated software, implement an automated patch management policy to regularly
  update the central server’s operating system and applications. To address the weak staff passwords being targeted by external brute-force attempts, enforce MFA.
  Even if an external hacker guesses a staff password from an unfamiliar IP address, they will be blocked without the second verification factor
  (like a mobile push notification or token).
3. Control for Risk 3: Interception of campus file transfers
	Recommended Control: Encryption in Transit (Site-to-Site VPN or SFTP)
  How it works: To protect data traveling between the two separate campuses, you must stop using unencrypted protocols (like standard FTP or HTTP).
  Instead, implement SFTP (SSH File Transfer Protocol) or HTTPS, which encrypts the files before they leave one campus and decrypts them only when they safely arrive at the other.
   Alternatively, the IT team can build a permanent, encrypted Site-to-Site VPN (Virtual Private Network) tunnel between the two campuses,
   ensuring all data passing between them is automatically scrambled and hidden from packet sniffers.
