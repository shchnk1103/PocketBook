import { createRouter, createWebHistory } from "vue-router";
import LoginPages from "../views/LoginPages";
import test from "../views/test";

const routes = [
  {
    path: "/",
    name: "Login",
    component: LoginPages,
  },
  {
    path: "/test",
    name: "Test",
    component: test,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
