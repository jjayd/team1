package naver.board;

import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.firestore.CollectionReference;
import com.google.firebase.firestore.FirebaseFirestore;
import com.google.firebase.firestore.QueryDocumentSnapshot;
import com.google.firebase.firestore.QuerySnapshot;

import java.util.ArrayList;
import java.util.List;

public class RecruitActivity extends AppCompatActivity {
    private FirebaseFirestore mStore = FirebaseFirestore.getInstance();
    RecyclerView rcv;
    LinearLayoutManager llm;
    WrittingAdapter wadapter;
    private RecyclerView listView;          // 검색을 보여줄 리스트변수
    private EditText editSearch;        // 검색어를 입력할 Input 창
    private SearchAdapter adapter;      // 리스트뷰에 연결할 아답터
    private List<Board> arraylist;
    public List<Board> list;
    private TextView label;
    boolean change = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recruit);

        rcv = (RecyclerView) findViewById(R.id.article_part);

        editSearch = (EditText) findViewById(R.id.editSearch);
        listView = (RecyclerView) findViewById(R.id.article_part);
        label = (TextView) findViewById(R.id.label);

        //editSearch.setVisibility(View.VISIBLE);
        //label.setVisibility(View.VISIBLE);

        llm = new LinearLayoutManager(this);
        rcv.setHasFixedSize(true);
        rcv.setLayoutManager(llm);

        list = new ArrayList<>();
        CollectionReference board = mStore.collection("recruit");

        mStore.collection("recruit")
                .get()
                .addOnCompleteListener(new OnCompleteListener<QuerySnapshot>() {
                    @Override
                    public void onComplete(@NonNull Task<QuerySnapshot> task) {
                        if (task.isSuccessful()) {
                            for (QueryDocumentSnapshot document : task.getResult()) {
                                //Log.d(TAG, document.getId() + " => " + document.getData());
                                mStore.collection("recruit").document(document.getId()).delete();
                            }
                            for (int i = 0; i < 5; i++) {
                                Board bo = new Board("Los Angeles" + i, "CA3", "USA", "5000000L");
                                mStore.collection("recruit").add(bo);
                            }
                            for (QueryDocumentSnapshot document : task.getResult()) {
                                String id = (String) document.getData().get("id");
                                String title = (String) document.getData().get("title");
                                String contents = (String) document.getData().get("contents");
                                String name = (String) document.getData().get("name");
                                Board data = new Board(id, title, contents, name);
                                list.add(data);
                            }
                            //change = true;
                            wadapter = new WrittingAdapter(list);
                            rcv.setAdapter(wadapter);
                        } else {
                            //Log.d(TAG, "Error getting documents: ", task.getException());
                        }
                    }
                });
    }
}
