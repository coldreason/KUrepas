using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;

public class Taxi3 : MonoBehaviour
{
    public Animator anim;
    private float y = 0f;
    private string id = "taxi3";    // taxi1 �̶�� ���̵� ����� ���°Ÿ� �ϴ� �ϵ��ڵ�

    // Start is called before the first frame update
    void Start()
    {
        anim = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        if (id == "taxi3")
        {
            Vector3 target = new Vector3(60, 0, 60);

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
        Vector3 pos = transform.position;

        // �ٶ󺸴� ���� ����
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
        // ������ �������� ����
        transform.rotation = Quaternion.LookRotation(dir);
    }

    void Task_Complete(Vector3 destination)
    {
        y += 100f * Time.deltaTime;
        transform.rotation = Quaternion.Euler(0, y, 0);
        transform.position = Vector3.Slerp(transform.position, destination, 0.1f);
        
        // db�� task complete ���� ������
        
    }
    // ���߿� ����� ���� �����ؾ� �ϴ� ��. ���� ��ġ �ޱ�, id �� �ν��ϱ�
    void get_destination()
    {
        List<int> destination = new List<int>();
        destination.Add(10);
        destination.Add(0);
        destination.Add(0);
        Debug.Log(destination);
    }
}
