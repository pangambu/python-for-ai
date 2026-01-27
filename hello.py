class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model=model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"


# Creating different configurations
# Using positional arguments, named for optional
dev_config = APIConfig("sk_dev_key", max_tokens=50)

# using all nameed arguments (clearest)
prod_config = APIConfig(api_key="sk_prod_key", model="gpt-4", max_tokens=100)

# Access the configuration
print(dev_config.model)
print(prod_config.model)
print(prod_config.max_tokens)


class DataValidator:
    def __init__(self):
        self.errors = []
    
    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")

    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}") 
            return False
        return True
    
    def get_errors(self):
        return self.errors
    


# use the validator
validator = DataValidator()

# Notice we don't pass self, just the email
validator.validate_email("bad_email")
validator.validate_age(200)

# Or using positional arguments
validator.validate_email("another_bad_email")
validator.validate_age(150)

print(validator.get_errors())