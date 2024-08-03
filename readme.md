Program dikembangkan menggunakan bahasa pemrograman Python, sehingga untuk menjalankan program diperlukan untuk menginstall bahasa program, text editor, dan ekstensi text editor pendukungnya.

1. Visual Studio Code (https://code.visualstudio.com/Download)
2. Python programming language (https://python.org/downloads)
3. Python linter (VS Code Extension)

## Cara menginstall Python Linter

Pergi ke _Extension_ tab pada sidebar > cari Python > klik Install
![[Pasted image 20240803145344.png]]

## Cara memeriksa apakah Python terinstall

Pada _command prompt_ / terminal, eksekusi perintah dibawah

```bash
python --version
atau
python3 --version
```

Jika Python terinstall, ia akan menampilkan informasi seperti berikut

```bash
# output
Python 3.10.13
```

## Cara menjalankan program

Sebelum menjalankan program, lakukan instalasi library terlebih dahulu seperti berikut (pastikan python terinstall dengan benar).

```bash
pip install -r requirements.txt
```

Pip adalah singkatan untuk _python installation package_ yang biasanya sudah terinstall bersamaan dengan python.

Jika semua yang dibutuhkan untuk menjalankan program telah terinstall. Selanjutnya eksekusi `main.py` melalui VS Code terminal sebagai berikut

```
python main.py
```

Atau buka main.py pada VS Code, jalankan program menggunakan tombol Run pada bagian pojok kanan atas.
![[Pasted image 20240803152105.png]]

Secara otomatis, program akan membaca data didalam `data.xlsx` dan mengashilkan output `result.xlsx`

## Yang perlu diketahui ketika menjalankan program

Ketika menjalankan main.py, kamu akan melihat baris kode seperti

```python
if __name__ == "__main__":
    # main()
    run()
```

Pada bahasa pemrograman python "#" berarti baris kode yang tidak akan dieksekusi oleh program. Sedangkan setiap _code_ yang diawali dengan `def` berarti suatu kelompok program. Sehingga apa yang terjadi di `main.py` adalah berjalannya fungsi bernama `run()` yang sebenarnya adalah repitisi sebanyak 10 kali dari fungsi `main()`

Untuk menjalankan satu kali program `main()`, bisa dilakukan dengan cara mengubah kode setelah _main gate_ menjadi sebagai berikut

```python
if __name__ == "__main__":
    main()
    # run()
```
