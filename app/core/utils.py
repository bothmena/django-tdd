def normalize_email_domain_name(email: str) -> str:
    username, domain_name = email.split('@')
    return '@'.join([username, domain_name.lower()])
