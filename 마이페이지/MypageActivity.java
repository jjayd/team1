package naver.board;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MypageActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_mypage);
        Button btn1 = (Button) findViewById(R.id.button1);
        Button btn2 = (Button) findViewById(R.id.button2);
        TextView label = (TextView) findViewById(R.id.textView);

        label.setText("ID : king182@skku.edu\n\n이름 : 김락원\n");

        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MypageActivity.this, fieldActivity.class));
                finish();
            } // end onClick
        }); // end setOnClickListener

        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MypageActivity.this, fieldActivity.class));
                finish();
            } // end onClick
        }); // end setOnClickListener

    }
}
