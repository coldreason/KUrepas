import { Tooltip } from "@mui/material";
import { motion } from "framer-motion";
import { useState } from "react";
import API from "../utils/axios";
import { styled } from "styled-components";
function EdgeCard({ edge }) {
  const [tooltipText, setTooltipText] = useState("");

  const onTooltipOpen = async (id) => {
    const fetchData = async () => {
      try {
        const { data } = await API.get(`/get_task/${id}`);
        console.log(data);
        setTooltipText(
          `시점 x: ${data.pos_s_x}, y: ${data.pos_s_y} | 종점 x: ${data.pos_e_x}, y: ${data.pos_e_y}`
        );
      } catch (error) {
        console.log(error);
      }
    };
    fetchData();
  };
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        padding: "20px",
        width: "250px",
        height: "200px",
        marginTop: "20px",
        marginBottom: "20px",
        marginRight: "20px",
        marginLeft: "20px",
        borderRadius: "20px",
        backgroundColor: "#1a1b23",
        boxShadow: "5px 5px 20px #00000050",
      }}
    >
      <div style={{ display: "flex", flexDirection: "row" }}>
        <div style={{ display: "flex", flexDirection: "column", flex: 5 }}>
          <p
            style={{
              width: "fit-content",
              padding: "5px",
              fontWeight: 800,
              margin: "0px",
              borderRadius: "5px",
              backgroundColor: "#646cff80",
            }}
          >{`Edge ${edge ? edge.edge_id : ""}`}</p>
          <div
            style={{ display: "flex", flexDirection: "row", marginTop: "30px" }}
          >
            <p style={{ fontWeight: 600, margin: "0px" }}>{`x: ${
              edge ? edge.pos_x : ""
            }`}</p>
            <p
              style={{ fontWeight: 600, margin: "0px", marginLeft: "30px" }}
            >{`y: ${edge ? edge.pos_y : ""}`}</p>
          </div>
          <p style={{ fontWeight: 600, margin: "0px", marginTop: "10px" }}>
            {`현재 Task : ${edge ? edge.current_task : ""}`}
          </p>
        </div>
        {edge ? (
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              flex: 3,
              justifyContent: "center",
            }}
          >
            <div
              style={{
                width: "100px",
                height: "100px",
                border: "1px solid white",
              }}
            >
              {JSON.parse(edge.task_set).map((e1, index1) => (
                <div
                  key={[edge.edge_id, index1, e1]}
                  style={{ display: "flex", flexDirection: "row" }}
                >
                  {e1.map((e2, index2) => (
                    <div
                      key={[edge.edge_id, index1, index2]}
                      style={{
                        width: "5px",
                        height: "5px",
                        backgroundColor: e2 == 1 ? "white" : "transparent",
                      }}
                    ></div>
                  ))}
                </div>
              ))}
            </div>
          </div>
        ) : null}
      </div>
      <p style={{ fontWeight: 800, margin: "0px", marginTop: "30px" }}>
        Task List
      </p>
      {edge ? (
        <motion.div
          layout
          // layoutId={edge.edge_id}
          // key={list}
          style={{
            width: "fit-content",
            display: "flex",
            flexDirection: "row",
            marginTop: "5px",
            borderRadius: "5px",
            overflow: "hidden",
            border: edge.task_list.length > 0 ? "1px solid white" : "0px none",
          }}
        >
          {edge.task_list.map((e, index) => (
            <Tooltip
              key={index}
              title={tooltipText}
              onOpen={() => {
                onTooltipOpen(e);
              }}
              arrow
            >
              <Box
                style={{
                  cursor: "pointer",
                  width: "25px",
                  height: "25px",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  borderRight:
                    index === edge.task_list.length - 1
                      ? "0px"
                      : "1px solid white",
                }}
              >
                <p style={{ margin: "0px" }}>{e}</p>
              </Box>
            </Tooltip>
          ))}
        </motion.div>
      ) : null}
    </div>
  );
}
export default EdgeCard;
const Box = styled.div`
  background-color: #3c3e52;
  &:hover {
    background-color: #3c3e5250;
  }
`;
