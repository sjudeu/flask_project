drop table if exists articles;
create table articles (
    id integer primary key autoincrement,
    title text not null,
    content text not null
);
