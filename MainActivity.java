package com.naver.recyclerviewproject;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    RecyclerView rcv;
    LinearLayoutManager llm;
    com.naver.recyclerviewproject.WrittingAdapter wadapter;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        rcv = (RecyclerView)findViewById(R.id.article_part);
        llm = new LinearLayoutManager(this);//종류는 총 3가지, ListView를 사용하기 위한 사용
        rcv.setHasFixedSize(true);//각 아이템이 보여지는 것을 일정하게
        rcv.setLayoutManager(llm);//앞서 선언한 리싸이클러뷰를 레이아웃메니저에 붙힌다

        ArrayList<com.naver.recyclerviewproject.itemForm> list = new ArrayList<>();//ItemFrom을 통해 받게되는 데이터를 어레이 리스트화 시킨다.

        list.add(new com.naver.recyclerviewproject.itemForm("seolwon",R.drawable.jjang1,"안녕하세요"));
        list.add(new com.naver.recyclerviewproject.itemForm("seol",R.drawable.jjang2,"안녕하세요1"));
        list.add(new com.naver.recyclerviewproject.itemForm("won",R.drawable.jjang3,"안녕하세요2"));
        list.add(new com.naver.recyclerviewproject.itemForm("seolwon2",R.drawable.jjang4,"안녕하세요3"));
        list.add(new com.naver.recyclerviewproject.itemForm("seolwon3",R.drawable.jjang1,"안녕"));
        list.add(new com.naver.recyclerviewproject.itemForm("seolwon4",R.drawable.jjang2,"안녕ss"));
        list.add(new com.naver.recyclerviewproject.itemForm("seolwon5",R.drawable.jjang3,"안녕서런아"));
        list.add(new com.naver.recyclerviewproject.itemForm("seolwon6",R.drawable.jjang4,"안녕하쇼"));// 앞서 선언한 list에다가 ItemFrom을 통해서 값을 주면 이렇게 준 형태가 각각의 리싸이클러뷰 아이템의 형태에서 나타나게 된다.


        wadapter = new com.naver.recyclerviewproject.WrittingAdapter(this, list);//앞서 만든 리스트를 어뎁터에 적용시켜 객체를 만든다.
        rcv.setAdapter(wadapter);// 그리고 만든 겍체를 리싸이클러뷰에 적용시킨다.

    }
}
