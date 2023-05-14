import axios from "axios";

const API = axios.create({
  baseURL: "http://172.20.10.3:5000/",
});

export default API;
