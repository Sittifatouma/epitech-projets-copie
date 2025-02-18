import { createRouter, createWebHashHistory } from "vue-router";
import MainPage from "@/views/MainPage.vue";
import RegisterPage from "@/views/RegisterPage.vue";
import SignIn from "@/views/SignIn.vue";
import MyProfil from "@/views/profil/MyProfil.vue"
import ListPraticiensView from "@/views/ListPraticiensView.vue"
import AboutView from "@/views/AboutView.vue"
import CopyrightView from "@/views/CopyrightView.vue"
import PolitiqueConf from "@/views/PolitiqueConf.vue"



const routes = [
  { path: "/", redirect: "/home" },
  {
    path: "/home",
    name: "home",
    component: MainPage,
  },
  {
    path: "/praticiens",
    name: "praticiens",
    component: ListPraticiensView,
  },
  {
    path: "/myprofil",
    name: "profil",
    component: MyProfil,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterPage,
  },
  {
    path: "/signin",
    name: "signin",
    component: SignIn,
  },
  {
    path: "/about",
    name: "about",
    component: AboutView,

  },
  {
    path: "/copyrightview",
    name: "copyrightview",
    component: CopyrightView,

  },
  {
    path: "/PolitiqueConf",
    name: "PolitiqueConf",
    component: PolitiqueConf,

  },
];
PolitiqueConf
const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
