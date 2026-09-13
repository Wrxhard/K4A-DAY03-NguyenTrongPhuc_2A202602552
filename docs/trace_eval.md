# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Trọng Phúc  
> **Mã Sinh Viên / Mã Học viên:** 2A202602552  
> **Chủ đề Lựa chọn:** Trợ lý Học vụ & Tra cứu Lịch thi VinUni

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Phải phân tích yêu cầu, tìm tool và workflow phù hợp, đôi khi yêu cầu sẽ bao gồm nhiều vấn đề khác nhau|
| **2. Tool Interaction** | 2 / 5 | Hệ thống cần gọi đến dữ liệu tra cứu bên ngoài như lịch thi và quy trình xử lý các tác vụ liên quan đến học vụ|
| **3. Dynamic Decision** | 3 / 5 | Có việc phân tích đúng vấn đề sẽ là tiền đề để quyết định nên chọn tool và workflow nào phù hợp |
| **4. Long Horizon Goal** | 4 / 5 | Có cần phải giữ ngữ cảnh xuyên suối để Model nhận biết vấn đề đã được giải quyết hay chưa và cũng như lưu ngữ cảnh từ các dữ liệu bên ngoài |
| **TỔNG ĐIỂM AGENTIC FIT** | 14 / 20 | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Chào bạn, bạn có thể giới thiệu quy chế học vụ cơ bản của Đại học VinUni không?",
    "action_type": "FINAL_ANSWER",
    "thought": "OpenAI phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Quy chế học vụ của Đại học VinUni bao gồm nhiều quy định quan trọng liên quan đến việc học tập, đánh giá, và quản lý sinh viên. Dưới đây là một số nội dung cơ bản:\n\n1. **Điều kiện nhập học**: Quy định về tiêu chuẩn đầu vào cho sinh viên, bao gồm kết quả học tập, các chứng chỉ cần thiết.\n\n2. **Chương trình đào tạo**: Chi tiết về các ngành học, môn học, và cấu trúc chương trình đào tạo, bao gồm tín chỉ học phần.\n\n3. **Đánh giá và thi cử**: Quy định về các hình thức đánh giá (thi giữa kỳ, cuối kỳ, báo cáo dự án) và cách tính điểm.\n\n4. **Quy định về vắng mặt**: Chính sách về việc xin nghỉ học, tham gia lớp học và các quy định liên quan đến sự hiện diện của sinh viên.\n\n5. **Quy định về học phí**: Thông tin về mức học phí, thời hạn thanh toán, và các khoản phí phát sinh.\n\n6. **Khen thưởng và kỷ luật**: Các hình thức khen thưởng cho sinh viên xuất sắc và hình thức xử lý kỷ luật đối với sinh viên vi phạm quy định.\n\n7. **Hỗ trợ học vụ**: Các dịch vụ hỗ trợ sinh viên như tư vấn học tập, hỗ trợ tâm lý, và các hoạt động ngoại khóa.\n\nMọi sinh viên cần tìm hiểu và tuân thủ quy chế học vụ này để đảm bảo quyền lợi và nghĩa vụ trong quá trình học tập tại trường. Nếu bạn cần thông tin chi tiết hơn về từng phần, xin vui lòng cho biết!",
    "latency_ms": 5316.04
  },
  {
    "step": 1,
    "query": "Hãy tra cứu thông tin học vụ của sinh viên SV2026001.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "class": "AI-K4",
        "gpa": 3.85,
        "email": "an.nv@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A"
      }
    },
    "latency_ms": 838.96
  },
  {
    "step": 2,
    "query": "Hãy tra cứu thông tin học vụ của sinh viên SV2026001.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Kết quả tra cứu cho sinh viên SV2026001 (Nguyễn Văn An): Lớp AI-K4, GPA: 3.85, Email: an.nv@vinuni.edu.vn, Trạng thái: Đang học, Cố vấn: PGS.TS Nguyễn Văn A.",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Tôi là sinh viên SV2026002 và muốn đặt lịch hẹn với cố vấn học tập vào ngày 25/09/2026 lúc 14:30 để tư vấn về kế hoạch học tập học kỳ tới.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "schedule_appointment",
    "arguments": {
      "student_id": "SV2026002",
      "datetime_str": "14:30 25/09/2026"
    },
    "observation": {
      "status": "SUCCESS",
      "booking_id": "BK-SV2026002-99",
      "student_id": "SV2026002",
      "datetime": "14:30 25/09/2026",
      "advisor": "PGS.TS Nguyễn Văn A",
      "message": "Đặt lịch thành công cho sinh viên SV2026002 với PGS.TS Nguyễn Văn A vào lúc 14:30 25/09/2026."
    },
    "latency_ms": 1338.97
  },
  {
    "step": 2,
    "query": "Tôi là sinh viên SV2026002 và muốn đặt lịch hẹn với cố vấn học tập vào ngày 25/09/2026 lúc 14:30 để tư vấn về kế hoạch học tập học kỳ tới.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Đặt lịch thành công cho sinh viên SV2026002 với PGS.TS Nguyễn Văn A vào lúc 14:30 25/09/2026.",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Sinh viên SV2026003 muốn biết thông tin học vụ hiện tại của mình (GPA, số tín chỉ) và muốn đặt lịch hẹn với cố vấn vào ngày 27/09/2026 lúc 10:00 để thảo luận về kế hoạch nâng cao GPA.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026003"
    },
    "observation": {
      "status": "NOT_FOUND",
      "message": "Không tìm thấy dữ liệu sinh viên có mã 'SV2026003'"
    },
    "latency_ms": 1072.86
  },
  {
    "step": 2,
    "query": "Sinh viên SV2026003 muốn biết thông tin học vụ hiện tại của mình (GPA, số tín chỉ) và muốn đặt lịch hẹn với cố vấn vào ngày 27/09/2026 lúc 10:00 để thảo luận về kế hoạch nâng cao GPA.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Không tìm thấy dữ liệu sinh viên có mã 'SV2026003'",
    "latency_ms": 10.0
  },
  {
    "step": 1,
    "query": "Hãy tra cứu thông tin học vụ của sinh viên có mã SV9999999.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV9999999"
    },
    "observation": {
      "status": "NOT_FOUND",
      "message": "Không tìm thấy dữ liệu sinh viên có mã 'SV9999999'"
    },
    "latency_ms": 850.96
  },
  {
    "step": 2,
    "query": "Hãy tra cứu thông tin học vụ của sinh viên có mã SV9999999.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Không tìm thấy dữ liệu sinh viên có mã 'SV9999999'",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
