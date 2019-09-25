GOOGLE.md

App Engine Quickstart

# Introduction

This tutorial shows you how to deploy a sample Python application to App Engine using the gcloud command.

Here are the steps you will be taking.

Create a project

Projects bundle code, VMs, and other resources together for easier development and monitoring.

Build and run your "Hello World!" app

You will learn how to run your app using Cloud Shell, right in your browser. At the end, you'll deploy your app to the web using the gcloud command.

After the tutorial...

Your app will be real and you'll be able to experiment with it after you deploy, or you can remove it and start fresh.

# Project Setup

GCP organizes resources into projects, which collect all of the related resources for a single application in one place.

Begin by creating a new project or selecting an existing project for this tutorial.

For details, see [https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project].

# Using Cloud Shell

Cloud Shell is a built-in command-line tool for the console. We're going to use Cloud Shell to deploy our app.

## Open Cloud Shell

Open Cloud Shell by clicking the Activate Cloud Shell button in the navigation bar in the upper-right corner of the console.

## Clone the sample code

Use Cloud Shell to clone and navigate to the "Hello World" code. The sample code is cloned from your project repository to the Cloud Shell.

Note: If the directory already exists, remove the previous files before cloning.

In Cloud Shell, enter the following:

  git clone https://github.com/GoogleCloudPlatform/python-docs-samples

Then, switch to the tutorial directory:

  cd python-docs-samples/appengine/standard_python37/hello_world

# Configuring your deployment

You are now in the main directory for the sample code. We'll look at the files that configure your application.

## Exploring the application

Enter the following command to view your application code:

  cat main.py

The application is a simple Python application that uses the Flask web framework. This Python app responds to a request with an HTTP header and the message Hello World!.

## Exploring your configuration

App Engine uses YAML files to specify a deployment's configuration. app.yaml files contain information about your application, like the runtime environment, environment variables, and more.

Enter the following command to view your configuration file:

  cat app.yaml

This file contains the minimal amount of configuration required for a Python 3 application. The runtime field specifies the python37 run-time environment.

The syntax of this file is YAML. For a complete list of configuration options, see the app.yaml reference.

# Testing your app

Test your app on Cloud Shell

Cloud Shell lets you test your app before deploying to make sure it's running as intended, just like debugging on your local machine.

To test your app, first create an isolated virtual environment. This ensures that your app does not interfere with other Python applications that may be available on your system.

  virtualenv --python python3 ~/envs/hello_world

Activate your newly created virtual environment:

  source ~/envs/hello_world/bin/activate

Use pip to install project dependencies. This "Hello World" app depends on the Flask microframework:

  pip install -r requirements.txt

Finally, run your app in Cloud Shell using the Flask development server:

python main.py

## Preview your app with "Web preview"

Your app is now running on Cloud Shell. You can access the app by clicking the Web preview button at the top of the Cloud Shell pane and choosing Preview on port 8080.

## Terminating the preview instance

Terminate the instance of the application by pressing Ctrl+C in the Cloud Shell.

# Deploying to App Engine

## Create an application

In order to deploy your app, you need to create an app in a region:

  gcloud app create

Note: If you already created an app, you can skip this step.

Deploying with Cloud Shell

You can use Cloud Shell to deploy your app. To deploy your app enter the following:

  gcloud app deploy app.yaml --project nest-lab-37fc8

# Visit your app

Congratulations! Your app has been deployed. The default URL of your app is a subdomain on appspot.com that starts with your project's ID: http://nest-lab-37fc8.appspot.com/.

Try visiting your deployed application.

# View your app's status

You can check in on your app by monitoring its status on the App Engine dashboard.

Open the Navigation menu in the upper-left corner of the console.

Then, select the App Engine section.

# Disable your project

1. Go to the Settings page.

2. Click Disable Application.

This is sufficient to stop billing from this app. More details on the relationship between apps and projects and how to manage each can be found here.

# Delete your project

If you would like to completely delete the app, you must delete the project in the Manage resources page. This is not reversible, and any other resources you have in your project will be destroyed:

1. Go to IAM & admin.

2. Click Settings.

3. Select the checkbox next to your project.

4. Click Shut down.

# Conclusion

You have successfully deployed an App Engine application!

Here are some next steps:

# Download the Google Cloud SDK  and develop locally

See https://cloud.google.com/sdk/downloads#interactive/

# Install the Google Cloud SDK on your local machine.

Build your next application

Learn how to use App Engine with other GCP products:

Run Django (https://cloud.google.com/python/django/appengine).

Develop Django apps running on App Engine.

Build a web app (https://cloud.google.com/appengine/docs/standard/python3/building-app/).

Learn the basics of creating Python web services on App Engine.
