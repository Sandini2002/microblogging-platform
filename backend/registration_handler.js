const db = require('./db'); // Import your database connection
const bcrypt = require('bcrypt'); // For hashing passwords

async function registerUser(username, email, password) {
    try {
        // Hash the password
        const passwordHash = await bcrypt.hash(password, 10);

        // Insert user into the database
        const query = `
            INSERT INTO users (username, email, password_hash)
            VALUES (?, ?, ?)
        `;
        await db.execute(query, [username, email, passwordHash]);

        console.log('User registered successfully');
    } catch (error) {
        console.error('Error registering user:', error);
        throw error;
    }
}

module.exports = { registerUser };
