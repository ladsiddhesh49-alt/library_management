const API_URL = "http://127.0.0.1:8000";

document
.getElementById("userForm")
.addEventListener("submit", async (e) => {

    e.preventDefault();

    const user = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        is_librarian: false
    };

    await fetch(`${API_URL}/users/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(user)
    });

    loadUsers();
});

async function loadUsers() {

    const response =
        await fetch(`${API_URL}/users/`);

    const users =
        await response.json();

    const table =
        document.getElementById("userTable");

    table.innerHTML = "";

    users.forEach(user => {

        table.innerHTML += `
        <tr>
            <td>${user.id}</td>
            <td>${user.name}</td>
            <td>${user.email}</td>
        </tr>`;
    });
}

loadUsers();