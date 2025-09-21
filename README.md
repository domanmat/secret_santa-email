# Secret Santa Email Sender

A Python script for automatically sending Secret Santa gift assignment emails to participants.

## Overview

This script reads pre-assigned Secret Santa pairs and sends personalized email notifications to each participant, informing them who they should buy a gift for. The emails are sent in Polish with a festive Santa Claus theme.

## Features

- **Secure credential input**: Prompts for Gmail credentials without storing them in code
- **Hidden password entry**: Uses getpass for secure password input
- **Error handling**: Comprehensive error checking and user feedback
- **Progress tracking**: Shows sending progress and final summary
- **Gmail integration**: Uses SMTP with STARTTLS encryption

## Requirements

- Python 3.x
- Gmail account with App Password enabled
- `prezenty_losowanie.py` module containing the gift assignments

### Python Modules
- `smtplib` (built-in)
- `ssl` (built-in)  
- `getpass` (built-in)
- `time` (built-in)

## Setup

### 1. Gmail App Password Setup
Since this script uses Gmail SMTP, you need an App Password:

1. Enable 2-factor authentication on your Google account
2. Go to Google Account settings → Security → App passwords
3. Generate a new app password for "Mail"
4. Use this 16-character password (not your regular Gmail password)

### 2. Gift Assignment Module
Create or ensure you have `prezenty_losowanie.py` with this structure:
```python
# prezenty_losowanie.py
pary = [
    ["Anna", "anna@example.com", "Jan"],
    ["Jan", "jan@example.com", "Maria"],
    ["Maria", "maria@example.com", "Anna"]
]
```

Each list contains: `[recipient_name, recipient_email, assigned_person]`

## Usage

1. **Run the script**:
   ```bash
   python3 prezenty_email-anon.py
   ```

2. **Follow the prompts**:
   - Enter your Gmail address
   - Enter your Gmail App Password (input will be hidden)
   - Confirm to proceed with sending

3. **Monitor progress**:
   - The script shows each email being sent
   - Final summary displays success/failure counts

## Email Content

Participants receive emails in Polish:
```
Subject: Wiadomość z Laponii

Hohoho [Name]!

W losowaniu został(a) przydzielony(a) Ci [Assigned Person].

Pozdrawiam, Święty Mikołaj
```

Translation: "Ho ho ho [Name]! In the draw, you have been assigned [Assigned Person]. Regards, Santa Claus"

## Security Features

- **No credential storage**: Email and password are only held in memory during execution
- **Secure input**: Password input is hidden using getpass
- **Encrypted connection**: Uses STARTTLS for secure email transmission
- **User confirmation**: Requires explicit confirmation before sending emails

## Troubleshooting

### Authentication Errors
- Ensure you're using an App Password, not your regular Gmail password
- Verify 2-factor authentication is enabled on your Google account
- Check that the Gmail address is correct

### Import Errors
- Ensure `prezenty_losowanie.py` exists in the same directory
- Verify the `pary` variable is properly defined in the module
- Check that email addresses in the pairs are valid

### Connection Issues
- Check your internet connection
- Verify Gmail SMTP isn't blocked by firewall
- Try running the script from a different network if issues persist

## Sample Output

```
Secret Santa Email Sender
=========================
This script will send Secret Santa assignment emails to all participants.

Do you want to continue? (y/n): y

Email Configuration
--------------------
Enter your Gmail address: santa@gmail.com
Enter your Gmail app password (input hidden): 

Sending emails to 3 recipients...
========================================
Sending to Anna (anna@example.com)...
✓ Successfully sent to Anna
Sending to Jan (jan@example.com)...
✓ Successfully sent to Jan
Sending to Maria (maria@example.com)...
✓ Successfully sent to Maria

========================================
Email Sending Summary:
Successful: 3
Failed: 0
Total: 3
```

## Important Notes

- **Test first**: Consider sending to yourself first to verify the email format
- **Rate limiting**: The script includes 1.5-second delays between emails to respect Gmail's limits
- **Privacy**: The script doesn't log or store any email addresses or content
- **Single use**: Designed for one-time Secret Santa notifications

## License

This script is provided for personal and educational use.
