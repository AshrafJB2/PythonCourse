const express = require("express");
const router = express.Router();
const controller = require("../controllers/userController");

router.post("/register", controller.register);
router.post("/login", controller.login);
router.get("/users", controller.getAllUsers);
router.get("/users/:id", controller.getUserById);
router.put("/users/:id", controller.updateUserById);

module.exports = router;
