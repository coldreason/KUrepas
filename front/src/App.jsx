import { Routes, Route } from "react-router-dom";
import UploadModel from "./routes/UploadModel";
import NewTask from "./routes/NewTask";
import Monitor from "./routes/Monitor";

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Monitor />} />
        <Route path="/upload_model" element={<UploadModel />} />
        <Route path="/new_task" element={<NewTask />} />
      </Routes>
    </div>
  );
}

export default App;
