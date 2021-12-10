# Notecast

Notecast enables students to convert notes into synthesised speech. The generated speech is served as audio files via a clean, minimal interface. Emphasis is placed on ensuring generated speech is convincing, with APIs from Microsoft's cognitive service helping to achieve this.

## Prerequisites

- Microsoft Azure account with a valid payment method on file
- Amazon AWS S3 bucket 
- Python >=2.7.16

## Installation

First, clone the repository:

```bash
git clone https://github.com/ben-maclaurin/set09103-advanced-web-technologies.git
```

Next, create virtual environment inside of the `set09103-advanced-web-technologies` directory:

```bash
python3 -m venv venv
```

Once a virtual environment has been initialised, activate it:

```bash
. venv/bin/activate
```

Now install the dependencies:

```bash
pip install -r requirements.txt
```

After installing the requirements, initialise the database using:

```bash
flask init-database 
```

Now create a `dotenv` file in the project root. All of the variables are required. Some examples have been included below: 

```bash
# /set09103-advanced-web-technologies/.env 

export SECRET_KEY=some_scret_key
export DATABASE=notecast.sqlite
export MICROSOFT_REGION=eastus
export MICROSOFT_KEY=ca29b34f9eb9d39d939b9339f3929d
export BUCKET_URL=https://some-bucket-url.s3.us-east-2.amazonaws.com/
```

Finally, your AWS credentials are required for `boto3` to work. [Follow these instructions to set up](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html#configuration).

## Usage

Run the following Bash commands:

```bash
export FLASK_APP=notecast
export FLASK_ENV=development 
flask run
```

The application should now be available at `http://127.0.0.1:5000/`.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
