//
// Created by hxs on 2023/12/26.
//

#include <sqlite3.h>
#include <iostream>


int db_hander_function() {
    sqlite3 *db;
    char *errmsg;
    int rc;

    rc = sqlite3_open("db.db", &db);

    if (rc != SQLITE_OK) {
        std::cout << "无法打开数据库: " << sqlite3_errmsg(db) << std::endl;
        return rc;
    } else {
        std::cout << "成功打开数据库" << std::endl;
    }

//    // 执行 SQL 查询或操作
//    // SQL查询语句
//    const char *sql = "SELECT * FROM users";
//    // 执行查询语句
//    rc = sqlite3_exec(db, sql, callback, 0, &errmsg);
//    if (rc != SQLITE_OK) {
//        fprintf(stderr, "查询错误: %s\n", errmsg);
//        sqlite3_free(errmsg);
//        sqlite3_close(db);
//        return rc;
//    }

    sqlite3_close(db);
    std::cout << "成功关闭数据库" << std::endl;
    return 0;
}