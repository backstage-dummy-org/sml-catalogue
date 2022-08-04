# SML Catalogue

This repo contains the build environment and code to generate and upload the Statistical Methods Library (SML) Catalogue website.

## Build and deploy

### S3 Bucket creation

[Terraform](https://www.terraform.io/intro) is used to deploy the S3 Bucket where the website is hosted. The S3 bucket will be suffixed with the currently checked-out gt branch name.

Fetch your AWS credentials and export them to the terminal. Then:

```shell
cd terraform
terraform init
terraform apply \
  -var "suffix=`git branch --show-current`"
```

### Fetch ONS Design System

Download the release of the ONS Design System, and unpack them into the correct location with this command:

```shell
./get_design_system.sh
```

### Make the site

You will first need to install the python dependencies, including [Frozen-flask](https://pythonhosted.org/Frozen-Flask/), the static website generator:

```shell
pipenv sync
```

With [Jsonnet](https://jsonnet.org/learning/getting_started.html) content in the `content/` directory, you should now be able to run the Flask demo server:

```shell
pipenv run flask --app sml_builder --debug run
```

If this all goes well with no errors, you should now be able to navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the site. And if that all looks good, you can now "freeze" the site, renderng it to HTML with:

```shell
pipenv run python freeze.py
```

And finally, upload to the S3 bucket (assuming you still have valid AWS credentials exported to the terminal):

```shell
aws s3 sync build s3://sml-catalogue-`git branch --show-current` --acl public-read --delete --content-type "text/html"
```
