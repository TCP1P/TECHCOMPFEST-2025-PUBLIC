// Learn more about Tauri commands at https://tauri.app/develop/calling-rust/
#[tauri::command]
fn greet(name: &str) -> String {
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[tauri::command]
fn get_aes_key() -> String {
    let key = vec![0x0c,0x58,0x43,0x2c,0x34,0x02,0x0a,0x27,0x51,0x41,0x2c,0x34,0x58,0x4a,0x01,0x11];
    let xor_key = "x0r_k3y".as_bytes();
    let mut result = String::new();
    for i in 0..key.len() {
        result.push((key[i] ^ xor_key[i % xor_key.len()]) as char);
    }
    result // th1s_1s_a3s_k3y!
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .invoke_handler(tauri::generate_handler![greet])
        .invoke_handler(tauri::generate_handler![get_aes_key])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
