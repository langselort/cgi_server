namespace cpp img_service
namespace java img_service

struct GeneralResponse {
    1: i32 code,
    2: string msg,
    3: string data,
}

struct GeneralRequest {
    1: i32 code,
    2: string msg,
    3: string data,
}

service WebCgi {
  GeneralResponse transport (1: GeneralRequest request),
}
