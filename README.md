<h1>Recipe API</h1>
    <h2>Overview</h2>
    <p>
        The Recipe API is a RESTful service built using the Django Rest Framework (DRF) that allows users to manage and share recipes. 
        It supports user authentication, CRUD operations, and category-based recipe filtering.
    </p>
    <hr>
    <h2>Features</h2>
    <ul>
        <li><strong>User Authentication</strong>: Secure registration, login, and token-based authentication.</li>
        <li><strong>CRUD Operations</strong>: Create, read, update, and delete recipes.</li>
        <li><strong>Categories</strong>: Organize recipes into categories (e.g., Breakfast, Lunch, Dinner).</li>
        <li><strong>Ingredients</strong>: Manage ingredients with their quantities for each recipe.</li>
        <li><strong>Pagination</strong>: Browse recipes with pagination for large datasets.</li>
        <li><strong>Filtering & Search</strong>: Filter recipes by category, ingredients, or keywords.</li>
        <li><strong>Image Upload</strong>: Attach images to recipes for a better user experience.</li>
    </ul>
    <hr>
    <h2>Endpoints</h2>
    <table border="1" cellpadding="10">
        <thead>
            <tr>
                <th>Endpoint</th>
                <th>HTTP Method</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><code>/api/recipes/</code></td>
                <td>GET</td>
                <td>List all recipes.</td>
            </tr>
            <tr>
                <td><code>/api/recipes/{id}/</code></td>
                <td>GET</td>
                <td>Retrieve a single recipe by ID.</td>
            </tr>
            <tr>
                <td><code>/api/recipes/</code></td>
                <td>POST</td>
                <td>Create a new recipe.</td>
            </tr>
            <tr>
                <td><code>/api/recipes/{id}/</code></td>
                <td>PUT</td>
                <td>Update an existing recipe.</td>
            </tr>
            <tr>
                <td><code>/api/recipes/{id}/</code></td>
                <td>DELETE</td>
                <td>Delete a recipe.</td>
            </tr>
            <tr>
                <td><code>/api/categories/</code></td>
                <td>GET</td>
                <td>List all categories.</td>
            </tr>
        </tbody>
    </table>
    <hr>
    <h2>Authentication</h2>
    <p>
        The API uses token-based authentication. Users must include the token in the <code>Authorization</code> header 
        for endpoints that require authentication.
    </p>
    <pre><code>Authorization: Token YOUR_API_TOKEN</code></pre>
    <hr>
    <h2>Models</h2>
    <ul>
        <li><strong>Recipe</strong>: Contains details like name, description, instructions, and category.</li>
        <li><strong>Category</strong>: Organizes recipes into logical groups.</li>
        <li><strong>Ingredient</strong>: Stores ingredient names and quantities for each recipe.</li>
    </ul>
    <hr>
    <h2>Example Response</h2>
    <pre><code>
{
    "id": 1,
    "name": "Pancakes",
    "description": "Fluffy homemade pancakes.",
    "instructions": "Mix all ingredients and cook on a hot skillet.",
    "category": "Breakfast",
    "ingredients": [
        {"name": "Flour", "quantity": "2 cups"},
        {"name": "Milk", "quantity": "1.5 cups"},
        {"name": "Eggs", "quantity": "2"}
    ],
    "image_url": "http://example.com/media/pancakes.jpg"
}
    </code></pre>

    <hr>

    <h2>Setup</h2>
    <ol>
        <li>Clone the repository.</li>
        <li>Install dependencies with <code>pip install -r requirements.txt</code>.</li>
        <li>Run migrations with <code>python manage.py migrate</code>.</li>
        <li>Start the server using <code>python manage.py runserver</code>.</li>
    </ol>
