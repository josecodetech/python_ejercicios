Algoritmo adivina_numero
	secreto := numero_aleatorio
	Repetir
		
	
	si intento < secreto
		Imprimir "Demasiado bajo"
	FinSi
		si intento > secreto
			Imprimir  "Demasiado alto"
		FinSi
		Hasta Que  intento == secreto
		Imprimir "Correcto"
		
	
	
FinAlgoritmo
