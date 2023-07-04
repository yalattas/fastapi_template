db.createUser(
    {
        user: "busername",
        pwd: "bpassowrd",
        roles: [
            {
                role: "readWrite",
                db: "data"
            }
        ]
    }
);