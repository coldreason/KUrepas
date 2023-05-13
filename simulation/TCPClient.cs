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
        string serverIP = "54.180.109.46"; // ���� IP �ּ� �Է�
        int serverPort = 5000; // ���� ��Ʈ ��ȣ �Է�

        try
        {
            client.Connect(serverIP, serverPort);
            stream = client.GetStream();

            // ���� ����
            Debug.Log("������ ����Ǿ����ϴ�.");

            // ������ ������ ������ ����
            string message = "Hello, server!";
            byte[] sendBuffer = Encoding.UTF8.GetBytes(message);
            stream.Write(sendBuffer, 0, sendBuffer.Length);

            // �������� ������ �ޱ� ����
            //int bytesRead = stream.Read(receiveBuffer, 0, receiveBuffer.Length);
            //string receivedMessage = Encoding.UTF8.GetString(receiveBuffer, 0, bytesRead);
            //Debug.Log("�������� ���� ������: " + receivedMessage);
        }
        catch (Exception e)
        {
            Debug.LogError("���� ��� �� ���� �߻�: " + e.Message);
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