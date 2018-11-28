package naver.board;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TextView;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

public class fieldActivity extends AppCompatActivity {
        public ArrayList<String> list = new ArrayList<>();
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_field);

            final CheckBox cb1 = (CheckBox) findViewById(R.id.checkBox1);
            final CheckBox cb2 = (CheckBox) findViewById(R.id.checkBox2);
            final CheckBox cb3 = (CheckBox) findViewById(R.id.checkBox3);
            final CheckBox cb4 = (CheckBox) findViewById(R.id.checkBox4);
            final CheckBox cb5 = (CheckBox) findViewById(R.id.checkBox5);
            final CheckBox cb6 = (CheckBox) findViewById(R.id.checkBox6);
            final CheckBox cb7 = (CheckBox) findViewById(R.id.checkBox7);
            final CheckBox cb8 = (CheckBox) findViewById(R.id.checkBox8);
            final CheckBox cb9 = (CheckBox) findViewById(R.id.checkBox9);
            final CheckBox cb10 = (CheckBox) findViewById(R.id.checkBox10);
            final CheckBox cb11 = (CheckBox) findViewById(R.id.checkBox11);
            final CheckBox cb12 = (CheckBox) findViewById(R.id.checkBox12);
            final CheckBox cb13 = (CheckBox) findViewById(R.id.checkBox13);
            final CheckBox cb14 = (CheckBox) findViewById(R.id.checkBox14);
            final CheckBox cb15 = (CheckBox) findViewById(R.id.checkBox15);
            final CheckBox cb16 = (CheckBox) findViewById(R.id.checkBox16);
            final CheckBox cb17 = (CheckBox) findViewById(R.id.checkBox17);
            final CheckBox cb18 = (CheckBox) findViewById(R.id.checkBox18);

            String arr[] = {"기계",
                    "전자/전기",
                    "화학",
                    "신소재",
                    "IT",
                    "통계",
                    "의예",
                    "건축/토목",
                    "항공",
                    "경영",
                    "경제/회계",
                    "법학/로스쿨",
                    "사회/국제",
                    "언론/신방",
                    "정치외교",
                    "언어",
                    "세무/관세",
                    "역사"};
            Button b = (Button) findViewById(R.id.button1);

            b.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    String result = "";
                    if (cb1.isChecked() == true) list.add(cb1.getText().toString());
                    if (cb2.isChecked() == true) list.add(cb2.getText().toString());
                    if (cb3.isChecked() == true) list.add(cb3.getText().toString());
                    if (cb4.isChecked() == true) list.add(cb4.getText().toString());
                    if (cb5.isChecked() == true) list.add(cb5.getText().toString());
                    if (cb6.isChecked() == true) list.add(cb6.getText().toString());
                    if (cb7.isChecked() == true) list.add(cb7.getText().toString());
                    if (cb8.isChecked() == true) list.add(cb8.getText().toString());
                    if (cb9.isChecked() == true) list.add(cb9.getText().toString());
                    if (cb10.isChecked() == true) list.add(cb10.getText().toString());
                    if (cb11.isChecked() == true) list.add(cb11.getText().toString());
                    if (cb12.isChecked() == true) list.add(cb12.getText().toString());
                    if (cb13.isChecked() == true) list.add(cb13.getText().toString());
                    if (cb14.isChecked() == true) list.add(cb14.getText().toString());
                    if (cb15.isChecked() == true) list.add(cb15.getText().toString());
                    if (cb16.isChecked() == true) list.add(cb16.getText().toString());
                    if (cb17.isChecked() == true) list.add(cb17.getText().toString());
                    if (cb18.isChecked() == true) list.add(cb18.getText().toString());

                } // end onClick
            }); // end setOnClickListener
        }
}
