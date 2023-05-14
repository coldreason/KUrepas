import { useState } from "react";
import { styled } from "styled-components";
import API from "../utils/axios";

function TaskCard() {
  const [x1, setX1] = useState("");
  const [y1, setY1] = useState("");
  const [x2, setX2] = useState("");
  const [y2, setY2] = useState("");
  const register = async () => {
    const re = /^-?[0-9]+([.,][0-9]+)?$/;
    if (!re.test(x1) || !re.test(y1) || !re.test(x2) || !re.test(y2)) {
      alert("정수 또는 소수만 입력 가능합니다.");
      return;
    }
    try {
      const result = await API.post(`/taskqueue`, {
        pos_s_x: x1,
        pos_s_y: y1,
        pos_e_x: x2,
        pos_e_y: y2,
      });
      console.log(result);
      setX1("");
      setY1("");
      setX2("");
      setY2("");
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        width: "300px",
        marginTop: "30px",
        marginBottom: "30px",
        borderRadius: "20px",
        backgroundColor: "#1a1b23",
        boxShadow: "5px 5px 20px #00000050",
      }}
    >
      <div
        style={{ display: "flex", flexDirection: "column", marginTop: "20px" }}
      >
        <div style={{ display: "flex", flexDirection: "row" }}>
          <p style={{ fontWeight: 700, marginRight: "10px" }}>시점</p>
          <Input
            placeholder="x"
            value={x1}
            onChange={(e) => {
              setX1(e.target.value);
            }}
          />
          <Input
            placeholder="y"
            value={y1}
            onChange={(e) => {
              setY1(e.target.value);
            }}
          />
        </div>
        <div style={{ display: "flex", flexDirection: "row" }}>
          <p style={{ fontWeight: 700, marginRight: "10px" }}>종점</p>
          <Input
            placeholder="x"
            value={x2}
            onChange={(e) => {
              setX2(e.target.value);
            }}
          />
          <Input
            placeholder="y"
            value={y2}
            onChange={(e) => {
              setY2(e.target.value);
            }}
          />
        </div>
      </div>

      <RegisterBtn onClick={register}>등록하기</RegisterBtn>
    </div>
  );
}
export default TaskCard;

const Input = styled.input`
  width: 70px;
  background-color: transparent;
  margin-left: 10px;
  margin-right: 10px;
  border-top: 0px none;
  border-left: 0px none;
  border-right: 0px none;
  border-bottom: 1.5px solid #646cff;
`;
const RegisterBtn = styled.button`
  width: 100%;
  margin-top: 30px;
  background-color: #2d2f54;
  border-radius: 0px 0px 20px 20px;
  &:hover {
    background-color: #646cff;
  }
`;
