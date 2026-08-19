# Cẩm Nang Ôn Tập Java Core & JDBC (Chuẩn Bị Cho Cuộc Audit)

Bộ tài liệu này tổng hợp toàn bộ câu trả lời, mã nguồn minh họa và các **câu hỏi xoáy (Trap)** từ người Audit dành cho toàn bộ 6 ngày trong chương trình học của bạn.

---

### 🗂️ Tổng Quan Lộ Trình Ôn Tập (6 Ngày)

| Nhóm 1: Cơ bản & Hướng đối tượng (Day 0 - 2) | Nhóm 2: Nâng cao & Kết nối CSDL (Day 3 - 5) |
| :--- | :--- |
| [📅 Day 0: Environment Setup (Môi trường)](#-day-0-environment-setup-cai-dat-moi-truong) | [📅 Day 3: Collections, String, Exception & I/O](#-day-3-collections-string-exception--file-io) |
| [📅 Day 1: Java Fundamentals (Cơ bản)](#-day-1-java-fundamentals--basic-programming-nen-tang-java) | [📅 Day 4: Introduction to Thread (Đa luồng)](#-day-4-introduction-to-thread-in-java-da-luong-co-ban) |
| [📅 Day 2: Object-Oriented Programming (OOP)](#-day-2-object-oriented-programming-huong-doi-tuong---oop) | [📅 Day 5: Database Connectivity (JDBC)](#-day-5-database-connectivity-jdbc) |

---

## 📅 Day 0: Environment Setup (Cài Đặt Môi Trường)

### 1. Version JDK & Cách Kiểm Tra
*   **Trả lời:** Cần biết chính xác phiên bản JDK đang dùng (ví dụ: Java 17 hoặc Java 21).
*   **Cách kiểm tra:** Chạy lệnh trên Terminal/Cmd:
    ```bash
    java -version   # Kiểm tra JRE (Runtime) chạy ứng dụng
    javac -version  # Kiểm tra JDK (Compiler) biên dịch mã nguồn
    ```
*   **Trap:** *"Nếu máy bạn cài cả Java 11 và Java 17, làm sao để hệ điều hành biết dùng bản nào?"*
    *   **Trả lời:** Dựa vào biến môi trường `JAVA_HOME` trỏ tới đường dẫn của JDK mong muốn, và biến `PATH` phải chứa `%JAVA_HOME%\bin` (Windows) hoặc `$JAVA_HOME/bin` (macOS/Linux) ở đầu danh sách.

### 2. Tính năng của IDE (IntelliJ IDEA / Eclipse)
*   **Trả lời:** IDE giúp tăng tốc độ phát triển nhờ: Auto-completion (gợi ý code), Real-time compilation (báo lỗi cú pháp ngay lập tức), Debugger (chạy từng bước sửa lỗi), Refactoring tools (đổi tên class/method an toàn ở mọi nơi), và tích hợp Build tools (Maven/Gradle).

### 3. Quản lý Database (DBeaver / MySQL Workbench)
*   **Trả lời:** Các tool này là Client để kết nối và quản trị hệ quản trị cơ sở dữ liệu (DBMS - ví dụ MySQL, PostgreSQL).
*   **Cách dùng:** Tạo Connection bằng cách nhập: Host (thường là `localhost` hoặc IP), Port (3306 cho MySQL), Username, Password, Database Name. Sau đó dùng để chạy SQL Script, xem cấu trúc bảng (ER Diagram), import/export dữ liệu.

### 4. Quản lý Dependency (Thư viện ngoài)
*   **Trả lời:** IDE quản lý thư viện thông qua các công cụ tự động như **Maven** (`pom.xml`) hoặc **Gradle** (`build.gradle`).
*   *Cơ chế:* Khi khai báo thư viện trong file cấu hình, Maven/Gradle sẽ tự động tải thư viện đó và toàn bộ các thư viện liên quan của nó (Transitive Dependencies) từ repository trung tâm (Maven Central) về lưu trữ cục bộ (Local Repository - thư mục `.m2` hoặc `.gradle`).

---

## 📅 Day 1: Java Fundamentals & Basic Programming (Nền Tảng Java)

### 1. Phân biệt JDK vs JRE vs JVM

| Thành phần | Đặc điểm & Vai trò |
| :--- | :--- |
| **JVM** (Java Virtual Machine) | **Máy ảo thực thi Bytecode** (`.class`). Giúp Java có tính độc lập nền tảng (Write Once, Run Anywhere). |
| **JRE** (Java Runtime Environment) | **Môi trường chạy ứng dụng**. Chứa JVM và các thư viện cốt lõi (`rt.jar`), đủ để chạy chương trình Java. |
| **JDK** (Java Development Kit) | **Bộ công cụ phát triển**. Chứa JRE và các công cụ lập trình (compiler `javac`, debugger, v.v.) dành cho nhà phát triển. |

*   **Công thức nhớ nhanh:** `JDK = JRE + Development Tools`; `JRE = JVM + Core Libraries`.

### 2. Quy trình biên dịch và chạy Hello World
*   **Quy trình:**
    1. Viết mã nguồn trong file `.java` (ví dụ `Hello.java`).
    2. Dùng `javac Hello.java` để biên dịch thành Bytecode trong file `Hello.class`.
    3. Dùng lệnh `java Hello` để JVM nạp class đó vào bộ nhớ và chạy hàm `main`.

### 3. Kiểu dữ liệu nguyên thủy (Primitive Types) và Toán tử
*   **8 kiểu dữ liệu nguyên thủy:** `byte` (1 byte), `short` (2), `int` (4), `long` (8), `float` (4), `double` (8), `char` (2), `boolean` (1 bit).
*   **Trap:** *"Kiểu dữ liệu nguyên thủy lưu trữ ở đâu trong bộ nhớ?"*
    *   **Trả lời:** Nếu là biến cục bộ trong phương thức, chúng lưu ở **Stack**. Nếu là thuộc tính của một đối tượng, chúng lưu cùng đối tượng đó ở **Heap**.

### 4. Cấu trúc điều khiển (Control Flow)
*   `if-else`, `switch-case` (từ Java 7 hỗ trợ `String`, Java 12+ hỗ trợ Switch Expression).
*   Vòng lặp: `for`, `while`, `do-while` (luôn thực thi khối mã ít nhất 1 lần trước khi kiểm tra điều kiện).

### 5. Khai báo và duyệt Array
```java
int[] numbers = new int[5]; // Khai báo kích thước cố định
int[] primes = {2, 3, 5, 7}; // Khởi tạo nhanh

// Duyệt mảng bằng For-each (Read-only, không sửa được phần tử)
for (int num : primes) {
    System.out.println(num);
}
```

### 6. Pass-by-value (Truyền tham trị) trong Java
*   **Khẳng định cốt lõi:** **Java chỉ truyền tham trị (Strictly Pass-by-Value).**
*   *Với kiểu nguyên thủy:* Giá trị được sao chép sang một vùng nhớ mới. Phương thức thay đổi giá trị này không ảnh hưởng đến biến gốc.
*   *Với đối tượng (Object):* Java truyền bản sao của **Tham chiếu** (Địa chỉ ô nhớ).
    *   Bạn **có thể** thay đổi trạng thái của đối tượng gốc thông qua tham chiếu đó (`person.setName("New Name")`).
    *   Bạn **không thể** đổi địa chỉ ô nhớ mà biến gốc đang trỏ tới.
    ```java
    void update(Person p) {
        p.setName("Vinh"); // Làm thay đổi đối tượng gốc
        p = new Person("An"); // p lúc này trỏ sang ô nhớ mới, không ảnh hưởng biến gốc ngoài hàm
    }
    ```

---

## 📅 Day 2: Object-Oriented Programming (Hướng Đối Tượng - OOP)

### 1. Class và Object
*   **Class:** Là khuôn mẫu/bản thiết kế định nghĩa các thuộc tính (State) và phương thức (Behavior).
*   **Object:** Là một thực thể (Instance) cụ thể được tạo ra từ khuôn mẫu Class đó nằm trên vùng nhớ Heap.

### 2. Encapsulation (Tính đóng gói)
*   **Định nghĩa:** Che giấu trạng thái bên trong của đối tượng và chỉ cho phép truy cập thông qua các phương thức công khai.
*   **Cách làm:** Khai báo thuộc tính là `private`, viết các hàm `getX()` và `setX()` public. Tại hàm setter, ta có thể viết thêm logic để kiểm tra tính hợp lệ của dữ liệu đầu vào.

### 3. Constructor (Hàm khởi tạo)
*   **Định nghĩa:** Phương thức đặc biệt trùng tên với Class, không có kiểu trả về (kể cả `void`). Gọi bằng từ khóa `new` dùng để khởi tạo trạng thái ban đầu cho đối tượng.
*   **Trap:** *"Nếu bạn không viết Constructor nào thì sao?"*
    *   **Trả lời:** Trình biên dịch tự động tạo một Default Constructor không tham số. Nhưng nếu bạn đã viết ít nhất 1 Constructor có tham số, Default Constructor sẽ biến mất (muốn dùng phải tự viết lại).

### 4. Constructor Overloading
*   Là việc khai báo nhiều Constructor trong một Class nhưng khác nhau về số lượng hoặc kiểu dữ liệu của tham số đầu vào.

### 5. Từ khóa `this`, `static`, `final`

| Từ khóa | Ý nghĩa & Cách dùng |
| :--- | :--- |
| **`this`** | Tham chiếu đến chính đối tượng hiện tại. Dùng để phân biệt thuộc tính Class với biến tham số trùng tên. |
| **`static`** | Thuộc về **Class** (dùng chung cho mọi đối tượng). Được nạp vào bộ nhớ duy nhất một lần khi JVM load Class. Biến static dùng chung cho mọi instance; phương thức static chỉ gọi được phương thức/biến static khác. |
| **`final`** | • **Với biến**: Biến thành hằng số (chỉ gán giá trị được 1 lần).<br>• **Với phương thức**: Ngăn chặn lớp con ghi đè (Override).<br>• **Với lớp**: Ngăn chặn lớp khác kế thừa (ví dụ: `String` class). |

### 6. Inheritance (Tính kế thừa)
*   Dùng từ khóa `extends` giúp lớp con thừa hưởng lại các thuộc tính và phương thức phi-private của lớp cha, hỗ trợ tái sử dụng mã nguồn. Java chỉ hỗ trợ **đơn kế thừa lớp** để tránh lỗi kim cương (Diamond Problem).

### 7. Polymorphism (Tính đa hình) & Overriding
*   **Đa hình:** Một đối tượng có thể đóng nhiều vai trò khác nhau. Lớp cha trỏ tới lớp con: `Animal myDog = new Dog();`.
*   **Overriding (Ghi đè - Đa hình lúc Runtime):** Lớp con định nghĩa lại phương thức của lớp cha có cùng tên, cùng tham số truyền vào và cùng kiểu trả về (hoặc kiểu đồng biến).

### 8. Từ khóa `super`
*   `super(...)`: Gọi constructor của lớp cha (phải là dòng lệnh đầu tiên trong constructor của lớp con).
*   `super.methodName()`: Gọi phương thức gốc của lớp cha khi phương thức đó đã bị ghi đè ở lớp con.

### 9. Phân biệt Abstract Class vs Interface

| Lớp trừu tượng (Abstract Class) | Giao diện (Interface) |
| :--- | :--- |
| **Bản chất & Kế thừa**:<br>• Là một lớp cha (is-a).<br>• Đơn kế thừa (extends 1 class). | **Bản chất & Kế thừa**:<br>• Là một tập hợp các hành vi (can-do).<br>• Đa kế thừa (implements nhiều interfaces). |
| **Thuộc tính & Constructor**:<br>• Chứa instance variable thông thường.<br>• Có Constructor (để lớp con gọi qua `super`). | **Thuộc tính & Constructor**:<br>• Chỉ chứa hằng số (`public static final`).<br>• Không có Constructor. |
| **Phương thức**:<br>• Có cả phương thức trừu tượng và thông thường. | **Phương thức**:<br>• Từ Java 8 hỗ trợ `default`, `static`. Java 9 hỗ trợ `private`. |

---

## 📅 Day 3: Collections, String, Exception & File I/O

### 1. String vs StringBuilder vs StringBuffer

| Đối tượng | Đặc tính & Môi trường sử dụng |
| :--- | :--- |
| **`String`** | **Bất biến (Immutable)**. Mỗi lần sửa đổi sẽ tạo ra đối tượng mới trong String Pool. Không tối ưu bộ nhớ nếu thay đổi chuỗi liên tục. |
| **`StringBuilder`** | **Khả biến (Mutable) - Đơn luồng (Non-thread-safe)**. Tốc độ xử lý rất nhanh, khuyên dùng khi chỉ thao tác trên một luồng duy nhất. |
| **`StringBuffer`** | **Khả biến (Mutable) - Đa luồng (Thread-safe)**. Các phương thức được đồng bộ hóa (`synchronized`), đảm bảo an toàn khi nhiều luồng truy cập nhưng chạy chậm hơn `StringBuilder`. |

### 2. Java Collections Framework
*   **Sơ đồ phân cấp:**
    *   `Collection` (Interface gốc)
        *   `List` (ArrayList, LinkedList): Cho phép trùng lặp, giữ đúng thứ tự thêm vào.
        *   `Set` (HashSet, TreeSet): Không cho phép trùng lặp phần tử.
        *   `Queue` (PriorityQueue, ArrayDeque): Vào trước ra trước (FIFO).
    *   `Map` (HashMap, TreeMap): Lưu dữ liệu dạng Key-Value (không kế thừa `Collection`).

### 3. ArrayList vs LinkedList
*   `ArrayList`: Sử dụng mảng động dưới nền. Truy cập phần tử ngẫu nhiên rất nhanh ($O(1)$) qua chỉ mục, nhưng thêm/xóa ở giữa mảng chậm ($O(n)$) do phải dịch chuyển các phần tử.
*   `LinkedList`: Sử dụng danh sách liên kết đôi (Doubly Linked List). Thêm/xóa phần tử cực nhanh ($O(1)$) chỉ cần đổi con trỏ, nhưng truy cập ngẫu nhiên chậm ($O(n)$) vì phải duyệt tuần tự.

### 4. Cách hoạt động của HashMap
*   Sử dụng cơ chế Bảng băm (Hashing). Khi gọi `put(key, value)` hoặc `get(key)`:
    1. JVM gọi hàm `key.hashCode()` để tính toán vị trí chỉ mục (bucket).
    2. Nếu xảy ra đụng độ băm (Hash Collision - nhiều key khác nhau có cùng hashCode):
        * Các phần tử đụng độ sẽ được liên kết với nhau dưới dạng **Linked List**.
        * Từ Java 8, nếu số phần tử trong 1 bucket vượt quá 8, Linked List sẽ tự chuyển đổi thành **Red-Black Tree** (Cây đỏ đen) để tăng tốc tìm kiếm từ $O(n)$ lên $O(\log n)$.
    3. Khi so sánh key để lấy dữ liệu, Java dùng hàm `equals()`.

### 5. Sắp xếp: Comparable vs Comparator
*   **`Comparable`:** Định nghĩa thứ tự sắp xếp mặc định (Natural Ordering) của lớp. Class đó phải `implements Comparable<T>` và override phương thức `compareTo(T o)`.
*   **`Comparator`:** Định nghĩa các thứ tự sắp xếp tùy chỉnh bên ngoài lớp. Class viết riêng hoặc dùng Lambda để override phương thức `compare(T o1, T o2)`.
    ```java
    // Sắp xếp danh sách sinh viên theo tên bằng Comparator Lambda
    list.sort((s1, s2) -> s1.getName().compareTo(s2.getName()));
    ```

### 6. Exception Handling & try-catch-finally
*   `try`: Chứa đoạn code có khả năng phát sinh lỗi.
*   `catch`: Bắt và xử lý lỗi cụ thể.
*   `finally`: **Luôn luôn chạy** dù có xảy ra lỗi hay không (kể cả khi trong block try/catch có lệnh `return`). Thường dùng để đóng các kết nối tài nguyên (File, Database).
*   **Trap:** *"Trường hợp nào block `finally` không được thực thi?"*
    *   **Trả lời:** Khi gọi lệnh tắt máy ảo đột ngột `System.exit(0)` hoặc máy tính bị mất nguồn đột ngột.

### 7. Checked vs Unchecked Exception
*   **Checked Exception (Bắt buộc xử lý lúc compile):** Lớp con của `Exception` (ngoại trừ `RuntimeException`). Trình biên dịch bắt buộc bạn phải dùng `try-catch` hoặc khai báo `throws` ở chữ ký hàm (ví dụ: `IOException`, `SQLException`).
*   **Unchecked Exception (Lỗi lúc runtime):** Lớp con của `RuntimeException`. Xảy ra do lỗi logic lập trình, trình biên dịch không bắt ép xử lý trước (ví dụ: `NullPointerException`, `ArithmeticException` - chia cho 0).

### 8. File I/O: BufferedReader vs PrintWriter
*   `BufferedReader`: Đọc ký tự từ file hiệu quả nhờ cơ chế bộ đệm (buffering), đọc từng dòng rất tiện bằng hàm `readLine()`.
*   `PrintWriter`: Hỗ trợ ghi dữ liệu dạng văn bản định dạng vào file (hỗ trợ `print()`, `println()`, `printf()`).

### 9. Serialization (Tuần tự hóa)
*   **Khái niệm:** Quá trình chuyển đổi trạng thái của một đối tượng thành một chuỗi byte để lưu xuống file hoặc truyền qua mạng.
*   **Cách làm:** Class cần implements interface đánh dấu `Serializable` (Interface này không có phương thức nào).
*   **Từ khóa `transient`:** Dùng để đánh dấu các thuộc tính bảo mật (như mật khẩu) mà bạn không muốn tuần tự hóa lưu xuống file.

---

## 📅 Day 4: Introduction to Thread in Java (Đa Luồng Cơ Bản)

### 1. Hai cách tạo luồng (Thread)
*   **Cách 1:** Kế thừa lớp `Thread` -> Dễ viết nhưng bị giới hạn do Java không hỗ trợ đa kế thừa.
*   **Cách 2:** Implement interface `Runnable` -> Tách biệt phần xử lý logic khỏi cơ chế luồng, class vẫn kế thừa được lớp khác (Khuyên dùng).

### 2. Vòng đời của Thread (Thread States)
*   `NEW`: Vừa tạo bằng `new Thread()`, chưa chạy `start()`.
*   `RUNNABLE`: Sẵn sàng chạy trong CPU, đang đợi scheduler cấp time-slice.
*   `BLOCKED`: Đang đợi lấy Monitor Lock (bị chặn ngoài khối `synchronized`).
*   `WAITING`: Đợi vô hạn cho đến khi luồng khác đánh thức (qua `wait()`, `join()`).
*   `TIMED_WAITING`: Đợi có thời hạn (qua `Thread.sleep(ms)`).
*   `TERMINATED`: Hàm `run()` hoàn thành, luồng kết thúc.

### 3. start() vs run()
*   `t.start()`: Tạo ra một luồng hệ thống mới và gọi bất đồng bộ hàm `run()` trên luồng mới đó.
*   `t.run()`: Chỉ là gọi hàm thông thường trên luồng hiện tại (không tạo ra luồng mới).

### 4. Thread.sleep() vs Object.wait()
*   `Thread.sleep(ms)`: Luồng đi ngủ nhưng **vẫn giữ khóa (Lock)** đang nắm giữ.
*   `object.wait()`: Phải gọi trong khối `synchronized`. Luồng đi ngủ đồng thời **giải phóng khóa (Lock)** để luồng khác vào tranh chấp tài nguyên.

### 5. join()
*   Cho phép luồng hiện tại dừng lại đợi đến khi luồng đích thực thi xong hoàn toàn rồi mới tiếp tục chạy.

### 6. Race Condition (Tranh chấp dữ liệu)
*   Xảy ra khi nhiều luồng cùng truy cập và thay đổi một tài nguyên chung (Shared Mutable State) đồng thời mà không được đồng bộ hóa, dẫn đến kết quả cuối cùng bị sai lệch tùy theo tốc độ thực thi của mỗi luồng.

### 7. Đồng bộ hóa với từ khóa `synchronized`
*   Giúp khóa (Lock) một phương thức hoặc một đoạn code để tại một thời điểm chỉ có tối đa 1 luồng được truy cập, đảm bảo tính nguyên tử (Atomicity) và an toàn đa luồng.

---

## 📅 Day 5: Database Connectivity (JDBC)

### 1. 5 bước cơ bản làm việc với JDBC
1.  **Nạp Driver:** `Class.forName("com.mysql.cj.jdbc.Driver");` (Từ JDBC 4.0 trở lên, việc này tự động được thực hiện nhờ cơ chế Service Provider).
2.  **Mở Connection:** `DriverManager.getConnection(url, username, password);`
3.  **Tạo Statement:** Tạo `Statement` hoặc `PreparedStatement`.
4.  **Thực thi truy vấn:** Gọi `executeQuery()` cho SELECT hoặc `executeUpdate()` cho các câu lệnh thay đổi dữ liệu (INSERT, UPDATE, DELETE).
5.  **Đóng kết nối:** Đóng các tài nguyên `ResultSet`, `Statement`, `Connection` theo thứ tự ngược lại (Khuyên dùng cú pháp **Try-with-resources** để tự đóng tài nguyên an toàn).

### 2. Thực thi SELECT bằng Statement & ResultSet
```java
String sql = "SELECT id, name FROM users";
try (Connection conn = DriverManager.getConnection(url, user, pass);
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery(sql)) {
     
    while (rs.next()) {
        int id = rs.getInt("id");
        String name = rs.getString("name");
        System.out.println(id + " - " + name);
    }
}
```

### 3. Tại sao nên dùng PreparedStatement?
*   **Tránh SQL Injection:** SQL Injection là lỗ hổng bảo mật khi kẻ tấn công chèn mã SQL độc hại vào các ô nhập liệu của người dùng.
    *   *Statement:* Thực hiện ghép chuỗi thô trực tiếp: `SELECT * FROM users WHERE pass = '` + input + `'` -> Nhập `' OR '1'='1` sẽ hack qua được mật khẩu.
    *   *PreparedStatement:* Biên dịch khung câu lệnh SQL trước ở Database DB Server bằng ký tự hỏi chấm `?`. Khi truyền tham số vào bằng `setString()`, DB coi đó thuần túy là dữ liệu dạng Text thô (literal), loại bỏ hoàn toàn khả năng thực thi mã lệnh ẩn.
*   **Hiệu năng tốt hơn:** Database biên dịch trước câu lệnh SQL mẫu và lưu vào bộ nhớ cache, khi chạy nhiều lần với tham số khác nhau sẽ không cần biên dịch lại.

### 4. Batch Processing (Xử lý theo lô)
*   **Tại sao:** Thay vì gửi 1000 câu lệnh INSERT riêng lẻ về Database gây nghẽn mạng do round-trip liên tục, ta gom chúng lại gửi đi duy nhất 1 lần.
*   **Cách viết:**
    ```java
    conn.setAutoCommit(false); // Tắt auto commit để kiểm soát transaction
    try (PreparedStatement pstmt = conn.prepareStatement("INSERT INTO log VALUES (?)")) {
        for (int i = 0; i < 1000; i++) {
            pstmt.setString(1, "log_" + i);
            pstmt.addBatch(); // Gom lệnh vào hàng đợi
        }
        pstmt.executeBatch(); // Gửi toàn bộ đi một lúc
        conn.commit(); // Lưu thay đổi
    }
    ```

### 5. Kỹ năng Debug nâng cao
*   **Breakpoints:** Điểm đánh dấu dừng chương trình để theo dõi trạng thái lúc runtime.
*   **Step Over (F8):** Chạy qua dòng lệnh hiện tại, chuyển sang dòng tiếp theo trong cùng phương thức.
*   **Step Into (F7):** Nhảy vào bên trong phương thức đang được gọi để xem chi tiết bên trong nó chạy gì.
*   **Step Return (Shift+F8):** Thực thi nốt các dòng còn lại của hàm hiện tại và nhảy ngược ra ngoài nơi gọi phương thức đó.

### 6. Cách dùng tab Variables và Expressions trong Debug
*   **Variables Window:** Tự động liệt kê toàn bộ các biến cục bộ đang tồn tại trong phạm vi hiện tại cùng giá trị thực tế của chúng.
*   **Expressions Window:** Cho phép bạn tự gõ các biểu thức logic hoặc gọi các phương thức tùy chỉnh của Java ngay tại thời điểm dừng breakpoint để kiểm tra giá trị trả về ngay lập tức mà không cần viết thêm mã nguồn.

### 7. Bài tập lớn / Project cuối khóa
*   *Lưu ý khi trả lời Audit:* Bạn cần sẵn sàng vẽ ER Diagram của project của bạn trên bảng, giải thích luồng hoạt động từ Client gửi request qua Controller xử lý thế nào, gọi Model/DAO để tương tác Database qua JDBC ra sao, và cách bạn giải quyết các lỗi Connection leak bằng Try-with-resources.
