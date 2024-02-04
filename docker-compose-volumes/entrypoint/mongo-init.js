use chartdata
db.createUser({
    user: process.env.DB_MONGO_USERNAME, pwd: process.env.DB_MONGO_PASSWORD, roles: ["dbOwner"]
});

db.orders.insert({title: "Test"});
