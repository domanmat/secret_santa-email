#!/usr/bin/env python3

import smtplib
import ssl
import time
import getpass
import sys
import prezenty_losowanie

def get_email_credentials():
    """Get email credentials from user input with proper security."""
    print("Email Configuration")
    print("-" * 20)
    
    # Get sender email
    while True:
        sender_email = input("Enter your Gmail address: ").strip()
        if '@gmail.com' in sender_email and '@' in sender_email:
            break
        else:
            print("Please enter a valid Gmail address (example@gmail.com)")
    
    # Get password securely (won't display on screen)
    while True:
        password = getpass.getpass("Enter your Gmail app password (input hidden): ")
        if password.strip():
            break
        else:
            print("Password cannot be empty. Please try again.")
    
    return sender_email, password

def send_secret_santa_emails():
    """Send Secret Santa emails to all participants."""
    
    # Check if prezenty_losowanie module is available
    try:
        pairs = prezenty_losowanie.pary
        if not pairs:
            print("Error: No gift pairs found in prezenty_losowanie.pary")
            return
    except AttributeError:
        print("Error: prezenty_losowanie.pary not found. Make sure the module is properly configured.")
        return
    except ImportError:
        print("Error: Cannot import prezenty_losowanie module.")
        return
    
    # Get email credentials
    try:
        sender_email, password = get_email_credentials()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return
    
    # Email server configuration
    smtp_server = "smtp.gmail.com"
    port = 587  # For STARTTLS
    
    # Create SSL context
    context = ssl.create_default_context()
    
    print(f"\nSending emails to {len(pairs)} recipients...")
    print("=" * 40)
    
    successful_sends = 0
    failed_sends = 0
    
    for j, pair in enumerate(pairs):
        try:
            recipient_name = pair[0]
            recipient_email = pair[1]
            assigned_person = pair[2]
            
            print(f"Sending to {recipient_name} ({recipient_email})...")
            
            # Create email message
            message = f"""\
Subject: Wiadomość z Laponii

Hohoho {recipient_name}!

W losowaniu został(a) przydzielony(a) Ci {assigned_person}.

Pozdrawiam, Święty Mikołaj""".encode('utf-8')
            
            # Send email
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(sender_email, password)
                server.sendmail(sender_email, recipient_email, message)
            
            print(f"✓ Successfully sent to {recipient_name}")
            successful_sends += 1
            
            # Add delay between emails to be respectful to the server
            time.sleep(1.5)
            
        except smtplib.SMTPAuthenticationError:
            print(f"✗ Authentication failed. Please check your email and password.")
            print("Note: You may need to use an 'App Password' instead of your regular password.")
            print("See: https://support.google.com/accounts/answer/185833")
            break
        except smtplib.SMTPRecipientsRefused:
            print(f"✗ Failed to send to {recipient_email} - invalid email address")
            failed_sends += 1
        except Exception as e:
            print(f"✗ Error sending to {recipient_name}: {str(e)}")
            failed_sends += 1
    
    # Summary
    print("\n" + "=" * 40)
    print("Email Sending Summary:")
    print(f"Successful: {successful_sends}")
    print(f"Failed: {failed_sends}")
    print(f"Total: {len(pairs)}")

def main():
    """Main function with user confirmation."""
    print("Secret Santa Email Sender")
    print("=" * 25)
    print("This script will send Secret Santa assignment emails to all participants.")
    print("\nIMPORTANT SECURITY NOTES:")
    print("- Use an App Password, not your regular Gmail password")
    print("- Your password will not be displayed on screen")
    print("- No credentials are stored or logged")
    
    # Confirm before proceeding
    while True:
        proceed = input("\nDo you want to continue? (y/n): ").strip().lower()
        if proceed in ['y', 'yes']:
            break
        elif proceed in ['n', 'no']:
            print("Operation cancelled.")
            return
        else:
            print("Please enter 'y' for yes or 'n' for no.")
    
    try:
        send_secret_santa_emails()
    except KeyboardInterrupt:
        print("\nOperation interrupted by user.")
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}")
        print("Please check your configuration and try again.")

if __name__ == "__main__":
    main()