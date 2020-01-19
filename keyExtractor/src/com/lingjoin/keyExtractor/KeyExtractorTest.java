package com.lingjoin.keyExtractor;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

public class KeyExtractorTest {

	static {
		if ( CLibraryKeyExtractor.instance.KeyExtract_Init("", 1, "") ) {
			System.out.println("KeyExtractor��ʼ���ɹ�");
		} else {
			System.out.println("KeyExtractor��ʼ��ʧ��");
			System.exit(-1);
		}
	}
	/**
	 * ��ȡtxt�ļ�������
	 * @param file ��Ҫ��ȡ���ļ�����
	 * @return �����ļ�����
	 */
	public static String txtToString(File file){
	// 	StringBuilder result = new StringBuilder();
	// 	try{
	// 		BufferedReader br = new BufferedReader(new FileReader(file));//����һ��BufferedReader������ȡ�ļ�
	// 		String s = null;
	// 		while((s = br.readLine())!=null){//ʹ��readLine������һ�ζ�һ��
	// 			result.append(System.lineSeparator()+s);
	// 		}
	// 		br.close();
	// 	}catch(Exception e){
	// 		e.printStackTrace();
	// 	}
	// 	return result.toString();
	// }
	public static void keyWords(String string){
		System.out.println("11111111");
		String keyWordsStr= CLibraryKeyExtractor.instance.KeyExtract_GetKeyWords(string, 1000000000, true);
		System.out.println(keyWordsStr.replaceAll("#","\n"));
	}
	public static void main(String[] args) {


		//00
//		int num=0;
//		for (int i=0;i<24;i++){
//			String path = "C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\"+num+".txt";
//			System.out.println(path);
//			File file = new File(path);
//			keyWords(txtToString(file));
//			num++;
//		}
		// File file0 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\0.txt");
		// keyWords(txtToString(file0));

		// File file1 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\1.txt");
		// keyWords(txtToString(file1));

		// File file2 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\2.txt");
		// keyWords(txtToString(file2));

		// File file3 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\3.txt");
		// keyWords(txtToString(file3));

		// File file4 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\4.txt");
		// keyWords(txtToString(file4));

		// File file5 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\5.txt");
		// keyWords(txtToString(file5));

		// File file6 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\6.txt");
		// keyWords(txtToString(file6));

		// File file7 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\7.txt");
		// keyWords(txtToString(file7));

		// File file8 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\8.txt");
		// keyWords(txtToString(file8));

		// File file9 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\9.txt");
		// keyWords(txtToString(file9));

		// File file10 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\10.txt");
		// keyWords(txtToString(file10));

		// File file11 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\11.txt");
		// keyWords(txtToString(file11));

		// File file12 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\12.txt");
		// keyWords(txtToString(file12));

		// File file13 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\13.txt");
		// keyWords(txtToString(file13));

		// File file14 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\14.txt");
		// keyWords(txtToString(file14));

		// File file15 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\15.txt");
		// keyWords(txtToString(file15));

		// File file16 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\16.txt");
		// keyWords(txtToString(file16));

		// File file17 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\17.txt");
		// keyWords(txtToString(file17));

		// File file18 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\18.txt");
		// keyWords(txtToString(file18));

		// File file19 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\19.txt");
		// keyWords(txtToString(file19));

		// File file20 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\20.txt");
		// keyWords(txtToString(file20));

		// File file21 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\21.txt");
		// keyWords(txtToString(file21));

		// File file22 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\22.txt");
		// keyWords(txtToString(file22));

		// File file23 = new File("C:\\Users\\SAMSUNG\\Downloads\\keyExtractor\\Data\\txt\\23.txt");
		// keyWords(txtToString(file23));

		// System.out.println("�����ѽ�������");

		String content = "��ȫ�����бر��������Ѻú�����̸�й��ܱ��⽻�������޹����ദ֮����ǿ�������š���ͬ���졢����������������Ӯ���������ɹ�ϵ��չ��ʱ�������������ȶ�����";
		String keyWordsStr = CLibraryKeyExtractor.instance.KeyExtract_GetKeyWords(content, 10, true);
		// keyWords(txtToString(content));
		CLibraryKeyExtractor.instance.KeyExtract_Exit();


	}
}
