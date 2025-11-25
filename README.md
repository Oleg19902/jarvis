# JARVIS Voice Assistant

![We are NOT limited by the technology of our time!](poster.jpg)

`Jarvis` - is a voice assistant made as an experiment using neural networks for things like **STT/TTS/Wake Word/NLU** etc.

The main project challenges we try to achieve is:
 - 100% offline *(no cloud)*
 - Open source *(full transparency)*
 - No data collection *(we respect your privacy)*

Our backend stack is 🦀 **[Rust](https://www.rust-lang.org/)** with ❤️ **[Tauri](https://tauri.app/)**.<br>
For the frontend we use ⚡️ **[Vite](https://vitejs.dev/)** + 🛠️ **[Svelte](https://svelte.dev/)**.

*Other libraries, tools and packages can be found in source code.*

## Neural Networks

This are the neural networks we are currently using:

 - Speech-To-Text
	 - [Vosk Speech Recognition Toolkit](https://github.com/alphacep/vosk-api) via [Vosk-rs](https://github.com/Bear-03/vosk-rs)
 - Text-To-Speech
	 - [~~Silero TTS~~](https://github.com/snakers4/silero-models) *(currently not used)*
	 - [~~Coqui TTS~~](https://github.com/coqui-ai/TTS) *(currently not used)*
	 - [~~WinRT~~](https://github.com/ndarilek/tts-rs) *(currently not used)*
	 - [~gTTS~](https://github.com/nightlyistaken/tts_rust) *(currently not used)*
	 - [~~SAM~~](https://github.com/s-macke/SAM) *(currently not used)*
 - Wake Word
	 - [Rustpotter](https://github.com/GiviMAD/rustpotter) *(Partially implemented, still WIP)*
	 - [Picovoice Porcupine](https://github.com/Picovoice/porcupine) via [official SDK](https://github.com/Picovoice/porcupine#rust) *(requires API key)*
	 - [Vosk Speech Recognition Toolkit](https://github.com/alphacep/vosk-api) via [Vosk-rs](https://github.com/Bear-03/vosk-rs) *(very slow)*
	 - [~~Snowboy~~] *(currently not used)*
 - NLU
	 - Nothing yet.
- Chat
	- [~~ChatGPT~~](https://chat.openai.com/) (coming soon)

## Supported Languages

Currently, only Russian language is supported.<br>
But soon, Ukranian and English will be added for the interface, wake-word detection and speech recognition.

## Installation

### Linux
1. Install system dependencies:
   - Rust toolchain with `rustup` (nightly is not required).
   - Node.js 18+ and `pnpm` or `npm`.
   - ALSA development libraries and a C toolchain (`build-essential` on Debian/Ubuntu) for the audio backends.
   - Optional: platform libraries for [PvRecorder](https://github.com/Picovoice/pvrecorder) and [Vosk](https://github.com/alphacep/vosk-api).
2. Install JavaScript dependencies from the repo root:
   - `cd gui && pnpm install` (or `npm install`), then return to the root.
3. Build and run:
   - Development: `cargo tauri dev`
   - Release bundle: `cargo tauri build`

### Windows
1. Install tooling:
   - [Rust](https://www.rust-lang.org/tools/install) with the MSVC toolchain.
   - [Node.js 18+](https://nodejs.org/) and `pnpm` or `npm`.
   - [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/) with C++ workload for native crates.
   - Optional: platform-specific assets for [PvRecorder](https://github.com/Picovoice/pvrecorder) and [Vosk](https://github.com/alphacep/vosk-api).
2. Install frontend dependencies:
   - `cd gui && pnpm install` (or `npm install`), then go back to the repo root.
3. Build and run:
   - Development: `cargo tauri dev`
   - Release bundle: `cargo tauri build`

## How to build?

Nothing special was used to build this project.<br>
You need only Rust and NodeJS installed on your system.<br>
Other than that, all you need is to install all the dependencies and then compile the code with `cargo tauri build` command.<br>
Or run dev with `cargo tauri dev`.

<br><br>
*Thought you might need some of the platform specific libraries for [PvRecorder](https://github.com/Picovoice/pvrecorder) and [Vosk](https://github.com/alphacep/vosk-api).* 

## Author

Abraham Tugalov

## Python version?
Old version of Jarvis was built with Python.<br>
The last Python version commit can be found [here](https://github.com/Priler/jarvis/tree/943efbfbdb8aeb5889fa5e2dc7348ca4ea0b81df).

## License

[Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/)<br>
See LICENSE.txt file for more details.