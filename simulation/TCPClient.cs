using System;
using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class TCPClient : MonoBehaviour
{
    TcpClient client;
    NetworkStream stream;
    byte[] receiveBuffer = new byte[1024];
  
    void Start()
    {
        client = new TcpClient();
        string serverIP = "54.180.109.46"; // 서버 IP 주소 입력
        int serverPort = 5000; // 서버 포트 번호 입력

        try
        {
            client.Connect(serverIP, serverPort);
            stream = client.GetStream();

            // 연결 성공
            Debug.Log("서버에 연결되었습니다.");

            // 서버로 데이터 보내기 예시
            string message = "Hello, server!";
            byte[] sendBuffer = Encoding.UTF8.GetBytes(message);
            stream.Write(sendBuffer, 0, sendBuffer.Length);

            // 서버에서 데이터 받기 예시
            //int bytesRead = stream.Read(receiveBuffer, 0, receiveBuffer.Length);
            //string receivedMessage = Encoding.UTF8.GetString(receiveBuffer, 0, bytesRead);
            //Debug.Log("서버에서 받은 데이터: " + receivedMessage);
        }
        catch (Exception e)
        {
            Debug.LogError("소켓 통신 중 오류 발생: " + e.Message);
        }
    }

    void OnDestroy()
    {
        if (stream != null)
            stream.Close();

        if (client != null)
            client.Close();
    }
}