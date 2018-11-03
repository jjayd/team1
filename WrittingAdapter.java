package com.naver.recyclerviewproject;

import android.app.Activity;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;

/**
 * Created by SM-PC on 2018-04-11.
 */

public class WrittingAdapter extends RecyclerView.Adapter<WrittingAdapter.MyViewholder> {



    private Activity activity;
    private ArrayList<itemForm> datalist;


    //getItemCount, onCreateViewHolder, MyViewHolder, onBindViewholder 순으로 들어오게 된다.
    // 뷰홀더에서 초기세팅해주고 바인드뷰홀더에서 셋텍스트해주는 값이 최종적으로 화면에 출력되는 값


    @Override
    public WrittingAdapter.MyViewholder onCreateViewHolder(ViewGroup parent, int viewType) { // 디자인 한 부분 적용
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_layout, parent, false); // 이미지 불러오기
        MyViewholder viewholder1 = new MyViewholder(view);


        return viewholder1;
    }

    @Override
    public void onBindViewHolder(WrittingAdapter.MyViewholder holder, int position) { // 디자인 부분에 내용 변경
        itemForm data = datalist.get(position);
        holder.personalId.setText(data.getId());
        holder.profile.setImageResource(data.getImageNumber());
        holder.writtingTxt.setText(data.getTxt());

    }

    @Override
    public int getItemCount() { // 아이템이 5개면 5번 돌게끔 해줌
        return datalist.size();
    }
    public class MyViewholder extends RecyclerView.ViewHolder
    {
        ImageView profile;
        TextView writtingTxt;
        TextView personalId;

        public MyViewholder(View itemview){
            super(itemview);

            profile = (ImageView) itemview.findViewById(R.id.image_jjang);
            writtingTxt = (TextView) itemview.findViewById(R.id.person_id1);
            personalId = (TextView) itemview.findViewById(R.id.person_id);
            itemview.setOnClickListener(new View.OnClickListener(){
                @Override
                public void onClick(View v) {
                    Toast.makeText(activity, "c",Toast.LENGTH_LONG).show();;
                }
            });

        }

    }
    public WrittingAdapter(Activity activity, ArrayList<itemForm> datalist){
        this.activity = activity;
        this.datalist = datalist;

    }
}