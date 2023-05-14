import { useRef } from "react";

function UploadModel() {
  const fileInput = useRef(null);

  const handleButtonClick = () => {
    fileInput.current.click();
  };
  return (
    <div
      style={{
        width: "100vw",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        marginTop: "10vh",
      }}
    >
      <h2>모델을 업로드해주세요.</h2>
      <button onClick={handleButtonClick} style={{ width: "150px" }}>
        파일 선택
      </button>
      <input type="file" ref={fileInput} style={{ display: "none" }} />
      <button
        onClick={() => {
          setTimeout(() => {
            alert("모델 업로드 성공");
          }, 800);
        }}
        style={{
          width: "150px",
          marginTop: "10px",
          backgroundColor: "#646cff",
        }}
      >
        업로드
      </button>
    </div>
  );
}
export default UploadModel;
