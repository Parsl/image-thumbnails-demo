import files;
import io;
import string;

int workers;

printf("turbine_workers()=%d",turbine_workers() );

app myconvert(string infoto)
{
	"myconvert.py" infoto 
}

string fotos[]= file_lines(input("foto_list.txt") );
foreach foto in fotos
{
	printf("swift-t scheduled myconvert.py : %s", foto);
	myconvert(foto);
}
