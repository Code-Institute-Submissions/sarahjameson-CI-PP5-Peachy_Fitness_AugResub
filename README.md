# Peachy Fitness

insert pic and deployed site links/github

## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [Ideal User Demographic](#Ideal-User-Demographic)
    2. [User Stories](#User-Stories)
    3. [Development Planes](#Development-Planes)
    4. [Design](#Design)
3. [Features](#Features)
    1. [Design Features](#Design-Features) 
    2. [Existing Features](#Existing-Features)
    3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     2. [Additional Languages Used](#Additional-Languages-Used)
     3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
     1. [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
     1. [Deploying on Heroku](#Deploying-on-Heroku)
     2. [Forking the Repository](#Forking-the-Repository)
     3. [Creating a Clone](#Creating-a-Clone)
8. [Credits](#Credits)
     1. [Content](#Content)
     2. [static/Media](#static/Media)
     3. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)

## Introduction

Peachy Fitness seeks to empower women and get them more into fitness. The site offers all that a person could need starting out on their fitness journey.

[Back to top ⇧](#)

## UX 
### Ideal User Demographic
The ideal user of this website is:
- Women/girls from ages 14 - 40
- Fashion-conscious people
- Motivated people

### User Stories

#### Site User:
- As a Site User, I want to be able to view a list of products so that I can select some to purchase.
- As a Site User, I want to be able to view individual product details so that I can identify the price, description, product rating, product image and sizes.
- As a Site User, I want to be able to easily view the total of my purchase at any time so that I can avoid spending too much.
- As a Site User, I want to be able to easily log in or log out so that I can access my personal account information.
- As a Site User, I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
- As a Site User, I want to be able to receive an email confirmation after registering so that I can verify my account registration was successful.
- As a Site User, I want to be able to have a personalised user profile so that I can view my order history and order confirmations and save my payment information.
- As a Site User, I want to be able to sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products.
- As a Site User, I want to be able to sort a specific category of product so that I can find the best-priced or best-rated product in a specific category, or sort the products in that category by name.
- As a Site User, I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase.
- As a Site User, I want to be able to easily see what I've searched for and the number of results so that I can quickly decide whether the product I want is available.
- As a Site User, I want to be able to easily select the size and quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product, quantity or size.
- As a Site User, I want to be able to view a specific category of products so that I can quickly find products I'm interested in without having to search through all products.
- As a Site User, I want to be able to view items in my bag to be purchased so that I can Identify the total cost of my purchase.
- As a Site User, I want to be able to adjust the number of individual items in my bag so that I can easily make changes to my purchase before checkout.
- As a Site User, I want to be able to receive an email confirmation after checking out so that I can keep the confirmation of what I've purchased for my records.
- As a Site User, I want to be able to easily enter my payment info so that I can check out quickly and with no hassles.
- As a Site User, I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
- As a Site User, I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes.

#### Store Owner
- As a Store Owner, I want to be able to add a product so that I can add new items to my store.
- As a Store Owner, I want to be able to edit/update a product so that I can edit product prices, descriptions, images, and other product criteria.
- As a Store Owner, I want to be able to delete a product so that I can remove items that I no longer wish to sell.

### Development Planes
To prepare for this project, I researched other fitness brand websites. This preparation helped me create the user stories. Some of the websites I used were:
- [Gymshark](https://eu.gymshark.com/)
- [Gym plus Coffee](https://gympluscoffee.com/)
- [Shreddy](https://shreddy.com/)

#### Strategy
With this website, I concentrated on the following aspects:
- Roles
    - Site User
    - Site Owner
- Demographic
    - Women/girls around 14-40
    - Fitness enthusiasts
- Psychographics
    - Personality & Attitudes:
        - Playful
        - Sporty
        - Outgoing
        - Motivated

    - Values:
        - Has a growth mindset
        - Positive
        - Fashionable

    - Lifestyles:
        - Has friends who have similar interests such as hiking or other outdoor activities
        - Keeps up with the latest trends
        - Likes trying out different things like Irish dancing or painting etc
        - Likes to look good

I found that the website needs to enable the **Site User** to:
- Find attractive and high quality exercise products for women in all sizes.
- Add the desired products to the shopping bag for purchasing.
- Filter the products based on name, categories, rating and prices.
- Search products by name or description.
- Create a profile with the saved user info and past orders.

The website needs to enable the **Site Owner** to:
- Add, edit and delete products on the site.
- View orders on the admin panel.

##### **eCommerce Application Type and Marketing Strategy**
To create a site that fit the user's needs, I planned the following marketing strategy:

- **eCommerce Type:**
    - **B2C** - I used SEO (Search Engine Optimisation), Content Marketing in the form of a newsletter, and Social Media Marketing in the form of a Facebook and Instagram page.

- Marketing Types:
    - **SEO** - SEO is useful for ensuring a good online presence. It is important to be present in the digital landscape as this form is everywhere around us and an important platform for a business. SEO must be carefully managed to not be treated as spam. I tried to avoid spaming the page content with words. I made sure to fill the meta tag with valuable keywords and a useful description.

    - **Content Marketing** - I used a newsletter. This marketing can help keep the business stay in the mind of the customer and convey a personality to them also. It allows the store to talk about what they are most knowledgable about and as a result build confidence in the users reading the content.

    - **Social Media Marketing** - I used Organic Social Media Marketing. It is a free and easy way to get a brand across. The site can be shared with others and special events or sales can be shared free of charge. This allows the store to connect directly with the consumer and build relationships and loyalty with the customers. This form of marketing can also be used to improve the store's customer service and support. Issues can be dealt with publically in a friendly or even funny way. The social media chosen for this project was [Facebook](https://www.facebook.com/Peachy-Fitness-104511555665795).

![Facebook Page for Peachy Fitness](media/README/facebook.png)

### **Scope**
I defined a scope to identify what needed to be done to align features with the strategy previously defined. This was broken into two categories:

- **Content Requirements**
    - The user will be looking for:
        - A variety of products to choose from that come under fitness goals
        - Details of the products provided
        - A way to search the site using the name or description fields
        - A filtering function by rating, name, price and category
        - A  Profile Page displaying the user's saved address and past order
- **Functionality Requirements**
    - The user will be able to:
        - Select their desired size for each product
        - Update their profile with with a address
        - Easily navigate the site to find product information

#### **Structure**
The website was organized in a hierarchical tree structure to ensure that users could navigate through the site with easily.

#### **Skeleton**
I created the Wireframe mockups using [Balsamiq](https://balsamiq.com/). Please find the file below:
- [Wireframes](media/README/wireframes)

[Back to top ⇧](#)

### Design
#### **Colour Scheme**
The colour scheme was influenced by the home page photo. The purple and pink are fun playful colours. A very faint purple was used as a contrast to the deeper purple and pink.

![](media/README/colour-scheme.png)

#### **Typography**
The font chosen for the headings was Dancing Script. All the other test was done in Mulish. The Dancing Script was used as the logo. It is fun and elegant. Mulish is very modern and trendy. It is easy to read.

#### **Imagery**
The imagery used in this site is entirely related to the products being sold - exercise goods.

[Back to top ⇧](#)

## Features
## Design Features
**Navigation & Header**

Each page of the website features a consistent responsive navigational system:
- **Logo** - The Logo heading is linked to the home page, clicking it will bring the user back to the home page.
- **Search Bar** - The search bar is coded to display the results of the user's search request.
- **Shopping Bag Icons** - There is an icon and a link to the shopping bag showing the current bag total. The icon's dropdown selection is updated depending on whether the user is logged in or logged out.
- **Link to user's profile** - There is a link to the user's profile depending on if they are linked in or not.
- **Links to Category Pages** - There are links to several categories of product pages. These pages show products of certain categories grouped by different categories such as leggings and sports_bras.

**Footer**
Each page of the website features a consistent responsive footer design:
- **A 'Stay in touch' Piece Of Text** - The footer displays a text asking the users to stay in touch.
- **Social Media Links** - These links connect the site user to the store's business Facebook page.
- **Subscribe to newsletter** - Mailchimp form is present in the footer.

**Home Page**
The home page is the main entry page to the site and gives the customer a call to action straight away. The purpose of the site is clear.
- **Main Image** - This feature is an image underneath the navigation bar and Custom Orders message bar. The image displayed is of some fitness products on the floor. It is not too overwhelming an image.
- **Call to action button** - A call to action button urges the user to shop now.

**Products Page**
This page displays a list of all products. The user can use filters and search queries to filter the list to their desired results.
- **Product Category Links** - There are set of button links that filter the list of products to the selected category.
- **Products Home Link** - There is a link to bring the user back to the 'Products Home', this will display all products rather than filtering by category or search queries.
- **Search Results/Product Counters** - Right next to the link to the 'Products Home' is a counter that tells the user how many products are displayed on the page. If the user has entered a search query, the counter will advise how many products were found for that specific search query.
- **Sort By Selector** -This selector allows the user to order the products displayed by name, rating, price and category in both ascending and descending orders.
- **Product Cards** - The product cards display the products listed on the site and also show some more information about the product such as the rating and price.

**Product Info Page**
This page will render the information for the chosen product and allow the user to select a size and add the item to the shopping bag.
- Product Details - The product details change for each product. This would include the product image, name, description, price, rating and category.
- Size Selector - The size selector can be used to select the specific size for the user.
- Add to Bag Button - When the user has selected their chosen size, they would click the Add to Bag button to add the desired product and size to their shopping bag for purchasing.
- Update/Delete Links - Visible only to an authorised user, underneath the product name are two links. One brings the autorised user to the edit product page, the other one deletes the product. Selecting the delete button will immediately delete the product.
- Comment List - The feature displays any comments available for a certain product.
- Comments Form - Visible only to a logged in user, this feature allows logged in users to add a comment to the product page. If the user is not logged in, a log in button appears with a message advising the user they are unable to leave a comment unless they log in.

**Shopping Bag Page**
This page allows the user to view, edit and delete items in their shopping bag before going to the checkout screen.
- Product Information - This feature displays the information of each item added to the shopping bag. This includes the name, price, image, size and quantity of the product.
- Update/Remove Buttons - These features allow the user to update the quantity of an item in their shopping bag, or remove it entirely.
- Updated Total, Shipping and Grand Total - The total cost of the shopping bag updates each time an item is added, updated or removed from the shopping bag. If the user spends more than €100.00 on items, they qualify for free shipping. Otherwise, shipping is calculated to be 10% of the user's total cost, which is then added to create the grand total.

**Checkout Page**
This page allows the user to securely enter their payment information before pay for their items.
- Shipping Info Form - This feature allows the user to enter the shipping details they wish their items to be delivered to. These details are then displayed on the confirmation screen.
- Order Summary - This feature allows the user to take one more look at the items in their shopping bag and the total cost before paying and submitting their order.
- Stripe Payment Feature - This feature allows the user to securely submit their payment information to the Stripe payment system, securing the placement of their order.

**Orer Confirmation Page**
This page shows the order details of the purchase that was just carried out.
- Order summary - This features details the order summary, containing the shipping information, product details and cost information. A unique order number is also provided.

**Profile Page**
This page displays the users profile and their past orders.
- Order History Log - This feature is a list of past orders placed while logged in. There are links on each order which allows the user to go to the order history page to get a detailed view of the order placed.
- Link to Order summaries of all past orders - This features details the order summary, containing the shipping information, product details and cost information. A unique order number is also provided.
- Return To Profile Button - This button brings the user back to the user profile.

**Add Product Page**
This page allows the authorised user to add a product to the store.
Add Product - This form allows the authorised user to create a new product.

**Edit Product Page**
This page allows the authorised user to edit a product in the store.
- Edit Product Form - This form allows the authorised user to edit the product's details.

### Existing Features
- **Search bar** - This feature is used to find items on the site, matching the query's keywords to the item's name or description. These results are shown on the products page with an indicator of how many items were found using the keyword(s).
- **Shopping Bag Icon** - This feature shows the user the current total cost of the items in the shopping bag, including shipping.
- **Back-to-Top Button** - This feature is only available on certain pages - product page and shopping bag page - and will bring the user back to the top of the page when clicked.
- **Contact Form** - This feature allows the user to contact the store owner.
- **Category Buttons** - This feature is a selection of buttons which filters the selection of products by certain categories.
- **Sort-By Selector** - This feature is a selector box whose selections sort the product list by name, category, rating and price in both ascending and descending order.
- **Size Selector And Guide** - This feature only appears when the item has size options available. If the item has sizes, a selector box appears with a list of sizes.
- **Increment/Decrement Quantity Buttons** - This feature is visible in the product detail and shopping bag pages. It allows the user to click a button to update the item quantity instead of typing it in manually.
- **Success Message - Add A Product** - This feature appears each time the user adds an item to the shopping bag successfully.
- **Update/Delete Buttons** - This feature is shown across the site.
- **Checkout Form** - This feature allows the user to enter payment details, allowing them to purchase the items in their shopping bag.
- **Order Confirmation** - This feature is shown after a purchase is made. It details the items purchased, their sizes, prices and quantity. It also lists the details provided on the checkout page as the shipping address.
- **Add/Edit Product Form** - This feature allows the site admin to add or edit a product on the site.

[Back to top ⇧](#)

## Issues and Bugs 
Below are some issues that I ran into while creating this project:
- Jquery was not working at first. It turns out I had the wrong link.
- I had a few issues with html and rows. Things were not in the correct place. One such example was my footer. I had to carefully read through the code and see that the tags were in the correct place.
- The Javascript script that I was using for the toast notifications was one for Bootstrap4 so they were not working properly. I read through the bootstrap5 documentation on toasts and eventually figured out what to do.
- I was receiving a programming error when trying to refresh the heroku site. It turns out that I needed to run migrations from the Heroku CLI as well.

[Back to top ⇧](#)

## Technologies Used
### Main Languages Used
-[Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-[JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-[CSS](https://en.wikipedia.org/wiki/CSS)
-[HTML](https://en.wikipedia.org/wiki/HTML)

### Frameworks, Libraries, Programs and Additional Languages Used
- [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
    - Used to build the pages used in the site and the working of the website.

- [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
    - Used to add styling to the website.

- [GitPod](https://gitpod.io/)
    - Used for the IDE.

- [GitHub](https://github.com/)
    - Used for version control.

- [Heroku](https://heroku.com/)
    - Used for the deployment of the website.

- [AWS](https://aws.amazon.com/)
    - Used to host MEDIA and STATIC files for the deployed site.

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/)
    - Used for the site's authentication system.

- [AmIResponsive](https://ui.dev/amiresponsive "AmIResponsive Site")
    - Used to generate mockup imagery of the finished website.

[Back to top ⇧](#)

## Testing
### User Stories:
#### Site User
- As a Site User, I want to be able to leave a comment on a product so that others can see my thoughts regarding the product.    
    - There is a form on the product detail page that allows the user to add a title and the body of a comment to the product page. The comment will detail the user's username, date of entry, and the title and body of the comment.
- As a Site User, I want to be able to search for a product by name or description so that I can find a specific product I'd like to purchase.
    - There is a search bar in the nav that allows users to search for products based on keywords in the description or name fields.
- As a Site User, I want to be able to sort the list of available products so that I can easily identify the best rated, best priced and categorically sorted products.
    - There is a 'sort-by' selector box on the products page which allows the user to sort the products by rating, name, price and category in ascending or decending order.
- As a Site User, I want to be able to sort a specific category of product so that I can find the best-priced or best-rated product in a specific category, or sort the products in that category by name.
    - There are navigation links and filter buttons that allow the user to view all products of a certin category or group of categories.
- As a Site User, I want to be able to easily select the size and quantity of a product when purchasing it so that I can ensure I don't accidentally select the wrong product, quantity or size.
    - On the product detail page, there is a selection box for sizes and a quantity selector with increment and decrement buttons beside it.
- As a Site User, I want to be able to adjust the number of individual items in my bag so that I can easily make changes to my purchase before checkout.
    - There is a quantity increment and decrement button with an update button that allows the user to increase or decrease the number of the specific item they wish to purchase.
- As a Site User, I want to be able to easily log in or log out so that I can access my personal account information.
    - There is a link in the header which allows the user to log in, log out and register for an account.
- As a Site User, I want to be able to easily recover my password in case I forget it so that I can recover access to my account.
    - There is an option on the log in page to request a reset password link be sent to the user's email address. Clicking the link and entering an email address sends an email to the person's email address to reset their password.
- As a Site User, I want to be able to receive an email confirmation after registering so that I can verify my account registration was successful.
    - On registering for an account, a verification email is sent to the user's registered email so they can verify their account and log in.
- As a Site User, I want to be able to easily enter my payment info so that I can check out quickly and with no hassles.
    - The checkout screen uses the Stripe payment system for safe and secure payment of purchases.
- As a Site User, I want to be able to have a user profile so that I can view my order history and order confirmations and save my payment information.
    - On registration of a new account, a user profile is automatically rendered. Here the user can view their order history and shipping details.
- As a Site User, I want to be able to view a list of products so that I can select some to purchase.
    - On the porducts page, a list of product cards are visible, showing the product name, rating, price, category and an image.
- As a Site User, I want to be able to easily see what I have searched for and the number of results so that I can quickly decide whether the product I want is available.
    - When a search query has been entered, the user is brought to a filtered products page where they can see the products which align with their search, as well as an indicator of how many items where found relating to the search query.
- As a Site User, I want to be able to view a specific category of products so that I can quickly find products I am interested in without having to search through all products.
    - In the nav there are links to each category class for ease of access. In addition, on the products page, there are category buttons that filter with the products currently visible.
- As a Site User, I want to be able to view individual product details so that I can identify the price, description, product rating, product image and sizes.
    - Each product in the products list has it's own info page which details the price, description, product rating, product image and sizes.
- As a Site User, I want to be able to easily view the total of my purchase at any time so that I can avoid spending too much.
    - The shopping bag icon in the header gives an up-to-date counter of the current shopping bag total. In addition, each item added to the shopping bag activates a pop-up which details your current bag summary, prices, total cost and shipping.
- As a Site User, I want to be able to view items in my bag to be purchased so that I can identify the total cost of my purchase and all items I will receive.
    - There is a shopping bag page which allows the user to view all products currently sleected, their sizes and quantities, and the total cost with and without shipping if applicable. Here the user can also update and delete items from the shopping bag if required.
- As a Site User, I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the needed information to make a purchase.
    - The link to the shopping bag page advises the checkout is secure, and the payment information input is set to ensure the user's information is correct and valid before purchasing.
- As a Site User, I want to be able to view an order confirmation after checkout so that I can verify that I haven't made any mistakes.
    - On submitting a purchase, the user is shown the order confirmation page which details the order information, the shipping details, product information and the total cost. This information can also be viewed on the user profile in the order history section.

#### Store Owner
- As a Store Owner, I want to be able to add a product so that I can add new items to my store.
    - There is a page accessible only by superusers where store owners can add products to the store. The link for this page is in the user acconut dropdown in the header. This link takes the user to the add product page where they can fill the product details in the form.
- As a Store Owner, I want to be able to edit/update a product so that I can change product prices, descriptions, images, and other product criteria.
    - On the individual products' pages, admin users can can see a link to update the product information. Clicking the link brings the store owner to a prepopulated form where adjustments can be made to the specific product.
- As a Store Owner, I want to be able to delete a product so that I can remove items that are no longer for sale.
    - On the individual products' pages, superusers can can see a link to delete the product information. Clicking the link immediately deletes the product page and information.

[Back to top](#)

### Automated Testing
#### Code Validation
HTML pages - PASSES
Create post - PASSES
User profile - PASSES
Post detail - PASSES
Edit post - PASSES

### Compatibility Testing
- The site looks the same on different browsers.
- The site is responsive across devices.

## Deployment 
For the project, I used the [GitPod](https://gitpod.io/) cloud development IDE. I committed the code to Git and then pushed to [GitHub](https://github.com/) using the terminal. After, I deployed to code to [Heroku](https://heroku.com/).

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the URL next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary URL, adding into the settings.py file also.
    - In settings.py add the following sections:
        - STATIC_URL
        - STATICFILES_DIRS
        - MEDIA_URL
        - MEDIA_ROOT
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['app_name.herokuapp.com', 'localhost']

4. Set DISABLE_COLLECTSTATIC and Deploy to Heroku:
    - Create three directories in the main directory; media, storage and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - in the terminal, log in to Heroku and then enter the following:
        - heroku config:set DISABLE_COLLECTSTATIC=1 --app (Heroku App Name)
    - Go to the 'Deploy' tab on Heroku and connect to GitHub, then to the required repository.
    Click on 'Deploy Branch' and wait for the build to load. When the build is complete, the app can be opened through Heroku. 

### Forking the Repository
By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps:

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/KryanLive "Link to GitHub Repo").
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.

### Creating a Clone
How to run this project locally:
1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/KryanLive "Link to GitHub Repo").
5. Click the green "GitPod" button in the top right corner of the repository.
This will trigger a new GitPod workspace to be created from the code in GitHub where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](repo URL "Link to GitHub Repo").
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.

```
git clone https://github.com/USERNAME/REPOSITORY
```

8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "Link to GitHub troubleshooting")

[Back to top ⇧](#)

## Credits 

## Acknowledgements 

- Thank you to my wonderful family for always supporting me
- Thank you to Hassan for always listening to me, encouraging, supporting me and giving me his opinion when I need it


