import { Link } from "react-router-dom";

function Header() {
  return (
    <div
      style={{
        width: "100vw",
        height: "50px",
        position: "fixed",
        left: 0,
        top: 0,
        backgroundColor: "#1a1b23",
        display: "flex",
        flexDirection: "row",
        alignItems: "center",
        paddingLeft: "20px",
      }}
    >
      {" "}
      <Link to="/">
        <h3
          style={{
            margin: 0,
            color: "white",
          }}
        >
          Max-Connnect
        </h3>
      </Link>
      <Link to="/new_task">
        <p style={{ margin: 0, marginLeft: "50px", color: "#ffffffc0" }}>
          Task 추가
        </p>
      </Link>
      <Link to="/upload_model">
        <p style={{ margin: 0, marginLeft: "25px", color: "#ffffffc0" }}>
          Model 업로드
        </p>
      </Link>
    </div>
  );
}
export default Header;
