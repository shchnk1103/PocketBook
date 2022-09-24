import { createRouter, createWebHistory } from "vue-router";
import LoginPage from "@/views/LoginPage";
import HomePage from "@/views/HomePage";

const routes = [
  {
    path: "/",
    name: "Login",
    component: LoginPage,
  },
  {
    path: "/home",
    name: "Home",
    component: HomePage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
