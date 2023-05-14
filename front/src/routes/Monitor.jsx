import { styled } from "styled-components";
import EdgeCard from "../components/EdgeCard";
import { useEffect, useState } from "react";
import API from "../utils/axios";
import { motion } from "framer-motion";
import { Tooltip } from "@mui/material";
import { Unity, useUnityContext } from "react-unity-webgl";

function Monitor() {
  const [edges, setEdges] = useState([]);
  const [taskQueue, setTaskQueue] = useState([]);
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
  useEffect(() => {
    const fetchData = async () => {
      try {
        const { data } = await API.get(`/get_edge`);
        setEdges(data);
        console.log(data);
      } catch (error) {
        console.log(error);
      }
    };
    const fetchTaskQueue = async () => {
      try {
        const { data } = await API.get(`/get_task_queue`);
        setTaskQueue(data);
      } catch (error) {
        console.log(error);
      }
    };
    setInterval(() => {
      fetchData();
      fetchTaskQueue();
    }, 600);
  }, []);
  const { unityProvider } = useUnityContext({
    loaderUrl: "build/myunityapp.loader.js",
    dataUrl: "build/myunityapp.data",
    frameworkUrl: "build/myunityapp.framework.js",
    codeUrl: "build/myunityapp.wasm",
  });
  return (
    <MainContainer>
      <UnityContainer>
        <div>
          <Unity
            unityProvider={unityProvider}
            style={{ width: "400px", height: "500px" }}
          />
        </div>
        <p
          style={{
            fontWeight: 700,
            margin: "0px",
            marginLeft: "20px",
            marginTop: "30px",
            marginBottom: "10px",
            fontSize: "30px",
          }}
        >
          Task Queue
        </p>
        <motion.div
          layout
          layoutId="taskQueue"
          key="taskQueue"
          style={{
            width: "fit-content",
            height: "50px",
            display: "flex",
            flexDirection: "row",
            marginLeft: "20px",
            marginTop: "5px",
            borderRadius: "15px",
            overflow: "hidden",
            border: taskQueue.length ? "1.5px solid white" : "0px none",
          }}
        >
          {taskQueue.map((e, index) => (
            <Tooltip
              key={e}
              title={tooltipText}
              onOpen={() => {
                onTooltipOpen(e);
              }}
              arrow
            >
              <Box
                style={{
                  cursor: "pointer",
                  width: "50px",
                  height: "50px",
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  borderRight:
                    index === taskQueue.length - 1
                      ? "0px"
                      : "1.5px solid white",
                }}
              >
                <p style={{ margin: "0px", fontWeight: 700, fontSize: "20px" }}>
                  {e}
                </p>
              </Box>
            </Tooltip>
          ))}
        </motion.div>
      </UnityContainer>
      <div
        style={{
          width: "2px",
          backgroundColor: "#1a1b23",
        }}
      />
      <MonitorContainer>
        <CardsContainer>
          <EdgeCard edge={edges[0]} />
          <EdgeCard edge={edges[1]} />
          <EdgeCard edge={edges[2]} />
          <EdgeCard edge={edges[3]} />
          <EdgeCard edge={edges[4]} />
        </CardsContainer>
      </MonitorContainer>
    </MainContainer>
  );
}
export default Monitor;
const MainContainer = styled.div`
  display: flex;
  flex-direction: row;
  width: 100vw;
  min-height: 100vh;
`;
const UnityContainer = styled.div`
  width: 400px;
  margin-top: 50px;
`;
const MonitorContainer = styled.div`
  display: flex;
  flex-direction: column;
  margin-top: 50px;
`;
const Row = styled.div`
  display: flex;
  flex-direction: row;
`;
const Box = styled.div`
  background-color: #3c3e52;
  &:hover {
    background-color: #3c3e5250;
  }
`;

const CardsContainer = styled.div`
  margin-top: 20px;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 1fr;
  @media screen and (max-width: 1400px) {
    grid-template-columns: repeat(2, 1fr);
  }
  @media screen and (max-width: 1080px) {
    grid-template-columns: repeat(1, 1fr);
  }
`;
