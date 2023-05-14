using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class Taxi1 : MonoBehaviour
{
    public Vector3 pos;
    
    public Animator anim;
    private float y = 0f;
    private string id = "taxi1";    // taxi1 이라는 아이디 명령이 들어온거를 일단 하드코딩

    // Start is called before the first frame update
    void Start()
    {
        anim = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        if (id == "taxi1")
        {
            Vector3 target = new Vector3(0, 0, 20);

            Move(target);
            get_destination();
            if (transform.position == target)
            {
                Task_Complete(target);
            }
        }
        
    }

    void Move(Vector3 destination)
    {
        pos = transform.position;

        // 바라보는 방향 벡터
        Vector3 dir = new Vector3(0, 0, 0);
        
        float diff_x = destination.x - pos.x;
        float diff_z = destination.z - pos.z;

        Vector3 pseudo_destination_x = new Vector3(destination.x, 0, pos.z);
        Vector3 pseudo_destination_z = new Vector3(pos.x, 0, destination.z);
        if (diff_x != 0 && pos.z % 20 == 0)
        {
            transform.position = Vector3.MoveTowards(pos, pseudo_destination_x, 60f * Time.deltaTime);
            if(diff_x > 0)
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
        y += 100f * Time.deltaTime;
        transform.rotation = Quaternion.Euler(0, y, 0);
        transform.position = Vector3.Slerp(transform.position, destination, 0.1f);
        
        // db에 task complete 여부 보내기
        
    }
    // 나중에 통신을 통해 연결해야 하는 것. 목적 위치 받기, id 도 인식하기
    void get_destination()
    {
        List<int> destination = new List<int>();
        destination.Add(10);
        destination.Add(0);
        destination.Add(0);
        Debug.Log(destination);
    }
}
