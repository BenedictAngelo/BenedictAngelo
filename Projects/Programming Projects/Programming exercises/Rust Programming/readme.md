# Documentation of Learning **Rust** Programming language
---
## What is **Rust**?
-**Rust** is a systems programming language that emphasizes **performance, reliability, and productivity** 

- It's designed to be blazingly fast and memory-efficient, with no runtime or garbage collector, making it ideal for performance-critical services and embedded devices 

### Key Features:

- **Memory safety**: Rust's type system and ownership model guarantee memory-safety and thread-safety, eliminating many classes of bugs at compile-time 
- **Performance**: Comparable to C/C++ with low-level hardware control, but with built-in safety guarantees 
- **Modern tooling**: Includes Cargo (integrated package manager), great documentation, and helpful compiler error messages 

### What it's used for:

- Command-line tools 

- Web development and WebAssembly 

- Network services 

- Embedded systems 

- Operating systems 

### Why it matters:

- Unlike C/C++, Rust prevents common programming errors like null pointer dereferences by using optional types that the compiler forces you to handle properly 

- The U.S. White House has even recommended moving to memory-safe languages like Rust for critical software development 

- Rust combines the control and performance of low-level languages with the safety features typically found in higher-level languages

---

## Download Rust compiler:
Official download page:
 https://rust-lang.org/tools/install/
 
---

## Creating and executing Rust file
- Compile Rust file with `rustc [Filename]`
-  Run the executable file using `./Filename` or `.\Filename` on windows, it will have `.exe` at windows and none at UNIX systems
---

## Using **Cargo** for auto compile and file management
- Go into your Rust directory where you plan to have all your rust projects
- Run `cargo new [Filename]`
- You will see your new project folder, inside is `src` directory, where it will contain the `main.rs` file, your source code, and `Cargo.toml`, don't worry about this.
- CD into the newly created project directory and run `cargo build` to compile all the necessary source code and create the executable file.
- You will see new files inside the your project directory such as `Cargo.lock`, `target` directory, and inside it is `debug` directory, don't worry about most of these files.
- CD into `target/debug/` here you will see the executable file, and then you can run it.
- All of these can have a shortcut, by going back into the your project folder and run `cargo run` essentially this would do all the compiling straight up run the executable file in the terminal, which is in default just an "Hello World!" code, which you can then start coding from in `main.rs`.
- Additional you can run `cargo check` to check if the project is compile-able and `cargo fmt` to auto format the source code, just from main project directory.



---

##### Back to [README](../../../../README.md) Mainpage
