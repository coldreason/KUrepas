import axios from "axios";

const API = axios.create({
  baseURL: "http://54.180.109.46:5000/",
});

export default API;
