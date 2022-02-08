<h1>LÀM QUEN VỚI AWS DynamoDB</h1>

<h2>Nội dung</h2>

<h3>I.GIỚI THIỆU</h3>

<h3>II.CHUẨN BỊ</h3>

<h3>III.DỌN DẸP TÀI NGUYÊN</h3>

<h1><b>I.GIỚI THIỆU</b></h1>

<b>Amazon DynamoDB</b> là một dịch vụ cơ sở dữ liệu NoSQL được quản lý hoàn toàn, cung cấp hiệu suất nhanh và có thể dự đoán được với khả năng mở rộng liền mạch. DynamoDB cho phép giảm bớt gánh nặng quản trị của việc vận hành và mở rộng cơ sở dữ liệu phân tán, cung cấp phần cứng, thiết lập và cấu hình, sao chép, vá lỗi phần mềm hoặc mở rộng cụm. DynamoDB cũng cung cấp mã hóa ở trạng thái nghỉ.

- DynamoDB tạo các bảng cơ sở dữ liệu có thể lưu trữ và truy xuất bất kỳ lượng dữ liệu nào và phục vụ bất kỳ mức lưu lượng yêu cầu nào. Có thể tăng hoặc giảm quy mô công suất thông qua bảng của mình mà không có thời gian chết hoặc giảm hiệu suất. 

- DynamoDB cung cấp khả năng sao lưu theo yêu cầu. Nó cho phép bạn tạo bản sao lưu đầy đủ các bảng  để lưu giữ và lưu trữ lâu dài cho các nhu cầu tuân thủ quy định.

- Có thể tạo bản sao lưu theo yêu cầu và bật khôi phục tại thời điểm cho các bảng Amazon DynamoDB. Khôi phục theo thời gian giúp bảo vệ bảng khỏi các thao tác ghi hoặc xóa ngẫu nhiên. Với khôi phục theo thời gian, có thể khôi phục bảng về bất kỳ thời điểm nào trong 35 ngày qua.

- DynamoDB cho phép tự động xóa các mục đã hết hạn khỏi bảng giúp giảm mức sử dụng bộ nhớ và chi phí lưu trữ dữ liệu không còn phù hợp.

<h2><b>1.1 Các thành phần cốt lõi của Amazon DynamoDB</b></h2>


- <b>Tables</b> - Tương tự như các hệ thống cơ sở dữ liệu khác, DynamoDB lưu trữ dữ liệu trong bảng. Table là một tập hợp dữ liệu.

- <b>Items</b> - Mỗi bảng chứa không hoặc nhiều mục. Các mục trong DynamoDB theo nhiều cách tương tự với hàng, bản ghi hoặc bộ dữ liệu trong các hệ thống cơ sở dữ liệu khác. Trong DynamoDB, không có giới hạn về số lượng mục bạn có thể lưu trữ trong một bảng.

- <b>Attributes</b> - Mỗi mục bao gồm một hoặc nhiều thuộc tính. Attributes là một phần tử dữ liệu cơ bản, không cần phải chia nhỏ thêm nữa. Các thuộc tính trong DynamoDB theo nhiều cách tương tự với các trường hoặc cột trong các hệ thống cơ sở dữ liệu khác.

<h2><b>1.2 Primary Key</b></h2>

- Khi bạn tạo một bảng, ngoài tên bảng, bạn phải chỉ định primary key của bảng. 

- Primary key xác định duy nhất từng mục trong bảng, do đó không có hai mục nào có thể có cùng một khóa.

- DynamoDB hỗ trợ hai loại primary key khác nhau:
	-  Partition key
	-  Composite primary key

<h3><b>1.2 a. Partition key</b></h3>

- Một khóa chính đơn giản, bao gồm một thuộc tính được gọi là khóa phân vùng.

- DynamoDB sử dụng giá trị của khóa phân vùng làm đầu vào cho hàm băm bên trong. Đầu ra từ hàm băm xác định phân vùng (bộ nhớ vật lý bên trong DynamoDB) mà mục sẽ được lưu trữ.

- Trong bảng chỉ có khóa phân vùng, không có hai mục nào có thể có cùng giá trị khóa phân vùng.

<h3><b>1.2.b Composite primary key</b></h3>

- Thuộc tính đầu tiên là partition key và thuộc tính thứ hai là sort key.

- DynamoDB sử dụng giá trị partition key làm đầu vào cho hàm băm bên trong. Đầu ra từ hàm băm xác định phân vùng (bộ nhớ vật lý bên trong DynamoDB) mà mục sẽ được lưu trữ. Tất cả các mục có cùng giá trị partition key được lưu trữ cùng nhau, theo thứ tự được sắp xếp theo giá trị sort key.

- Trong bảng có khóa phân vùng và khóa sắp xếp, nhiều mục có thể có cùng giá trị partition key. Tuy nhiên, các mục đó phải có các giá trị sort key khác nhau.

- Composite primary key giúp bạn linh hoạt hơn khi truy vấn dữ liệu.

<h2><b>1.3 Secondary Indexes</b></h2>

- Bạn có thể tạo một hoặc nhiều secondary index trên một bảng. 

- Secondary index cho phép truy vấn dữ liệu trong bảng bằng khóa thay thế, ngoài các truy vấn đối với khóa chính. DynamoDB không yêu cầu sử dụng các chỉ mục, nhưng chúng giúp các ứng dụng của bạn linh hoạt hơn khi truy vấn dữ liệu. Sau khi tạo secondary index trên bảng, bạn có thể đọc dữ liệu từ chỉ mục theo cách giống như cách bạn làm từ bảng.

- DynamoDB hỗ trợ hai loại chỉ mục:
	- Global secondary index <br> - Chỉ mục có khóa phân vùng và khóa sắp xếp có thể khác với các chỉ mục trên bảng.

	- Local secondary index  <br> - Chỉ mục có cùng khóa phân vùng với bảng nhưng có khóa sắp xếp khác.

- Mỗi bảng trong DynamoDB có hạn ngạch 20 chỉ mục phụ toàn cục (hạn ngạch mặc định) và 5 chỉ mục phụ cục bộ.

<h2><b>1.4 Quy tắc đặt tên và kiểu dữ liệu</b></h2>

<h3><b>1.4.a Quy tắc đặt tên</b></h3>

- Các bảng, thuộc tính và các đối tượng khác trong DynamoDB phải có tên.

- Sau đây là các quy tắc đặt tên cho DynamoDB:

	- Tất cả các tên phải được mã hóa bằng UTF-8 và có phân biệt chữ hoa chữ thường.

	- Tên bảng và tên chỉ mục phải dài từ 3 đến 255 ký tự và chỉ được chứa các ký tự sau:
		- a-z
		- A-Z
		- 0-9
		- _(gạch dưới)
		- -(gạch ngang)
		- . (dấu chấm)

- Tên thuộc tính phải dài ít nhất một ký tự, nhưng không dài hơn 64 KB.

- Sau đây là các trường hợp ngoại lệ. Các tên thuộc tính này không được dài quá 255 ký tự:

	- Tên khóa của phân vùng chỉ mục phụ.

	- Chỉ mục phụ sắp xếp các tên khóa.

	- Tên của bất kỳ thuộc tính dự kiến ​​nào do người dùng chỉ định (chỉ áp dụng cho các chỉ mục phụ cục bộ).

<h3><b>1.4.b Kiểu dữ liệu</b></h3>
DynamoDB hỗ trợ nhiều kiểu dữ liệu khác nhau cho các thuộc tính trong bảng. Chúng có thể được phân loại như sau:

- Các kiểu vô hướng <br> - Một kiểu vô hướng có thể biểu diễn chính xác một giá trị. Các kiểu vô hướng là số, chuỗi, nhị phân, Boolean và null.

- Loại tài liệu <br>- Một loại tài liệu có thể đại diện cho một cấu trúc phức tạp với các thuộc tính lồng nhau, chẳng hạn như bạn sẽ tìm thấy trong tài liệu JSON. Các loại tài liệu là danh sách và bản đồ.

- Loại tập hợp <br>- Một loại tập hợp có thể đại diện cho nhiều giá trị vô hướng. Các loại tập hợp là tập hợp chuỗi, tập hợp số và tập hợp nhị phân.
 
<h2><b>1.5 Read Consistency</b></h2>

<h3><b>1.5.a Eventually Consistent Reads</b></h3>

- Khi bạn đọc dữ liệu từ bảng DynamoDB, phản hồi có thể không phản ánh kết quả của một thao tác ghi đã hoàn thành gần đây.  

- Phản hồi có thể bao gồm một số dữ liệu cũ. 

- Nếu bạn lặp lại yêu cầu đọc của mình sau một thời gian ngắn, phản hồi sẽ trả về dữ liệu mới nhất.

<h3><b>1.5.b Strongly Consistent Reads</b></h3>

Khi bạn yêu cầu đọc nhất quán mạnh mẽ, DynamoDB trả về phản hồi với dữ liệu cập nhật nhất, phản ánh các cập nhật từ tất cả các hoạt động ghi trước đó đã thành công. Tuy nhiên, tính nhất quán này đi kèm với một số nhược điểm:

- Việc đọc nhất quán mạnh có thể không khả dụng nếu có sự cố mạng hoặc ngừng hoạt động. Trong trường hợp này, DynamoDB có thể trả về lỗi máy chủ (HTTP 500).

- Các lần đọc nhất quán mạnh có thể có độ trễ cao hơn các lần đọc nhất quán cuối cùng.

- Các chỉ số phụ toàn cầu không được hỗ trợ đọc nhất quán.

- Các lần đọc nhất quán mạnh sử dụng nhiều dung lượng thông lượng hơn so với các lần đọc nhất quán cuối cùng.

<h2><b>1.6 Read/Write Capacity Mode</b></h2>

<h3><b>1.6.a On-Demand Mode</b></h3>
Amazon DynamoDB on-demand là một tùy chọn thanh toán linh hoạt có khả năng phục vụ hàng nghìn yêu cầu mỗi giây mà không cần lập kế hoạch dung lượng. DynamoDB theo yêu cầu cung cấp giá trả theo yêu cầu cho các yêu cầu đọc và ghi để bạn chỉ trả tiền cho những gì bạn sử dụng.

Khi bạn chọn chế độ theo yêu cầu, DynamoDB ngay lập tức đáp ứng các khối lượng công việc của bạn khi chúng tăng hoặc giảm đến bất kỳ mức lưu lượng truy cập nào đã đạt được trước đó. Nếu mức lưu lượng của khối lượng công việc đạt đến đỉnh mới, DynamoDB sẽ thích ứng nhanh chóng để đáp ứng khối lượng công việc. Các bảng sử dụng chế độ theo yêu cầu cung cấp cùng độ trễ mili giây một chữ số, cam kết thỏa thuận mức dịch vụ (SLA) và bảo mật mà DynamoDB đã cung cấp. Bạn có thể chọn theo yêu cầu cho cả bảng mới và bảng hiện có và bạn có thể tiếp tục sử dụng các API DynamoDB hiện có mà không cần thay đổi mã.

Chế độ theo yêu cầu là một lựa chọn tốt nếu bất kỳ điều nào sau đây là đúng:

- Bạn tạo bảng mới với khối lượng công việc không xác định.

- Bạn có lưu lượng ứng dụng không thể đoán trước.

- Bạn chỉ thích dễ dàng thanh toán cho những gì bạn sử dụng.

<h3><b>1.6.b Provisioned Mode</b></h3>

Nếu bạn chọn chế độ được cấp phép, bạn chỉ định số lần đọc và ghi mỗi giây mà bạn yêu cầu cho ứng dụng của mình. Bạn có thể sử dụng tính năng tự động chia tỷ lệ để tự động điều chỉnh dung lượng được cung cấp của bảng để đáp ứng với những thay đổi về lưu lượng truy cập. Điều này giúp bạn quản lý việc sử dụng DynamoDB của mình để duy trì bằng hoặc thấp hơn tỷ lệ yêu cầu xác định để có được khả năng dự đoán chi phí.

Chế độ được cung cấp là một tùy chọn tốt nếu bất kỳ điều nào sau đây là đúng:

- Bạn có lưu lượng ứng dụng có thể dự đoán được.

- Bạn chạy các ứng dụng có lưu lượng truy cập nhất quán hoặc tăng dần.

- Bạn có thể dự báo các yêu cầu về năng lực để kiểm soát chi phí.


<h1><b>II. CHUẨN BỊ</b></h1>

<h2><b>1.Sử dụng AWS Management Console</b></h2>

<h2><b>1.1 Tạo Access key cho người dùng IAM</b></h2>

Bước 1: Đăng nhập vào Bảng điều khiển quản lý AWS và mở bảng điều khiển IAM tại https://console.aws.amazon.com/iam/.

Bước 2: Trong ngăn dẫn hướng, chọn <b>Users</b>.

Bước 3: Chọn tên của người dùng có khóa truy cập bạn muốn tạo, sau đó chọn tab <b>Security credentials</b>.

Bước 4: Trong phần Access keys, chọn <b>Create access key</b>.

Bước 5: Để xem access key mới, hãy chọn <b>Show</b>. Thông tin đăng nhập của bạn sẽ trông giống như sau:

	Access key ID: AKIAIOSFODNN7EXAMPLE
	Secret access key: wJalrXUtnFEMI / K7MDENG / bPxRfiCYEXAMPLEKEY``

Bước 6: Để tải xuống cặp khóa, hãy chọn  <b>Download .csv file</b>. 

Bước 7: Sau khi bạn tải xuống tệp  <b>.csv</b>, chọn <b>Close</b> . 

<h2><b>1.2 Tạo bảng </b></h2>
Trong bước này, bạn tạo một  bảng Music trong Amazon DynamoDB. Bảng có các chi tiết sau:

- <b>Partition key</b> — Artist

- <b>Sort key</b> — SongTitle

Bước 1: Đăng nhập vào Bảng điều khiển quản lý AWS và mở DynamoDB Console tại https://console.aws.amazon.com/dynamodb/.

Bước 2: Trong ngăn điều hướng ở bên trái của bảng điều khiển, chọn <b>Dashboard</b>.

Bước 3: Ở phía bên phải của bảng điều khiển, chọn <b>Create Table</b>.

![Create Table Dashboard!](./images/CreateTableDashboard-1.png "CreateTableDashboard")

Bước 4: Nhập chi tiết bảng như sau:

- Đối với  <b>Table name</b>, hãy nhập <b>```Music```</b>.

- Đối với  <b>Partition key</b>, hãy nhập <b>```Artist```</b>.

- Nhập <b>SongTitle</b> làm <b>Sort key</b>.

- Chọn <b>Default settings</b>.

Bước 5:  Chọn <b>Create table</b> để tạo bảng.

![Create Table Dashboard!](./images/CreateTable-2.png "CreateTableDashboard")

<b>Kết quả:</b>

![Create Table Dashboard!](./images/CreateTable-3.png "CreateTableDashboard")


<h2><b>1.3 Ghi dữ liệu </b></h2>

Các bước ghi dữ liệu vào bảng Music(đã tạo ở mục 1.2):

- Bước 1: Mở bảng DynamoDB console tại https://console.aws.amazon.com/dynamodb/

- Bước 2: Trong thanh điều hướng ở bên trái của bảng điều khiển, chọn <b>Tables</b>.

- Bước 3: Trong danh sách bảng, hãy chọn bảng <b>Music</b>.

![Write Data  Dashboard!](./images/Writedata.png "WriteData")

- Bước 4: Chọn <b>Explore items</b>

![Write Data  Dashboard!](./images/Writedata-1.png "WriteData")

- Bước 5: Trong giao diện Items, chọn <b>Create item</b>


![Write Data  Dashboard!](./images/WriteData-2.png "WriteData")


- Bước 6: Chọn <b>Add new attribute</b>, sau đó chọn <b>Number</b>. Tên trường: <b>Awards.</b>

- Bước 7: Lặp lại bước 6 tạo <b> AlbumTitle</b> với kiểu <b>String.</b>

- Bước 8: Nhập các giá trị cho các item:

	- <b>Artist</b>, nhập <b>`No One You Know`</b>

	- <b>SongTitle</b>, nhập <b>`Call Me Today`</b>

	- <b>AlbumTitle</b>, nhập <b>`Somewhat Famous`</b>

	- <b>Awards</b>, nhập <b>`1`</b>.

- Bước 9: Chọn <b>Create item.</b>

![Write Data  Dashboard!](./images/Writedata-3.png "WriteData")

- Bước 10: Lặp lại bước 8 và tạo một mục khác với các giá trị sau:

	- <b>Artist</b>, nhập <b>`Acme Band`</b>.

	- <b>SongTitle</b> nhập <b>`Happy Day`</b>.

	- <b>AlbumTitle</b>, nhập <b>`Songs About Life`</b>.

	- <b>Awards</b>, nhập <b>`10`</b>.

- Bước 11: Thực hiện thao tác này một lần nữa để tạo một mục khác có cùng một Artist như bước trước, nhưng các giá trị khác nhau cho các thuộc tính khác:
	- <b>Artist</b>, nhập <b>`Acme Band`</b>.

	- <b>SongTitle</b> nhập <b>`PartiQL Rocks`</b>.

	- <b>AlbumTitle</b>, nhập <b>`Another Album Title`</b>.

	- <b>Awards</b>, nhập <b>`8`</b>.

- Bước 12: Kết quả:

![Write Data  Dashboard!](./images/Writedata-4.png "WriteData")


<h2><b>1.4 Đọc dữ liệu </b></h2>

Các bước đọc dữ liệu từ bảng Music bằng DynamoDB console:

- Bước 1: Mở DynamoDB console  tại  https://console.aws.amazon.com/dynamodb/

- Bước 2: Trong thanh điều hướng ở bên trái của bảng điều khiển, chọn <b>Tables</b>

- Bước 3: Chọn bảng <b>Music</b> từ danh sách bảng.

- Bước 4: Chọn <b>Actions</b>, sau đó chọn <b>Explore item.</b>

- Bước 5: Chọn <b>Query</b> , sau đó điền <b>Artist (Partition key)</b> là <b>`Acme Band`</b>

- Bước 6: Chọn <b>Run</b> và thu kết quả như hình:


![Read Data  Dashboard!](./images/Readdata.png "ReadData")


<h2><b>1.5 Cập nhật dữ liệu </b></h2>

Các bước cập nhật dữ liệu bảng Music như sau:

- Bước 1: Mở bảng DynamoDB console tại  https://console.aws.amazon.com/dynamodb/

- Bước 2: Trong thanh điều hướng ở bên trái của bảng điều khiển, chọn <b>Tables</b>

- Bước 3: Chọn bảng <b>Music</b> từ danh sách bảng.

- Bước 4: Chọn <b>Actions</b>, sau đó chọn <b>Explore item.</b>

- Bước 5: Chọn item có giá trị <b>Artist</b> là <b>Acme Band</b> và giá trị <b>SongTitle</b> là <b>Happy Day</b>.

- Bước 6: Cập nhật giá trị <b>Album Title</b> thành <b>Album Title Updated</b>, sau đó chọn <b>Save changes</b> .

![Update Data  Dashboard!](./images/update-data.png "UpdateData")


<h2><b>1.6 Truy vấn dữ liệu </b></h2>

Các bước truy vấn dữ liệu bảng <b>Music</b> như sau:

- Bước 1: Mở bảng DynamoDB console tại  https://console.aws.amazon.com/dynamodb/

- Bước 2: Trong thanh điều hướng ở bên trái của bảng điều khiển, chọn <b>Tables</b>

- Bước 3: Chọn bảng <b>Music</b> từ danh sách bảng.

- Bước 4: Chọn <b>Actions</b>, sau đó chọn <b>Explore item.</b>

- Bước 5: Chọn <b>Query</b>

- Bước 6: Nhập chi tiết các key:

	- Đối với <b>Artist (Partition key)</b>, nhập <b>Acme Band</b>

	- Đối với <b>SongTitle (Sort key)</b>, nhập <b>PartiQL Rocks</b>

- Bước 7: Chọn <b>Run</b>


 ![Query Data  Dashboard!](./images/Querydata.png "UpdateData")


 
<h2><b>1.7 Tạo Global Secondary Index </b></h2>

- Bước 1: Mở bảng DynamoDB console tại  https://console.aws.amazon.com/dynamodb/

- Bước 2: Trong thanh điều hướng ở bên trái của bảng điều khiển, chọn <b>Tables</b>

- Bước 3: Chọn bảng <b>Music</b> từ danh sách bảng.

- Bước 4: Chọn tab <b>Indexes</b> từ bảng <b>Music</b>.

- Bước 5: Chọn <b>Create index</b>

 ![Create Global Secondary Index!](./images/create-index.png "Create Global Secondary Index")

- Bước 6: Đối với <b>Partition key</b> , nhập <b>`AlbumTitle`</b>.

- Bước 7: Đối với <b>Index name</b>, nhập <b>`AlbumTitle-index`</b>.

- Bước 8: Các mục khác để mặc định và chọn <b>Create index</b>

 ![Create Global Secondary Index!](./images/create-index-2.png "Create Global Secondary Index")

 <b>Kết quả</b>

  ![Create Global Secondary Index!](./images/create-index-3.png "Create Global Secondary Index")


<h2><b>1.8 Truy vấn Global Secondary Index </b></h2>

- Bước 1: Mở bảng DynamoDB console tại  https://console.aws.amazon.com/dynamodb/

- Bước 2: Trong thanh điều hướng ở bên trái của bảng điều khiển, chọn <b>Tables</b>

- Bước 3: Chọn bảng <b>Music</b> từ danh sách bảng.

- Bước 4: Chọn <b>Actions</b>, sau đó chọn <b>Explore item.</b>

- Bước 5: Chọn <b>Query</b>

- Bước 6: Trong danh sách thả xuống bên dưới <b>Query</b>, chọn <b>AlbumTitle-index</b>

- Bước 7: Đối với <b>AlbumTitle</b> , nhập <b>`Somewhat Famous`</b>, rồi chọn <b>Run</b>.

![Query Global Secondary Index!](./images/query-index.png "Query Global Secondary Index")

<h2>2.SỬ DỤNG AWS CLOUDSHELL</h1>

<h3>2.1 Tạo bảng </h2>

Bước 1: Khởi động AWS CloudShell tại https://console.aws.amazon.com/cloudshell/home?region=us-east-1

Bước 2: Gõ lệnh  ```aws configure```

Bước 3: Nhập chi tiết thông tin từ file csv ở phần 2.1:
 - AWS Access Key ID 
 - AWS Secret Access Key
 - Default region name
 - Default output format: bỏ trống

![Create Table Dashboard!](./images/CreateTable-4.png "CreateTableDashboard")


Bước 4: Để tạo bảng, ta sử dụng lệnh ` create-table` . Gõ lệnh:
```aws dynamodb create-table \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema \
        AttributeName=Artist,KeyType=HASH \
        AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5 \
    --table-class STANDARD```
 
 

![Create Table Dashboard!](./images/CreateTable-5.png "CreateTableDashboard")

<b>Kết quả:</b>

`{
    "TableDescription": {
        "AttributeDefinitions": [
            {
                "AttributeName": "Artist",
                "AttributeType": "S"
            },
            {
                "AttributeName": "SongTitle",
                "AttributeType": "S"
            }
        ],
        "TableName": "Music",
        "KeySchema": [
            {
                "AttributeName": "Artist",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "SongTitle",
                "KeyType": "RANGE"
            }
        ],
        "TableStatus": "CREATING",
        "CreationDateTime": "2022-02-08T06:15:18.343000+00:00",
        "ProvisionedThroughput": {
            "NumberOfDecreasesToday": 0,
            "ReadCapacityUnits": 10,
            "WriteCapacityUnits": 5
        },
        "TableSizeBytes": 0,
        "ItemCount": 0,
        "TableArn": "arn:aws:dynamodb:us-east-2:089359461550:table/Music",
        "TableId": "4b2a1e9a-c223-4b07-a536-c4b85a67df96",
        "TableClassSummary": {
            "TableClass": "STANDARD"
        }
    }
}`

Bước 5: Kiểm tra trạng thái bảng:

- Gõ lệnh `aws dynamodb describe-table --table-name Music | grep TableStatus`

- Khi DynamoDB hoàn thành việc tạo bảng, giá trị của TableStatus là ACTIVE: `"TableStatus": "ACTIVE",`

<h3>2.2 Ghi dữ liệu </h3>

- Để ghi dữ liệu, sử dụng lệnh `put-item`

- Sau khi tạo bảng ở bước 2.1, tiếp tục gõ lệnh:

`aws dynamodb put-item \
    --table-name Music  \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}, "Awards": {"N": "1"}}'`

`aws dynamodb put-item \
    --table-name Music  \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Howdy"}, "AlbumTitle": {"S": "Somewhat Famous"}, "Awards": {"N": "2"}}'`

`aws dynamodb put-item \
    --table-name Music \
    --item \
        '{"Artist": {"S": "Acme Band"}, "SongTitle": {"S": "Happy Day"}, "AlbumTitle": {"S": "Songs About Life"}, "Awards": {"N": "10"} }'`
                            
`aws dynamodb put-item \
    --table-name Music \
    --item \
        '{"Artist": {"S": "Acme Band"}, "SongTitle": {"S": "PartiQL Rocks"}, "AlbumTitle": {"S": "Another Album Title"}, "Awards": {"N": "8"} }'`

<h3>2.3 Đọc dữ liệu </h3>

- Để đọc dữ liệu, sử dụng lệnh `get-item` và tham số `consistent-read` thể hiện <b>strongly consistent reads</b>.

- Mặc định của AWS DynamoDB là <b>eventually consistent reads</b>.

- Gõ lệnh:

`aws dynamodb get-item --consistent-read \
    --table-name Music \
    --key '{ "Artist": {"S": "Acme Band"}, "SongTitle": {"S": "Happy Day"}}'`

<h3>2.4 Cập nhật dữ liệu </h3>

- Để cập nhật dữ liệu, sử dụng lệnh `update-item`

- Gõ lệnh:

`aws dynamodb update-item \
    --table-name Music \
    --key '{ "Artist": {"S": "Acme Band"}, "SongTitle": {"S": "Happy Day"}}' \
    --update-expression "SET AlbumTitle = :newval" \
    --expression-attribute-values '{":newval":{"S":"Updated Album Title"}}' \
    --return-values ALL_NEW`

<h3>2.5 Truy vấn dữ liệu </h3>

- Để truy vấn dữ liệu từ bảng, sử dụng lệnh `query` và cung cấp partition key.

- Gõ lệnh:

`aws dynamodb query \
    --table-name Music \
    --key-condition-expression "Artist = :name" \
    --expression-attribute-values  '{":name":{"S":"Acme Band"}}'`

<h3>2.6 Tạo Global Secondary Index</h3>

- Để tạo Global Secondary Index, sử dụng lệnh `update-table`

- Gõ lệnh: 

`aws dynamodb update-table \
    --table-name Music \
    --attribute-definitions AttributeName=AlbumTitle,AttributeType=S \
    --global-secondary-index-updates \
        "[{\"Create\":{\"IndexName\": \"AlbumTitle-index\",\"KeySchema\":[{\"AttributeName\":\"AlbumTitle\",\"KeyType\":\"HASH\"}], \
        \"ProvisionedThroughput\": {\"ReadCapacityUnits\": 10, \"WriteCapacityUnits\": 5      },\"Projection\":{\"ProjectionType\":\"ALL\"}}}]"`

<h3>2.7 Truy vấn Global Secondary Index</h3>

- Để truy vấn Global Secondary Index, sử dụng lệnh `query`

- Gõ lệnh:

`aws dynamodb query \
    --table-name Music \
    --index-name AlbumTitle-index \
    --key-condition-expression "AlbumTitle = :name" \
    --expression-attribute-values  '{":name":{"S":"Somewhat Famous"}}'`

<h1>III.DỌN DẸP TÀI NGUYÊN</h1>

<h3>1.1 Sử dụng AWS Management Console</h2>

- Bước 1: Mở bảng DynamoDB console tại  https://console.aws.amazon.com/dynamodb/

- Bước 2: Trong thanh điều hướng ở bên trái của bảng điều khiển, chọn <b>Tables</b>

- Bước 3: Chọn bảng <b>Music</b> từ danh sách bảng.

- Bước 4: Chọn <b>Actions</b>, sau đó chọn <b>Delete table</b>.



![Delete Table!](./images/delete-table.png "Delete Table")


<h3>1.2 Sử dụng AWS CloudShell</h2>

- Để xóa bảng, sử dụng lệnh `delete-table`

- Gõ lệnh:

`aws dynamodb delete-table --table-name Music`











