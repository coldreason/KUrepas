using System.Collections;
using UnityEngine;
using UnityEngine.Networking;
using System.Collections.Generic;
using System.IO;
using Newtonsoft.Json;



public class JsonDataReceiver : MonoBehaviour
{
    public Vector3 pos;  // 현재 위치 저장
    public int complete = 0; // task 수행여부

    public string data;  // 
    public int taskID;// json에서 taskID 받기
    public string unitID;// json에서 unitID 받기
    public float pos_s_x, pos_s_y, pos_e_x, pos_e_y; // json에서 목적 position 정보 받기

    private float pos_sx, pos_sy, pos_ex, pos_ey;
    private int old_taskID;

    private int flag = 0; // flag로 작업 상황.
    private float y = 0f; // 회전 factor.

    private string url = "http://54.180.109.46:5000/designate/1"; // JSON 데이터를 받을 URL

    private void Start()
    {
        StartCoroutine(GetJsonData());
    }

    private IEnumerator GetJsonData()
    {
        using (UnityWebRequest www = UnityWebRequest.Get(url))
        {
            yield return www.SendWebRequest();

            if (www.result != UnityWebRequest.Result.Success)
            {
                Debug.LogError("Failed to retrieve JSON data: " + www.error);
                yield break;
            }

            string json = www.downloadHandler.text;
            ProcessJsonData(json);
        }
    }


    private void ProcessJsonData(string json)
    {
        // JSON 데이터를 원하는 형식으로 파싱하여 사용
        JsonData jsonData = JsonUtility.FromJson<JsonData>(json);

        Debug.Log("Received JSON data:");
        Debug.Log("ID: " + jsonData.id);
        Debug.Log("Pos_e_x: " + jsonData.pos_e_x);
        Debug.Log("Pos_e_y: " + jsonData.pos_e_y);
        Debug.Log("Pos_s_x: " + jsonData.pos_s_x);
        Debug.Log("Pos_s_y: " + jsonData.pos_s_y);
        taskID = jsonData.id;
        pos_s_x = jsonData.pos_s_x * 20;
        pos_s_y = jsonData.pos_s_y * 20;
        pos_e_x = jsonData.pos_e_x * 20;
        pos_e_y = jsonData.pos_e_y * 20;

    }

    void Update()
    {
        // json task list 읽기 //
        /////////////////// 예시 //////////////////////////
        pos_sx = pos_s_x;
        pos_sy = pos_s_y;
        pos_ex = pos_e_x;
        pos_ey = pos_e_y;

        /////////////////// json에 current position 값 /////////////////////
        pos = transform.position;
        PositionData positionData = new PositionData();
        positionData.cur_pos_x = pos.x;
        positionData.cur_pos_y = pos.z;
        positionData.complete = complete;

        string json = JsonUtility.ToJson(positionData);

        string fileName = "positionData1.json";
        string directoryPath = @"C:\Users\Goseumdochy\Documents";
        string filePath = Path.Combine(directoryPath, fileName);
        File.WriteAllText(filePath, json);

        
        /////////////////////////////////////////////////////////////////////

        ////////////////////// 움직이기 /////////////////////////////////////
        if (taskID == old_taskID)
        {
            if (flag == 0 && pos == new Vector3(pos_sx, 0, pos_sy))
            {
                flag = 1;
            }
            if (flag == 0) // 첫번째 시작지점 도달 전까지
            {
                Move(new Vector3(pos_sx, 0, pos_sy));
            }
            else if (flag == 1 && pos == new Vector3(pos_ex, 0, pos_ey))
            {
                flag = 2;
                // complete 정보 보내기 //
            }
            else if (flag == 1)
            {
                Move(new Vector3(pos_ex, 0, pos_ey));
            }
            if (flag == 2 && pos == new Vector3(pos_ex, 0, pos_ey)) // 도착하고 나서 빙글빙글 돌고 있기
            {
                // TaskComplete() //
                y += 100f * Time.deltaTime;
                transform.rotation = Quaternion.Euler(0, y, 0);
            }
        }

        if (taskID != old_taskID)
        {
            flag = 0;
            old_taskID = taskID;
        }


    }
    void Move(Vector3 destination)
    {

        // 바라보는 방향 벡터
        Vector3 dir = new Vector3(0, 0, 0);

        float diff_x = destination.x - pos.x;
        float diff_z = destination.z - pos.z;

        Vector3 pseudo_destination_x = new Vector3(destination.x, 0, pos.z);
        Vector3 pseudo_destination_z = new Vector3(pos.x, 0, destination.z);
        if (diff_x != 0 && pos.z % 20 == 0)
        {
            transform.position = Vector3.MoveTowards(pos, pseudo_destination_x, 60f * Time.deltaTime);
            if (diff_x > 0)
            {
                dir.x = 1;
                dir.y = 0;
                dir.z = 0;
            }
            else
            {
                dir.x = -1;
                dir.y = 0;
                dir.z = 0;
            }
        }
        else if (diff_z != 0)
        {
            transform.position = Vector3.MoveTowards(pos, pseudo_destination_z, 60f * Time.deltaTime);
            if (diff_z > 0)
            {
                dir.x = 0;
                dir.y = 0;
                dir.z = 1;
            }
            else
            {
                dir.x = 0;
                dir.y = 0;
                dir.z = -1;
            }
        }
        // 나가는 방향으로 보기
        transform.rotation = Quaternion.LookRotation(dir);
    }

    void Task_Complete(Vector3 destination)
    {

    }

}

[System.Serializable]
public class JsonData
{
    public int id;
    public float pos_e_x;
    public float pos_e_y;
    public float pos_s_x;
    public float pos_s_y;
}