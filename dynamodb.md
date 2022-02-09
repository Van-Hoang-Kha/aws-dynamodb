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


Bước 4: Để tạo bảng, ta sử dụng lệnh `create-table` . Gõ lệnh:
```
aws dynamodb create-table \
    --table-name Music \
    --attribute-definitions \
        AttributeName=Artist,AttributeType=S \
        AttributeName=SongTitle,AttributeType=S \
    --key-schema \
        AttributeName=Artist,KeyType=HASH \
        AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5 \
    --table-class STANDARD
  ```
 
 

![Create Table Dashboard!](./images/CreateTable-5.png "CreateTableDashboard")

<b>Kết quả:</b>
```
{
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
}
```

Bước 5: Kiểm tra trạng thái bảng:

- Gõ lệnh: 
```
aws dynamodb describe-table --table-name Music | grep TableStatus
```

- Khi DynamoDB hoàn thành việc tạo bảng, giá trị của TableStatus là ACTIVE: `"TableStatus": "ACTIVE",`

<h3>2.2 Ghi dữ liệu </h3>

- Để ghi dữ liệu, sử dụng lệnh `put-item`

- Sau khi tạo bảng ở bước 2.1, tiếp tục gõ lệnh:

```
aws dynamodb put-item \
    --table-name Music  \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Call Me Today"}, "AlbumTitle": {"S": "Somewhat Famous"}, "Awards": {"N": "1"}}'

aws dynamodb put-item \
    --table-name Music  \
    --item \
        '{"Artist": {"S": "No One You Know"}, "SongTitle": {"S": "Howdy"}, "AlbumTitle": {"S": "Somewhat Famous"}, "Awards": {"N": "2"}}'

aws dynamodb put-item \
    --table-name Music \
    --item \
        '{"Artist": {"S": "Acme Band"}, "SongTitle": {"S": "Happy Day"}, "AlbumTitle": {"S": "Songs About Life"}, "Awards": {"N": "10"} }'
                            
aws dynamodb put-item \
    --table-name Music \
    --item \
        '{"Artist": {"S": "Acme Band"}, "SongTitle": {"S": "PartiQL Rocks"}, "AlbumTitle": {"S": "Another Album Title"}, "Awards": {"N": "8"} }'
```
<h3>2.3 Đọc dữ liệu </h3>

- Để đọc dữ liệu, sử dụng lệnh `get-item` và tham số `consistent-read` thể hiện <b>strongly consistent reads</b>.

- Mặc định của AWS DynamoDB là <b>eventually consistent reads</b>.

- Gõ lệnh:
```
aws dynamodb get-item --consistent-read \
    --table-name Music \
    --key '{ "Artist": {"S": "Acme Band"}, "SongTitle": {"S": "Happy Day"}}'
```

<h3>2.4 Cập nhật dữ liệu </h3>

- Để cập nhật dữ liệu, sử dụng lệnh `update-item`

- Gõ lệnh:
```
aws dynamodb update-item \
    --table-name Music \
    --key '{ "Artist": {"S": "Acme Band"}, "SongTitle": {"S": "Happy Day"}}' \
    --update-expression "SET AlbumTitle = :newval" \
    --expression-attribute-values '{":newval":{"S":"Updated Album Title"}}' \
    --return-values ALL_NEW
 ```

<h3>2.5 Truy vấn dữ liệu </h3>

- Để truy vấn dữ liệu từ bảng, sử dụng lệnh `query` và cung cấp partition key.

- Gõ lệnh:
```
aws dynamodb query \
    --table-name Music \
    --key-condition-expression "Artist = :name" \
    --expression-attribute-values  '{":name":{"S":"Acme Band"}}'
 ```

<h3>2.6 Tạo Global Secondary Index</h3>

- Để tạo Global Secondary Index, sử dụng lệnh `update-table`

- Gõ lệnh: 
```
aws dynamodb update-table \
    --table-name Music \
    --attribute-definitions AttributeName=AlbumTitle,AttributeType=S \
    --global-secondary-index-updates \
        "[{\"Create\":{\"IndexName\": \"AlbumTitle-index\",\"KeySchema\":[{\"AttributeName\":\"AlbumTitle\",\"KeyType\":\"HASH\"}], \
        \"ProvisionedThroughput\": {\"ReadCapacityUnits\": 10, \"WriteCapacityUnits\": 5      },\"Projection\":{\"ProjectionType\":\"ALL\"}}}]"
```

<h3>2.7 Truy vấn Global Secondary Index</h3>

- Để truy vấn Global Secondary Index, sử dụng lệnh `query`

- Gõ lệnh:
```
aws dynamodb query \
    --table-name Music \
    --index-name AlbumTitle-index \
    --key-condition-expression "AlbumTitle = :name" \
    --expression-attribute-values  '{":name":{"S":"Somewhat Famous"}}'
 ```
<h1>III. BẮT ĐẦU VỚI AWS SDK</h1>

<h2>1. CHUẨN BỊ</h2> 

Sử dụng AWS SDK cho Python (Boto3) để viết các chương trình đơn giản nhằm thực hiện các hoạt động Amazon DynamoDB sau:

- Tạo một bảng được gọi Moviesvà tải dữ liệu mẫu ở định dạng JSON.

- Thực hiện các thao tác tạo, đọc, cập nhật và xóa trên bảng.

- Chạy các truy vấn đơn giản.

<h3>1.1 Cấu hình AWS CLI</h3>

- Bước 1: Mở <b>Window Command Prompt</b>, chọn chế độ <b>`Run as administrator`</b>

- Bước 2: Gõ lệnh <b>`aws configure`</b>

- Bước 3: Nhập chi tiết thông tin từ file csv ở phần 2.1:

    - AWS Access Key ID 

    - AWS Secret Access Key

    - Default region name

    - Default output format: bỏ trống

- Bước 4: Cài đặt <b>Python 2.6</b> trở lên.

- Bước 5: Kiểm tra version python để xác định đã cài đặt thành công bằng lệnh <b>`python --version`</b>

- Bước 5: Cài đặt thư viện Boto3 bằng lệnh <b>`pip install boto3`</b>

<h3>1.2 Boto 3: Resource vs Client</h3>

<h3>1.2.a Resource</h3>

<b>Resource</b> là một phần trừu tượng cấp cao hơn so với các máy khách. Chúng được tạo từ mô tả tài nguyên JSON có trong chính thư viện boto. Ví dụ: đây là định nghĩa tài nguyên cho S3 .

Tài nguyên cung cấp giao diện hướng đối tượng để tương tác với các dịch vụ AWS khác nhau. Các tài nguyên có thể được khởi tạo như sau:
```
import boto3

s3 = boto3.resource("s3")

```

<h3>1.2.b Client</h3>

<b>Client</b>cung cấp giao diện cấp thấp cho dịch vụ AWS. Định nghĩa của chúng được tạo bởi mô tả dịch vụ JSON có trong thư viện botocore . Gói botocore được chia sẻ giữa boto3 cũng như AWS CLI .

Định nghĩa dịch vụ cho AWS S3 được lưu trữ dưới dạng JSON trong gói botocore .

Lợi ích chính của việc sử dụng ứng dụng Boto3 Client là:

- Nó ánh xạ 1: 1 với API dịch vụ AWS thực tế.
- Tất cả các hoạt động dịch vụ AWS được hỗ trợ bởi Client

Ví dụ: nếu bạn muốn liệt kê tất cả các nhóm S3 trong tài khoản AWS của mình, bạn có thể sử dụng ứng dụng khách S3 như sau:

```
import boto3

# Retrieve the list of existing buckets
s3 = boto3.client("s3")
response = s3.list_buckets()

# Output the bucket names
print("Existing buckets:")
for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')

```

<h2>2. Bắt đầu phát triển với Python và DynamoDB </h2>

<h3><b>2.1 Tạo bảng</b></h3>

Tạo một bảng có tên Movies. Khóa chính cho bảng bao gồm các thuộc tính sau:

<b>year</b> – The partition key. AttributeType là N(number).

<b>title</b> – The sort key. AttributeType là S(string).

- Bước 1: Tạo file có tên <b>`MoviesCreateTable.py`</b>

- Bước 2: Sao chép đoạn mã sau và dán vào file <b>`MoviesCreateTable.py`</b>

```
import boto3


def create_movie_table(dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    movie_table = create_movie_table()
    print("Table status:", movie_table.table_status)

```

- Bước 3: Chạy chương trình bằng Window Command Prompt đã được xác thực và cấu hình ở bước 1.1. Gõ lệnh:
```
python MoviesCreateTable.py
```
Trường hợp khác: sử dụng `python "đường dẫn file MoviesCreateTable.py"`

- Bước 4: Sau khi chạy chương trình trả về <b>`Table status: CREATING`</b> là tạo bảng thành công.
<h3>2.2 Ghi dữ liệu</h3>

Thực hiện thêm item vào bảng Movies vừa tạo ở bước 2.1

- Bước 1: Tạo file có tên <b>`MoviesItemOps01.py`</b> 

- Bước 2: Sao chép chương trình sau và dán vào file <b>`MoviesItemOps01.py`</b>

```
from pprint import pprint
import boto3


def put_movie(title, year, plot, rating, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')
    response = table.put_item(
        Item={
            'year': year,
            'title': title,
            'info': {
                'plot': plot,
                'rating': rating
            }
        }
    )
    return response


if __name__ == '__main__':
    movie_resp = put_movie("The Big New Movie", 2015,
                           "Nothing happens at all.", 0)
    print("Put movie succeeded:")
    pprint(movie_resp, sort_dicts=False)

```

- Bước 3: Chạy chương trình bằng Window Command Prompt đã được xác thực và cấu hình ở bước 1.1. Gõ lệnh:

```
python MoviesItemOps01.py
```
Trường hợp khác: sử dụng `python "đường dẫn file MoviesItemOps01.py"`

- Bước 4: Sau khi chạy chương trình, thu được kết quả:

```
Put movie succeeded:
{'ResponseMetadata': {'RequestId': 'U9PQSVRR5PKKDD7NPV0NH91JD7VV4KQNSO5AEMVJF66Q9ASUAAJG',
                      'HTTPStatusCode': 200,
                      'HTTPHeaders': {'server': 'Server',
                                      'date': 'Wed, 09 Feb 2022 03:11:45 GMT',
                                      'content-type': 'application/x-amz-json-1.0',
                                      'content-length': '2',
                                      'connection': 'keep-alive',
                                      'x-amzn-requestid': 'U9PQSVRR5PKKDD7NPV0NH91JD7VV4KQNSO5AEMVJF66Q9ASUAAJG',
                                      'x-amz-crc32': '2745614147'},
                      'RetryAttempts': 0}}

```

<h3>2.3 Đọc dữ liệu</h3>

- Bước 1: Tạo file có tên <b>`MoviesItemOps02.py`</b>

- Bước 2: Sao chép đoạn mã sau và dán vào file <b>`MoviesItemOps02.py`</b>

```
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_movie(title, year, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')

    try:
        response = table.get_item(Key={'year': year, 'title': title})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    movie = get_movie("The Big New Movie", 2015,)
    if movie:
        print("Get movie succeeded:")
        pprint(movie, sort_dicts=False)

```
- Bước 3: Chạy chương trình bằng Window Command Prompt đã được xác thực và cấu hình ở bước 1.1. Gõ lệnh:

```
python MoviesItemOps02.py
```
Trường hợp khác: sử dụng `python "đường dẫn file MoviesItemOps02.py"`

- Bước 4: Sau khi chạy chương trình, thu được kết quả:

```
Get movie succeeded:
{'year': Decimal('2015'),
 'info': {'rating': Decimal('0'), 'plot': 'Nothing happens at all.'},
 'title': 'The Big New Movie'}
```

<h3>2.4 Cập nhật dữ liệu</h3>

- Bước 1: Tạo file có tên <b>`MoviesItemOps03.py`</b>

- Bước 2: Sao chép đoạn mã sau và dán vào file <b>`MoviesItemOps03.py`</b>

```
from decimal import Decimal
from pprint import pprint
import boto3


def update_movie(title, year, rating, plot, actors, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p, info.actors=:a",
        ExpressionAttributeValues={
            ':r': Decimal(rating),
            ':p': plot,
            ':a': actors
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_movie(
        "The Big New Movie", 2015, 5.5, "Everything happens all at once.",
        ["Larry", "Moe", "Curly"])
    print("Update movie succeeded:")
    pprint(update_response, sort_dicts=False)

```

- Bước 3: Chạy chương trình bằng Window Command Prompt đã được xác thực và cấu hình ở bước 1.1. Gõ lệnh:

```
python MoviesItemOps03.py
```
Trường hợp khác: sử dụng `python "đường dẫn file MoviesItemOps03.py"`

- Bước 4: Sau khi chạy chương trình, thu được kết quả:

```
Update movie succeeded:
{'Attributes': {'info': {'actors': ['Larry', 'Moe', 'Curly'],
                         'plot': 'Everything happens all at once.',
                         'rating': Decimal('5.5')}},
 'ResponseMetadata': {'RequestId': 'RFMTVB72A6E2J39HBPIK8SHBN7VV4KQNSO5AEMVJF66Q9ASUAAJG',
                      'HTTPStatusCode': 200,
                      'HTTPHeaders': {'server': 'Server',
                                      'date': 'Wed, 09 Feb 2022 03:29:15 GMT',
                                      'content-type': 'application/x-amz-json-1.0',
                                      'content-length': '156',
                                      'connection': 'keep-alive',
                                      'x-amzn-requestid': 'RFMTVB72A6E2J39HBPIK8SHBN7VV4KQNSO5AEMVJF66Q9ASUAAJG',
                                      'x-amz-crc32': '3767510606'},
                      'RetryAttempts': 0}}

```


<h3>2.5 Xóa dữ liệu</h3>

- Bước 1: Tạo file có tên <b>`MoviesItemOps04.py`</b>

- Bước 2: Sao chép đoạn mã sau và dán vào file <b>`MoviesItemOps04.py`</b>

```
from decimal import Decimal
from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def delete_underrated_movie(title, year, rating, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')

    try:
        response = table.delete_item(
            Key={
                'year': year,
                'title': title
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response


if __name__ == '__main__':
    print("Attempting a conditional delete...")
    delete_response = delete_underrated_movie("The Big New Movie", 2015, 5)
    if delete_response:
        print("Delete movie succeeded:")
        pprint(delete_response, sort_dicts=False)

```
- Bước 3: Chạy chương trình bằng Window Command Prompt đã được xác thực và cấu hình ở bước 1.1. Gõ lệnh:

```
python MoviesItemOps03.py
```
Trường hợp khác: sử dụng `python "đường dẫn file MoviesItemOps03.py"`

- Bước 4: Sau khi chạy chương trình, thu được kết quả: 

```
Attempting a conditional delete...
Delete movie succeeded:
{'ResponseMetadata': {'RequestId': 'HHA9MQ2U0UP1CL7CECBAAQRMMVVV4KQNSO5AEMVJF66Q9ASUAAJG',
                      'HTTPStatusCode': 200,
                      'HTTPHeaders': {'server': 'Server',
                                      'date': 'Wed, 09 Feb 2022 03:39:32 GMT',
                                      'content-type': 'application/x-amz-json-1.0',
                                      'content-length': '2',
                                      'connection': 'keep-alive',
                                      'x-amzn-requestid': 'HHA9MQ2U0UP1CL7CECBAAQRMMVVV4KQNSO5AEMVJF66Q9ASUAAJG',
                                      'x-amz-crc32': '2745614147'},
                      'RetryAttempts': 0}}
```


<h3>2.6 Tải dữ liệu mẫu</h3>

- Bước 1: Tải xuống dữ liệu mẫu <b>moviedata.zip</b>

- Bước 2: Giải nén tệp dữ liệu ( moviedata.json) từ kho lưu trữ.

- Bước 3: Sao chép tệp moviedata.json vào thư mục hiện tại của bạn.

- Bước 4: Tạo file có tên <b>`MoviesLoadData.py`</b>

- Bước 5: Sao chép đoạn mã sau và dán vào file <b>`MoviesLoadData.py`</b>

```
from decimal import Decimal
import json
import boto3


def load_movies(movies, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        print("Adding movie:", year, title)
        table.put_item(Item=movie)


if __name__ == '__main__':
    with open("moviedata.json") as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)
    load_movies(movie_list)

```
- Bước 3: Chạy chương trình bằng Window Command Prompt đã được xác thực và cấu hình ở bước 1.1. Gõ lệnh:

```
python MoviesLoadData.py
```
Trường hợp khác: sử dụng `python "đường dẫn file MoviesLoadData.py"`

- Bước 4: Sau khi chạy chương trình, thu được kết quả: 
```
Adding movie: 2013 Insidious: Chapter 2
Adding movie: 2013 World War Z
Adding movie: 2014 X-Men: Days of Future Past
Adding movie: 2014 Transformers: Age of Extinction
Adding movie: 2013 Now You See Me
Adding movie: 2013 Gravity
Adding movie: 2013 We're the Millers
Adding movie: 2013 Riddick
Adding movie: 2013 The Family
Adding movie: 2013 Star Trek Into Darkness
Adding movie: 2013 After Earth
Adding movie: 2013 The Great Gatsby
Adding movie: 2014 Divergent
Adding movie: 2013 We Are What We Are
Adding movie: 2013 Iron Man 3
Adding movie: 2014 The Amazing Spider-Man 2
Adding movie: 2013 Curse of Chucky
Adding movie: 2013 The Conjuring
Adding movie: 2013 Oldboy
Adding movie: 2013 Escape Plan
Adding movie: 2013 Elysium
Adding movie: 2013 Cloudy with a 
```
Lưu ý: Đúng đường dẫn file <b>`moviedata.json`</b>


<h3>2.7 Truy vấn dữ liệu</h3>

Truy xuất tất cả các phim được phát hành vào năm 1985 từ dữ liệu mẫu được tải lên ở mục 2.6


- Bước 1: Tạo file có tên <b>`MoviesQuery01.py`</b>

- Bước 2: Sao chép đoạn mã sau và dán vào file <b>`MoviesQuery01.py`</b>
```
import boto3
from boto3.dynamodb.conditions import Key


def query_movies(year, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')
    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )
    return response['Items']


if __name__ == '__main__':
    query_year = 1985
    print(f"Movies from {query_year}")
    movies = query_movies(query_year)
    for movie in movies:
        print(movie['year'], ":", movie['title'])

```
- Bước 3: Chạy chương trình bằng Window Command Prompt đã được xác thực và cấu hình ở bước 1.1. Gõ lệnh:

```
python MoviesQuery01.py
```
Trường hợp khác: sử dụng `python "đường dẫn file MoviesQuery01.py"`

- Bước 4: Sau khi chạy chương trình, thu được kết quả: 

```
Movies from 1985
1985 : A Nightmare on Elm Street Part 2: Freddy's Revenge
1985 : A Room with a View
1985 : A View to a Kill
1985 : Back to the Future
1985 : Better Off Dead...
1985 : Brazil
1985 : Clue
1985 : Cocoon
1985 : Commando
1985 : Day of the Dead
1985 : Flesh+Blood
1985 : Friday the 13th: A New Beginning
1985 : Fright Night
1985 : Girls Just Want to Have Fun
1985 : Just One of the Guys
1985 : Legend
1985 : Mad Max Beyond Thunderdome
1985 : Mask
1985 : Pale Rider
1985 : Pee-wee's Big Adventure
1985 : Police Academy 2: Their First Assignment
1985 : Rambo: First Blood Part II
1985 : Real Genius
1985 : Return to Oz
1985 : Rocky IV
1985 : Silverado
1985 : St. Elmo's Fire
1985 : Teen Wolf
1985 : The Breakfast Club
1985 : The Color Purple
1985 : The Goonies
1985 : The Last Dragon
1985 : The Return of the Living Dead
1985 : Weird Science
1985 : Witness

```

<h3>2.8 Quét dữ liệu</h3>

Phương thức <b>scan</b> đọc mọi mục trong toàn bộ bảng và trả về tất cả dữ liệu trong bảng. Bạn có thể cung cấp một tùy chọn <b>`filter_expression`</b> để chỉ những mặt hàng phù hợp với tiêu chí của bạn mới được trả lại. Tuy nhiên, bộ lọc chỉ được áp dụng sau khi toàn bộ bảng đã được quét.

Chương trình sau quét toàn bộ bảng Movies, trong đó có khoảng 5.000 mục. Quá trình quét chỉ định bộ lọc tùy chọn để chỉ lấy các phim từ những năm 1950 (khoảng 100 mục) và loại bỏ tất cả các phim khác.

- Bước 1: Tạo file có tên <b>`MoviesScan.py`</b>

- Bước 2: Sao chép đoạn mã sau và dán vào file <b>`MoviesScan.py`</b>

```
from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def scan_movies(year_range, display_movies, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Movies')
    scan_kwargs = {
        'FilterExpression': Key('year').between(*year_range),
        'ProjectionExpression': "#yr, title, info.rating",
        'ExpressionAttributeNames': {"#yr": "year"}
    }

    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        display_movies(response.get('Items', []))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None


if __name__ == '__main__':
    def print_movies(movies):
        for movie in movies:
            print(f"\n{movie['year']} : {movie['title']}")
            pprint(movie['info'])

    query_range = (1950, 1959)
    print(
        f"Scanning for movies released from {query_range[0]} to {query_range[1]}...")
    scan_movies(query_range, print_movies)
```
Chú thích:

     ProjectionExpression chỉ định các thuộc tính bạn muốn trong kết quả quét.

     FilterExpression chỉ định một điều kiện chỉ trả về các mục thỏa mãn điều kiện. Tất cả các mục khác đều bị loại bỏ.

- Bước 3 Chạy chương trình bằng Window Command Prompt đã được xác thực và cấu hình ở bước 1.1. Gõ lệnh:

```
python MoviesScan.py
```
Trường hợp khác: sử dụng `python "đường dẫn file MoviesScan.py"`

- Bước 4: Sau khi chạy chương trình, thu được kết quả

```

1958 : Cat on a Hot Tin Roof
{'rating': Decimal('8')}

1958 : Monster on the Campus
{'rating': Decimal('5.7')}

1958 : No Time for Sergeants
{'rating': Decimal('7.5')}

1958 : Teacher's Pet
{'rating': Decimal('7')}

1958 : Touch of Evil
{'rating': Decimal('8.2')}

1958 : Vertigo
{'rating': Decimal('8.5')}

1951 : A Streetcar Named Desire
{'rating': Decimal('8')}

1951 : Alice in Wonderland
{'rating': Decimal('7.4')}

1951 : An American in Paris
{'rating': Decimal('7.2')}

1951 : Operation Pacific
{'rating': Decimal('6.5')}

1951 : Storm Warning
{'rating': Decimal('7')}

1951 : Strangers on a Train
{'rating': Decimal('8.2')}

1951 : The African Queen
{'rating': Decimal('8')}

```

<h3>2.9 Xóa dữ liệu bảng</h3>

- Bước 1: Tạo file có tên <b>`MoviesDeleteTable.py`</b>

- Bước 2: Sao chép đoạn mã sau và dán vào file <b>`MoviesDeleteTable.py`</b>
```
import boto3


def delete_movie_table(dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')
    table.delete()


if __name__ == '__main__':
    delete_movie_table()
    print("Movies table deleted.")
```
- Bước 3 Chạy chương trình bằng Window Command Prompt đã được xác thực và cấu hình ở bước 1.1. Gõ lệnh:

```
python MoviesDeleteTable.py
```
Trường hợp khác: sử dụng `python "đường dẫn file MoviesDeleteTable.py"`

- Bước 4: Sau khi chạy chương trình, thu được kết quả

```
Movies table deleted.
```

<h1>IV.DỌN DẸP TÀI NGUYÊN</h1>

<h3>1.1 Sử dụng AWS Management Console</h2>

- Bước 1: Mở bảng DynamoDB console tại  https://console.aws.amazon.com/dynamodb/

- Bước 2: Trong thanh điều hướng ở bên trái của bảng điều khiển, chọn <b>Tables</b>

- Bước 3: Chọn bảng <b>Music</b> từ danh sách bảng.

- Bước 4: Chọn <b>Actions</b>, sau đó chọn <b>Delete table</b>.



![Delete Table!](./images/delete-table.png "Delete Table")


<h3>1.2 Sử dụng AWS CloudShell</h2>

- Để xóa bảng, sử dụng lệnh `delete-table`

- Gõ lệnh:
```
aws dynamodb delete-table --table-name Music
```











