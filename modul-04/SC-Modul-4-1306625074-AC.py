5) Print Out Coding

import pandas as pd

def hitung_grade(na):
  if na >= 86:
    return "A"
  elif na >= 81:
    return "A-"
  elif na >= 76:
    return "B+"
  elif na >= 71:
    return "B"
  elif na >= 66:
    return "B-"
  elif na >= 61:
    return "C+"
  elif na >= 56:
    return "C"
  else:
    return "TL"

def main():
  print("Program  Granding")
  print("Nama \t: Andita Chairunsukma")
  print("NIM \t: 1306625074")
  print("\nLAPORAN GRANDING MAHASISWA\n")

  try:
    df = pd.read_excel('DataNilai.xlsx')
  except FileNotFoundError:
    print("Error: File 'DataNilai.xlsx' tidak ditemukan. Pastikan file ada di folder yang sama.")
    return

  col_nama = df.columns[0]
  col_lain2 = df.columns[2]
  col_uts = df.columns[3]
  col_uas = df.columns[4]

  rekap = {
      "A" : 0,
      "A-" : 0,
      "B+" : 0,
      "B" : 0,
      "B-" : 0,
      "C+" : 0,
      "C" : 0,
      "TL" : 0
  }
  print("-" * 45)
  print(f"{'No':<4} | {'Nama Mahasiswa':<15} | {'Nilai Akhir':<11} | {'Grade':<5}")
  print("-" * 45)

  i = 0
  total_mahasiswa = len(df)

  while i < total_mahasiswa:
    row = df.iloc[i]
    nama_mhs = str(row[col_nama])
    n_lain2 = float(row[col_lain2])
    n_uts = float(row[col_uts])
    n_uas = float(row[col_uas])

    nilai_akhir = (0.3 * n_lain2) + (0.35 * n_uts) + (0.35 * n_uas)
    grade = hitung_grade(nilai_akhir)

    if grade in rekap:
      rekap[grade] += 1

    print(f"{i+1:<4} | {nama_mhs:<15} | {nilai_akhir:<11.2f} | {grade:<5}")
    i += 1

  print("-" * 45)
  print("\nRekapitulasi :")
  print(f"Grade A : {rekap['A']}")
  print(f"Grade A- : {rekap['A-']}")
  print(f"Grade B+ : {rekap['B+']}")
  print(f"Grade B : {rekap['B']}")
  print(f"Grade B- : {rekap['B-']}")
  print(f"Grade C+ : {rekap['C+']}")
  print(f"Grade C : {rekap['C']}")
  print(f"Tidak Lulus (TL) : {rekap['TL']}")
  print(f"Total Mahasiswa = {total_mahasiswa}")
  print("\n*selesai*")

if __name__ == "__main__":
  main()


























6) Screen Hasil Keluaran




