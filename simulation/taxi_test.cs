using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Newtonsoft.Json.Linq;
using System.IO;
using UnityEngine.Networking;
using Newtonsoft.Json;

public class PositionData
{
    public float cur_pos_x;
    public float cur_pos_y;
    public float complete;
}

public class taxi_test : MonoBehaviour
{
    public Vector3 pos;  // ���� ��ġ ����
    public int complete = 0; // task ���࿩��

    public string data;  // 
    public string taskID;// json���� taskID �ޱ�
    public string unitID;// json���� unitID �ޱ�
    public string pos_s_x, pos_s_y, pos_e_x, pos_e_y; // json���� ���� position ���� �ޱ�

    private float pos_sx, pos_sy, pos_ex, pos_ey;
    private string old_taskID;

    private int flag = 0; // flag�� �۾� ��Ȳ.
    private float y = 0f; // ȸ�� factor.

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        // json task list �б� //
        /////////////////// ���� //////////////////////////
        pos_sx = float.Parse(pos_s_x);
        pos_sy = float.Parse(pos_s_y);
        pos_ex = float.Parse(pos_e_x);
        pos_ey = float.Parse(pos_e_y);

        /////////////////// json�� current position �� /////////////////////
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
        
        ////////////////////// �����̱� /////////////////////////////////////
        if (taskID == old_taskID)
        {
            if (flag == 0 && pos == new Vector3(pos_sx, 0, pos_sy))
            {
                flag = 1;
            }
            if (flag == 0) // ù��° �������� ���� ������
            {
                Move(new Vector3(pos_sx, 0, pos_sy));
            }
            else if (flag == 1 && pos == new Vector3(pos_ex, 0, pos_ey))
            {
                flag = 2;
                // complete ���� ������ //
            }
            else if (flag == 1)
            {
                Move(new Vector3(pos_ex, 0, pos_ey));
            }
            if (flag == 2 && pos == new Vector3(pos_ex, 0, pos_ey)) // �����ϰ� ���� ���ۺ��� ���� �ֱ�
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
        
        // �ٶ󺸴� ���� ����
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
        // ������ �������� ����
        transform.rotation = Quaternion.LookRotation(dir);
    }

    void Task_Complete(Vector3 destination)
    {
        
    }
}
