#include <iostream>
#include <string>
#include <conio.h>

using namespace std;

main() {
	cout << "========================================================================== \n";
	cout << "|SELAMAT DATANG DI KLINIK JANICE, SILAHKAN ISI DATA DAN PILIH KELUHAN ANDA ! \n"; 
	cout << "========================================================================== \n";
	int n = 0;
	cout << "Total jumlah pasien: ";
	cin >> n;
	cout << "--------------------------------------------------------------------------\n";
	
	string names[n];
	string results[n];
	
	for (int i = 0; i < n; i++) {
		string nama, umur, NIK, alamat, nomortelepon;
		
		cout << "\nMasukan Data Pasien Ke-" << i + 1 << "\n";
		
		cout << "Nama Pasien: ";
		cin >> nama;
		names[i] = nama;
		
		cout << "Umur : ";
		cin >> umur;
		cout << "NIK : ";
		cin >> NIK;
		cout << "Alamat : ";
		cin >> alamat;
		cout << "Nomor Telepon : ";
		cin >> nomortelepon;
		
	    cout <<"============================================================================= \n";  
		 
		cout <<"Silahkan Pilih Keluhan Anda! \n";
		cout << "\nTulis 'Y/y' jika pernyataan berikut benar, atau 'T/t' jika salah \n";
		
		char batukkering, batuklendir, bersin, pilek, nyeritubuh;
		char kelemahanotot, demamringan, demamtinggi, sulitbernafas, hilangindra;
		
		cout << "Apakah " << nama << " batuk kering? ";
		cin >> batukkering;
		
		cout << "Apakah " << nama << " batuk lendir? ";
		cin >> batuklendir;
		
		cout << "Apakah " << nama << " bersin? ";
		cin >> bersin;
		
		cout << "Apakah " << nama << " pilek? ";
		cin >> pilek;
		
		cout << "Apakah " << nama << " nyeri tubuh? ";
		cin >> nyeritubuh;
		
		cout << "Apakah " << nama << " kelemahan otot? ";
		cin >> kelemahanotot;
		
		cout << "Apakah " << nama << " demam ringan? ";
		cin >> demamringan;
		
		cout << "Apakah " << nama << " demam tinggi? ";
		cin >> demamtinggi;
		
		cout << "Apakah " << nama << " sulit bernafas? ";
		cin >> sulitbernafas;
		 
		cout << "Apakah " << nama << " hilang indra? ";
		cin >> hilangindra;
		
		cout << "\n";
		if (
		   tolower(batukkering) == 'y' && tolower(bersin) == 'y'
		) {
			cout << "Indikasi penyakit karena polusi udara";
			results[i] = "Polusi Udara";	
		} else if ( 
			tolower(bersin) == 'y' && 
			tolower(batuklendir) == 'y' && 
			tolower(pilek) == 'y'
		) {
			cout << "Indikasi penyakit karena pilek biasa";
			results[i] = "Pilek Biasa";
	    }else if(
			tolower(bersin) == 'y' && 
			tolower(batuklendir) == 'y' && 
			tolower(pilek) == 'y' && 
			tolower(nyeritubuh) == 'y' && 
			tolower(kelemahanotot) == 'y' && 
			tolower(demamringan) == 'y'
			) {
			cout << "Indikasi penyakit karena sakit flu";
			results[i] = "Sakit Flu";
		} else if (
		    tolower(batukkering) == 'y'&&
			tolower(bersin) == 'y' && 
			tolower(nyeritubuh) == 'y' && 
			tolower(kelemahanotot) == 'y' && 
			tolower(demamtinggi) == 'y' && 
			tolower(sulitbernafas) == 'y' && 
			tolower(hilangindra) == 'y'
		) {
			cout << "Indikasi penyakit karena virus corona";
			results[i] = "Virus Corona";	
		} else {
			cout << "Tidak ada indikasi";
			results[i] = "Sehat";
		}
	}
	
	system("cls");
	
	cout << "Hasil Pemeriksaan Untuk Menentukan Penyakit yang diderita\n";
	
	cout << "No\tNama\tHasil\n";
	cout << "========================================================================== \n";
	for (int i = 0; i<n; i++) {
		cout << (i+1) << '\t' << names[i] << '\t' << results[i] << '\n';
	}
	cout << "========================================================================== \n";
	
	cout << "\nSemoga cepat sembuh!";
	cout << "\nJanice Claresta Lingga \n";
	getch();
}
