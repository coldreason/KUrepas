create table users (
  id INT(11) NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);



create table tasks (
  id INT(10) NOT NULL AUTO_INCREMENT,
  pos_s_x VARCHAR(20) NOT NULL,
  pos_s_y VARCHAR(20) NOT NULL,
  pos_e_x VARCHAR(20) NOT NULL,
  pos_e_y VARCHAR(20) NOT NULL,
  finish boolean NOT NULL
  PRIMARY KEY (id)
);

insert into tasks(pos_s_x, pos_s_y,pos_e_x,pos_e_y,finish ) values ('0.0', '0.0',"20.0","20.0",FALSE);

insert into users(name, email, ) values ('lee', 'test1');
insert into users(name, email, ) values ('jho', 'test1');


-- create table authority(
--     authority_name varchar(10)
-- );
-- insert into authority (authority_name) values ('ROLE_USER');
-- insert into authority (authority_name) values ('ROLE_ADMIN');

-- not used due to use data.sql

-- create table member(
--     member_id int not null auto_increment,
--     user_nm varchar(20) not null,
--     email varchar(20) not null,
--     password varchar(20) not null,
--     report_no int,
--     ban_st boolean
--     primary key(member_id,email)
-- );

-- create table quiz(
--     quiz_id int not null auto_increment,
--     quiz_nm varchar(20) not null,
--     content varchar(50),
--     writer_id int not null,
--     category varchar(20) not null
--     primary key(quiz_id),
--     foreign key (writer_id) references member (member_id)
-- );

-- create table comment(
--     comment_id int not null auto_increment,
--     content varchar(20) not null,
--     writer_id int not null,
--     comment_quiz_id int not null,
--     primary key(comment_id)
--     foreign key (writer_id) references member (member_id)
--     foreign key (comment_quiz_id) references quiz (quiz_id)
-- );

-- create table heart(
--     heart_id int not null auto_increment,
--     heart_user_id int not null,
--     heart_quiz_id int not null,
--     heart_dt datetime
--     primary key(heart_id)
--     foreign key (heart_user_id) references member (member_id)
--     foreign key (heart_quiz_id) references quiz (quiz_id)
-- );

-- create table scrap(
--     scrap_id int not null auto_increment,
--     scrap_nm varchar(20) not null,
--     scrap_user_id int not null,
--     primary key(scrap_id)
--     foreign key (scrap_user_id) references member (member_id)
-- );

-- insert into member(email, user_nm, password) values ('test1@gmail.com', 'test1', 'pw1');
-- insert into member(email, user_nm, password) values ('test2@gmail.com', 'test2', 'pw2');
-- insert into member(email, user_nm, password) values ('test3@gmail.com', 'test3', 'pw3');
-- insert into member(email, user_nm, password) values ('test4@gmail.com', 'test4', 'pw4');
-- insert into member(email, user_nm, password) values ('test5@gmail.com', 'test5', 'pw5');
-- insert into member(email, user_nm, password) values ('test6@gmail.com', 'test6', 'pw6');
-- insert into member(email, user_nm, password) values ('test7@gmail.com', 'test7', 'pw7');
-- insert into member(email, user_nm, password) values ('test8@gmail.com', 'test8', 'pw8');

-- insert into quiz(category, content, quiz_nm, writer_id) values ('초성퀴즈', '초성퀴즈입니다', 'quiz1', 1);
-- insert into quiz(category, content, quiz_nm, writer_id) values ('이구동성', '이구동성입니다', 'quiz2', 2);
-- insert into quiz(category, content, quiz_nm, writer_id) values ('영화명대사퀴즈', '영화명대사퀴즈입니다', 'quiz3', 3);

-- insert into comment(content, writer_id, comment_quiz_id) values('재밌어용', 1, 1);
-- insert into comment(content, writer_id, comment_quiz_id) values('하하하', 2, 1);
-- insert into comment(content, writer_id, comment_quiz_id) values('잘 보고 갑니다~~!', 3, 1);
-- insert into comment(content, writer_id, comment_quiz_id) values('호호호', 1, 2);
-- insert into comment(content, writer_id, comment_quiz_id) values('비밀 덧글입니다.', 2, 2);
-- insert into comment(content, writer_id, comment_quiz_id) values('호응이 좋네요', 3, 2);
-- insert into comment(content, writer_id, comment_quiz_id) values('히히히', 1, 3);
-- insert into comment(content, writer_id, comment_quiz_id) values('내용이 좀 부실해요', 2, 3);
-- insert into comment(content, writer_id, comment_quiz_id) values('오타 있어요!', 3, 3);

-- insert into heart(heart_user_id, heart_quiz_id) values(1, 1);
-- insert into heart(heart_user_id, heart_quiz_id) values(2, 1);
-- insert into heart(heart_user_id, heart_quiz_id) values(1, 2);
-- insert into heart(heart_user_id, heart_quiz_id) values(2, 2);
-- insert into heart(heart_user_id, heart_quiz_id) values(1, 3);
-- insert into heart(heart_user_id, heart_quiz_id) values(2, 3);

-- insert into scrap(scrap_nm, scrap_user_id) values('18기 레크리에이션 퀴즈 모음', 1);
-- insert into scrap(scrap_nm, scrap_user_id) values('개인 저장용', 1);