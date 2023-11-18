[![Django CI](https://github.com/kuisskui/Audience-Application/actions/workflows/django.yml/badge.svg)](https://github.com/kuisskui/Audience-Application/actions/workflows/django.yml)

# Audience-Application
Explore the web application designed to enhance the experience for audiences attending the 2024 Paris Olympic Games.

Visit our website : http://www.nongallnew.online/

## Installation
### Prerequisites
Make sure you have Python 3.8, 3.9, 3.10, or 3.11 installed on your system.

1. Clone the repository.

    ```shell
    git clone https://github.com/kuisskui/Audience-Application.git
    ```

2. Change the directory to the project.

    ```shell
    cd Audience-Application
    ```

3. Install the required packages from the `requirements.txt` file.

    ```shell
    python -m pip install -r requirements.txt
    ```

4. Create and apply the database migrations.

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Collect static files.

    ```shell
    python manage.py collectstatic
    ```

6. Run the development server.

    ```shell
    python manage.py runserver
    ```

7. Explore the web application in your browser at **http://127.0.0.1:8000**.

## Setting Up Social Applications (Optional)
To enable social login features, follow these steps to set up social applications in the Django admin site:

1. Login to the Django admin site. You can access it at **http://127.0.0.1:8000/admin/**.

2. In the Site section, add the site **http://127.0.0.1:8000**.

3. Under the "Social applications" section, add social applications for the authentication providers you want to use (e.g., Google).

4. For each social application, you'll typically need to provide the following information:
   - Name
   - Client ID or Key
   - Secret Key
   - Sites (You can choose the default site or the site corresponding to your application's domain)

5. Save the social applications.

**Note**: Setting up social applications is optional. If you don't have local settings available or don't want to enable social logins, you can skip this step. Users can still log in and register using the traditional authentication method.

Now, your Audience Application is ready to use, and users can access it without social login features if you choose not to configure them.
