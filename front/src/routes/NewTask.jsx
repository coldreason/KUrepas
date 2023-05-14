import TaskCard from "../components/TaskCard";
import "react-horizontal-scrolling-menu/dist/styles.css";

function NewTask() {
  return (
    <div
      style={{
        width: "100vw",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        marginTop: "10vh",
      }}
    >
      <h2>Task를 등록해주세요.</h2>
      <div>
        <TaskCard />
      </div>
    </div>
  );
}
export default NewTask;
