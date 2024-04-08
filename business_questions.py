import sqlite3

def create_database():
    conn = sqlite3.connect('business_questions.db')
    cursor = conn.cursor()

    # Create a table to store the questions
    cursor.execute('''CREATE TABLE IF NOT EXISTS questions (
                        id INTEGER PRIMARY KEY,
                        category TEXT,
                        question TEXT,
                        option_a TEXT,
                        option_b TEXT,
                        option_c TEXT,
                        option_d TEXT,
                        answer TEXT
                        )''')

    conn.commit()
    conn.close()

def populate_database():
    question_sets = {
        "Business Management": [
            {"question": "What is the primary goal of financial management?", "a": "Maximize customer satisfaction", "b": "Maximize shareholder wealth", "c": "Maximize employee happiness", "d": "Maximize market share", "answer": "b"},
            {"question": "Define SWOT analysis in business management.", "a": "Strength, Weakness, Operation, Technology", "b": "Strength, Weakness, Opportunity, Threat", "c": "Strength, Wealth, Opportunity, Technology", "d": "Strategy, Weakness, Opportunity, Trade", "answer": "b"},
            {"question": "What is the difference between leadership and management?", "a": "Leadership focuses on strategy, management focuses on execution", "b": "Leadership is about inspiring, management is about controlling", "c": "Leadership is about short-term goals, management is about long-term goals", "d": "There is no difference between leadership and management", "answer": "b"},
            {"question": "Explain the concept of economies of scale.", "a": "Cost advantages by increasing the scale of production", "b": "Cost disadvantages by increasing the scale of production", "c": "Maintaining the same cost regardless of production scale", "d": "Cost advantages by decreasing the scale of production", "answer": "a"},
            {"question": "What is marketing segmentation?", "a": "Dividing a market into smaller groups based on specific characteristics", "b": "Selling products to different markets", "c": "Focusing marketing efforts on a single segment", "d": "Creating a single marketing message for all customers", "answer": "a"},
            {"question": "Define corporate social responsibility (CSR).", "a": "Cost-saving measures in a corporation", "b": "Integrating social and environmental concerns in operations", "c": "Maximizing profits at any cost", "d": "A corporate charity fund", "answer": "b"},
            {"question": "What is the importance of strategic planning in business management?", "a": "It reduces the need for day-to-day management", "b": "It aligns organizational efforts to achieve long-term goals", "c": "It eliminates the need for change management", "d": "It ensures short-term profitability", "answer": "b"},
            {"question": "Explain the concept of supply chain management.", "a": "Managing the flow of goods from producers to consumers", "b": "Managing the flow of goods within a company", "c": "Managing the flow of money within a company", "d": "Managing the flow of information within a company", "answer": "a"},
            {"question": "What are the key components of a business plan?", "a": "Executive summary, company description, market analysis", "b": "Marketing and sales strategy, financial projections, appendix", "c": "Organization and management structure, product or service offerings", "d": "All of the above", "answer": "d"},
            {"question": "Define organizational culture.", "a": "The physical layout of an organization", "b": "The shared values, beliefs, and behaviors within an organization", "c": "The strategic goals of an organization", "d": "The number of employees in an organization", "answer": "b"}
        ],
        "Business Stats": [
            {"question": "What is regression analysis used for in business statistics?", "a": "To predict future stock prices", "b": "To identify patterns and relationships between variables", "c": "To calculate the mean and standard deviation", "d": "To measure central tendency", "answer": "b"},
            {"question": "Define standard deviation in statistics.", "a": "The average of all data points", "b": "The spread or dispersion of a set of data", "c": "The middle value of a dataset", "d": "The number of times a value occurs in a dataset", "answer": "b"},
            {"question": "What is correlation analysis used for in business statistics?", "a": "To predict future trends", "b": "To identify patterns and relationships between variables", "c": "To calculate the mean and standard deviation", "d": "To measure central tendency", "answer": "b"},
            {"question": "Define probability distribution in statistics.", "a": "A function that describes the likelihood of obtaining the possible values of a random variable", "b": "A method for organizing and summarizing data", "c": "A measure of the dispersion of a set of data", "d": "The number of times a value occurs in a dataset", "answer": "a"},
            {"question": "What is the difference between population and sample in statistics?", "a": "Population refers to a subset of the sample", "b": "Sample refers to a subset of the population", "c": "There is no difference between population and sample", "d": "Population refers to descriptive statistics, sample refers to inferential statistics", "answer": "b"},
            {"question": "Explain the concept of hypothesis testing.", "a": "A method for organizing and summarizing data", "b": "A process of making predictions about future outcomes based on past data", "c": "A statistical method used to make inferences about a population parameter", "d": "A measure of the dispersion of a set of data", "answer": "c"},
            {"question": "What is the purpose of regression analysis in business statistics?", "a": "To determine the probability of an event occurring", "b": "To identify the relationship between two or more variables", "c": "To calculate the mean and standard deviation", "d": "To measure central tendency", "answer": "b"},
            {"question": "Define standard error in statistics.", "a": "The average of all data points", "b": "The spread or dispersion of a set of data", "c": "A measure of the accuracy of a sample statistic in estimating a population parameter", "d": "The number of times a value occurs in a dataset", "answer": "c"},
            {"question": "What is the significance level in hypothesis testing?", "a": "The probability of rejecting a true null hypothesis", "b": "The probability of failing to reject a false null hypothesis", "c": "The probability of rejecting a false null hypothesis", "d": "The probability of failing to reject a true null hypothesis", "answer": "a"},
            {"question": "Define confidence interval in statistics.", "a": "The range of values within which a population parameter is likely to fall", "b": "The mean value of a dataset", "c": "A measure of the dispersion of a set of data", "d": "The number of times a value occurs in a dataset", "answer": "a"}
        ],
        "Database Management": [
            {"question": "What is a primary key in a database table?", "a": "A key used to unlock the database", "b": "A unique identifier for each record in the table", "c": "The first column in the table", "d": "The last column in the table", "answer": "b"},
            {"question": "Define normalization in database management.", "a": "The process of reducing data redundancy and improving data integrity", "b": "The process of increasing data redundancy and decreasing data integrity", "c": "The process of organizing data in alphabetical order", "d": "The process of deleting duplicate records", "answer": "a"},
            {"question": "What is the purpose of a foreign key in a database?", "a": "To ensure data integrity and enforce relationships between tables", "b": "To speed up query performance", "c": "To store large binary data", "d": "To generate unique identifiers for each record", "answer": "a"},
            {"question": "Define database normalization.", "a": "The process of reducing data redundancy and improving data integrity", "b": "The process of increasing data redundancy and decreasing data integrity", "c": "The process of organizing data in alphabetical order", "d": "The process of deleting duplicate records", "answer": "a"},
            {"question": "What is the difference between a SQL query and a SQL statement?", "a": "There is no difference, they are synonyms", "b": "A query retrieves data, a statement performs an action", "c": "A query performs an action, a statement retrieves data", "d": "A query is used for data manipulation, a statement is used for data definition", "answer": "b"},
            {"question": "Explain the concept of data warehousing.", "a": "Storing data in a centralized location for reporting and analysis", "b": "Storing data in a distributed manner for improved performance", "c": "Storing data in a hierarchical structure for easy access", "d": "Storing data in a relational database for transaction processing", "answer": "a"},
            {"question": "What is the purpose of a stored procedure in database management?", "a": "To optimize query performance by storing frequently used queries", "b": "To enforce referential integrity between tables", "c": "To define a set of SQL statements that perform a specific task", "d": "To generate unique identifiers for each record", "answer": "c"},
            {"question": "Define database indexing.", "a": "The process of adding data to a database", "b": "The process of organizing data in alphabetical order", "c": "The process of improving query performance by creating searchable keys", "d": "The process of storing large binary data", "answer": "c"},
            {"question": "What is ACID compliance in database management?", "a": "A standard for ensuring data integrity and consistency in transactions", "b": "A standard for encrypting data stored in a database", "c": "A standard for optimizing query performance", "d": "A standard for defining database schema", "answer": "a"},
            {"question": "Explain the concept of database mirroring.", "a": "A technique for optimizing query performance by storing data in multiple locations", "b": "A technique for ensuring high availability and disaster recovery by maintaining redundant copies of a database", "c": "A technique for encrypting sensitive data stored in a database", "d": "A technique for synchronizing data between different databases", "answer": "b"}
        ],
        "Marketing": [
            {"question": "What is the purpose of a marketing plan?", "a": "To set financial goals", "b": "To outline the company's organizational structure", "c": "To define marketing objectives and strategies", "d": "To analyze competitors' pricing strategies", "answer": "c"},
            {"question": "Define market segmentation in marketing.", "a": "The process of targeting a single market segment", "b": "The process of dividing a broad target market into smaller groups based on specific characteristics", "c": "The process of increasing market share", "d": "The process of reducing production costs", "answer": "b"},
            {"question": "What is the marketing mix?", "a": "A strategy for distributing products to consumers", "b": "A framework for analyzing and implementing marketing strategies", "c": "A measure of a company's market share", "d": "A tool for managing customer relationships", "answer": "b"},
            {"question": "Define brand positioning in marketing.", "a": "The process of pricing products based on brand reputation", "b": "The place where a product is sold in a retail store", "c": "The way a brand is perceived in relation to competitors", "d": "The process of designing a logo for a brand", "answer": "c"},
            {"question": "What is the purpose of market segmentation?", "a": "To sell products to different markets", "b": "To identify potential customers with similar needs and characteristics", "c": "To increase market share by targeting all customer segments", "d": "To minimize marketing expenses", "answer": "b"},
            {"question": "Explain the concept of product lifecycle in marketing.", "a": "The process of introducing a new product to the market", "b": "The stages a product goes through from introduction to decline", "c": "The process of testing a product before launch", "d": "The process of promoting a product to potential customers", "answer": "b"},
            {"question": "What is the purpose of a SWOT analysis in marketing?", "a": "To identify internal strengths and weaknesses, as well as external opportunities and threats", "b": "To analyze customer satisfaction levels", "c": "To determine pricing strategies", "d": "To measure brand awareness", "answer": "a"},
            {"question": "Define market research in marketing.", "a": "The process of identifying and analyzing potential customers", "b": "The process of setting prices for products", "c": "The process of promoting products through various channels", "d": "The process of gathering, analyzing, and interpreting information about a market", "answer": "d"},
            {"question": "What is the purpose of a marketing plan?", "a": "To set financial goals", "b": "To outline the company's organizational structure", "c": "To define marketing objectives and strategies", "d": "To analyze competitors' pricing strategies", "answer": "c"},
            {"question": "Define customer segmentation in marketing.", "a": "The process of targeting a single market segment", "b": "The process of dividing a broad target market into smaller groups based on specific characteristics", "c": "The process of increasing market share", "d": "The process of reducing production costs", "answer": "b"}
        ],
        "Business Application Development": [
            {"question": "What is the purpose of version control in software development?", "a": "To manage customer relations", "b": "To track changes in code and collaborate with team members", "c": "To monitor server performance", "d": "To analyze user behavior", "answer": "b"},
            {"question": "Define agile methodology in software development.", "a": "A software development approach that emphasizes planning and documentation", "b": "A software development approach that focuses on flexibility, collaboration, and incremental development", "c": "A software development approach that prioritizes individual productivity over team collaboration", "d": "A software development approach that relies on a fixed scope and timeline", "answer": "b"},
            {"question": "What statement allows you to display strings and integers in the python terminal?","a": "console.log", "b": "console/log", "c": "print","d": "Print","answer": "c"},
            {"question": "What is python?", "a": "a spider", "b": "a bird", "c": "a programming language", "d": "a mobile app", "answer": "c"},
            {"question": "How many functions are in python?", "a": "127", "b": "11900", "c": "To many to worry about", "d": "1", "answer": "c"},
            {"question": "Which of the following is not a programming language", "a": "C++", "b": "A+", "c": "Java", "d": "C sharp", "answer": "b"},
            {"question": "What kind of jobs can you journey into with Python knowledge", "a": "Software Devolpment", "b": "Data Anaylst", "c": "Janitor", "d": "Machine learning Engineer", "answer": "c"},
            {"question": "What is sql used for? ", "a": "To manage customer relations", "b": "To track changes in code and collaborate with team members", "c": "To monitor server performance", "d": "stroing and controlling data", "answer": "d"},
            {"question": "Which of the follwing is not a loop in python", "a": "for loop", "b": "Through loop", "c": "for loop", "d": "none of the above", "answer": "b"},
            {"question": "Which loop iterates over itself for a controlled number of times?", "a": "for loop", "b": "while loop", "c": "swing loop", "d": "all of the above", "answer": "a"},
        ]
    }

    conn = sqlite3.connect('business_questions.db')
    cursor = conn.cursor()

    for category, questions in question_sets.items():
        for question in questions:
            cursor.execute('''INSERT INTO questions (category, question, option_a, option_b, option_c, option_d, answer)
                              VALUES (?, ?, ?, ?, ?, ?, ?)''', (category,
                                                                question['question'],
                                                                question['a'],
                                                                question['b'],
                                                                question['c'],
                                                                question['d'],
                                                                question['answer']))

    conn.commit()
    conn.close()

def print_table():
    conn = sqlite3.connect('business_questions.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

def main():
    create_database()
    populate_database()
    print_table()

if __name__ == "__main__":
    main()
