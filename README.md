# UX
## Project Goals


## User Stories

1. As a user, I want to create an account so that I can save my basket and wishlist.

    **Acceptance Criteria**
    - User can register with email and username
    - User can log in and log out successfully
    - User session persists across pages

2. As a user, I want to browse available retro games so I can find items to purchase.

    **Acceptance Criteria**
    - User can see list of games
    - Each game displays title, console, genre, and image

3. As a user, I want to view detailed information about a game so I can decide if I want to buy it.

    **Acceptance Criteria**
    - Clicking a game opens the detail page
    - Page shows all relevant information
    
4. As a user, I want to filter games by console, genre, price, and grade so I can find specific items quickly.

    **Acceptance Criteria**
    - User can filter by console, genre, price, and grade
    - Results update based on filter selection

    **Notes**
    - Filtering was adapted to better reflect the data model. Console, genre, and availability filtering were implemented at game level, while price and grade filtering were excluded as these are attributes of individual graded items rather than the game itself.

5. As a user, I want to add graded games to my basket so I can purchase them later.

    **Acceptance Criteria**
    - User can add items to basket
    - Basket updates correctly with selected items

6. As a user, I want to view my basket so I can see selected items and total cost.

    **Acceptance Criteria**
    - Basket shows all selected items
    - Total price is calculated correctly
    

7. As a user, I want to update or remove items in my basket so I can adjust my purchase before checkout.

    **Acceptance Criteria**
    - User can increase/decrease quantity
    - User can remove items from basket

    **Notes**
    - Quantity adjustment was not implemented as each graded item is a unique product instance.
    

8. As a user, I want to securely pay for my items so I can complete my purchase.

    **Acceptance Criteria**
    - User can complete payment using Stripe test mode
    - Successful payment redirects to confirmation page

9. As a user, I want to see a confirmation after payment so I know my order was successful.

    **Acceptance Criteria**
    - User sees order summary after payment
    - Order is saved in database

10. As a user, I want to save items to a wishlist so I can view them later.

    **Acceptance Criteria**
    - User can save items to wishlist
    - Wishlist persists across sessions

11. As a site owner, I want to add, edit, and delete products so I can manage inventory.

    **Acceptance Criteria**
    - Admin can add new games and graded items
    - Changes update on site

12. As a user, I want to view my past orders so I can track my purchases.

    **Acceptance Criteria**
    - User can see all previous orders
    - Each order shows purchased items and totals

## Wireframes



## Design Choices


### Color Scheme


### Fonts


### Layout


### Imagery


# Database Design


## Models


## Relationships


# Features
## Existing Features


## CRUD Functionality
**Create:** 

**Read:** 

**Update:** 

**Delete:** 


# Technologies Used
## Languages


## Frameworks & Libraries


## Tools


# Testing

## User Story Testing
**User Story 1**



**Expected Result:**


**Test Steps**


**Result: **



**User Story 2**



**Expected Result:**


**Test Steps**


**Result: **


**User Story 3**



**Expected Result:**


**Test Steps**


**Result: **

**User Story 4**



**Expected Result:**


**Test Steps**


**Result: **

**User Story 5**


**Expected Result:**


**Test Steps**


**Result: **


**User Story 6**


**Expected Result:**


**Test Steps**


**Result: **

**User Story 7**


**Expected Result:**


**Test Steps**


**Result: **



**User Story 8**


**Expected Result:**


**Test Steps**



**Result: **



**User Story 9**



**Expected Result:**


**Test Steps**


**Result: **

**User Story 10**



**Expected Result:**


**Test Steps**


**Result: **

**User Story 11**



**Expected Result:**


**Test Steps**


**Result: **

**User Story 12**



**Expected Result:**


**Test Steps**


**Result: **



## Controls


### Buttons


### Forms


### Navigation


## Responsive Design


## Visual Feedback


### Examples


## Bugs & Fixes


## Validator Testing

### HTML Validation


### CSS Validation


### Lighthouse Scores
**Performance:** 

**Accessibility:** 

**Best Practices:** 

### Python Validation


# Deployment
## GitHub Repository


## Heroku Deployment



# Credits

