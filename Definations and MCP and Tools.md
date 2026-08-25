superbase MCP - Interact with DB using natural language
Data warehouse - (KIMBALL)Copy of transaction data specifically structured for query and analysis

Sources -> ETL -> Dimensional Data -> Business Intelligence APP

- Fact Tables -
    - Record business events, like an order, a phone call, a book review
    - Fact tables columns record events recorded in quantifiable metrics like quantity of an item, duration of a call, a book rating
- Dimension Tables
    - Record the context of the business events, e.g. who, what, where, why, etc..
    - Dimension tables columns contain attributes like the store at which an item is purchased, or the customer who made the call, etc.


<img width="1538" height="1440" alt="image" src="https://github.com/user-attachments/assets/7b72c218-a910-4696-88ee-1d776d865ff5" />

<img width="1094" height="1326" alt="image" src="https://github.com/user-attachments/assets/59d3dc36-108f-4815-a6c8-623c69ca1f2c" />


-
Get Months from date => EXTRACT(month FROM p.payment_date) as months -> [1,2,3,...]
IS Weekend => CASE WHEN EXTRACT(ISODOW FROM p.payment_date) IN (6, 7) THEN true ELSE false

3NF => customer -> address -> city -> country

<img width="1096" height="553" alt="image" src="https://github.com/user-attachments/assets/01fe34a6-1566-4168-b31a-31fc8bff5a89" />

<img width="1099" height="578" alt="image" src="https://github.com/user-attachments/assets/803e3682-055a-4031-a19e-58a4b48d813c" />

<img width="1104" height="574" alt="image" src="https://github.com/user-attachments/assets/de915f51-992d-4087-a4ed-ae71276b4fa2" />

<img width="1111" height="582" alt="image" src="https://github.com/user-attachments/assets/a43231ee-cd93-4c77-ab6e-ea268ac77825" />

<img width="1079" height="526" alt="image" src="https://github.com/user-attachments/assets/dc720a65-9328-49e0-b271-89406a01bd14" />


