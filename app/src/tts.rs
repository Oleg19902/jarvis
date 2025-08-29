use once_cell::sync::OnceCell;
use std::sync::Mutex;
use tts::{Tts, Error};

static TTS: OnceCell<Mutex<Tts>> = OnceCell::new();

pub fn init() -> Result<(), Error> {
    match Tts::default() {
        Ok(tts) => {
            TTS.set(Mutex::new(tts)).unwrap();
            info!("TTS engine initialized.");
            Ok(())
        },
        Err(e) => {
            error!("Failed to initialize TTS engine: {}", e);
            Err(e)
        }
    }
}

pub fn speak(text: &str) {
    if let Some(tts_mutex) = TTS.get() {
        let mut tts = tts_mutex.lock().unwrap();
        // The second argument is `interrupt`. We'll set it to `true` to
        // make it speak immediately.
        match tts.speak(text, true) {
            Ok(_) => info!("Speaking: {}", text),
            Err(e) => error!("Failed to speak: {}", e),
        }
    } else {
        error!("TTS engine not initialized.");
    }
}
